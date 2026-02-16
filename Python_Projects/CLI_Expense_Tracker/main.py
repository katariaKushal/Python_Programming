from tracker import ExpenseTracker

def main():
    tracker = ExpenseTracker()
    
    while True:
        print("\n💰 EXPENSE TRACKER")
        print("1. Add Expense")
        print("2. View All")
        print("3. Delete Expense")
        print("4. Monthly Summary")
        print("5. Exit")
        
        choice = input("\nChoice: ")
        
        if choice == '1':
            amount = input("Amount: ")
            category = input("Category: ")
            description = input("Description: ")
            tracker.add_expense(amount, category, description)
        elif choice == '2':
            tracker.view_all()
        elif choice == '3':
            tracker.view_all()
            index = int(input("Index to delete: "))
            tracker.delete_expense(index)
        elif choice == '4':
            tracker.monthly_summary()
        elif choice == '5':
            break

if __name__ == "__main__":
    main()
