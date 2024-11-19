import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["projects"]

with open("Task_25.txt", "r", encoding="utf-8") as file:
    data = file.readlines()

projects = []
for line in data:
    line = line.strip()
    parts = line.split("\t")
    project = {
        "project_type": parts[0].strip(),
        "project_name": parts[1].strip(),
        "programming_language": parts[2].strip(),
        "points": int(parts[3].split("+")[0].strip())
    }
    projects.append(project)

collection.insert_many(projects)

print("Дані успішно збережено в базі даних MongoDB.")
