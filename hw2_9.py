import json
import csv

factory = {
    'It department': 10,
    'Sales dep': 15,
    'Prodaction dep': 20,
    'Law dep': 5,
    'Construction dep': 8
}

factory['It department'] += 2

factory['Marketing dep'] = 12

del factory['Law dep']

total_employees = sum(factory.values())
print("Загальна кількість співробітників у компанії:", total_employees)

with open('factory_data.json', 'w') as json_file:
    json.dump(factory, json_file)

with open('factory_data.json', 'r') as json_file:
    factory = json.load(json_file)

total_employees = sum(factory.values())
print("Загальна кількість співробітників у компанії:", total_employees)

with open('factory_data.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Department', 'Employees'])
    for department, employees in factory.items():
        writer.writerow([department, employees])

with open('factory_data.json', 'r') as json_file:
    factory = json.load(json_file)

with open('factory_data.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    next(reader)
    for row in reader:
        department = row[0]
        employees = int(row[1])
        factory[department] = employees

total_employees = sum(factory.values())
print("Загальна кількість співробітників у компанії:", total_employees)