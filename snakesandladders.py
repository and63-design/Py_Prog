from dataclasses import dataclass
from random import randint

p1_snake = 0
p2_snake = 0
p1_ladder = 0
p2_ladder = 0


class dice():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def throw_dice(self):
        self.num1 = randint(1, 6)
        self.num2 = randint(1, 6)


class Player(dice):
    def __init__(self, pos):
        self.pos = pos

    def move_to(self, num1, num2):
        self.pos = self.pos + self.num1 + self.num2


@dataclass
class Board:
    game: str
    start: int
    end: int
    snake: list
    ladder: list


sandl = Board(game='Snakes And Ladders', start=0, end=100, snake=[
              30, 40, 50, 60, 70, 90], ladder=[15, 25, 35, 45, 55, 65])

print(f'The game is: {sandl.game}')
print(f'Begins at {sandl.start} and ends at {sandl.end}')
print(f'There is a ladder at {sandl.ladder} and a snake at {sandl.snake}\n')

player1 = Player(0)
player2 = Player(0)

print(f'Player 1 is on square {player1.pos}')
print(f'Player 2 is on square {player2.pos}\n')

# while (player2.pos or player1.pos) < sandl.end:

while True:
    throw_a_dice = input('Throw Dice Y or N ')
    if throw_a_dice == 'n':
        break
    else:
        player1.throw_dice()
        player2.throw_dice()

    player1.move_to(player1.num1, player1.num2)
    player2.move_to(player2.num1, player2.num2)

    if player1.pos == sandl.end:
        print(f'Player 1 threw {player1.num1}')
        print(f'Player 1 threw {player1.num2}')
        print(f'Player 1 is now on square {player1.pos}')
        print('Player 1 is the winner \n')
        print(f'Player 1 climbed {p1_ladder} ladders')
        print(f'Player 1 dropped {p1_snake} snakes')
        print(f'Player 2 climbed {p2_ladder} ladders')
        print(f'Player 2 dropped {p2_snake} snakes')
        break
    if player2.pos == sandl.end:
        print(f'Player 2 threw {player2.num1}')
        print(f'Player 2 threw {player2.num2}')
        print(f'Player 2 is now on square {player2.pos}')
        print('Player 2 is the winner \n')
        print(f'Player 2 climbed {p2_ladder} ladders')
        print(f'Player 2 dropped {p2_snake} snakes')
        print(f'Player 1 climbed {p1_ladder} ladders')
        print(f'Player 1 dropped {p1_snake} snakes')
        break

    if player1.pos > sandl.end:
        player1.pos = 80
    if player2.pos > sandl.end:
        player2.pos = 80

   # player1.pos = int(player1.pos + player1.num1 + player1.num2)
   # player2.pos = int(player2.pos + player2.num1 + player2.num2)

    if (player1.pos in sandl.snake):
        player1.pos = player1.pos - 10
        p1_snake = p1_snake + 1
        print(f'Player 1 threw {player1.num1}')
        print(f'Player 1 threw {player1.num2}')
        print('Player 1 landed on a snake')
        print(f'Total: {player1.num1 + player1.num2}')
        print(f'Player 1 is now on square {player1.pos}\n \n')

    if (player1.pos in sandl.ladder):
        player1.pos = player1.pos + 10
        p1_ladder = p1_ladder + 1
        print(f'Player 1 threw {player1.num1}')
        print(f'Player 1 threw {player1.num2}')
        print('Player 1 landed on a ladder')
        print(f'Total: {player1.num1 + player1.num2}')
        print(f'Player 1 is now on square {player1.pos}\n \n')

    else:
        print(f'Player 1 threw {player1.num1}')
        print(f'Player 1 threw {player1.num2}')
        print(f'Total: {player1.num1 + player1.num2}')
        print(f'Player 1 is now on square {player1.pos}\n \n')

    if (player2.pos in sandl.snake):
        player2.pos = player2.pos - 10
        p2_snake = p2_snake + 1
        print(f'Player 2 threw {player2.num1}')
        print(f'Player 2 threw {player2.num2}')
        print(f'Total: {player2.num1 + player2.num2}')
        print('Player2 landed on a snake')
        print(f'Player 2 is now on square {player2.pos}\n \n')

    if (player2.pos in sandl.ladder):
        player2.pos = player1.pos + 10
        p2_ladder = p2_ladder + 1
        print(f'Player 2 threw {player1.num1}')
        print(f'Player 2 threw {player1.num2}')
        print('Player 2 landed on a ladder')
        print(f'Total: {player1.num1 + player1.num2}')
        print(f'Player 2 is now on square {player1.pos}\n \n')

    else:
        print(f'Player 2 threw {player2.num1}')
        print(f'Player 2 threw {player2.num2}')
        print(f'Total: {player2.num1 + player2.num2}')
        print(f'Player 2 is now on square {player2.pos}\n \n')
