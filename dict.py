import json

# 读取 JSON 文件
with open('students.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 访问 JSON 数据
students = data["students"]

# 遍历学生列表
for student in students:
    print(f"ID: {student['id']}")
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Grades: {student['grades']}")

# 访问学生的成绩并计算平均成绩
for student in students:
    grades = student['grades']
    average_grade = sum(grades.values()) / len(grades)
    print(f"{student['name']}'s average grade: {average_grade}")