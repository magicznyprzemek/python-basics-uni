import sqlite3
import time

DB_NAME = 'tasks.db'

def consume_task():
    while True:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id TEXT PRIMARY KEY,
            status TEXT NOT NULL
        )
        """)

        cursor.execute("SELECT id FROM tasks WHERE status = 'pending' LIMIT 1")
        task = cursor.fetchone()

        if not task:
            print("brak tasków")
            conn.close()
            time.sleep(5)
            continue

        task_id = task[0]
        print(f"przetwarzanie id: {task_id}")

        cursor.execute("UPDATE tasks SET status = 'in_progress' WHERE id = ?", (task_id,))
        conn.commit()

        time.sleep(30)

        print(f"ukończono id: {task_id}.")

        cursor.execute("UPDATE tasks SET status = 'done' WHERE id = ?", (task_id,))
        conn.commit()

        conn.close()

if __name__ == "__main__":
    consume_task()
