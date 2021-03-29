import random


class Die:
    def __init__(self, seed):
        random.seed(seed)

    def roll(self):
        return random.randint(1, 6)


class Player:
    def __init__(self, name):
        self.name = name
        self.total = 0
        # we might not need turn total

    def __str__(self):
        return f"{self.name} has {self.total}points"


class Game:
    def __init__(self, name1, name2):
        self.players = [Player(name1), Player(name2)]
        self.turn_total = 0
        self.total = 0
        self.current_player = 0

    def next_player(self):
        if self.current_player + 1 == len(self.players):
            self.current_player = 0
        else:
            self.current_player += 1

    def play(self):
        turn_total = 0
        while self.players[0].total < 100 and self.players[1].total < 100:
            turn_input = input(f'{self.players[self.current_player].name}, do you want to roll or hold? ')
            if turn_input == 'r':
                die_value = random.randint(1, 6)
                if die_value == 1:
                    print(f"{self.players[self.current_player].name} you roll a 1. Your score for this round is 0")
                    print("----------------------------------------------------------------")
                    turn_total = 0
                    self.next_player()
                    continue
                else:
                    print(f"{self.players[self.current_player].name} you roll a {die_value}.")
                    turn_total += die_value
                    if turn_total + self.players[self.current_player].total >= 100:
                        self.players[self.current_player].total += turn_total
                        print(f"{self.players[self.current_player].name} you are the WINNER.")
                        print(f"Your winning score is {self.players[self.current_player].total}")
                        continue

                    print(f"Your turn score is {turn_total}")
                    print(f"Your possible score if you hold is {turn_total + self.players[self.current_player].total}")
            elif turn_input == 'h':
                self.players[self.current_player].total += turn_total
                print(f"Your score is {self.players[self.current_player].total}. Turn is over")
                print("----------------------------------------------------------------")
                turn_total = 0
                self.next_player()
            else:
                print("Game is over!")


def main():
    my_game = Game("Jhon", "Michael")
    my_game.play()

# play the game
main()