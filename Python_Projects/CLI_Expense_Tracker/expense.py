import csv
from datetime import datetime

class Expense:
    def __init__(self, amount, category, description):
        self.date = datetime.now().strftime("%Y-%m-%d")
        self.amount = float(amount)
        self.category = category
        self.description = description
    
    def to_list(self):
        return [self.date, self.amount, self.category, self.description]
