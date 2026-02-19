import os
import chromadb
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext
from llama_index.vector_stores.chroma import ChromaVectorStore
from modules.config import setup_llm

DB_PATH = "./chroma_db"
DATA_PATH = "./data"

def init_rag_pipeline():
    setup_llm()

    # Setup ChromaDB
    db = chromadb.PersistentClient(path=DB_PATH)
    chroma_collection = db.get_or_create_collection("pengetahuan_perusahaan")
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)

    # Buat folder data kalau belum ada
    if not os.path.exists(DATA_PATH):
        os.makedirs(DATA_PATH)

    # Cek apakah ada file di folder data
    files = [f for f in os.listdir(DATA_PATH) if not f.startswith('.')]
    if not files:
        raise RuntimeError(
            f"❌ Folder '{DATA_PATH}' kosong! "
            "Tambahkan dokumen pengetahuan (.txt / .pdf / .docx) ke folder tersebut, "
            "lalu jalankan ulang aplikasi."
        )

    docs = SimpleDirectoryReader(DATA_PATH).load_data()

    if not docs:
        raise RuntimeError(
            f"❌ Tidak ada dokumen yang berhasil dibaca dari folder '{DATA_PATH}'. "
            "Pastikan formatnya didukung: .txt, .pdf, .docx, .md"
        )

    print(f"✔ {len(docs)} dokumen berhasil dimuat dari '{DATA_PATH}'")

    index = VectorStoreIndex.from_documents(docs, storage_context=storage_context)

    return index.as_query_engine(
        similarity_top_k=5,
        response_mode="compact",
        streaming=True
    )