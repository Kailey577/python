from random import randrange

def main():
    # number of trials to run
    how_many = int(input("> "))
    total_wins, total_loses = multiple_games(how_many)
    print("number of wins: ",total_wins," number of losses: ",total_loses)
    print("probability of winning: ",total_wins/int(how_many))

def multiple_games(n: int) -> (int, int):
    # simulates n games producing (totalWins, totalLoss)
    total_wins = 0
    total_loses = 0
    for game_num in range(n):
        win, lose = one_game()
        total_wins += win
        total_loses += lose
    return total_wins, total_loses

def roll() -> int:
    # returns a nuber in [1,6]
    return randrange(1, 7)

def one_game() -> (int, int):
    # runs one round of the game returns
    # (winCount, lossCount)
    lose = win = 0
    first_roll, second_roll = roll(), roll()
    total = first_roll + second_roll
    if total == 2:
        lose+=1
    elif total == 3:
        lose+=1
    elif total == 12:
        lose+=1
    elif total == 7:
        win+=1
    elif total == 11:
        win+=1
    else:
        while lose == 0 and win == 0:
            next_total = roll() + roll()
            if next_total == 7:
                lose+=1
            if next_total == total:
                win+=1
    return win, lose

main()
