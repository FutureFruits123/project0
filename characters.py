"""
The `Player` class represents a player in the game. It has an inventory and a dialogue.

The `NPC` class represents a non-player character in the game. It has dialogue.
"""
class Player:
  def __init__(self, inventory, dialogue):
    self.inventory = inventory
    self.dialogue = dialogue

class NPC:
  def __init__(self, dialogue):
    self.dialogue = dialogue