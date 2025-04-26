import sqlite3
class Student:
    def __init__(self, name, lastname, midlname, group, grade):
        self.name = name
        self.lastname = lastname
        self.midlname = midlname
        self.group = group
        self.grade = grade
class Student_BD:
    def __init__(self, db_name = "Student.db"):
        self.db_name = db_name
        self.con = sqlite3.connect(self.db_name)
        self.cursor = self.con.cursor()
        self.create_table()
    def create_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS students
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            lastname TEXT NOT NULL,
                            midlname TEXT,
                            group_name TEXT NOT NULL,
                            grade1 INTEGER NOT NULL,
                            grade2 INTEGER NOT NULL,
                            grade3 INTEGER NOT NULL,
                            grade4 INTEGER NOT NULL
                            )
                        """)
        self.con.commit()
    def add_student(self,student):
        self.cursor.execute("INSERT INTO students (name, lastname, midlname, group_name, grade1, grade2, grade3, grade4) VALUES (?,?,?,?,?,?,?,?)",
                      (student.name, student.lastname, student.midlname, student.group, student.grade[0], student.grade[1], student.grade[2],
                                student.grade[3]))
        self.con.commit()
    def info_all_student(self):
        self.cursor.execute("SELECT * FROM students")
        print(self.cursor.fetchall())
    def info_id_student(self, student_id):
        self.cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
        data = self.cursor.fetchone()
        if data:
            name = data[1]
            lastname = data[2]
            midlname = data[3]
            group = data[4]
            grade1 = data[5]
            grade2 = data[6]
            grade3 = data[7]
            grade4 = data[8]
            student = Student(name, lastname, midlname, group, [grade1, grade2, grade3, grade4])
            avarag = sum(student.grade) / len(student.grade)
            print(data, avarag)
        else:
            print("Студент не найден")
    def redactor_student(self, student_id, student):
        self.cursor.execute("UPDATE students SET name = ?, lastname = ?, midlname = ?, group_name = ?, grade1 = ?, grade2 = ?, grade3 = ?, grade4 = ? WHERE id = ?",
                            (student.name, student.lastname, student.midlname, student.group, student.grade[0], student.grade[1], student.grade[2],
                             student.grade[3], student_id))
        self.con.commit()
    def delet_student(self, student_id):
        self.cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
        self.con.commit()
    def average_grade_group(self, group):
        self.cursor.execute("SELECT * FROM students WHERE group_name = ?",(group,))
        data = self.cursor.fetchall()
        total_averag = 0
        count_student = 0
        if data:
            for i in data:
                name = i[1]
                lastname = i[2]
                midlname = i[3]
                group_name = i[4]
                grade1 = i[5]
                grade2 = i[6]
                grade3 = i[7]
                grade4 = i[8]
                student = Student(name, lastname, midlname, group_name, [grade1, grade2, grade3, grade4])
                avarag = sum(student.grade) / len(student.grade)
                total_averag += avarag
                count_student += 1
            if count_student > 0:
                group_averag = total_averag / count_student
                print(f"Средний балл студентов: {group_averag}")
        else:
            print("Группа не найдена")
db = Student_BD()
student1 = Student("Иван", "Петров", "Сергеевич", "221", [4, 5, 4, 5])
student2 = Student("Владимир", "Заблоцкий", "Александрович", "643", [5, 5, 5, 5])
student3 = Student("Петр", "Сидоров", "Иванович", "221", [3, 4, 3, 4])
student4 = Student("Анна", "Смирнова", "Дмитриевна", "223", [4, 4, 4, 4])
student5 = Student("Сергей", "Кузнецов", "Владимирович", "224", [5, 4, 5, 4])
db.add_student(student1)
db.add_student(student2)
db.add_student(student3)
db.add_student(student4)
db.add_student(student5)
print("Все студенты:")
db.info_all_student()
print("Студент с ID = 1:")
db.info_id_student(1)
new_student = Student("Елена", "Федорова", "Петровна", "225", [3, 3, 3, 3])
db.redactor_student(2, new_student)
print("Студент с ID = 2 после редактирования:")
db.info_id_student(2)
db.delet_student(3)
print("Все студенты после удаления студента с ID = 3:")
db.info_all_student()
print("Средний балл для группы 221:")
db.average_grade_group("221")
db.con.close()
import psutil
import sqlite3
from datetime import datetime
class System_monitor:
    def __init__(self, db_name = "monitoring_system.db"):
        self.db_name = db_name
        self.con = sqlite3.connect(self.db_name)
        self.cursor = self.con.cursor()
        self.create_table()
    def create_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS information_system
                            (time DATATIME PRIMARY KEY,
                            cpu REAL NOT NULL,
                            memory REAL NOT NULL,
                            disk REAL NOT NULL
                            )
                        """)
        self.con.commit()
    def information_system(self):
        cpu = psutil.cpu_percent()
        memory = psutil.virtual_memory().percent
        disk = psutil.disk_usage('C:\\').percent
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return time, cpu, memory, disk
    def insert_bd(self, time, cpu, memory, disk):
        self.cursor.execute("INSERT INTO information_system (time, cpu, memory, disk) VALUES (?, ?, ?, ?)", (time, cpu, memory, disk))
        self.con.commit()
    def information_display(self, time, cpu, memory, disk):
        print(f"Время: {time}")
        print(f"CPU информация: {cpu}%")
        print(f"Оперативная память: {memory}%")
        print(f"Диск {disk}%")
    def run_monitoring(self):
        time, cpu, memory, disk = self.information_system()
        self.insert_bd(time, cpu, memory, disk)
        self.information_display(time, cpu, memory, disk)
    def close(self):
        self.con.close()
monitor = System_monitor()
monitor.run_monitoring()
monitor.close()