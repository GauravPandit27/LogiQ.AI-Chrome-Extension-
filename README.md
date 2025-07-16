
# 🔍 LogiQ.AI – Chrome Extension for Instant AI-Powered Question Solving

![LogiQ.AI Banner](https://your-banner-image-url.com) <!-- Optional: add banner later -->

LogiQ.AI is a lightweight Chrome extension built to solve math, science, GK, and coding questions directly from your browser popup. Paste your question or input it manually — and get instant AI-powered answers using LangChain + Groq.

---

## ⚙️ Features

✅ Clean, minimal UI  
✅ LangChain-powered prompt pipeline  
✅ Groq LLM integration (e.g. `llama3-8b-8192`)  
✅ FastAPI backend for serving answers  
✅ Built with modern extension architecture  
✅ Perfect for students, devs, and curious minds  

---

## 🧠 How It Works

1. **Frontend (Chrome Extension)**  
   - User inputs or pastes a question into the popup.
   - Presses `Solve` → sends it to the backend API.
  
2. **Backend (FastAPI + LangChain)**  
   - LangChain handles prompt templating.
   - Groq’s LLM processes and returns the solution.

3. **Frontend (Result)**  
   - Answer is displayed in the popup UI.

---

## 🏗 Tech Stack

| Layer         | Stack                          |
|--------------|---------------------------------|
| Frontend      | JavaScript, HTML/CSS           |
| Backend       | Python, FastAPI                |
| AI Integration| LangChain, Groq API            |
| Extension API | Chrome Extensions (MV3)        |

---

## 📂 Folder Structure

```

LogiQ.AI/
├── backend/
│   ├── main.py                # FastAPI server
│   ├── constants.py           # Secret key (Groq)
│   ├── langchain\_solver.py    # LangChain + Groq logic
├── popup.html                 # Extension UI
├── popup.js                   # Frontend logic
├── background.js              # (optional)
├── content.js                 # (optional)
├── manifest.json              # Chrome extension manifest (v3)
├── requirements.txt           # Python dependencies

````

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-username/LogiQ.AI.git
cd LogiQ.AI
````

### 2. Start the backend server

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

> 🔐 Make sure to add your Groq API key in `constants.py`

---

### 3. Load the Extension in Chrome

1. Open Chrome and go to `chrome://extensions/`
2. Enable **Developer Mode**
3. Click **Load Unpacked**
4. Select the project root folder (`LogiQ.AI/`)

---

## 🧪 Example Prompt

**Input:**

```
What is the derivative of x^2?
```

**Output:**

```
The derivative of x^2 is 2x.
```

---

## 🧠 Future Enhancements (Optional)

* 🖼 OCR-based screen capture for scanning visible questions
* 🎤 Voice input
* 🌐 Hosted backend for public users
* 🧪 Educational mode with timed quizzes and progress tracking

---

## 🤝 Credits

Built with ❤️ by [Gaurav Pandit](https://www.linkedin.com/in/gauravpandit-ai/)
Powered by LangChain + Groq

---

## 📄 License

MIT License – use freely, just don’t steal my vibes.

---

```

---

Let me know if you want:
- Banner image for branding
- GitHub topics to add
- GitHub actions to auto-lint backend
- Public demo version using Render/Fly.io

Say the word: **"Open Book, let’s launch this portfolio-ready."** 💥
```
