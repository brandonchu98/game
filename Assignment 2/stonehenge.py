"""
An implementation of Stonehenge
"""
from typing import Any
import copy
from game import Game
from game_state import GameState

ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


class StonehengeGame(Game):
    """
    Abstract class for a game to be played with two players.
    """

    def __init__(self, p1_starts):
        """
        Initialize this Game, using p1_starts to find who the first player is.
        """
        board_size = 0
        while board_size not in range(1, 6):
            board_size = int(input("Enter the side length of the board: "))
        board = self.initialize_board(board_size)
        ley_lines = [list((board_size + 1) * '@'),  # rows
                     list((board_size + 1) * '@'),  # down left
                     list((board_size + 1) * '@')]  # down right
        self.current_state = StonehengeState(p1_starts, board, ley_lines)

    def initialize_board(self, board_size) -> list:
        """
        Generate initial board

        Pre-condition: board_size must be <= 5 and >= 1
        """
        initial_board = []
        starting_point = 0
        for i in range(2, board_size + 2):
            initial_board.append(ALPHABET[starting_point: starting_point + i])
            starting_point += i
        last_i = ALPHABET.index(initial_board[-1][-1]) + 1
        initial_board.append(ALPHABET[last_i:last_i + board_size])
        return initial_board

    def get_instructions(self) -> str:
        """
        Return the instructions for this Game.
        """
        instructions = 'Players take turns claiming cells. When a player ' \
                       'captures at least half of the cells in a ley-line, ' \
                       'then the player captures that ley-line. The ' \
                       'first player to capture at least half of the ' \
                       'ley-lines is the winner. A ley-line, once claimed, ' \
                       'cannot be taken by the other player.'
        return instructions

    def is_over(self, state):
        """
        Return whether or not this game is over.
        """
        flat_list = [ley for direction in state.ley_lines for ley in direction]
        return (flat_list.count('1') >= len(flat_list) / 2 or
                flat_list.count('2') >= len(flat_list) / 2)

    def is_winner(self, player):
        """
        Return whether player has won the game.

        Precondition: player is 'p1' or 'p2'.
        """
        return (self.current_state.get_current_player_name() != player
                and self.is_over(self.current_state))

    def str_to_move(self, string: str):
        """
        Return the move that string represents. If string is not a move,
        return an invalid move.
        """
        if type(string) in ALPHABET:
            return -1
        return string


