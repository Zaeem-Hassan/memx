import sqlite3
from datetime import datetime

class MemoryDB:
    def __init__(self, path="memx.db"):
        self.conn = sqlite3.connect(path)
        self._create_table()

    def _create_table(self):
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS memories (
            id TEXT PRIMARY KEY,
            user_id TEXT,
            text TEXT,
            created_at TEXT,
            updated_at TEXT
        )
        """)
        self.conn.commit()

    def insert(self, memory):
        self.conn.execute("""
        INSERT INTO memories VALUES (?, ?, ?, ?, ?)
        """, (
            memory["id"],
            memory["user_id"],
            memory["text"],
            memory["created_at"],
            memory["updated_at"]
        ))
        self.conn.commit()

    def delete(self, memory_id):
        self.conn.execute("DELETE FROM memories WHERE id=?", (memory_id,))
        self.conn.commit()

    def get_all(self, user_id):
        cur = self.conn.execute("SELECT * FROM memories WHERE user_id=?", (user_id,))
        rows = cur.fetchall()
        return [
            {
                "id": r[0],
                "user_id": r[1],
                "text": r[2],
                "created_at": r[3],
                "updated_at": r[4]
            }
            for r in rows
        ]