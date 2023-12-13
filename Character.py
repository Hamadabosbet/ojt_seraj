import  random


class Character():


    def __init__(self, name: str, character_class: str):

        self.name = name
        self.character_class = character_class
        self.health = 100
        self.items = []
        self.score=0


    def update_score(self, points: int):
        """
        Update the score based on the points earned.

        Parameters:
        - points: int
            The points to add to the score.
        """

        self.score += points


    def collect_item(self, item_name: str):
        """
        Collect an item in the game.

        Parameters:
        - item_name: str
            The name of the item to collect.
        """

        self.items.append(item_name)

    def   explore_location(self, location_name: str):
        """
        Explore a location in the game world.

        Parameters:
        - location_name: str
            The name of the location to explore.

        Returns:
        - str:
            A message describing the characteristics and challenges of the location.
        """

        if location_name == "Forest":
            return "You are in a dense forest. Watch out for wild animals and hidden treasures!"
        elif location_name == "Castle":
            return "You have entered a majestic castle. Be prepared for encounters with knights and puzzles to solve."
        elif location_name == "Cave":
            return "You find yourself in a dark cave. Beware of dangerous creatures lurking in the shadows."

        return "This location does not exist in the game world."

    def  encounter_Creatures(self, creature_name: str):
        """
        Engage in combat with a creature.

        Parameters:
        - creature_name: str
            The name of the creature to battle.

        Returns:
        - str:
            A message describing the outcome of the battle.
        """

        if creature_name == "Dragon":
            if self.character_class == "Warrior":
                self.health -= 10
                return "You defeated the Dragon, but suffered some injuries."
            elif self.character_class == "Mage":
                self.health -= 10
                return "You used your magical powers to defeat the Dragon with minimal injuries."
            elif self.character_class == "Rogue":
                self.health -= 10
                return "You managed to outsmart the Dragon and defeat it, but got a few scratches."

        return "You encountered an unknown creature."