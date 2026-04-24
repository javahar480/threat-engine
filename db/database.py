import sqlite3

conn = sqlite3.connect("threats.db", check_same_thread=False)
cur = conn.cursor()

def init_db():
    cur.execute("""
    CREATE TABLE IF NOT EXISTS alerts (
        id INTEGER PRIMARY KEY,
        timestamp TEXT,
        ip TEXT,
        threat TEXT,
        score INTEGER
    )
    """)
    conn.commit()

def insert_alert(ts, ip, threat, score):
    cur.execute(
        "INSERT INTO alerts VALUES (NULL, ?, ?, ?, ?)",
        (ts, ip, threat, score)
    )
    conn.commit()
