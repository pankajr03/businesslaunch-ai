# 🚀 BusinessLaunch AI

BusinessLaunch AI is a **Streamlit app** that helps entrepreneurs instantly generate **creative business ideas** and understand **initial investment requirements** using **LangChain + OpenAI**.

---

## 🧩 Features
- Choose your company type (IT, Food, Health, etc.)
- Get a unique AI-generated business name
- Receive key investment details and setup suggestions
- Built using:
  - 🧠 LangChain
  - 💬 OpenAI LLMs
  - 🌐 Streamlit UI

---

## ⚙️ Setup Instructions

### 1️⃣ Clone this Repository
```bash
git clone https://github.com/<your-username>/businesslaunch-ai.git
cd businesslaunch-ai

---

### 2️⃣ Create a Virtual Environment
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows

### 3️⃣ Install Dependencies
pip install -r requirements.txt

### 4️⃣ Add Your OpenAI Key

Create a file named secret_key.py:

api_key_client = "sk-your-openai-api-key"

### 5️⃣ Run the App
streamlit run streamlit_app.py

### 🧱 Tech Stack

Frontend/UI: Streamlit

AI Engine: LangChain + OpenAI

Language: Python 3.10+

### 🛡️ Security

Your API key is stored locally in secret_key.py and is excluded from Git via .gitignore.

### 📄 License

This project is open-source under the MIT License.
