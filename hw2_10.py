def count_brackets(string):
    '''Підраховує кількість дужок у заданому рядку.

    Аргументи:
    string (str): Рядок, в якому потрібно підрахувати кількість дужок.

    Повертає:
    dict: Словник, в якому ключі - це дужки ('(', ')', '[', ']', '{', '}'), а значення - кількість кожної дужки у рядку.
    '''
    brackets = {'(': 0, ')': 0, '[': 0, ']': 0, '{': 0, '}': 0}
    for char in string:
        if char in brackets:
            brackets[char] += 1
    return brackets

def check_balanced_brackets(string):
    '''Перевіряє, чи є дужки в заданому рядку збалансованими.

    Аргументи:
    string (str): Рядок, що містить дужки, які потрібно перевірити.

    Повертає:
    bool: True, якщо дужки збалансовані, інакше False.
    '''
    stack = []
    for char in string:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack:
                return False
            opening_bracket = stack.pop()
            if (char == ')' and opening_bracket != '(') or \
                    (char == ']' and opening_bracket != '[') or \
                    (char == '}' and opening_bracket != '{'):
                return False
    return not stack

def check_balanced_brackets_advanced(string):
    '''Перевіряє, чи є дужки в заданому рядку збалансованими з урахуванням усіх відповідних пар.

    Аргументи:
    string (str): Рядок, що містить дужки, які потрібно перевірити.

    Повертає:
    bool: True, якщо дужки збалансовані, інакше False.
    '''
    stack = []
    opening_brackets = '([{'
    closing_brackets = ')]}'
    bracket_pairs = {'(': ')', '[': ']', '{': '}'}
    for char in string:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack:
                return False
            opening_bracket = stack.pop()
            if bracket_pairs[opening_bracket] != char:
                return False
    return not stack