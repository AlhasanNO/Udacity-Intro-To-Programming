"""Play a Rock, Paper, Scissors game against different AI opponents."""

import random

moves = ['rock', 'paper', 'scissors']


class Player:
    """Play moves in the Rock, Paper, Scissors game."""

    def move(self):
        """Return a move for the player."""
        return 'rock'

    def learn(self, my_move, their_move):
        """Learn from the opponent's move."""
        pass


class RockPlayer(Player):
    """Always play 'rock' in the game."""

    def move(self):
        """Return 'rock' every time."""
        return 'rock'


class RandomPlayer(Player):
    """Play random moves in the game."""

    def move(self):
        """Return a random move."""
        return random.choice(moves)


class HumanPlayer(Player):
    """Handle human player interactions."""

    def move(self):
        """Get the human player's move through console input.

        Prompts for input until a valid move is entered or player quits.
        """
        while True:
            move = input(
                "Enter your move (rock, paper, scissors, or 'quit' to exit): "
            ).strip().lower()
            if move in moves:
                return move
            elif move in ['quit', 'q']:
                return 'quit'
            print(f"'{move}' is not a valid move. Please try again.")


class ReflectPlayer(Player):
    """Play moves by reflecting the opponent's previous move."""

    def __init__(self):
        """Initialize with no knowledge of opponent's moves."""
        self.opponent_last_move = None

    def move(self):
        """Return the opponent's last move or a random first move."""
        if self.opponent_last_move is None:
            return random.choice(moves)
        return self.opponent_last_move

    def learn(self, my_move, their_move):
        """Remember the opponent's move for next round."""
        self.opponent_last_move = their_move


class CyclePlayer(Player):
    """Play moves in a cyclical pattern."""

    def __init__(self):
        """Initialize with no previous moves."""
        self.my_last_move = None

    def move(self):
        """Return the next move in sequence or a random first move."""
        if self.my_last_move is None:
            return random.choice(moves)
        next_index = (moves.index(self.my_last_move) + 1) % len(moves)
        return moves[next_index]

    def learn(self, my_move, their_move):
        """Remember the last move played."""
        self.my_last_move = my_move


def beats(one, two):
    """Determine if move 'one' beats move 'two'.

    Args:
        one (str): The first move.
        two (str): The second move.

    Returns:
        bool: True if 'one' beats 'two', False otherwise.
    """
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    """Manage the Rock, Paper, Scissors game flow."""

    def __init__(self, p1, p2):
        """Initialize the game with two players and zero scores.

        Args:
            p1 (Player): The first player.
            p2 (Player): The second player.
        """
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self):
        """Execute a single round of the game.

        Gets moves from both players, determines the winner,
        and updates scores.
        """
        move1 = self.p1.move()
        if move1 == 'quit':
            return False

        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")

        if beats(move1, move2):
            print("Player 1 wins this round!")
            self.p1_score += 1
        elif beats(move2, move1):
            print("Player 2 wins this round!")
            self.p2_score += 1
        else:
            print("This round is a tie!")

        print(
            "Scores => Player 1: {},"
            " Player 2: {}".format(
                self.p1_score,
                self.p2_score
            )
        )
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        return True

    def play_game(self):
        """Start and manage the complete game flow.

        Continues until player quits and displays final results.
        """
        print("Game start!")
        round_number = 1
        while True:
            print(f"Round {round_number}:")
            if not self.play_round():
                break
            round_number += 1

        print("Game over!")
        score_msg = "Final Scores => Player 1: {}, Player 2: {}"
        print(score_msg.format(self.p1_score, self.p2_score))
        if self.p1_score > self.p2_score:
            print("Player 1 is the overall winner!")
        elif self.p2_score > self.p2_score:
            print("Player 2 is the overall winner!")
        else:
            print("The game is a tie!")


if __name__ == '__main__':
    """Set up and start the game based on user's opponent choice."""
    print(
        "Choose an opponent:\n"
        "1. RandomPlayer\n"
        "2. ReflectPlayer\n"
        "3. CyclePlayer\n"
        "4. RockPlayer"
    )
    choice = input("Enter the number of your choice: ")
    if choice == '1':
        opponent = RandomPlayer()
    elif choice == '2':
        opponent = ReflectPlayer()
    elif choice == '3':
        opponent = CyclePlayer()
    elif choice == '4':
        opponent = CyclePlayer()
    else:
        print("Invalid choice! Defaulting to RandomPlayer.")
        opponent = RandomPlayer()

    game = Game(HumanPlayer(), opponent)
    game.play_game()
