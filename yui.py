# 1. Створити функцію, яка приймає один список та повертає найбільший парний елемент.
# 2. Створити функцію, яка приймає один список та повертає три максимуми зі списку. ( Наприклад список [1, 10, 4. 13. 22. 10. 0 , 105]. max_1 = 105, max_2 = 22. max_3 == 13 )
# 3. Створити функцію, яка приймає два списки і повертає True, якщо в першому списку парних елементів більше, ніж НЕПАРНИХ у другому.


def find_largest_even(numbers):
    max_even = None
    for num in numbers:
        if num % 2 == 0:
            if max_even is None or num > max_even:
                max_even = num
    return max_even

def find_three_max(numbers):
    sorted_nums = sorted(numbers, reverse=True)
    return sorted_nums[:3]

def compare_even_odd(list1, list2):
    count_even_list1 = sum(1 for num in list1 if num % 2 == 0)
    count_odd_list2 = sum(1 for num in list2 if num % 2 != 0)
    return count_even_list1 > count_odd_list2

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
largest_even = find_largest_even(numbers)
print("Найбільший парний елемент:", largest_even)

numbers = [1, 10, 4, 13, 22, 10, 0, 105]
three_max = find_three_max(numbers)
print("Три максимуми:", three_max)

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
result = compare_even_odd(list1, list2)
print("У першому списку парних елементів більше, ніж непарних у другому списку:", result)


