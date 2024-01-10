import re

def find_most_common_shortest_word(file_path: str) -> str:
    '''
    Зчитує вміст файлу з вказаного шляху і знаходить найкоротше слово,
    яке зустрічається найчастіше у тексті.
    '''
    with open(file_path, 'r') as file:
        text = file.read()

    words = re.findall(r'\b\w+\b', text.lower())
    words_count = {}

    for word in words:
        if word in words_count:
            words_count[word] += 1
        else:
            words_count[word] = 1

    most_common_word = min(words_count, key=lambda x: (words_count[x], len(x)))
    return most_common_word

file_path: str = 'Input_1.txt'
most_common_word: str = find_most_common_shortest_word(file_path)
print("Найкоротше слово, яке зустрічається найчастіше:", most_common_word)


def replace_words_with_caps(file_path: str, word: str) -> None:
    '''
    Зчитує вміст файлу з вказаного шляху і замінює всі входження вказаного слова
    на великі літери.
    '''
    with open(file_path, 'r') as file:
        text = file.read()

    text = text.replace(word, word.upper())

    with open(file_path, 'w') as file:
        file.write(text)
