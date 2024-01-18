def read_text(file_path: str) -> str:
    '''
    Зчитує текст з файлу і повертає його зміст.
    '''
    with open(file_path, 'r') as file:
        text = file.read()

    return text


def process_text(text: str) -> dict:
    '''
    Обробляє текст та знаходить кількість голосних та приголосних літер.
    Повертає словник, де ключами є "голосні" та "приголосні" і їх значеннями -
    кількість голосних та приголосних літер в тексті.
    '''
    vowels = ['a', 'e', 'i', 'o', 'u']  # список голосних літер
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y',
                  'z']  # список приголосних літер

    text = text.lower()  # перетворюємо текст на нижній регістр
    vowel_count = 0
    consonant_count = 0

    for char in text:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            elif char in consonants:
                consonant_count += 1

    return {"голосні": vowel_count, "приголосні": consonant_count}


# Зчитуємо текст з файлу
file_path = 'input_8.txt'
text = read_text(file_path)

# Обробляємо текст та знаходимо кількість голосних та приголосних літер
result = process_text(text)

# Виводимо результат
print("Кількість голосних літер:", result["голосні"])
print("Кількість приголосних літер:", result["приголосні"])


def find_most_common_vowels(text: str, n: int) -> list:
    '''
    Знаходить n найпопулярніших голосних літер в тексті.
    Повертає список з цими літерами, в порядку спадання популярності.
    '''
    vowels = ['a', 'e', 'i', 'o', 'u']  # список голосних літер
    vowel_counts = {vowel: 0 for vowel in vowels}

    for char in text:
        if char.isalpha() and char.lowerSorry, it seems that my response got cut off.Here's the complete code for finding the most common vowels and consonants:


```python


def find_most_common_vowels(text: str, n: int) -> list:
    '''
    Знаходить n найпопулярніших голосних літер в тексті.
    Повертає список з цими літерами, в порядку спадання популярності.
    '''
    vowels = ['a', 'e', 'i', 'o', 'u']  # список голосних літер
    vowel_counts = {vowel: 0 for vowel in vowels}

    for char in text:
        if char.isalpha() and char.lower() in vowels:
            vowel_counts[char.lower()] += 1

    sorted_vowels = sorted(vowel_counts, key=vowel_counts.get, reverse=True)
    return sorted_vowels[:n]


def find_most_common_consonants(text: str) -> str:
    '''
    Знаходить найпопулярнішу приголосну літеру в тексті.
    Повертає цю літеру.
    '''
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y',
                  'z']  # список приголосних літер
    consonant_counts = {consonant: 0 for consonant in consonants}

    for char in text:
        if char.isalpha() and char.lower() in consonants:
            consonant_counts[char.lower()] += 1

    most_common_consonant = max(consonant_counts, key=consonant_counts.get)
    return most_common_consonant


# Знайдемо найпопулярнішу приголосну літеру
most_common_consonant = find_most_common_consonants(text)
print("Найпопулярніша приголосна літера:", most_common_consonant)

# Знайдемо три найпопулярніші голосні літери
most_common_vowels = find_most_common_vowels(text, 3)
print("Три найпопулярніші голосні літери:", most_common_vowels)
def write_output(file_path: str, result: dict, most_common_vowels: list, most_common_consonant: str):
    '''
    Записує відповідь у файл.
    '''
    with open(file_path, 'w') as file:
        file.write(f"Кількість голосних літер: {result['голосні']}\n")
        file.write(f"Кількість приголосних літер: {result['приголосні']}\n")
        file.write(f"Найпопулярніша приголосна літера: {most_common_consonant}\n")
        file.write("Три найпопулярніші голосні літери: ")
        file.write(", ".join(most_common_vowels))

# Записуємо відповідь у файл
output_file_path = 'output.txt'
write_output(output_file_path, result, most_common_vowels, most_common_consonant)
