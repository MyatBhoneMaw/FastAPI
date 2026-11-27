# from fastapi import FastAPI
# from schemas.user import UserCreate
# from models.users import User
#
# app = FastAPI()
#
#
# @app.post(
# "/users",
# )
# def user_create(user: UserCreate):
# user.add(user)
#
#
# @app.get("/users")
# def get_all_user():
# pass
#
#
# @app.get("/users/{user_id}")
# def get_user_detail():
# pass
#
#
# @app.put("/users/update")
# def update_user():
# pass
#
#
# @app.delete("/users/{user_id}")
# def delete_user():
# pass
#
#
from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

#
from database import Base, engine, get_db
from models import User
from schemas import UserCreate, UserResponse, UserUpdate

#
# ORM model (User) တွေအတွက် DB table မရှိသေးရင် ဆောက်ပေးရန် (ရှိပြီးသားဆိုရင် ကျော်သွားပါမယ်)
Base.metadata.create_all(bind=engine)
#
# FastAPI application instance ဖန်တီးခြင်း (/docs Swagger UI title လည်း ဒီကနေ ယူပါမယ်)
app = FastAPI(title="Users CRUD API")


#
#
# [CREATE] User အသစ်တစ်ယောက် ဖန်တီးရန် (အောင်မြင်ရင် HTTP 201 Created ပြန်ပါမယ်)
@app.post("/users", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(payload: UserCreate, db: Session = Depends(get_db)):
    # Pydantic payload ကနေ SQLAlchemy User object ဆောက်ခြင်း
    user = User(name=payload.name, email=payload.email)
    db.add(user)
    try:
        # DB ထဲသို့ အမှန်တကယ် သိမ်းဆည်းခြင်း
        db.commit()
        # DB က generate လုပ်ပေးလိုက်တဲ့ id စတဲ့ latest data ကို ပြန်ဆွဲယူခြင်း
        db.refresh(user)
    except IntegrityError:
        # email unique constraint ချိုးဖောက်မှု စသည့် DB integrity error တက်ရင် transaction ကို ပြန်ဖျက် (rollback) ပါမယ်
        db.rollback()
        raise HTTPException(status_code=400, detail="Email already exists")
    return user


#
#
# [READ ALL] User စာရင်းအားလုံးကို id အစဉ်လိုက် ပြန်ထုတ်ရန်
@app.get("/users", response_model=list[UserResponse])
def list_users(db: Session = Depends(get_db)):
    stmt = select(User).order_by(User.id)
    # scalars().all() က tuple မဟုတ်ဘဲ User model object list အနေနဲ့ တိုက်ရိုက်ထုတ်ပေးပါတယ်
    return db.scalars(stmt).all()


#
#
# [READ ONE] သတ်မှတ်ထားသော user_id နဲ့ User တစ်ယောက်ကို ရှာဖွေရန်
@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    # Primary key (id) ဖြင့် အမြန်ဆုံး ရှာဖွေခြင်း
    user = db.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


#
#
# [UPDATE - PARTIAL] ရှိပြီးသား user ရဲ့ field တချို့ကိုပဲ ပြောင်းလဲရန် (PATCH)
@app.patch("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, payload: UserUpdate, db: Session = Depends(get_db)):
    user = db.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    #
    # Request ထဲမှာ ပါလာတဲ့ field ကိုသာ update လုပ်မယ် (None ဖြစ်နေရင် မထိခိုက်စေပါ)
    if payload.name is not None:
        user.name = payload.name
    if payload.email is not None:
        user.email = payload.email
    #
    try:
        db.commit()
        db.refresh(user)
    except IntegrityError:
        # အခြား user သုံးထားပြီးသား email နဲ့ တူသွားရင် rollback လုပ်ပြီး 400 error ပြန်ပါမယ်
        db.rollback()
        raise HTTPException(status_code=400, detail="Email already exists")
    return user


#
#
# [DELETE] သတ်မှတ်ထားသော user_id ကို ဖျက်ရန် (အောင်မြင်ရင် body မပါဘဲ 204 No Content ပြန်ပါမယ်)
@app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    #
    db.delete(user)
    db.commit()


#
