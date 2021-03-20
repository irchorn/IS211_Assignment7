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
        self.player = [Player(name1), Player(name2)]
        self.turn_total = 0
        self.total = 0


    def play(self):
        roll_die = 'r'
        hold = 'h'
        while self.player[0].total < 100 and self.player[1].total < 100:
            print()
            turn_input = input('Dou you want to roll or hold? ')
            if turn_input == 'r':
                die_value = random.randint(1, 6)
                if die_value == 1:
                    print("Your Scored 0")
                    self.total = 0

                elif 2 <= die_value <= 6:
                    print(f"You rolled a {die_value}")
                    self.total = self.total + die_value
                    print(f"Your score is {self.total}")

            elif turn_input == 'h':
                self.total += self.turn_total
                print(f"Your score is{self.total}. Turn is over")

            else:
                print("Game is over!")


def main():
    my_game = Game("Jhon", "Michael")
    my_game.play()

# play the game
main()