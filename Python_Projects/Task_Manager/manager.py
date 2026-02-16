import json
import os
from task import Task

class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = os.path.join(os.path.dirname(__file__), filename)
        self.tasks = self._load()
    
    def add_task(self, title, deadline, priority):
        task = Task(title, deadline, priority)
        self.tasks.append(task)
        self._save()
        print("✓ Task added")
    
    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self._save()
            print("✓ Task deleted")
        else:
            print("✗ Invalid index")
    
    def toggle_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = not self.tasks[index].completed
            self._save()
            print("✓ Status updated")
        else:
            print("✗ Invalid index")
    
    def view_tasks(self):
        if not self.tasks:
            print("No tasks found")
            return
        print("\n" + "="*60)
        for i, task in enumerate(self.tasks):
            print(f"{i}. {task}")
        print("="*60)
    
    def _load(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return [Task.from_dict(t) for t in json.load(f)]
        return []
    
    def _save(self):
        with open(self.filename, 'w') as f:
            json.dump([t.to_dict() for t in self.tasks], f, indent=2)
