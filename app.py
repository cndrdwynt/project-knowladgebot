import re
import urllib.parse
from fastapi import FastAPI, HTTPException, Header
from fastapi.responses import JSONResponse, StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from collections import defaultdict
from datetime import datetime, timedelta

from modules.database import init_db, simpan_log, get_session, save_session
from modules.rag import init_rag_pipeline

init_db()
print("Sedang memuat otak AI...")
query_engine = init_rag_pipeline()
print("Siap melayani!")

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

API_KEY = "BLSDM_2026_RahasiaBanget!@#"
rate_limit_store = defaultdict(list)
MAX_REQUESTS_PER_MINUTE = 10

class ChatRequest(BaseModel):
    prompt: str
    session_id: str

quick_replies = [
    {"text": "🏢 Profil & Lokasi", "value": "Jelaskan profil singkat BLSDM Komdigi dan dimana lokasi kantornya?"},
    {"text": "💼 Karir & Magang", "value": "Jelaskan secara singkat info lowongan kerja dan program magang yang tersedia"},
    {"text": "🎓 Program Pelatihan", "value": "Apa saja program pelatihan unggulan yang tersedia?"}
]

def check_rate_limit(session_id: str) -> bool:
    now = datetime.now()
    cutoff = now - timedelta(minutes=1)
    rate_limit_store[session_id] = [ts for ts in rate_limit_store[session_id] if ts > cutoff]
    if len(rate_limit_store[session_id]) >= MAX_REQUESTS_PER_MINUTE:
        return False
    rate_limit_store[session_id].append(now)
    return True

@app.post("/chat")
async def chat(request: ChatRequest, x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    if not check_rate_limit(request.session_id):
        raise HTTPException(status_code=429, detail="Terlalu banyak request. Tunggu sebentar ya!")

    sid = request.session_id
    msg = request.prompt.strip()

    # Ambil session dari DB (persistent, tidak hilang kalau server restart)
    state = get_session(sid)
    if state is None:
        state = {'step': 0, 'data': {'nama': 'User', 'kontak': '-'}}
        save_session(sid, state)

    if state['step'] == 0:
        state['step'] = 1
        save_session(sid, state)
        return JSONResponse({"type": "json", "message": "Halo Sobat Inovator! Rumino siap membantu. 🤖\n\nSiapa nama Kakak?", "quick_replies": []})
    elif state['step'] == 1:
        state['data']['nama'] = msg
        state['step'] = 2
        save_session(sid, state)
        return JSONResponse({"type": "json", "message": f"Halo Kak {msg}! 👋\n\nBoleh minta Email/WA untuk jaga-jaga?", "quick_replies": []})
    elif state['step'] == 2:
        state['data']['kontak'] = msg
        state['step'] = 3
        save_session(sid, state)
        return JSONResponse({"type": "json", "message": "Siap! Silakan tanya apa saja tentang UPT BLSDM Komdigi Surabaya.", "quick_replies": quick_replies})

    user_nama = state['data']['nama']
    print(f">> {user_nama}: {msg}")

    async def event_stream():
        start_time = datetime.now()
        full_response = ""

        try:
            # Keyword panjang → cukup cek substring
            substring_keywords = [
                "hubungi", "contact", "kontak", "whatsapp",
                "customer service", "nomor hp", "nomor telp", "nomor telepon"
            ]
            # Keyword pendek → harus kata utuh (biar "wisuda" tidak trigger "wa")
            whole_word_keywords = ["wa", "cp", "cs", "admin", "nomor"]

            msg_lower = msg.lower()
            wants_contact = (
                any(kw in msg_lower for kw in substring_keywords) or
                any(re.search(rf'\b{kw}\b', msg_lower) for kw in whole_word_keywords)
            )

            if wants_contact:
                full_response = (
                    "Baik! Berikut informasi kontak BLSDM Komdigi Surabaya:\n\n"
                    "📱 Instagram: @bpsdmp.surabaya (untuk info lowongan & pengumuman terkini)\n"
                    "📞 Telepon Kantor: (031) 8011944 (Senin-Jumat, 08.00-16.00 WIB)\n"
                    "📍 Alamat: Jl. Raya Ketajen No.36, Gedangan, Sidoarjo, Jawa Timur 61254\n\n"
                    "Untuk pertanyaan lebih lanjut, silakan hubungi admin melalui tombol di bawah ini:"
                )
                yield full_response

                pesan_wa = urllib.parse.quote(f"Halo Admin, saya {user_nama}. Saya ingin bertanya tentang BLSDM Komdigi.")
                link_wa = f"https://wa.me/6281234567890?text={pesan_wa}"

                yield (
                    '\n\n<div style="margin-top: 16px; padding: 12px; background: linear-gradient(135deg, #25D366 0%, #128C7E 100%); border-radius: 12px; box-shadow: 0 4px 12px rgba(37, 211, 102, 0.3);">'
                    f'<a href="{link_wa}" target="_blank" style="display: flex; align-items: center; justify-content: center; gap: 10px; color: white; text-decoration: none; font-weight: 600; font-size: 15px;">'
                    '<svg width="24" height="24" viewBox="0 0 24 24" fill="white">'
                    '<path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/>'
                    '</svg>'
                    '<span>💬 Chat dengan Admin via WhatsApp</span>'
                    '</a></div>'
                )

                response_time = (datetime.now() - start_time).total_seconds()
                simpan_log(sid, user_nama, state['data']['kontak'], msg,
                           full_response + " [WA Button]", response_time)

            else:
                response = query_engine.query(msg)

                for text in response.response_gen:
                    full_response += text
                    yield text

                response_time = (datetime.now() - start_time).total_seconds()
                simpan_log(sid, user_nama, state['data']['kontak'], msg, full_response, response_time)

        except Exception as e:
            yield f"Terjadi kesalahan teknis: {str(e)}"

    return StreamingResponse(event_stream(), media_type="text/plain")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)