"""
Keeps track of states for minimax iteration
"""


class StateTracker:
    """
    Class to store the state, children and score
    """
    def __init__(self, state: object, children: list, score: int):
        """
        Create a new StateTracker object
        """
        self.state = state
        self.children = children
        self.score = score

    def __eq__(self, other):
        """
        Return True if self.score is equal to other.score
        """
        return self.score == other.score

    def __gt__(self, other):
        """
        Return True if self.score is greater than other.score
        """
        return self.score > other.score

    def __lt__(self, other):
        """
        Return True if self.score is less than other.score
        """
        return self.score < other.score

    def __ge__(self, other):
        """
        Return True if self.score if greater than or equal to other.score
        """
        return self.score >= other.score

    def __le__(self, other):
        """
        Return True if self.score is less than or equal to other.score
        """
        return self.score <= other.score


if __name__ == "__main__":
    from python_ta import check_all
    check_all(config="a2_pyta.txt")
