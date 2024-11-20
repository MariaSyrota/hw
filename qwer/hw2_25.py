from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['my_database']
collection = db['projects']
longest_project = collection.find_one(sort=[("project_name", -1)])
if longest_project:
    longest_project_name = longest_project["project_name"]
    count_longest_project = collection.count_documents({"project_name": longest_project_name})
    print("Найдовша назва проекту:", longest_project_name)
    print("Кількість входжень найдовшої назви:", count_longest_project)
pipeline_languages = [
    {"$unwind": "$programming_language"},
    {"$group": {"_id": "$programming_language", "count": {"$sum": 1}}}
]
language_counts = list(collection.aggregate(pipeline_languages))
print("Кількість кожної використаної мови програмування:")
for language_count in language_counts:
    print(language_count["_id"], ":", language_count["count"])

projects_1500_plus = list(collection.find({"points": {"$gte": 1500}}))
print("Проекти з 1500 і більше поінтами:", projects_1500_plus)

access_projects = list(collection.find({"database": "Access"}))
print("Проекти, де використовується база даних Access:", access_projects)

count_projects_800_2220 = collection.count_documents({"points": {"$gte": 800, "$lte": 2220}})
print("Кількість проектів з 800 до 2220 поінтів:", count_projects_800_2220)