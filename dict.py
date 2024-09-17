import json

with open('student.json','r') as file:
    data = json.load(file)

    students= data['students']

    for i in students:
        print(f"ID: {i['id']}")
        print(f"name: {i['name']}")
        print(f"age: {i['age']}")
        print(f"Math Grade: {i['grades']['math']}")
        print(f"Science Grade: {i['grades']['science']}")
        print()

    
    with open('student.json', 'r') as file:
        data = json.load(file)

    data = {'name':'John', 'age': 30}
    with open('student.json', 'w') as file:
        json.dump(data,file)