# test_rag.py
from modules.rag import init_rag_pipeline

print("Menyiapkan mesin RAG dan ChromaDB...")
bot_engine = init_rag_pipeline()

# Mari kita tes dengan pertanyaan yang jawabannya ada di dalam dokumen panjang
pertanyaan = "Apa saja syarat spesifikasi laptop untuk ikut pelatihan Junior Network Administrator?"

print(f"\nUser bertanya: '{pertanyaan}'")
print("Bot sedang berpikir dan membalas...\n")
print("Jawaban: ", end="")

# Memanggil fungsi query
jawaban = bot_engine.query(pertanyaan)

# Mencetak jawaban kata demi kata (streaming)
for kata in jawaban.response_gen:
    print(kata, end="", flush=True)

print("\n\n✅ Pengujian selesai!")