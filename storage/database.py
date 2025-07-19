import sqlite3

def init_db():
    conn = sqlite3.connect("threats.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS threats (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        platform TEXT,
        username TEXT,
        content TEXT,
        threat TEXT,
        score REAL,
        url TEXT,
        timestamp TEXT
    )''')
    conn.commit()
    conn.close()

def save_threat(post, threat, score):
    conn = sqlite3.connect("threats.db")
    c = conn.cursor()
    c.execute('''INSERT INTO threats 
        (platform, username, content, threat, score, url, timestamp)
        VALUES (?, ?, ?, ?, ?, ?, ?)''',
        (post["platform"], post["username"], post["content"], threat, score, post["url"], post["timestamp"]))
    conn.commit()
    conn.close()

def get_all_threats():
    conn = sqlite3.connect("threats.db")
    c = conn.cursor()
    c.execute("SELECT * FROM threats ORDER BY id DESC")
    return c.fetchall()
