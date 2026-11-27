from pydantic import BaseModel, ConfigDict


# [CREATE] User အသစ်ဆောက်တဲ့အခါ (POST /users) client ဆီက လက်ခံမယ့် data ပုံစံ
class UserCreate(BaseModel):
    name: str
    email: str


# [UPDATE - PARTIAL] User အချက်အလက် ပြင်တဲ့အခါ (PATCH /users/{user_id}) သုံးမယ့် schema
# Field တွေကို Optional (| None = None) ထားထားလို့ ကိုယ်ပြောင်းချင်တဲ့ field တစ်ခုတည်းကိုပဲ ပို့လို့ရပါတယ်
class UserUpdate(BaseModel):
    name: str | None = None
    email: str | None = None


# [RESPONSE] API ကနေ client ဆီ ပြန်ထုတ်ပေးမယ့် data ပုံစံ (id ပါဝင်ပြီး DB model ကနေ တိုက်ရိုက်ပြောင်းယူနိုင်ပါတယ်)
class UserResponse(BaseModel):
    # SQLAlchemy ORM object (attribute တွေနဲ့ ရှိတဲ့ User instance) ကို Pydantic schema အဖြစ် တိုက်ရိုက်ဖတ်နိုင်စေရန်
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    email: str
