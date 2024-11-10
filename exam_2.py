class Person_t:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"姓名：{self.name}, 年龄：{self.age}")

class Student_t(Person_t):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def introduce(self):
        super().introduce()
        print(f"年级：{self.grade}")

class Teacher_t(Person_t):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def introduce(self):
        super().introduce()
        print(f"教授科目：{self.subject}")

class Course_t:
    def __init__(self, course_name, teacher):
        self.course_name = course_name
        self.teacher = teacher
        self.students = []  # 用列表存储学生

    def add_student(self, student):
        self.students.append(student)  # 将学生添加到列表中

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)  # 从列表中移除学生
            print(f"学生 {student.name} 已被移除。")
        else:
            print(f"学生 {student.name} 不在课程列表中。")

    def show_course_info(self):
        student_names = [student.name for student in self.students]  # 获取学生姓名列表
        print(f"课程名称：{self.course_name}, 授课教师：{self.teacher.name}, 学生列表：{', '.join(student_names) if student_names else '无'}")

# 创建学生和教师对象
stu1 = Student_t("赵1", 21, 10)
stu2 = Student_t("钱2", 22, 11)
stu3 = Student_t("孙3", 23, 12)

tea1 = Teacher_t("李4", 40, "chinese")
tea2 = Teacher_t("王5", 50, "math")

# 创建课程对象
course1 = Course_t("chinese", tea1)
course2 = Course_t("math", tea2)

# 显示课程信息
course1.show_course_info()
course2.show_course_info()

# 添加学生到课程
course1.add_student(stu1)
course1.add_student(stu3)
course2.add_student(stu2)

# 显示课程信息
course1.show_course_info()
course2.show_course_info()

# 移除学生
course1.remove_student(stu3)  # 移除学生孙3
course1.show_course_info()  # 查看更新后的课程信息

course2.remove_student(stu1)  # 尝试移除不在课程中的学生

course1.remove_student(stu1)

course1.show_course_info()

