def nsd_recursive(x, y):
    """
    Функція для знаходження найбільшого спільного дільника двох чисел за допомогою рекурсії.

    Параметри:
    - x (int): перше число
    - y (int): друге число

    Повертає:
    - int: найбільший спільний дільник чисел x і y
    """
    if y == 0:
        return x
    else:
        return nsd_recursive(y, x % y)

# Приклад використання:
x = 24
y = 36
result = nsd_recursive(x, y)
print(f"Найбільший спільний дільник чисел {x} і {y} дорівнює {result}")






class MyClass:
    """
    Клас MyClass представляє приклад класу з ініціалізатором.
    """

    def __init__(self, x, y):
        """
        Ініціалізатор класу MyClass.

        Параметри:
        - x (int): значення для атрибуту x
        - y (int): значення для атрибуту y
        """
        self.x = x
        self.y = y

    def print_values(self):
        """
        Метод print_values виводить значення атрибутів x та y.
        """
        print(f"x: {self.x}, y: {self.y}")

