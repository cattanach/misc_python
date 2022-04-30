total_games = 0
total_score = 0

for i in range(1,7):
    games = input(f"How many {i}s? ")
    total_score += i * int(games)
    total_games += int(games)

average_score = total_score / total_games

def response(average):
    if average < 2:
        return "Genius"
    elif average < 3:
        return "Magnificent"
    elif average < 4:
        return "Impressive"
    elif average < 5:
        return "Splendid"
    elif average < 6:
        return "Great"
    elif average == 6:
        return "Phew"
    
print(f"Over {total_games} games, your Wordle average is {average_score:.2f}.")
print(response(average_score))