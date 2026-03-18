import chromadb
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext
from llama_index.vector_stores.chroma import ChromaVectorStore

# 1. Memanggil konfigurasi AI yang SAMA PERSIS dengan bot kamu
from modules.config import setup_llm 

print("1. Menyiapkan mesin AI (Menyamakan frekuensi dengan bot)...")
setup_llm()

print("2. Membaca seluruh file .txt dari folder 'data_mentah'...")
# LlamaIndex akan otomatis membaca dan memotong-motong dokumen dengan sangat cerdas
dokumen = SimpleDirectoryReader("data_mentah").load_data()

print(f"   -> Berhasil memuat {len(dokumen)} halaman dokumen.")
print("3. Membangun fondasi ChromaDB...")
klien_chroma = chromadb.PersistentClient(path="./database_chroma")
koleksi = klien_chroma.get_or_create_collection("pengetahuan_blsdm")

# Menghubungkan LlamaIndex ke Chroma
vector_store = ChromaVectorStore(chroma_collection=koleksi)
storage_context = StorageContext.from_defaults(vector_store=vector_store)

print("4. Menyusun teks menjadi Vektor dan menyimpan ke database (Mohon tunggu)...")
# Tahap ini menggunakan model AI lokalmu, jadi jauh lebih aman dari putus internet
index = VectorStoreIndex.from_documents(
    dokumen,
    storage_context=storage_context,
    show_progress=True
)

print("\n✅ SUPER SEKALI! Gedung Perpustakaan (ChromaDB) berhasil dibangun dan 100% sinkron dengan Bot kamu!")