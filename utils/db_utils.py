import sqlite3
import os
from pathlib import Path

DB_PATH = "db/activity_log.db"

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS mouse_keyboard (
                          id INTEGER PRIMARY KEY AUTOINCREMENT,
                          event_type TEXT NOT NULL,
                          timestamp TEXT NOT NULL)''')
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS activity_log (
                          id INTEGER PRIMARY KEY AUTOINCREMENT,
                          application TEXT NOT NULL,
                          url TEXT,
                          timestamp TEXT NOT NULL)''')
        conn.commit()

def log_event(event_type):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO mouse_keyboard (event_type, timestamp) VALUES (?, datetime('now'))", (event_type,))
        conn.commit()

def log_application(application, url=None):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO activity_log (application, url, timestamp) VALUES (?, ?, datetime('now'))", (application, url))
        conn.commit()
        
def get_counts():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM mouse_keyboard WHERE event_type = 'mouse_click'")
        mouse_clicks = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM mouse_keyboard WHERE event_type = 'key_press'")
        key_presses = cursor.fetchone()[0]
        
    return mouse_clicks, key_presses

def get_recent_activity(limit=10):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT application, url, timestamp FROM activity_log ORDER BY timestamp DESC LIMIT ?", (limit,))
        rows = cursor.fetchall()
        return [{"application": row[0], "url": row[1], "timestamp": row[2]} for row in rows]


init_db()  # Initialize database tables on first run
