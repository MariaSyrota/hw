def remove_spaces(string):
    return string.replace(" ", "")

def is_palindrome(string):
    string = remove_spaces(string)
    return string == string[::-1]

input_string = input("Введіть рядок: ")
if is_palindrome(input_string):
    print("Рядок є паліндромом")
else:
    print("Рядок не є паліндромом")