class StonehengeState(GameState):
    """
    The state of a game at a certain point in time.
    """

    def __init__(self, is_p1_turn: bool, board: list, ley_lines: list) -> None:
        """
        Initialize this game state and set the current player based on
        is_p1_turn.
        """
        super().__init__(is_p1_turn)
        self.board = board
        self.ley_lines = ley_lines

    def board_1(self) -> str:
        """
        The string board layout of board_size 1
        """
        board_1 = '      {}   {}\n' \
                  '     /   /\n' \
                  '{} - {} - {}\n' \
                  '     \ / \\\n' \
                  '  {} - {}   {}\n' \
                  '       \\\n' \
                  '        {}'.format(
                      self.ley_lines[1][0], self.ley_lines[1][1],
                      self.ley_lines[0][0], self.board[0][0],
                      self.board[0][1], self.ley_lines[0][1],
                      self.board[1][0], self.ley_lines[2][0],
                      self.ley_lines[2][1])
        return board_1

    def board_2(self) -> str:
        """
        The string board layout of board_size 2
        """
        board_2 = '        {}   {}\n' \
                  '       /   /\n' \
                  '  {} - {} - {}   {}\n' \
                  '     / \ / \ /\n' \
                  '{} - {} - {} - {}\n' \
                  '     \ / \ / \\\n' \
                  '  {} - {} - {}   {}\n' \
                  '       \   \\\n' \
                  '        {}   {}\n'.format(
                      self.ley_lines[1][0], self.ley_lines[1][1],
                      self.ley_lines[0][0], self.board[0][0], self.board[0][1],
                      self.ley_lines[1][2], self.ley_lines[0][1],
                      self.board[1][0], self.board[1][1], self.board[1][2],
                      self.ley_lines[0][2], self.board[2][0], self.board[2][1],
                      self.ley_lines[2][0], self.ley_lines[2][2],
                      self.ley_lines[2][1])
        return board_2

    def board_3(self) -> str:
        """
        The string board layout of board_size 3
        """
        board_3 = '          {}   {}\n' \
                  '         /   /\n' \
                  '    {} - {} - {}   {}\n' \
                  '       / \ / \ /\n' \
                  '  {} - {} - {} - {}   {}\n' \
                  '     / \ / \ / \ /\n' \
                  '{} - {} - {} - {} - {}\n' \
                  '     \ / \ / \ / \\\n' \
                  '  {} - {} - {} - {}   {}\n' \
                  '       \   \   \\\n' \
                  '        {}   {}   {}'.format(
                      self.ley_lines[1][0], self.ley_lines[1][1],
                      self.ley_lines[0][0], self.board[0][0], self.board[0][1],
                      self.ley_lines[1][2], self.ley_lines[0][1],
                      self.board[1][0], self.board[1][1], self.board[1][2],
                      self.ley_lines[1][3], self.ley_lines[0][2],
                      self.board[2][0], self.board[2][1], self.board[2][2],
                      self.board[2][3], self.ley_lines[0][3], self.board[3][0],
                      self.board[3][1], self.board[3][2], self.ley_lines[2][0],
                      self.ley_lines[2][3], self.ley_lines[2][2],
                      self.ley_lines[2][1])
        return board_3

    def board_4(self) -> str:
        """
        The string board layout of board_size 4
        """
        board_4 = '            {}   {}\n' \
                  '           /   /\n' \
                  '      {} - {} - {}   {}\n' \
                  '         / \ / \ /\n' \
                  '    {} - {} - {} - {}   {}\n' \
                  '       / \ / \ / \ /\n' \
                  '  {} - {} - {} - {} - {}   {}\n' \
                  '     / \ / \ / \ / \ /\n' \
                  '{} - {} - {} - {} - {} - {}\n' \
                  '     \ / \ / \ / \ / \\\n' \
                  '  {} - {} - {} - {} - {}   {}\n' \
                  '       \   \   \   \\\n' \
                  '        {}   {}   {}   {}'.format(
                      self.ley_lines[1][0], self.ley_lines[1][1],
                      self.ley_lines[0][0], self.board[0][0], self.board[0][1],
                      self.ley_lines[1][2], self.ley_lines[0][1],
                      self.board[1][0], self.board[1][1], self.board[1][2],
                      self.ley_lines[1][3], self.ley_lines[0][2],
                      self.board[2][0], self.board[2][1], self.board[2][2],
                      self.board[2][3], self.ley_lines[1][4],
                      self.ley_lines[0][3], self.board[3][0], self.board[3][1],
                      self.board[3][2], self.board[3][3], self.board[3][4],
                      self.ley_lines[0][4], self.board[4][0], self.board[4][1],
                      self.board[4][2], self.board[4][3], self.ley_lines[2][0],
                      self.ley_lines[2][4], self.ley_lines[2][3],
                      self.ley_lines[2][2], self.ley_lines[2][1])
        return board_4

    def board_5(self) -> str:
        """
        The string board layout of board_size 5
        """
        board_5 = '              {}   {}\n' \
                  '             /   /\n' \
                  '        {} - {} - {}   {}\n' \
                  '           / \ / \ /\n' \
                  '      {} - {} - {} - {}   {}\n' \
                  '         / \ / \ / \ /\n' \
                  '    {} - {} - {} - {} - {}   {}\n' \
                  '       / \ / \ / \ / \ /\n' \
                  '  {} - {} - {} - {} - {} - {}   {}\n' \
                  '     / \ / \ / \ / \ / \ /\n' \
                  '{} - {} - {} - {} - {} - {} - {}\n' \
                  '     \ / \ / \ / \ / \ / \\\n' \
                  '  {} - {} - {} - {} - {} - {}   {}\n' \
                  '       \   \   \   \   \\\n' \
                  '        {}   {}   {}   {}   {}\n'.format(
                      self.ley_lines[1][0], self.ley_lines[1][1],
                      self.ley_lines[0][0], self.board[0][0], self.board[0][1],
                      self.ley_lines[1][2], self.ley_lines[0][1],
                      self.board[1][0], self.board[1][1], self.board[1][2],
                      self.ley_lines[1][3], self.ley_lines[0][2],
                      self.board[2][0], self.board[2][1], self.board[2][2],
                      self.board[2][3], self.ley_lines[1][4],
                      self.ley_lines[0][3], self.board[3][0], self.board[3][1],
                      self.board[3][2], self.board[3][3], self.board[3][4],
                      self.ley_lines[1][5], self.ley_lines[0][4],
                      self.board[4][0], self.board[4][1], self.board[4][2],
                      self.board[4][3], self.board[4][4], self.board[4][5],
                      self.ley_lines[0][5], self.board[5][0], self.board[5][1],
                      self.board[5][2], self.board[5][3], self.board[5][4],
                      self.ley_lines[2][0], self.ley_lines[2][5],
                      self.ley_lines[2][4], self.ley_lines[2][3],
                      self.ley_lines[2][2], self.ley_lines[2][1])
        return board_5

    def down_left_ley_lines(self, board: list) -> list:
        """
        Return a list of the down left ley-lines given a board
        """
        part_board = board[:-1]
        end_board = board[-1]
        down_left = []
        for i in range(len(part_board[-1])):
            row = [part_board[index][i]
                   for index in range(len(part_board))
                   if i <= len(part_board[index]) - 1]
            down_left.append(row)
        for i in range(1, len(down_left)):
            down_left[i].append(end_board[i - 1])
        return down_left

    def down_right_ley_lines(self, board: list) -> list:
        """
        Return a list of the down right ley-lines given a board
        """
        part_board = board[:-1]
        end_board = board[-1]
        down_right = []
        for i in range(-1, -len(part_board[-1]) - 1, -1):
            row = [part_board[index][i]
                   for index in range(len(part_board))
                   if i >= -len(part_board[index])]
            down_right.append(row)
        for i in range(1, len(down_right)):
            down_right[i].append(end_board[i * -1])
        return down_right

    def check_ley_line(self, ley_line: list) -> str:
        """
        Return a string representation of who claims a ley_line given a ley_line
        """
        p1_cells = 0
        p2_cells = 0
        for cell in ley_line:
            if cell == '1':
                p1_cells += 1
            if cell == '2':
                p2_cells += 1
        if p1_cells >= len(ley_line) / 2:
            return '1'
        elif p2_cells >= len(ley_line) / 2:
            return '2'
        return '@'

    def is_final_state(self) -> bool:
        """
        Return True if the StoneHengeState is the final state
        """
        flat_list = [ley for direction in self.ley_lines for ley in direction]
        return flat_list.count('1') >= len(flat_list) / 2 or \
            flat_list.count('2') >= len(flat_list) / 2

    def __str__(self) -> str:
        """
        Return a string representation of the current state of the game.
        """
        string_board = ''
        if len(self.board) == 2:
            string_board = self.board_1()
        if len(self.board) == 3:
            string_board = self.board_2()
        if len(self.board) == 4:
            string_board = self.board_3()
        if len(self.board) == 5:
            string_board = self.board_4()
        if len(self.board) == 6:
            string_board = self.board_5()
        return string_board

    def get_possible_moves(self) -> list:
        """
        Return all possible moves that can be applied to this state.
        """
        if self.is_final_state():
            return []
        return [cell for row in self.board for cell in row if cell in ALPHABET]

    def make_move(self, move: str) -> 'StonehengeState':
        """
        Return the GameState that results from applying move to this GameState.
        """
        new_board = copy.deepcopy(self.board)
        for i in range(len(new_board)):
            for index in range(len(new_board[i])):
                if new_board[i][index] == move and self.p1_turn:
                    new_board[i][index] = '1'
                elif new_board[i][index] == move and not self.p1_turn:
                    new_board[i][index] = '2'
        ley_line_row = [self.check_ley_line(new_board[i])
                        if self.ley_lines[0][i] == '@' else self.ley_lines[0][i]
                        for i in range(len(self.ley_lines[0]))]
        ley_line_down_left = [
            self.check_ley_line(self.down_left_ley_lines(new_board)[i])
            if self.ley_lines[1][i] == '@' else self.ley_lines[1][i]
            for i in range(len(self.ley_lines[1]))]
        ley_line_down_right = [
            self.check_ley_line(self.down_right_ley_lines(new_board)[i])
            if self.ley_lines[2][i] == '@' else self.ley_lines[2][i]
            for i in range(len(self.ley_lines[2]))]
        new_ley_lines = [ley_line_row, ley_line_down_left, ley_line_down_right]
        return StonehengeState(not self.p1_turn, new_board, new_ley_lines)

    def __repr__(self) -> Any:
        """
        Return a representation of this state (which can be used for
        equality testing).
        """
        return 'P1 Turn: {}, Board: {}'.format(self.p1_turn, self.board)

    def rough_outcome(self) -> float:
        """
        Return an estimate in interval [LOSE, WIN] of best outcome the current
        player can guarantee from state self.
        """
        rough_player = copy.deepcopy(self.p1_turn)
        rough_board = copy.deepcopy(self.board)
        rough_ley_lines = copy.deepcopy(self.ley_lines)
        if self.is_final_state():
            return self.LOSE
        for move in self.get_possible_moves():
            a = StonehengeState(rough_player, rough_board, rough_ley_lines)
            b = a.make_move(move)
            if b.is_final_state():
                return self.WIN
            for move2 in b.get_possible_moves():
                c = b.make_move(move2)
                if c.is_final_state():
                    return self.LOSE
        return self.DRAW


if __name__ == "__main__":
    from python_ta import check_all
    check_all(config="a2_pyta.txt")
