"""
The `Player` class represents a player in the game. It has an inventory and a dialogue.

The `NPC` class represents a non-player character in the game. It has dialogue.
"""

class Player:
  def __init__(self, inventory, dialogue, choice):
    self.inventory = inventory
    self.dialogue = dialogue
    self.choice = choice
  def say_dialogue(dialogue, trigger):
    print(dialogue[trigger])
  def scene_choice(choice, trigger):
    print(choice[trigger])

class NPC:
  def __init__(self, dialogue):
    self.dialogue = dialogue
  def say_dialogue(dialogue, trigger):
    print(dialogue[trigger])