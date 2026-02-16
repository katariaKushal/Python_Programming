from datetime import datetime

class Task:
    def __init__(self, title, deadline, priority, completed=False):
        self.title = title
        self.deadline = deadline
        self.priority = priority
        self.completed = completed
    
    def to_dict(self):
        return {
            'title': self.title,
            'deadline': self.deadline,
            'priority': self.priority,
            'completed': self.completed
        }
    
    @staticmethod
    def from_dict(data):
        return Task(data['title'], data['deadline'], data['priority'], data['completed'])
    
    def __str__(self):
        status = "✓" if self.completed else "○"
        return f"{status} [{self.priority}] {self.title} (Due: {self.deadline})"
