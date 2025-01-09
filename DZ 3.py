from datetime import datetime


class Task:
    def __init__(self, title, description, deadline):
        """
        Ініціалізує нове завдання.
        :param title: Назва завдання.
        :param description: Опис завдання.
        :param deadline: Дедлайн завдання (у форматі 'ДД-ММ-РРРР').
        """
        self.title = title
        self.description = description
        self.deadline = datetime.strptime(deadline, "%d-%m-%Y")
        self.is_completed = False

    def mark_as_completed(self):
        """Позначає завдання як виконане."""
        self.is_completed = True

    def __str__(self):
        """Повертає строкове представлення завдання."""
        status = "Виконано" if self.is_completed else "Не виконано"
        deadline_str = self.deadline.strftime("%d-%m-%Y")
        return f"[{status}] {self.title} (Дедлайн: {deadline_str}) - {self.description}"


class TaskManager:
    def __init__(self):
        """Ініціалізує менеджер завдань."""
        self.tasks = []

    def add_task(self, task):
        """Додає нове завдання до списку.
        :param task: Об'єкт класу Task.
        """
        self.tasks.append(task)
        print(f"Завдання '{task.title}' додано.")

    def remove_task(self, title):
        """Видаляє завдання за назвою.
        :param title: Назва завдання.
        """
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                print(f"Завдання '{title}' видалено.")
                return
        print(f"Завдання '{title}' не знайдено.")

    def mark_task_as_completed(self, title):
        """Позначає завдання як виконане.
        :param title: Назва завдання.
        """
        for task in self.tasks:
            if task.title == title:
                task.mark_as_completed()
                print(f"Завдання '{title}' позначено як виконане.")
                return
        print(f"Завдання '{title}' не знайдено.")

    def list_tasks(self):
        """Виводить список завдань."""
        if not self.tasks:
            print("Список завдань порожній.")
        else:
            print("Список завдань:")
            for task in self.tasks:
                print(f"- {task}")


# Приклад використання:
if __name__ == "__main__":
    manager = TaskManager()

    while True:
        print("\nМеню:")
        print("1. Додати завдання")
        print("2. Видалити завдання")
        print("3. Позначити завдання як виконане")
        print("4. Показати список завдань")
        print("0. Вийти")

        choice = input("Ваш вибір: ")

        if choice == "1":
            title = input("Назва завдання: ")
            description = input("Опис завдання: ")
            deadline = input("Дедлайн (ДД-ММ-РРРР): ")
            task = Task(title, description, deadline)
            manager.add_task(task)
        elif choice == "2":
            title = input("Назва завдання, яке потрібно видалити: ")
            manager.remove_task(title)
        elif choice == "3":
            title = input("Назва завдання, яке потрібно позначити як виконане: ")
            manager.mark_task_as_completed(title)
        elif choice == "4":
            manager.list_tasks()
        elif choice == "0":
            print("До побачення!")
            break
        else:
            print("Некоректний вибір, спробуйте ще раз.")