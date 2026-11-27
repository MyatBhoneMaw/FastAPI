import os
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

# Environment variable ထဲမှာ DATABASE_URL ရှိရင်ယူ၊ မရှိရင် local PostgreSQL (fastapi_db) ကို default အနေနဲ့သုံးမယ်
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg://postgres:p@55word@localhost:5432/fastapi_db",
)

# DB connection pool ဖန်တီးခြင်း (pool_pre_ping=True က connection သေ/မသေ query မလုပ်ခင် စစ်ပေးတယ်)
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

# Request တစ်ခုချင်းအတွက် DB session ထုတ်ပေးမယ့် factory (commit/flush ကို ကိုယ်တိုင်ထိန်းချုပ်မယ်)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


# ORM model တွေ (User, Post စသည်) အားလုံး inherit ယူရမယ့် base class
class Base(DeclarativeBase):
    pass


# FastAPI route ထဲမှာ Depends(get_db) နဲ့သုံးမယ်؛ ပြီးရင် session ကို အမြဲပြန်ပိတ်ပေးမယ်
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
