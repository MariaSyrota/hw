# 111111111111111111111111111111111111111111111111111111111
def find_gcd(x: int, y: int) -> int:
    """
    Знаходить найбільший спільний дільник (НСД) двох чисел за допомогою алгоритму Євкліда.

    Параметри:
    x (int): Перше число.
    y (int): Друге число.

    Повертає:
    int: Найбільший спільний дільник чисел x і y.
    """
    if y == 0:
        return x
    else:
        return find_gcd(y, x % y)


num1: int = int(input("Введіть перше число: "))
num2: int = int(input("Введіть друге число: "))

gcd: int = find_gcd(num1, num2)
print("Найбільший спільний дільник:", gcd)

# 222222222222222222222222222222222222222222222222222222222222222222222222222
def find_gcd_recursive(a: int, b: int) -> list[int]:
    """
    Знаходить найбільший спільний дільник (НСД) двох чисел за допомогою рекурсивного підходу.

    Параметри:
    a (int): Перше число.
    b (int): Друге число.

    Повертає:
    list[int]: Залишок після кожного рекурсивного кроку, поки НСД не знайдений.
    """
    if a == 0 or b == 0:
        return [a, b]
    elif a >= 2 * b:
        a = a - 2 * b
        return find_gcd_recursive(a, b)
    elif b >= 2 * a:
        b = b - 2 * a
        return find_gcd_recursive(a, b)
    else:
        return [a, b]


num1: int = int(input("Введіть перше число: "))
num2: int = int(input("Введіть друге число: "))

gcd: list[int] = find_gcd_recursive(num1, num2)
print("Найбільший спільний дільник:", gcd)