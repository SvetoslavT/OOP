from py_project import task
from task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, taski: Task):
        if task in self.tasks:
            return f"Task is already in the section {self.name}."
        self.tasks.append(taski.details())
        return f"Task {taski.details()} is added to the section"

    def complete_task(self, task_name: str):
        if task_name not in self.tasks:
            return f"Could not find task with the name {task_name}"
        task.Task.completed = True

    def clean_section(self):
        cleaned_tasks = len(self.tasks)
        self.tasks.clear()
        return f"Cleared {cleaned_tasks} tasks."

    def view_section(self):
        for taski in self.tasks:
            taski.details()



