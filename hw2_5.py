def gcd(a, b):
    """
    Функція для знаходження найбільшого спільного дільника двох натуральних чисел.

    Параметри:
    a (int): Перше число.
    b (int): Друге число.

    Повертає:
    list: Список, що містить найбільший спільний дільник та залишок.
    """
    if a == 0 or b == 0:
        return [a, b]
    elif a >= 2 * b:
        a = a - 2 * b
        return gcd(a, b)
    elif b >= 2 * a:
        b = b - 2 * a
        return gcd(a, b)
    else:
        return [a, b]
