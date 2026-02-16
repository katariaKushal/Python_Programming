import sqlite3
from student import Student

class StudentDatabase:
    def __init__(self, db_name="students.db"):
        import os
        db_path = os.path.join(os.path.dirname(__file__), db_name)
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self._create_table()
    
    def _create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER,
                grade TEXT
            )
        ''')
        self.conn.commit()
    
    def add_student(self, student):
        try:
            self.cursor.execute('INSERT INTO students VALUES (?, ?, ?, ?)', student.to_tuple())
            self.conn.commit()
            print("✓ Student added")
        except sqlite3.IntegrityError:
            print("✗ Student ID already exists")
    
    def update_student(self, student_id, name, age, grade):
        self.cursor.execute('UPDATE students SET name=?, age=?, grade=? WHERE id=?', 
                          (name, age, grade, student_id))
        self.conn.commit()
        print("✓ Student updated" if self.cursor.rowcount else "✗ Student not found")
    
    def delete_student(self, student_id):
        self.cursor.execute('DELETE FROM students WHERE id=?', (student_id,))
        self.conn.commit()
        print("✓ Student deleted" if self.cursor.rowcount else "✗ Student not found")
    
    def search_by_id(self, student_id):
        self.cursor.execute('SELECT * FROM students WHERE id=?', (student_id,))
        result = self.cursor.fetchone()
        if result:
            print(f"\n{Student(*result)}")
        else:
            print("✗ Student not found")
    
    def view_all(self):
        self.cursor.execute('SELECT * FROM students')
        students = self.cursor.fetchall()
        if not students:
            print("No students found")
            return
        print("\n" + "="*60)
        for s in students:
            print(Student(*s))
        print("="*60)
    
    def close(self):
        self.conn.close()
