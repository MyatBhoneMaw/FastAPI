from sqlalchemy import BigInteger, String
from sqlalchemy.orm import Mapped, mapped_column
from database import Base


# PostgreSQL ထဲက "users" table နဲ့ ချိတ်ဆက်မယ့် ORM Model class
class User(Base):
    # Database ထဲမှာ အသုံးပြုမယ့် table နာမည်
    __tablename__ = "users"

    # Primary key column (PostgreSQL မှာ BIGINT နဲ့ ကိုက်ညီပြီး index တင်ထားတယ်)
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, index=True)

    # User နာမည် column (အများဆုံး 100 characters၊ NULL မဖြစ်ရ)
    name: Mapped[str] = mapped_column(String(100), nullable=False)

    # Email column (အများဆုံး 150 characters၊ unique ဖြစ်ရမယ်၊ NULL မဖြစ်ရ၊ ရှာရလွယ်အောင် index တင်ထားတယ်)
    email: Mapped[str] = mapped_column(
        String(150), unique=True, nullable=False, index=True
    )
