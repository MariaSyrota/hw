# """
# Завдання 1
# Створіть програму на Python, яка моделюватиме студента та його заняття.
# Ваша програма має складатися з кількох класів, і вона має використовувати винятки, успадкування та ітератори.
# 
# Етапи завдання:
# Клас Student:
# Атрибути:
# Ім'я студента (name).
# Список предметів, на які студент записаний.
# Методи:
# Метод add_course(), який додає новий курс до списку предметів.
# Метод __str__(), який повертає строкове представлення об'єкта (ім'я студента і список його курсів).
# Клас StudentWithGrades (успадковує від Student):
# Атрибути:
# Оцінки за кожним курсом. Це словник, де ключ - назва предмета, а значення - оцінка.
# Методи:
# Метод add_grade(), який дозволяє додати оцінку для конкретного предмета.
# Метод get_average_grade(), який повертає середній бал студента за всіма курсами.
# Метод __str__(), який перевизначає строкове подання (додає інформацію про оцінки).
# Обробка винятків:
# Якщо спробувати додати оцінку для курсу, якого немає в списку предметів, має виникати виняток із повідомленням «Курс не знайдено».
# Якщо середній бал студента не може бути обчислений (наприклад, якщо в нього немає оцінок), то потрібно генерувати виняток «Немає оцінок для розрахунку середнього бала».
# Ітератор для проходження по курсах:
# Створіть ітератор для об'єкта StudentWithGrades, який дозволяє перебрати всі курси студента
# """


class Student:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def __str__(self):
        return f"Student {self.name} is enrolled in: {', '.join(self.courses)}"


class StudentWithGrades(Student):
    def __init__(self, name):
        super().__init__(name)
        self.grades = {}

    def add_grade(self, course, grade):
        if course in self.courses:
            self.grades[course] = grade
        else:
            raise Exception("Курс не знайдено")

    def get_average_grade(self):

        if self.grades:
            return sum(self.grades.values()) / len(self.grades)
        else:
            raise Exception("Немає оцінок для розрахунку середнього бала")

    def __str__(self):
        courses_info = ', '.join(self.courses)
        grades_info = ', '.join(f"{course}: {grade}" for course, grade in self.grades.items())
        return f"Student {self.name} is enrolled in: {courses_info}. Grades: {grades_info}"

    def __iter__(self):
        return iter(self.courses)


try:
    student = StudentWithGrades("Alex")
    student.add_course("Math")
    student.add_course("Physics")
    student.add_course("History")

    print(student)

    student.add_grade("Math", 90)
    student.add_grade("Physics", 85)
    try:
        student.add_grade("Biology", 95)
    except Exception as e:
        print(f"Error: {e}")

    print(student)

    try:
        print("Average Grade:", student.get_average_grade())
    except Exception as e:
        print(f"Error: {e}")

    print("Courses:")
    for course in student:
        print(course)

except Exception as main_error:
    print(f"Main Error: {main_error}")


# завдання 2
# Створіть програму на Python, яка моделюватиме бібліотеку та роботу з книжками. Ваша програма має включати кілька класів, обробку винятків і використання ітераторів.

# Етапи завдання:
# Клас Book:

# Атрибути:
# Назва книги (title).
# Автор книги (author).
# Рік видання книги (year).
# Методи:
# Метод __str__(), який повертає строкове представлення книги у форматі: «Назва книги - Автор - Рік».
# Клас Library:

# Атрибути:
# Список книг (books).
# Методи:
# Метод add_book(), який додає книгу в бібліотеку.
# Метод remove_book(), який видаляє книгу за назвою.
# Метод find_books_by_author(), який шукає книги за автором і повертає список цих книг.
# Метод __str__(), який повертає строкове подання всієї бібліотеки.
# Обробка винятків:

# Якщо спробувати видалити книжку, якої немає в бібліотеці, має виникати виняток із повідомленням «Книга не знайдена».
# Якщо під час пошуку книжок за автором не знайдено книжок, має виникати виняток із повідомленням «Книжок цього автора не знайдено».
# Ітератор для бібліотеки:

# Створіть ітератор для об'єкта Library, який дає змогу пройти по всіх книгах у бібліотеці.


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} - {self.author} - {self.year}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, title):
        for i, book in enumerate(self.books):
            if book.title == title:
                del self.books[i]
                return
        raise Exception("Книга не знайдена")

    def find_books_by_author(self, author):
        found_books = [book for book in self.books if book.author == author]
        if found_books:
            return found_books
        else:
            raise Exception("Книжок цього автора не знайдено")

    def __str__(self):
        return "\n".join(str(book) for book in self.books)

    def __iter__(self):
        return iter(self.books)


try:
    library = Library()
    library.add_book(Book("The Lord of the Rings", "J.R.R. Tolkien", 1954))
    library.add_book(Book("Pride and Prejudice", "Jane Austen", 1813))
    library.add_book(Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 1979))

    print(library)

    library.remove_book("Pride and Prejudice")
    print(library)

    try:
        library.remove_book("The Hobbit")
    except Exception as e:
        print(f"Error: {e}")

    try:
        books_by_author = library.find_books_by_author("J.K. Rowling")
        print(books_by_author)
    except Exception as e:
        print(f"Error: {e}")

    print("Books in the library:")
    for book in library:
        print(book)

except Exception as main_error:
    print(f"Main Error: {main_error}")

# завдання 3
# створити програму, яка буде парсити сайт з погодою та виводити на екран консолі поточну температуру


import requests

def get_weather_data(city):
    url = f"https://www.google.com/search?q=weather+{city}"

    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

    if response.status_code == 200:
        html_content = response.text

        temp_index = html_content.find("°C")
        if temp_index != -1:
            start_index = temp_index - 5
            temp_chunk = html_content[start_index:temp_index].strip()

            temp = ''.join([char for char in temp_chunk if char.isdigit() or char == '-'])

            if temp:
                return int(temp)
            else:
                raise ValueError("Температура не знайдена ")
        else:
            raise ValueError("Температура не знайдена чи такого місце не існує ")
    else:
        raise ConnectionError(f"Помилка завантаження сторінки")

if __name__ == "__main__":
    city = input("Введіть назву міста: ")
    try:
        temperature = get_weather_data(city)
        print(f"Поточна температура в {city}: {temperature} °C")
    except Exception as e:
        print(f"Помилка: {e}")








