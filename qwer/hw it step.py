# Створити 2 класи, які буде зберігати звичайні поля та колекцію, по якій можна пройтися в
# циклі for.
# реалізувати методи iter і next

class MyCollection:
    def __init__(self, elements):
        self.elements = elements
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.elements):
            value = self.elements[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration

class CustomObject:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return f"{self.name}: {self.value}"


obj1 = CustomObject("Item1", 100)
obj2 = CustomObject("Item2", 200)
obj3 = CustomObject("Item3", 300)

collection = MyCollection([obj1, obj2, obj3])

for item in collection:
    print(item)