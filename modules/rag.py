import os
import chromadb
from llama_index.core import (
    VectorStoreIndex,
    PromptTemplate,
)
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core.postprocessor import SimilarityPostprocessor

from .config import setup_llm

CHROMA_DIR = "./database_chroma"
COLLECTION_NAME = "pengetahuan_blsdm"

def get_index() -> VectorStoreIndex:
    print(f"📂 Menghubungkan ke ChromaDB di folder {CHROMA_DIR}...")
    
    # 1. Inisialisasi koneksi ke database Chroma yang sudah kita buat sebelumnya
    db = chromadb.PersistentClient(path=CHROMA_DIR)
    chroma_collection = db.get_collection(COLLECTION_NAME)
    
    # 2. Jadikan koleksi Chroma tersebut sebagai Vector Store untuk LlamaIndex
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    
    # 3. Load index dari vector store (Sangat cepat karena tidak baca file teks lagi)
    index = VectorStoreIndex.from_vector_store(vector_store)
    
    print("✅ Berhasil memuat index dari ChromaDB!")
    return index

def build_query_engine(index: VectorStoreIndex):
    qa_prompt_tmpl_str = (
        "Konteks informasi ada di bawah ini.\n"
        "---------------------\n"
        "{context_str}\n"
        "---------------------\n"
        "Berdasarkan konteks tersebut, jawab pertanyaan ini: {query_str}\n"
    )
    qa_prompt = PromptTemplate(qa_prompt_tmpl_str)

    query_engine = index.as_query_engine(
        similarity_top_k=3,
        text_qa_template=qa_prompt,
        node_postprocessors=[
            SimilarityPostprocessor(similarity_cutoff=0.1) 
        ],
        streaming=True
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
    print("🤖 Rumino RAG siap digunakan dengan ChromaDB (Opsi A Selesai!).")
    return SafeQueryEngine(engine)