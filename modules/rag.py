import os
from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage,
    PromptTemplate,
)
from llama_index.core.postprocessor import SimilarityPostprocessor

from .config import setup_llm

DATA_DIR    = "./data"
STORAGE_DIR = "./storage"

def get_index() -> VectorStoreIndex:
    if os.path.exists(STORAGE_DIR) and os.listdir(STORAGE_DIR):
        print("📂 Memuat index dari cache...")
        storage_context = StorageContext.from_defaults(persist_dir=STORAGE_DIR)
        index = load_index_from_storage(storage_context)
    else:
        print("🔨 Membangun index baru dari ./data ...")
        if not os.path.exists(DATA_DIR):
            raise FileNotFoundError(f"Folder '{DATA_DIR}' tidak ditemukan.")

        documents = SimpleDirectoryReader(
            input_dir=DATA_DIR,
            recursive=True,
            required_exts=[".txt"],
        ).load_data()

        if not documents:
            raise ValueError(f"Tidak ada file .txt di folder '{DATA_DIR}'.")

        print(f"✅ {len(documents)} dokumen berhasil dimuat.")
        index = VectorStoreIndex.from_documents(documents, show_progress=True)
        index.storage_context.persist(persist_dir=STORAGE_DIR)
        print(f"💾 Index disimpan ke '{STORAGE_DIR}'.")

    return index

def build_query_engine(index: VectorStoreIndex):
    qa_prompt_tmpl = (
        "Anda adalah Rumino. Gunakan dokumen referensi berikut HANYA sebagai sumber jawabanmu.\n"
        "---------------------\n"
        "{context_str}\n"
        "---------------------\n"
        "ATURAN MUTLAK:\n"
        "1. JANGAN PERNAH menyalin atau mengetik ulang isi dokumen referensi di atas! \n"
        "2. LANGSUNG jawab pertanyaan User berdasarkan intisarinya saja. Jangan bertele-tele.\n"
        "3. Sapa dengan ramah (Halo Kak!) dan gunakan emoji.\n"
        "4. Jika menjelaskan prosedur, buat dalam bentuk list angka (1, 2, 3).\n\n"
        "Pesan User: {query_str}\n"
        "Balasan Rumino:\n"
    )
    qa_prompt = PromptTemplate(qa_prompt_tmpl)

    query_engine = index.as_query_engine(
        streaming=True,
        similarity_top_k=5,
        text_qa_template=qa_prompt,
        node_postprocessors=[
            SimilarityPostprocessor(similarity_cutoff=0.1) 
        ],
    )
    return query_engine

class SafeQueryEngine:
    FALLBACK = (
        "Maaf ya Kak, Rumino belum punya info spesifik soal itu... 😅 "
        "Silakan cek Instagram @blsdm.komdigi.surabaya atau hubungi kantor di (031) 8011944 ya!"
    )

    def __init__(self, engine):
        self._engine = engine

    def query(self, text: str):
        response = self._engine.query(text)
        return _SafeResponse(response, self.FALLBACK)

class _SafeResponse:
    def __init__(self, original, fallback: str):
        self._original = original
        self._fallback = fallback

    @property
    def response_gen(self):
        yielded_any = False
        for token in self._original.response_gen:
            if token:
                yielded_any = True
                yield token
        if not yielded_any:
            print("⚠️  response_gen kosong — menggunakan fallback")
            yield self._fallback

def init_rag_pipeline() -> SafeQueryEngine:
    setup_llm()
    index = get_index()
    engine = build_query_engine(index)
    print("🤖 Rumino RAG siap digunakan.")
    return SafeQueryEngine(engine)

def reindex() -> SafeQueryEngine:
    import shutil
    if os.path.exists(STORAGE_DIR):
        shutil.rmtree(STORAGE_DIR)
        print(f"🗑️  Cache lama di '{STORAGE_DIR}' dihapus.")
    return init_rag_pipeline()