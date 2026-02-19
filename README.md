# 🤖 Rumino — Knowladge Bot

Chatbot berbasis RAG (Retrieval-Augmented Generation) untuk membantu masyarakat mendapatkan informasi seputar pelatihan, magang, dan lowongan kerja di UPT BLSDM Komdigi Surabaya.

---

## 🛠️ Teknologi yang Digunakan

- **Backend**: FastAPI + Python
- **LLM**: Ollama (llama3.2:3b) — berjalan lokal
- **RAG**: LlamaIndex + ChromaDB
- **Embedding**: HuggingFace (paraphrase-multilingual-MiniLM-L12-v2)
- **Frontend**: HTML + Tailwind CSS

---

## ⚙️ Cara Install & Menjalankan

### 1. Prasyarat
Pastikan sudah terinstall:
- Python 3.10+
- [Ollama](https://ollama.com/) — untuk menjalankan LLM secara lokal

### 2. Clone Repository
```bash
git clone https://github.com/USERNAME/rumino-chatbot.git
cd rumino-chatbot
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Download Model LLM
```bash
ollama pull llama3.2:3b
```

### 5. Jalankan Aplikasi
```bash
python app.py
```
atau
```bash
uvicorn app:app --reload
```

Server akan berjalan di `http://127.0.0.1:8000`

### 6. Buka Frontend
```bash
cd frontend
python -m http.server 3000
```
Lalu buka http://localhost:3000/ di browser.

---

## 📁 Struktur Project

```
rumino-chatbot/
├── app.py                  # Entry point FastAPI
├── requirements.txt        # Daftar dependencies
├── README.md
├── data/                   # Dokumen knowledge base
│   ├── profil_blsdm.txt
│   ├── program_layanan.txt
│   ├── pedoman_magang.txt
│   ├── info_rekrutmen.txt
│   └── prosedur_lamaran.txt
├── modules/
│   ├── config.py           # Konfigurasi LLM & system prompt
│   ├── database.py         # SQLite: log chat & session
│   └── rag.py              # Pipeline RAG (ChromaDB + LlamaIndex)
└── frontend/
    └── index.html          # Antarmuka chatbot
```

---

## 🔑 Catatan Penting

- File `chat_history.db` dan folder `chroma_db/` akan dibuat otomatis saat pertama kali dijalankan
- Pastikan folder `data/` tidak kosong sebelum menjalankan aplikasi
- API Key ada di `app.py` — ganti jika diperlukan

---
