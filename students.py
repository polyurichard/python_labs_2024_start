import json

# 读取JSON文件内容
with open('students.json', 'r') as file:
    data = file.read()

# 将JSON内容解析为Python字典
students_data = json.loads(data)

# 访问字典中的数据
students_list = students_data["students"]

# 处理学生列表中的数据
for student in students_list:
    print(f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}")

# 输出第二个学生的姓名
if len(students_list) > 1:
    second_student = students_list[1]
    print(f"Second student's name: {second_student['name']}")
else:
    print("There is no second student.")