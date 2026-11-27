# 🚀 FastAPI + PostgreSQL (SQLAlchemy) လေ့လာရန် လမ်းညွှန် (Roadmap)

ဒီ `README.md` ဖိုင်က FastAPI ကို အသုံးပြုပြီး PostgreSQL database (`SQLAlchemy` + `psycopg`) နဲ့ စနစ်တကျ REST API တည်ဆောက်တဲ့အခါ အဆင့်ဆင့် လေ့လာသင့်တဲ့ အကြောင်းအရာတွေကို စုစည်းပေးထားတာ ဖြစ်ပါတယ်။

---

## 📌 ၁။ အခြေခံ Concepts များ (Core Fundamentals)

API စတင်မရေးခင် ဒီအပိုင်းတွေကို အရင် နားလည်ထားသင့်ပါတယ်-

* **Python Type Hints:** `str`, `int`, `list[str]`, `str | None` စတဲ့ type annotations တွေ (FastAPI နဲ့ SQLAlchemy 2.x မှာ မရှိမဖြစ် သုံးရပါတယ်)။
* **HTTP Methods & Status Codes:** `GET` (200), `POST` (201), `PATCH`/`PUT` (200), `DELETE` (204), `404 Not Found`, `422 Unprocessable Entity` တို့ရဲ့ အသုံးဝင်ပုံ။
* **Sync vs Async (`def` vs `async def`):** I/O blocking ဖြစ်စေတဲ့ driver (ဥပမာ- standard `psycopg` sync session) နဲ့ async driver (`asyncpg` / `motor`) တွေကို ဘယ်လို ခွဲသုံးရမလဲဆိုတာ။

---

## 🗄️ ၂။ Database & ORM (SQLAlchemy 2.x + psycopg)

PostgreSQL နဲ့ Python ကို ချိတ်ဆက်တဲ့အခါ လေ့လာရမယ့် အဓိက အပိုင်းများ-

* **Database Connection & Pooling:** `create_engine()`, `SessionLocal`, `pool_pre_ping=True` အလုပ်လုပ်ပုံ။
* **Dependency Injection (`Depends`):** `get_db()` generator function သုံးပြီး request တစ်ခုချင်းစီအတွက် DB session ဖွင့်/ပိတ် လုပ်နည်း။
* **ORM Models (`DeclarativeBase`):** `Mapped` နဲ့ `mapped_column` သုံးပြီး Table schema တွေ ဆောက်နည်း။
* **CRUD Queries (SQLAlchemy 2.0 Style):**
  * Create: `db.add()`, `db.commit()`, `db.refresh()`
  * Read: `select(User)`, `db.scalars()`, `db.get()`
  * Update: Object attribute ပြင်ပြီး `db.commit()`
  * Delete: `db.delete()`, `db.commit()`
* **Relationships & Foreign Keys:** One-to-Many (`User` -> `Post`), Many-to-Many စတဲ့ table ချိတ်ဆက်မှုများ။

---

## 🛡️ ၃။ Data Validation & Schemas (Pydantic v2)

API ဆီ ဝင်လာတဲ့ data နဲ့ ပြန်ထုတ်ပေးမယ့် data ကို စစ်ဆေးပုံဖော်ခြင်း-

* **Request vs Response Models:** `UserCreate`, `UserUpdate`, `UserResponse` ဆိုပြီး သီးခြားခွဲရေးနည်း (Password လို sensitive data တွေ response မှာ မပါစေရန်)။
* **`ConfigDict(from_attributes=True)`:** SQLAlchemy ORM object ကို Pydantic model အဖြစ် အလိုအလျောက် ပြောင်းလဲပေးခြင်း။
* **Field Validation:** `EmailStr`, `Field(min_length=3, max_length=100)` စတာတွေနဲ့ input စစ်ဆေးခြင်း။

---

## 🏗️ ၄။ Project Structure ခွဲထုတ်ခြင်း (Scalable Architecture)

Code တွေ များလာတဲ့အခါ ထိန်းသိမ်းရ လွယ်ကူစေဖို့ folder structure ခွဲနည်း-

```text
app/
├── main.py              # FastAPI app initialization
├── database.py          # DB engine & session setup
├── models/              # SQLAlchemy DB models
├── schemas/             # Pydantic request/response schemas
├── routers/             # API endpoints (APIRouter ခွဲရေးခြင်း)
└── services/ (Optional) # Business logic များ သီးသန့်ခွဲထုတ်ခြင်း
```

---

## 🔄 ၅။ Database Migrations (Alembic)

* Production မှာ `Base.metadata.create_all()` အစား **Alembic** ကို သုံးပြီး table column အသစ်ထည့်တာ၊ ပြင်တာတွေကို data မပျက်စီးဘဲ version control လုပ်နည်း။

---

## 🔐 ၆။ Authentication & Security (Next Level)

CRUD ပြီးသွားရင် ဆက်လက်လေ့လာသင့်တဲ့ အပိုင်းများ-

* **Password Hashing:** `passlib` / `bcrypt` သုံးပြီး password တွေကို hash လုပ်သိမ်းဆည်းခြင်း။
* **JWT (JSON Web Tokens):** User Login ဝင်ပြီး Access Token ထုတ်ပေးခြင်း၊ Protected route တွေ ကာကွယ်ခြင်း (`OAuth2PasswordBearer`)။
* **Environment Variables:** `.env` ဖိုင်နဲ့ `pydantic-settings` သုံးပြီး secret key နဲ့ DB password တွေကို လုံခြုံစွာ သိမ်းဆည်းခြင်း။

---

## 🔗 အသုံးဝင်သော Official Documentation Links

1. **FastAPI Official Tutorial:** [https://fastapi.tiangolo.com/tutorial/](https://fastapi.tiangolo.com/tutorial/)
2. **SQLAlchemy 2.0 ORM Quickstart:** [https://docs.sqlalchemy.org/en/20/orm/quickstart.html](https://docs.sqlalchemy.org/en/20/orm/quickstart.html)
3. **Pydantic v2 Documentation:** [https://docs.pydantic.dev/latest/](https://docs.pydantic.dev/latest/)
4. **Alembic Tutorial:** [https://alembic.sqlalchemy.org/en/latest/tutorial.html](https://alembic.sqlalchemy.org/en/latest/tutorial.html)