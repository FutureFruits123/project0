"""
  Represents an item in the game.
  
  Args:
      name (str): The name of the item.
      description (str): A description of the item.
"""

class Item:
  def __init__(self, name, description):
    self.name = name
    self.description = description
  def added_to_inventory(item):
    print(item.name + " was added to your inventory.")
  def display_description(item):
    print(item.description)