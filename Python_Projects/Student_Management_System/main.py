from database import StudentDatabase
from student import Student

def main():
    db = StudentDatabase()
    
    while True:
        print("\n🎓 STUDENT MANAGEMENT SYSTEM")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Search by ID")
        print("5. View All Students")
        print("6. Exit")
        
        choice = input("\nChoice: ")
        
        if choice == '1':
            student_id = input("Student ID: ")
            name = input("Name: ")
            age = int(input("Age: "))
            grade = input("Grade: ")
            db.add_student(Student(student_id, name, age, grade))
        elif choice == '2':
            student_id = input("Student ID: ")
            name = input("New Name: ")
            age = int(input("New Age: "))
            grade = input("New Grade: ")
            db.update_student(student_id, name, age, grade)
        elif choice == '3':
            student_id = input("Student ID: ")
            db.delete_student(student_id)
        elif choice == '4':
            student_id = input("Student ID: ")
            db.search_by_id(student_id)
        elif choice == '5':
            db.view_all()
        elif choice == '6':
            db.close()
            break

if __name__ == "__main__":
    main()
