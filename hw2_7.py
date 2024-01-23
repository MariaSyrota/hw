import re


def find_most_common_shortest_word(file_path: str) -> str:
    '''Зчитує вміст файлу з вказаного шляху і знаходить найкоротше слово,
    яке зустрічається найчастіше у тексті.
    '''
    with open(file_path, 'r') as file:
        text = file.read()

    words = re.findall(r'\b\w+\b', text.lower())
    words_count = {}

    for word in words:
        if len(word) > 1:
            word = word.lower()
            if word in words_count:
                words_count[word] += 1
            else:
                words_count[word] = 1

    most_common_words = []
    max_count = max(words_count.values())

    for word, count in words_count.items():
        if count == max_count:
            most_common_words.append(word)

    shortest_word = min(most_common_words, key=len)
    return shortest_word


def replace_words_with_caps(file_path: str, word: str) -> None:
    '''Зчитує вміст файлу з вказаного шляху і замінює всі входження вказаного слова
    на великі літери.
    '''
    with open(file_path, 'r') as file:
        text = file.read()

    updated_text = re.sub(r'\b' + word + r'\b', word.upper(), text, flags=re.IGNORECASE)

    with open(file_path, 'w') as file:
        file.write(updated_text)

file_path = 'Input_1.txt'

most_common_word = find_most_common_shortest_word(file_path)
print("Найкоротше слово, яке зустрічається найчастіше:", most_common_word)

