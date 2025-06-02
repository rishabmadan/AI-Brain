# 🧠 UPLOAD_AI_BRAIN

Your personal AI brain — private, local, and powerful.  
Ask questions, get smart answers, all without sending a single byte to the cloud.

> ✨ Powered by [Mistral](https://mistral.ai) running locally on your machine.  
> 📦 Built using FastAPI & Python.  
> 💡 Designed for hackers, dreamers, tinkerers.

---

## 🚀 Features

- ✅ **Ask Anything**: Natural language Q&A powered by Mistral.
- 🔒 **100% Local**: No internet? No problem. Everything runs offline.
- 🖼️ **Future Vision**: Integrate file uploads, note memory, calendar insights, and more.
- 🧠 **Feels Like Magic**: But it’s all open source.

---

## 🛠️ Getting Started

> ⚠️ Requirements: A system with at least **8GB RAM** is recommended.

### 1. Clone the Repo

```bash
git clone https://github.com/rishabmadan/AI-Brain.git
cd AI-Brain
```

### 2. Set Up Python Environment
   ``` bash
    pip install -r requirements.txt
   ``` 
    ✅ Python 3.10+ recommended

### 3. Add Your Mistral Model
 
 Download the .gguf model from Hugging Face
 Create a folder named models/ in the project root
 Place your GGUF file inside it

``` 
📁 upload_ai_brain
 ┣ 📁 models
 ┃ ┗ 📄 mistral-model.gguf

```
### 4. Run the App
```bash
uvicorn app:app --reload
```
###  Visit http://127.0.0.1:8000 in your browser. Enjoy your brain 🧠

### 🧭 Project Structure
```graphql

upload_ai_brain/
├── app.py               # FastAPI app
├── model.py             # Mistral inference logic
├── requirements.txt     # Dependencies
├── models/              # Your local GGUF model goes here
└── README.md            # This file
```

### 🎯 Roadmap

 📄 File-based question support (PDFs, images)
 🧠 Memory & context retention
 🖼️ GUI version (Tauri or web)
 📱 App packaging (EXE, DMG, APK)

### 🤝 Contributing

    Pull requests are welcome! If you’ve got cool ideas, issues, or UX suggestions — open them up.

### 📫 Contact
    Email: rishabh.madan2002@gmail.com
    GitHub: @rishabmadan

### 💬 Final Thought
    “This isn’t just an app. It’s your second brain — offline, private, and yours alone.”
– Future You

