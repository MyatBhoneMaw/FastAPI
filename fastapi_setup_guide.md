# FastAPI Project Setup Guide (Ubuntu / Linux)

ဤလမ်းညွှန်ချက်သည် Ubuntu/Debian စနစ်များပေါ်တွင် Python 3.14 Virtual Environment တည်ဆောက်ခြင်း၊ VS Code နှင့် ချိတ်ဆက်ခြင်းနှင့် FastAPI စတင်အသုံးပြုခြင်း အဆင့်ဆင့်ကို ဖော်ပြထားပါသည်။

---

## ၁။ လိုအပ်သော Package များ Install လုပ်ခြင်း (Prerequisites)

Virtual Environment ဖန်တီးနိုင်ရန်အတွက် `python3.14-venv` package ကို စက်ထဲတွင် ဦးစွာ သွင်းထားရန် လိုအပ်ပါသည်။

```bash
sudo apt update
sudo apt install python3.14-venv
```

---

## ၂။ Virtual Environment ဖန်တီးခြင်း (Create `.venv`)

မိမိ၏ Project Folder (`~/Documents/FastApi`) ထဲသို့ ဝင်ပြီး `.venv` အမည်ဖြင့် Virtual Environment တစ်ခု ဖန်တီးပါ။

```bash
cd ~/Documents/FastApi
python3.14 -m venv .venv
```
*(မှတ်ချက်- System default Python သည် 3.14 ဖြစ်နေပါက `python3 -m venv .venv` ဟုလည်း ရိုက်နိုင်ပါသည်။)*

---

## ၃။ Virtual Environment ကို Activate / Deactivate လုပ်ခြင်း

### Activate လုပ်ရန်
Terminal တွင် Virtual Environment ကို စတင်အသုံးပြုရန် အောက်ပါ command ကို ရိုက်ထည့်ပါ။

```bash
source .venv/bin/activate
```

**မှန်ကန်ကြောင်း စစ်ဆေးခြင်း (Verification):**
အချို့ Terminal theme (ဥပမာ - Zsh themes) များတွင် prompt ရှေ့၌ `(.venv)` စာသား ပေါ်မလာတတ်ပါ။ အမှန်တကယ် active ဖြစ်မဖြစ် စစ်ဆေးရန် အောက်ပါ command ကို ရိုက်ကြည့်ပါ။

```bash
which python
```
ရလဒ်အနေဖြင့် `/home/<username>/Documents/FastApi/.venv/bin/python` ဟု ထွက်လာပါက အောင်မြင်စွာ activate ဖြစ်နေပြီ ဖြစ်ပါသည်။

### Deactivate (ပြန်ပိတ်) လုပ်ရန်
Virtual Environment ထဲမှ ပြန်ထွက်လိုပါက အောက်ပါ command ကို ရိုက်ပါ။

```bash
deactivate
```

---

## ၄။ VS Code တွင် Python Interpreter ရွေးချယ်ခြင်း

VS Code တွင် Code completion နှင့် Error checking များ မှန်ကန်စွာ အလုပ်လုပ်စေရန် အောက်ပါအတိုင်း သတ်မှတ်ပါ။

1. VS Code တွင် `Ctrl + Shift + P` (သို့မဟုတ် `F1`) ကို နှိပ်ပါ။
2. `Python: Select Interpreter` ကို ရိုက်ရှာပြီး နှိပ်ပါ။
3. စာရင်းထဲမှ **`.venv (3.14.8) ./.venv/bin/python` (Workspace)** ကို ရွေးချယ်ပါ။

---

## ၅။ FastAPI Install လုပ်ခြင်းနှင့် စမ်းသပ် Run ခြင်း

Virtual Environment (`source .venv/bin/activate`) ကို ဖွင့်ထားပြီးသော အခြေအနေတွင် FastAPI ကို install လုပ်ပါ။

```bash
pip install "fastapi[standard]"
```

### နမူနာ `main.py` ဖိုင် တည်ဆောက်ခြင်း
Project folder ထဲတွင် `main.py` ဖိုင်တစ်ခု ဆောက်ပြီး အောက်ပါ code ကို ထည့်ပါ။

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
```

### Development Server စတင် Run ခြင်း
```bash
fastapi dev main.py
```

Browser တွင် အောက်ပါ link များကို ဖွင့်၍ စစ်ဆေးနိုင်ပါသည်-
* **API Endpoint:** `http://127.0.0.1:8000`
* **Interactive API Docs (Swagger UI):** `http://127.0.0.1:8000/docs`

---

## ၆။ Git အတွက် `.gitignore` သတ်မှတ်ခြင်း (အကြံပြုချက်)

GitHub သို့ code များ တင်သည့်အခါ `.venv` folder ပါမသွားစေရန် `.gitignore` ဖိုင်ထဲတွင် အောက်ပါအတိုင်း ထည့်သွင်းထားပါ။

```text
.venv/
__pycache__/
*.pyc
```