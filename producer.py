import sqlite3
import uuid

DB_NAME = 'tasks.db'

def add_task():
    task_id = str(uuid.uuid4())
    task_status = 'pending'


    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id TEXT PRIMARY KEY,
        status TEXT NOT NULL
    )
    """)

    cursor.execute("INSERT INTO tasks (id, status) VALUES (?, ?)", (task_id, task_status))
    conn.commit()

    print(f"dodano ID: {task_id}")

    conn.close()

if __name__ == "__main__":
    add_task()
