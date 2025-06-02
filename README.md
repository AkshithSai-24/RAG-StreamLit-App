Thanks! Here's an updated and accurate `README.md` for your [RAG-StreamLit-App](https://github.com/AkshithSai-24/RAG-StreamLit-App), now reflecting that it uses **pip**, **LangChain**, and **Google Gemini** LLM:

---

# 🧠 RAG-StreamLit-App

A **Streamlit** application that leverages **Retrieval-Augmented Generation (RAG)** with **LangChain**, **Google Gemini**, and **Faiss** to provide intelligent, interactive question-answering from uploaded PDF documents.

---

## ✨ Features

* 📄 Upload and analyze multiple PDFs
* 🔍 Semantic document retrieval using **Faiss (Facebook AI Similarity Search)**
* 💬 Natural language querying with **Google Gemini** via **LangChain**
* ⚡ Clean, responsive interface via Streamlit

---

## 📦 Installation

### 🧰 Prerequisites

* Python 3.9+
* Google API key for Gemini
* `pip` package manager

### 🛠️ Setup Instructions

1. **Clone the Repository**

```bash
git clone https://github.com/AkshithSai-24/RAG-StreamLit-App.git
cd RAG-StreamLit-App
```

2. **Create a Virtual Environment (optional but recommended)**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

4. **Set Up Environment Variables**

Create a `.env` file in the root directory:

```
GOOGLE_API_KEY=your_google_api_key_here
```

> 🔑 Replace `your_google_api_key_here` with your actual Google Gemini API key.

5. **Run the App**

```bash
streamlit run Streamlit_App.py
```

---

## 🧪 Usage

1. Launch the app in your browser.
2. Upload one or more PDFs.
3. Ask natural language questions about the content.
4. Receive accurate, contextual answers powered by **LangChain + Gemini**.

---

## ⚙️ Tech Stack

| Layer             | Tool/Library                      |
| ----------------- | --------------------------------- |
| LLM               | Google Gemini                     |
| RAG Framework     | LangChain                         |
| Vector DB         | Faiss                             |
| UI                | Streamlit                         |
| PDF Parsing       | PyPDF                             |
| Embedding Backend | Google Embeddings (via LangChain) |

---


This project is licensed under the **MIT License**. See the [LICENSE](./LICENSE) file for more details.

---

Let me know if you want badges, deployment steps (e.g. Streamlit Cloud), or demo GIFs added!
