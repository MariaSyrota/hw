import io


def process_text(file_path: str) -> tuple[int, int, list[str], str]:
    '''Обробка тексту з файлу та підрахунок статистики

    Параметри:
    file_path (str): Шлях до файлу для обробки

    Повертає:
    tuple[int, int, list[str], str]: Кількість голосних літер, кількість приголосних літер,
                                     три найпопулярніші голосні літери, найпопулярніша приголосна літера
    '''
    with io.open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    vowels = 0
    consonants = 0
    for char in text:
        char = char.lower()
        if char.isalpha():
            if char in ['a', 'e', 'i', 'o', 'u']:
                vowels += 1
            else:
                consonants += 1

    letter_counts = {}
    for char in text:
        char = char.lower()
        if char.isalpha():
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1

    sorted_counts = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)

    popular_vowels = []
    popular_consonants = []
    if vowels > consonants:
        for char, count in sorted_counts:
            if char in ['a', 'e', 'i', 'o', 'u']:
                popular_vowels.append(char)
                if len(popular_vowels) == 3:
                    break
    else:
        for char, count in sorted_counts:
            if char not in ['a', 'e', 'i', 'o', 'u']:
                popular_consonants.append(char)
                break

    with io.open('output.txt', 'w', encoding='utf-8') as file:
        file.write(f"Кількість голосних літер: {vowels}\n")
        file.write(f"Кількість приголосних літер: {consonants}\n")
        file.write(f"Три найпопулярніші голосні літери: {' '.join(popular_vowels)}\n")
        file.write(f"Найпопулярніша приголосна літера: {' '.join(popular_consonants)}\n")

    return vowels, consonants, popular_vowels, popular_consonants


file_path = "Input_8.txt"
result = process_text(file_path)
print("Результати обробки:")
print(f"Кількість голосних літер: {result[0]}")
print(f"Кількість приголосних літер: {result[1]}")
print(f"Три найпопулярніші голосні літери: {' '.join(result[2])}")
print(f"Найпопулярніша приголосна літера: {result[3]}")
print("Результати записані в файл output.txt")