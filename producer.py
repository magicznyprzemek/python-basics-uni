import csv
import uuid

FILE_NAME = 'tasks.csv'

def add_task():
    task_id = str(uuid.uuid4())
    task_status = 'pending'
    task = [task_id, task_status]

    # Sprawdzenie, czy plik istnieje i nagłówki są zapisane
    try:
        with open(FILE_NAME, 'r') as f:
            pass
    except FileNotFoundError:
        with open(FILE_NAME, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['id', 'status'])

    # Dodanie nowego zadania
    with open(FILE_NAME, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(task)
        print(f"Added task with ID: {task_id}")

if __name__ == "__main__":
    add_task()
