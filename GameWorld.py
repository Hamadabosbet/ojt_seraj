class GameWorld:
    """
    Class to represent the game world.

    Attributes:
    - locations: list
        A list of locations in the game world.
    """

    def __init__(self):
        """
        Constructor to create the game world.
        """
        self.locations = ["Forest", "Castle", "Cave"]

    def get_locations(self):
        """
        Get the list of locations in the game world.

        Returns:
        - list:
            A list of locations.
        """

        return self.locations