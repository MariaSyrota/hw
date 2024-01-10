def get_election_winner(file_path: str) -> str:
    """
    Знаходить переможця виборів на загальному рівні.

    Параметри:
    file_path (str): Шлях до файлу з результатами виборів.

    Повертає:
    str: Ім'я переможця виборів.
    """
    total_votes = {}

    with open(file_path, 'r') as file:
        for line in file:
            name, votes = line.strip().split()

            if name in total_votes:
                total_votes[name] += int(votes)
            else:
                total_votes[name] = int(votes)

    winner = max(total_votes, key=total_votes.get)

    return winner


file_path = "input.txt"

president = get_election_winner(file_path)
print("Переможець виборів на загальному рівні:", president)