import csv
import time

FILE_NAME = 'tasks.csv'

def consume_task():
    while True:
        tasks = []

        # Wczytanie zadań z pliku
        try:
            with open(FILE_NAME, 'r') as f:
                reader = csv.reader(f)
                tasks = list(reader)
        except FileNotFoundError:
            print("No tasks found. Waiting...")
            time.sleep(5)
            continue

        if len(tasks) <= 1:
            print("No pending tasks. Waiting...")
            time.sleep(5)
            continue

        # Przetwarzanie pierwszego zadania o statusie "pending"
        for i, task in enumerate(tasks[1:], start=1):
            if task[1] == 'pending':
                print(f"Processing task ID: {task[0]}")
                tasks[i][1] = 'in_progress'

                # Aktualizacja statusu na in_progress
                with open(FILE_NAME, 'w', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerows(tasks)

                # Wykonanie zadania (symulacja)
                time.sleep(30)
                print(f"Task ID: {task[0]} completed.")
                tasks[i][1] = 'done'

                # Aktualizacja statusu na done
                with open(FILE_NAME, 'w', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerows(tasks)

                break
        else:
            print("No pending tasks. Waiting...")
            time.sleep(5)

if __name__ == "__main__":
    consume_task()
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        average_mark = sum(self.marks) / len(self.marks)
        return average_mark > 50

student1 = Student("A", [70, 65, 80])
student2 = Student("B", [40, 45, 35])

print(student1.is_passed())
print(student2.is_passed())
