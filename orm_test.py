import unittest
from orm import *
from datetime import datetime, date



class TestStudent(unittest.TestCase):



    def setUp(self):
        # инициализируем бд
        conn.init("test_orm.db")
        Student.create_table()
        Course.create_table()
        Student_Course.create_table()

    def tearDown(self):
        # очищаем бд
        Student.drop_table()
        Course.drop_table()
        Student_Course.drop_table()          


    def test_add_student(self):
        student = add_student("Max", "Adams", 24, "Spb")
        cursor = conn.cursor()  # создаем обьект, для доступа к базе 
        cursor.execute(f'''select * from student where id={student.id} ''')
        st = cursor.fetchone() # получение данных из cursor
        self.assertEquals(st[1], "Max")
        self.assertEquals(st[2], "Adams")
        self.assertEquals(int(st[3]), 24)
        self.assertEquals(st[4], "Spb")

    def test_add_course(self):
        course = add_course("python", date(2021, 7, 21), date(2021, 12, 21))
        cursor = conn.cursor()  # создаем обьект, для доступа к базе 
        cursor.execute(f'''select * from course where id={course.id} ''')
        st = cursor.fetchone() # получение данных из cursor
        self.assertEquals(st[1], course.name)
        start = datetime.strptime(st[2], '%Y-%m-%d')
        end = datetime.strptime(st[3], '%Y-%m-%d')
        self.assertEquals(date(start.year, start.month, start.day), course.time_start)
        self.assertEquals(date(end.year, end.month, end.day), course.time_end)

    def test_delete_student(self):
        student = add_student("Max", "Adams", 24, "Spb")
        course = add_course("python", date(2021, 7, 21), date(2021, 12, 21))
        sc = add_student_course(student.id, course.id)
        delete_student(sc.id,student.id)

        cursor = conn.cursor()  # создаем обьект, для доступа к базе 
        cursor.execute(f'''select * from student where id={student.id} ''')
        st = cursor.fetchone()
        self.assertIsNone(st)
        cursor.execute(f'''select * from student_course where id={sc.id} ''')
        sc_sql = cursor.fetchone()
        self.assertIsNone(sc_sql)

    def test_add_student_course(self):
        student = add_student("Max", "Adams", 24, "Spb")
        course = add_course("python", date(2021, 7, 21), date(2021, 12, 21))
        sc = add_student_course(student.id,course.id)
        cursor = conn.cursor()
        cursor.execute(f'''select * from student_course where id={sc.id} ''')
        st = cursor.fetchone()
        self.assertEquals(st[1],student.id)
        self.assertEquals(st[2],course.id)
       

if __name__ == "__main__":
    unittest.main()

