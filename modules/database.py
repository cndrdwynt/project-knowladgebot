import sqlite3
import json
from datetime import datetime

DB_NAME = 'chat_history.db'

def init_db():
    try:
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        # Tabel riwayat chat
        c.execute('''
            CREATE TABLE IF NOT EXISTS riwayat (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                waktu TEXT,
                session_id TEXT,
                nama TEXT,
                kontak TEXT,
                pesan_user TEXT,
                jawaban_bot TEXT,
                response_time REAL,
                user_agent TEXT
            )
        ''')
        # Tabel sessions 
        c.execute('''
            CREATE TABLE IF NOT EXISTS sessions (
                session_id TEXT PRIMARY KEY,
                state TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()
        print("✔ Database initialized")
    except Exception as e:
        print(f"Database Error: {e}")

def get_session(session_id: str):
    """Ambil state session dari DB. Return None kalau belum ada."""
    try:
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute("SELECT state FROM sessions WHERE session_id = ?", (session_id,))
        row = c.fetchone()
        conn.close()
        if row:
            return json.loads(row[0])
        return None
    except Exception as e:
        print(f"get_session Error: {e}")
        return None

def save_session(session_id: str, state: dict):
    """Simpan / update state session ke DB."""
    try:
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        c.execute('''
            INSERT INTO sessions (session_id, state, updated_at)
            VALUES (?, ?, ?)
            ON CONFLICT(session_id) DO UPDATE SET
                state = excluded.state,
                updated_at = excluded.updated_at
        ''', (session_id, json.dumps(state), updated_at))
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"save_session Error: {e}")

def simpan_log(session_id, nama, kontak, pesan, jawaban, response_time=0, user_agent=""):
    try:
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        c.execute('''INSERT INTO riwayat 
                     (waktu, session_id, nama, kontak, pesan_user, jawaban_bot, response_time, user_agent) 
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                  (waktu, session_id, nama, kontak, pesan, jawaban, response_time, user_agent))
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Log Error: {e}")