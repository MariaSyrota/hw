def get_election_winner(file_path):
    state_results = {}

    with open(file_path, 'r') as file:
        for line in file:
            name, votes = line.strip().split(',')

            if name in state_results:
                state_results[name] += int(votes)
            else:
                state_results[name] = int(votes)

    state_winners = {state: max(candidates, key=candidates.get) for state, candidates in state_results.items()}

    total_votes = {}
    for state, candidates in state_results.items():
        for candidate, votes in candidates.items():
            if candidate in total_votes:
                total_votes[candidate] += votes
            else:
                total_votes[candidate] = votes

    winner = max(total_votes, key=total_votes.get)

    return winner, state_winners


file_path = "input.txt"



president,state_winners = get_election_winner(file_path)
print("Переможець виборів на державному рівні:", president)
print("Переможці виборів у кожному штаті:", state_winners)