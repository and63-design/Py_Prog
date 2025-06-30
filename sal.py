#create a snakes and ladders class with a board of 100 squares
#add a dice class to roll a number between 1 and 6
#add a player class to hold player name and position
#each square has a number 
#There are 5 snakes and 5 ladders on the board
#snakes move the player down to a lower square
#ladders move the player up to a higher square


class Dice:
    def __init__(self):
        self.current_value = 1

    def roll(self):
        self.current_value = random.randint(1, 6)
        return self.current_value

    def get_current_value(self):
        return self.current_value

class Player:
    def __init__(self, name):
        self.name = name
        self.position = 1

    def move(self, steps):
        self.position += steps
        if self.position > 100:
            self.position = 100
        return self.position
    def get_position(self):
        return self.position
    def set_position(self, position):
        if 1 <= position <= 100:
            self.position = position
        else:
            raise ValueError("Position must be between 1 and 100.")
    def __str__(self):
        return f"Player {self.name} is at position {self.position}"
    def __repr__(self):
        return f"Player(name={self.name}, position={self.position})"
import random

class SnakesAndLadders:
    def __init__(self):
        self.board = {i: None for i in range(1, 101)}  # Initialize board with squares 1 to 100
        self.players = {}  # Dictionary to hold player positions

    def add_player(self, player_name):
        if player_name not in self.players:
            self.players[player_name] = 1  # Start at square 1
        else:
            raise ValueError(f"Player {player_name} already exists.")

    def move_player(self, player_name, steps):
        if player_name not in self.players:
            raise ValueError(f"Player {player_name} does not exist.")

        current_position = self.players[player_name]
        new_position = current_position + steps

        if new_position > 100:
            new_position = 100  # Cannot go beyond square 100

        # Check for snakes or ladders
        if new_position in self.board and self.board[new_position] is not None:
            new_position = self.board[new_position]  # Move to the end of the snake or ladder

        self.players[player_name] = new_position

    def set_snake_or_ladder(self, start, end):
        if start < 1 or start > 100 or end < 1 or end > 100:
            raise ValueError("Start and end positions must be between 1 and 100.")

        self.board[start] = end

    def get_player_position(self, player_name):
        return self.players.get(player_name, None)

    def __str__(self):
        return f"Snakes and Ladders Board: {self.board}\nPlayers: {self.players}"
    def reset(self):
        self.players = {player: 1 for player in self.players}
    def reset_board(self):
        self.board = {i: None for i in range(1, 101)}
    def __repr__(self):
        return f"SnakesAndLadders(board={self.board}, players={self.players})"
    def get_board(self):
        return self.board
    def get_players(self):
        return self.players
    def get_player_names(self):
        return list(self.players.keys())
    def get_player_positions(self):
        return list(self.players.values())
    def get_player(self, player_name):
        if player_name in self.players:
            return Player(player_name)
        else:
            raise ValueError(f"Player {player_name} does not exist.")
    def get_player_by_position(self, position):
        for player, pos in self.players.items():
            if pos == position:
                return Player(player)
        raise ValueError(f"No player found at position {position}.")
    def get_snake_or_ladder(self, start):
        if start in self.board:
            return self.board[start]
        else:
            raise ValueError(f"No snake or ladder at square {start}.")
    def get_snakes(self):
        return {start: end for start, end in self.board.items() if end is not None and end < start}
    def get_ladders(self):
        return {start: end for start, end in self.board.items() if end is not None and end > start}
    def get_snake_count(self):  
        return len(self.get_snakes())
    def get_ladder_count(self):
        return len(self.get_ladders())
    def get_square(self, square):
        if square in self.board:
            return self.board[square]
        else:
            raise ValueError(f"No snake or ladder at square {square}.")
    def is_snake(self, square):
        return square in self.board and self.board[square] is not None and self.board[square] < square
    def is_ladder(self, square):
        return square in self.board and self.board[square] is not None and self.board[square] > square
    def is_square_empty(self, square):
        return square in self.board and self.board[square] is None
    def is_player_at_square(self, player_name, square):
        return self.players.get(player_name) == square
    def get_winner(self):
        for player, position in self.players.items():
            if position == 100:
                return player
        return None
    def play_turn(self, player_name):
        if player_name not in self.players:
            raise ValueError(f"Player {player_name} does not exist.")
        
        dice = Dice()
        steps = dice.roll()
        print(f"{player_name} rolled a {steps}.")
        
        self.move_player(player_name, steps)
        new_position = self.players[player_name]
        
        print(f"{player_name} moved to square {new_position}.")
        
        if new_position == 100:
            print(f"{player_name} wins!")
            return True
        else:
            return False
    def play_game(self):
        while True:
            for player in self.players:
                if self.play_turn(player):
                    return
# Example usage:
if __name__ == "__main__":  
    game = SnakesAndLadders()
    game.add_player("Alice")
    game.add_player("Bob")

    # Set some snakes and ladders
    game.set_snake_or_ladder(16, 6)  # Snake from 16 to 6
    game.set_snake_or_ladder(47, 26)  # Snake from 47 to 26
    game.set_snake_or_ladder(49, 11)  # Snake from 49 to 11
    game.set_snake_or_ladder(56, 53)  # Snake from 56 to 53
    game.set_snake_or_ladder(62, 19)  # Snake from 62 to 19

    game.set_snake_or_ladder(1, 38)   # Ladder from 1 to 38
    game.set_snake_or_ladder(4, 14)   # Ladder from 4 to 14
    game.set_snake_or_ladder(9, 31)   # Ladder from 9 to 31
    game.set_snake_or_ladder(21, 42)   # Ladder from 21 to 42
    game.set_snake_or_ladder(28, 84)   # Ladder from 28 to 84

    print(game)

    game.play_game()