from Character import Character
from GameWorld import GameWorld
from Quest import Quest


character = Character("John", "Warrior")

# Game World
game_world = GameWorld()
locations = game_world.get_locations()

# Locations
location = character.explore_location("Forest")

# Combat System
combat_result = character.encounter_Creatures("Dragon")

# Quests
quest1 = Quest("Save the Princess", ["Rescue the princess from the castle", "Defeat the evil wizard"])
quest2 = Quest("Retrieve the Lost Artifact", ["Find the hidden map", "Solve the riddles", "Recover the artifact"])
quest1.complete_step()
quest2.complete_step()
character.update_score(100)


print(f"Character: {character.name}, Class: {character.character_class}")
print(f"Game World Locations: {locations}")
print(f"Location: {location}")
print(f"Combat Result: {combat_result}")
print(f"Quest 1 Completed: {quest1.completed}")
print(f"Quest 2 Completed: {quest2.completed}")
print(f"Score: {character.score}")