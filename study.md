# FastAPI + PostgreSQL (SQLAlchemy + psycopg) CRUD Learning Roadmap

ဒီ `README.md` က FastAPI နဲ့ PostgreSQL (`fastapi_db`) ကို တွဲသုံးပြီး CRUD REST API တစ်ခု တည်ဆောက်ရာမှာ အဆင့်လိုက် လေ့လာသင့်တဲ့ အကြောင်းအရာတွေနဲ့ ဖတ်ရှုလေ့လာနိုင်မယ့် link တွေကို စုစည်းပေးထားတာ ဖြစ်ပါတယ်။

---

## ၁။ FastAPI အခြေခံများ
* Path parameters, Query parameters နဲ့ Request body (`Pydantic`) အလုပ်လုပ်ပုံ
* Status codes (`201`, `400`, `404`, `204`) နဲ့ `HTTPException` သုံးပုံ
* `uvicorn` နဲ့ run ပြီး `/docs` (Swagger UI) မှာ စမ်းသပ်ပုံ
* **Links:**
  * [FastAPI Official Tutorial - First Steps](https://fastapi.tiangolo.com/tutorial/first-steps/)
  * [FastAPI - Request Body](https://fastapi.tiangolo.com/tutorial/body/)
  * [FastAPI - Handling Errors](https://fastapi.tiangolo.com/tutorial/handling-errors/)

---

## ၂။ PostgreSQL & Connection (`psycopg` + SQLAlchemy 2.x)
* PostgreSQL database (`fastapi_db`), schemas (`public`), tables (`users`) နဲ့ constraints (`PRIMARY KEY`, `UNIQUE`, `NOT NULL`)
* `create_engine`, `pool_pre_ping=True`, `sessionmaker` နဲ့ `get_db()` dependency
* `.env` နဲ့ environment variables တွေကို စနစ်တကျ စီမံပုံ
* **Links:**
  * [FastAPI - SQL (Relational) Databases](https://fastapi.tiangolo.com/tutorial/sql-databases/)
  * [SQLAlchemy 2.0 Documentation - Engine & Connection](https://docs.sqlalchemy.org/en/20/core/engines.html)
  * [SQLAlchemy 2.0 ORM - Session Basics](https://docs.sqlalchemy.org/en/20/orm/session_basics.html)
  * [Psycopg 3 Documentation](https://www.psycopg.org/psycopg3/docs/)

---

## ၃။ Models & Schemas ခွဲခြားရေးသားခြင်း
* **SQLAlchemy ORM Models (`models.py`):** `DeclarativeBase`, `Mapped`, `mapped_column` သုံးပြီး DB table တွေကို သတ်မှတ်ပုံ
* **Pydantic Schemas (`schemas.py`):** Create / Update / Response schema တွေ ခွဲရေးပုံ (`from_attributes=True`, `EmailStr`, optional fields)
* **Links:**
  * [SQLAlchemy 2.0 Declarative Mapping](https://docs.sqlalchemy.org/en/20/orm/declarative_mapping.html)
  * [Pydantic Docs - Models](https://docs.pydantic.dev/latest/concepts/models/)
  * [Pydantic Docs - Fields](https://docs.pydantic.dev/latest/concepts/fields/)

---

## ၄။ CRUD Operations & Error Handling (`main.py`)
* **Create (`POST`):** `db.add()`, `db.commit()`, `db.refresh()`, `IntegrityError` ဖမ်းပြီး `db.rollback()` လုပ်ပုံ
* **Read (`GET`):** `select()` + `db.scalars().all()` နဲ့ `db.get()` သုံးပုံ
* **Update (`PATCH`):** ရှိပြီးသား record ကို ရှာပြီး ပြောင်းလဲလိုတဲ့ field တွေကိုပဲ update လုပ်ပုံ
* **Delete (`DELETE`):** record ဖျက်ပုံနဲ့ `204 No Content` response ပြန်ပုံ
* **Links:**
  * [SQLAlchemy 2.0 ORM Querying Guide](https://docs.sqlalchemy.org/en/20/orm/queryguide/index.html)
  * [FastAPI - Response Model](https://fastapi.tiangolo.com/tutorial/response-model/)

---

## ၅။ Project ကြီးလာတဲ့အခါ ဆက်လေ့လာသင့်သော အဆင့်များ
* **Routers & Modular Structure:** `routers/users.py`, `routers/posts.py`, `APIRouter` နဲ့ folder ခွဲထုတ်ပုံ
* **Relationships (`ForeignKey`):** Table အချင်းချင်း ချိတ်ဆက်ပုံ (`User` <-> `Post`)
* **Database Migrations (Alembic):** Schema ပြောင်းလဲမှုတွေကို version control နဲ့ စီမံပုံ
* **Testing:** `pytest` နဲ့ `TestClient` သုံးပြီး API endpoint တွေ စမ်းသပ်ပုံ
* **Auth & Security:** Password hashing, JWT authentication နဲ့ role/permission စစ်ဆေးပုံ
* **Links:**
  * [FastAPI - Bigger Applications (APIRouter)](https://fastapi.tiangolo.com/tutorial/bigger-applications/)
  * [SQLAlchemy 2.0 Basic Relationship Patterns](https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html)
  * [Alembic Documentation](https://alembic.sqlalchemy.org/en/latest/)
  * [FastAPI - Testing](https://fastapi.tiangolo.com/tutorial/testing/)
  * [FastAPI - Security Tutorial](https://fastapi.tiangolo.com/tutorial/security/)