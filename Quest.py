

class Quest():
    """
    Class to represent a quest in the game.

    Attributes:
    - name: str
        The name of the quest.
    - steps: list
        A list of steps or tasks to complete the quest.
    - completed: bool
        Indicates whether the quest has been completed or not.
    """

    def __init__(self, name: str, steps: list):
        """
        Constructor to create a quest.

        Parameters:
        - name: str
            The name of the quest.
        - steps: list
            A list of steps or tasks to complete the quest.
        """
        self.name = name
        self.steps = steps
        self.completed = False
        self.score = 2

    def complete_step(self):
        """
        Complete a step of the quest.
        """
        if not self.completed:
            self.score += 10
            self.steps.pop(0)

            if len(self.steps) == 0:
                self.completed = True
