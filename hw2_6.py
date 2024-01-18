def read_election_results(file_path: str) -> dict:
    '''
    Зчитує дані з файлу з результатами виборів
    і повертає словник, де ключами є прізвища кандидатів,
    а значеннями - кількість голосів за кожного кандидата.
    '''
    election_results = {}

    with open(file_path, 'r') as file:
        for line in file:
            candidate, votes = line.strip().split()
            if candidate in election_results:
                election_results[candidate] += int(votes)
            else:
                election_results[candidate] = int(votes)

    return election_results

def find_presidential_winner(election_results: dict) -> str:
    '''
    Визначає переможця виборів президента на основі
    результатів голосування. Якщо є кілька переможців,
    проводиться третій тур голосування.
    '''
    max_votes = max(election_results.values())
    winners = [candidate for candidate, votes in election_results.items() if votes == max_votes]

    if len(winners) == 1:
        return winners[0]
    else:
        return "Потрібен третій тур голосування!"


file_path = 'input.txt'
election_results = read_election_results(file_path)

presidential_winner = find_presidential_winner(election_results)
print("Переможець виборів президента:", presidential_winner)
