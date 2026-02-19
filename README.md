# 🤖 Rumino — Knowledge Bot
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
- **Python 3.11** (Recommended) atau Python 3.10 - 3.12
- [Ollama](https://ollama.com/) — untuk menjalankan LLM secara lokal
- Git (untuk clone repository)

### 2. Clone Repository
```bash
git clone https://github.com/cndrdwynt/project-knowladgebot.git
cd project-knowladgebot
```

### 3. Buat Virtual Environment (venv)
**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

> **Catatan:** Setelah aktivasi, akan muncul `(venv)` di awal baris terminal.

### 4. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

> **Jika error ChromaDB di Python 3.14:** Gunakan Python 3.11 atau 3.12.

### 5. Download Model LLM
```bash
ollama pull llama3.2:3b
```

Pastikan Ollama sudah running di background.

### 6. Siapkan Data Knowledge Base
Pastikan folder `data/` berisi file-file knowledge base:
```
data/
├── profil_blsdm.txt
├── program_layanan.txt
├── pedoman_magang.txt
├── info_rekrutmen.txt
└── prosedur_lamaran.txt
```

### 7. Jalankan Backend Server
```bash
# Pastikan venv sudah aktif (ada tulisan (venv) di terminal)
python app.py
```

Server akan berjalan di: `http://127.0.0.1:8000`

### 8. Buka Frontend

```bash
# Di terminal baru (jangan tutup server backend)
python -m http.server 3000
```
Lalu buka: `http://localhost:3000/index.html`

---

## 🚀 Cara Menjalankan Setelah Install (Daily Use)

```bash
# 1. Masuk ke folder project
cd project-knowladgebot

# 2. Aktifkan venv
source venv/Scripts/activate  # Windows
# atau
source venv/bin/activate      # Mac/Linux

# 3. Jalankan server
python app.py

# 4. Buka index.html di browser
```

---

## 🛑 Cara Stop & Keluar

```bash
# Stop server
Ctrl+C

# Keluar dari venv (opsional)
deactivate
```

---

## 📁 Struktur Project
```
project-knowladgebot/
├── app.py                  # Entry point FastAPI
├── requirements.txt        # Daftar dependencies
├── README.md
├── index.html              # Frontend chatbot
├── venv/                   # Virtual environment (jangan di-commit)
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
├── chroma_db/              # ChromaDB vector store (auto-generated)
└── chat_history.db         # SQLite database (auto-generated)
```

---

## 🔑 Catatan Penting

### Database & Vector Store
- File `chat_history.db` dan folder `chroma_db/` akan dibuat otomatis saat pertama kali dijalankan
- Jika ingin rebuild ChromaDB, hapus folder `chroma_db/` dan restart server

### Knowledge Base
- Semua dokumen di folder `data/` akan di-index otomatis
- Untuk update knowledge base: tambah/edit file di `data/`, lalu hapus `chroma_db/` dan restart server

### Troubleshooting
**Error ChromaDB di Python 3.14:**
```bash
# Install Python 3.11, lalu bikin venv baru:
py -3.11 -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```

## 📄 Lisensi
MIT License - Silakan digunakan dan dimodifikasi sesuai kebutuhan.
