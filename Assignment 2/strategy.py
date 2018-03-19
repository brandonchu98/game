"""
A module for strategies.

NOTE: Make sure this file adheres to python-ta.
Adjust the type annotations as needed, and implement both a recursive
and an iterative version of minimax.
"""
from typing import Any
import copy
from stack import Stack
from iterative_state_tracker import StateTracker


def interactive_strategy(game: Any) -> Any:
    """
    Return a move for game through interactively asking the user for input.
    """
    move = input("Enter a move: ")
    return game.str_to_move(move)


def rough_outcome_strategy(game: Any) -> Any:
    """
    Return a move for game by picking a move which results in a state with
    the lowest rough_outcome() for the opponent.

    NOTE: game.rough_outcome() should do the following:
        - For a state that's over, it returns the score for the current
          player of that state.
        - For a state that's not over:
            - If there is a move that results in the current player winning,
              return 1.
            - If all moves result in states where the other player can
              immediately win, return -1.
            - Otherwise; return a number between -1 and 1 corresponding to how
              'likely' the current player will win from the current state.

        In essence: rough_outcome() will only look 1 or 2 states ahead to
        'guess' the outcome of the game, but no further. It's better than
        random, but worse than minimax.
    """
    current_state = game.current_state
    best_move = None
    best_outcome = -2  # Temporarily -- just so we can replace this easily later

    # Get the move that results in the lowest rough_outcome for the opponent
    for move in current_state.get_possible_moves():
        new_state = current_state.make_move(move)

        # We multiply the below by -1 since a state that's bad for the opponent
        # is good for us.
        guessed_score = new_state.rough_outcome() * -1
        if guessed_score > best_outcome:
            best_outcome = guessed_score
            best_move = move

    # Return the move that resulted in the best rough_outcome
    return best_move


def recursive_helper(game: Any) -> Any:
    """
    Return the score of the best move given the game
    """
    current_state = game.current_state
    list_ = []
    if current_state.p1_turn:
        player = 'p1'
    else:
        player = 'p2'
    if game.is_over(current_state) and not game.is_winner(player):
        return -1
    for move in current_state.get_possible_moves():
        new_game = copy.deepcopy(game)
        new_game.current_state = current_state.make_move(move)
        list_.append(recursive_helper(new_game) * -1)
    return max(list_)


def recursive_minimax_strategy(game: Any) -> Any:
    """
    Return the best move based off of the game recursively
    """
    current_state = game.current_state
    list_ = []
    for move in current_state.get_possible_moves():
        new_game = copy.deepcopy(game)
        new_game.current_state = current_state.make_move(move)
        list_.append(recursive_helper(new_game))
    list_ = [-1 * x for x in list_]
    best_move = max(list_)
    return current_state.get_possible_moves()[list_.index(best_move)]


def iterative_mini_max_strategy(game: Any) -> Any:
    """
    Return the best move based off of the game iteratively
    """
    current_state = game.current_state
    stack = Stack()
    tracker = StateTracker(current_state, None, None)
    stack.add(tracker)
    while not stack.is_empty():
        parent_ = stack.remove()
        new_game = copy.deepcopy(game)
        new_game.current_state = parent_.state
        if new_game.is_over(new_game.current_state):
            parent_.score = -1
        elif parent_.children is None:
            parent_.children = []
            for move in parent_.state.get_possible_moves():
                copy_parent = copy.deepcopy(parent_)
                new_state = copy_parent.state.make_move(move)
                new_tracker = \
                    StateTracker(new_state, None, None)
                parent_.children.append(new_tracker)
            stack.add(parent_)
            for child in parent_.children:
                stack.add(child)
        elif parent_.children is not None:
            new_score = max([-1 * child.score for child in parent_.children])
            parent_.score = new_score
    for child in tracker.children:
        child.score *= -1
    best_state = max(tracker.children).state
    for move in tracker.state.get_possible_moves():
        copy_state = copy.deepcopy(tracker.state)
        new_state = copy_state.make_move(move)
        if best_state.__repr__() == new_state.__repr__():
            return move
    return tracker.state.get_possible_moves()[0]


if __name__ == "__main__":
    from python_ta import check_all
    check_all(config="a2_pyta.txt")
