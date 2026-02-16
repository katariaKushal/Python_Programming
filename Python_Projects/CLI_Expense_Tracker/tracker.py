import csv
import os
from expense import Expense

class ExpenseTracker:
    def __init__(self, filename="expenses.csv"):
        self.filename = os.path.join(os.path.dirname(__file__), filename)
        self._init_file()
    
    def _init_file(self):
        if not os.path.exists(self.filename):
            with open(self.filename, 'w', newline='') as f:
                csv.writer(f).writerow(['Date', 'Amount', 'Category', 'Description'])
    
    def add_expense(self, amount, category, description):
        expense = Expense(amount, category, description)
        with open(self.filename, 'a', newline='') as f:
            csv.writer(f).writerow(expense.to_list())
        print(f"✓ Added: ${amount} - {category}")
    
    def delete_expense(self, index):
        expenses = self._read_all()
        if 0 <= index < len(expenses):
            expenses.pop(index)
            self._write_all(expenses)
            print("✓ Deleted")
        else:
            print("✗ Invalid index")
    
    def monthly_summary(self, month=None, year=None):
        if not month:
            month = int(input("Month (1-12): "))
        if not year:
            year = int(input("Year: "))
        
        expenses = self._read_all()
        total = sum(float(e[1]) for e in expenses if e[0].startswith(f"{year}-{month:02d}"))
        print(f"\n📊 Total for {month}/{year}: ${total:.2f}")
    
    def view_all(self):
        expenses = self._read_all()
        if not expenses:
            print("No expenses found")
            return
        print("\n" + "="*60)
        for i, e in enumerate(expenses):
            print(f"{i}. {e[0]} | ${e[1]} | {e[2]} | {e[3]}")
        print("="*60)
    
    def _read_all(self):
        with open(self.filename, 'r') as f:
            return list(csv.reader(f))[1:]
    
    def _write_all(self, expenses):
        with open(self.filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Date', 'Amount', 'Category', 'Description'])
            writer.writerows(expenses)
