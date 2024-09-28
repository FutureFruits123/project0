"""
Handles the main game loop and flow of the Wordle game.

This module contains the main entry point for the game, which includes:
- Initializing the player and NPC characters
- Displaying the initial game introduction
- Handling the player's actions in the basement and backyard
- Transitioning to the school sequence and completing the daily Wordle assignment

The game logic is divided into several functions that handle the different game sequences and player interactions.
"""
import random
from wordle import playGame
from items import Item
from characters import Player
from characters import NPC

#dialogue
player = Player([], {"wakeUp":"You: \"Ugh, w-where am I? I must've fallen asleep in here. Hmm, I can't see a thing, I should probably look around for the light switch\"\n", "lightsOn":"You: \"I can finally see. How the hell did I end up in Cynthia's basement? Wait, that's right, she was the one hosting the party last night. I must've had too much to drink and stumbled down here before falling asleep. I should probably quit drinking so much... whatever, I'm gonna be late to school at this rate, I should get going.\"", "admit":"You: \"Sorry about that, I must've stumbled down there at some point last night. I hope you weren't too worried.\"", "walk": "You: \"Nah, It's alright. I can walk home, it's only 10 minutes anyways. Thank you for the offer though.\"", "robotQuestAcceptP1":"You: \"Go ahead.\"", "robotQuestAcceptP2":"You: \"Yeah that's fine, I'll look around for it. What does it look like?\"", "flowersP":"You: \"They're really beautiful. I can tell you take great care of them.\"", "robotQuestCompletedP1":"You: \"It was sitting in a corner of your basement.\"", "classroomThanks":"You: \"Thank you very much Mrs. Catherine.\""}, {"invalid":"Invalid input.\n", "fWall":"You try to check the wall in front of you for the light switch, however it seems to be completely blocked off by a row of what feels like cardboard boxes.\n", "bWall":"You make your way to the wall behind you. After feeling around for the light switch, you conclude it must be somewhere else.\n", "lWall":"You make your way to the wall on your left. After feeling around for a moment, you locate the light switch and turn it on.", "rWall":"You try to make your way to the wall on your right, however you trip over something on the floor. After tripping over various objects a few more times, you decide it isn't worth it and go back.\n", "inspectBasement":"You decide to look around the basement for a bit.\n", "exitBasement":"You make your way to the stairs and exit the basement.", "picture":"You take a look at the framed picture. It contains a cute bunny with a suspiciously feline face.\n", "robot1":"You take a look at the toy robot. It has orange horns and some cool looking energy swords.\n", "robot2":"This is probably the robot Cynthia is looking for. You pick up the toy robot.", "plush":"You take a look at the large plush. It seems to be a monster made of flesh and bones.\n", "garden":"You take a look at Cynthia's garden. It contains a wide variety of beautiful flowers, all of which smell amazing.\n", "stay":"You decide to stay for a little bit longer.\n", "pinwheel":"You wait for about 10 minutes to make it seem like you made the flower pinwheel yourself. You walk up to Mrs. Catherine and show her the pinwheel.", "wordle":"\nYou show Mrs. Catherine the completed Wordle.\n", "classroom":"You take a look around the classroom. There are bookshelves filled to the brim with novels, pictures of old students, and a few motivational posters.\n"})
cynthia = NPC({"notice":"Cynthia: \"Oh, hey -----, so that's where you were.\"", "figured":"Cynthia: \"Don't stress about it, I figured something like that had probably happened. Classes start in about an hour, do you want me to drive you home?\"", "gardenEnd":"Cynthia: \"No problem. Well, I'm here if you need anything.\"\n", "robotQuestAcceptC1":"Cynthia: \"Actually -----, while you're still here, do you mind if I ask you something?\"", "robotQuestAcceptC2":"Cynthia: \"I lost one of my robots a few days ago, if you happen to see it could you let me know? I've already checked everywhere inside the house with no luck, I'm not really sure where else it could be.\"", "robotQuestAcceptC3": "Cynthia: \"Thank you so much, I really appreciate it. It has orange horns and is holding energy swords.\"", "flowersC":"Cynthia: \"Aren't the flowers pretty?\"", "robotQuestCompletedC1":"Cynthia: \"Oh, you found it! Thank you so much -----, where was it?\"", "robotQuestCompletedC2":"Cynthia: \"Huh, I wonder how it ended up down there? Regardless, I really appreciate the help. It isn't much, but have this. I made it myself a few days ago.\"", "robotQuestCompletedC3":"Cynthia: \"Um, by the way -----, you should probably apologize to Sydney the next time you see her.\"", "robotQuestEnd":"Cynthia: \"Oh, do you not rem... actually, forget I said anything. I'll see you at school -----.\"", "wordleCy":"Cynthia: \"Today's Wordle is really hard, I can't make any sense of it.\"\n"})
catherine = NPC({"assignment":"Mrs. Catherine: \"Good afternoon class! I hope all of you have had a wonderful day so far. For today's assignment, you have two options. You can either complete the daily Wordle, or you can use our arts and crafts supplies in the back to create something of your choice. That is all for today, you may start working.\"\n", "pinwheel":"Mrs. Catherine: \"Oh -----, this looks beautiful. You earn full points for today. You can have free time for the rest of class.\"", "wordleCa":"Mrs. Catherine: \"Good job -----, you earn full points for today. You can have free time for the rest of class.\""})

#items
toyRobot = Item("Toy Robot", "A toy robot with orange horns and some cool looking energy swords.")
flowerPinwheel = Item("Flower Pinwheel", "A hand-crafted flower pinwheel given to you by Cynthia.")

#prints text every time location changes
def locationText(location):
   print("\n\033[1m" + location + "\033[0m\n")

#inventory function
def openInventory():
   exitInventory = False
   inventory = "Inventory: "
   if len(player.inventory) == 1:
      if toyRobot in player.inventory:
         inventory += toyRobot.name
      if flowerPinwheel in player.inventory:
         inventory += flowerPinwheel.name
   else:
      print("Your inventory is currently empty.")
      return
   print(inventory)  
   while exitInventory != True:
      viewDescription = input("\nType the name of an item to view its description. Type \"close\" to close your inventory.\n")
      if toyRobot in player.inventory and viewDescription == toyRobot.name:
         Item.display_description(toyRobot)
      elif flowerPinwheel in player.inventory and viewDescription == flowerPinwheel.name:
         Item.display_description(flowerPinwheel)
      elif viewDescription == "close":
         exitInventory = True
      else:
         Player.scene_choice(player.choice, "invalid")

# intro sequence (multiple print statements are for formatting)
print("Welcome to ------------. Oh, are you not able to see that yet? Whatever, the name of this game isn't important. The date isn't important. Your name isn't important.")
print("What happened,\n \n \n \n \n\033[1mis important.\033[0m \n")
print("After a night of partying with classmates, a little too much drinking, and ir-ev-rs--le c-oi-e-, you find yourself lying down in a dark room, unsure of how you got there.")
print("Your adventure to rec-i-y your ---tak-s begins here.\n")
input("Type anything to continue.")

#first basement sequence
print("\n\033[1mMorning of the first day\033[0m")
locationText("Dark Room")
Player.say_dialogue(player.dialogue, "wakeUp")

switch = False
while switch == False:
   wallCheck = input("Which wall would you like to check? Type either \"front,\" \"behind,\" \"left,\" or \"right.\"")
   if wallCheck == "front":
      Player.scene_choice(player.choice, "fWall")
   elif wallCheck == "behind":
      Player.scene_choice(player.choice, "bWall")
   elif wallCheck == "left":
      Player.scene_choice(player.choice, "lWall")
      switch == True
      break
   elif wallCheck == "right":
      Player.scene_choice(player.choice, "rWall")
   elif wallCheck == "i":
      openInventory()
   else:
      Player.scene_choice(player.choice, "invalid")

#second basement sequence
locationText("Cynthia's Basement")
Player.say_dialogue(player.dialogue, "lightsOn")

def cynthiasBasement(exitBasement, backyardQuest):
   investigateBasement = ""
   while exitBasement != "Y":
      if exitBasement == "N":
         Player.scene_choice(player.choice, "inspectBasement")
         if flowerPinwheel not in player.inventory and toyRobot not in player.inventory:
            print("There is a lot of stuff scattered around the basement, among them you notice three things in particular. A framed picture, a toy robot, and a large plush.\n")
            while investigateBasement != "leave":
               investigateBasement = input("Which object do you want to look at? Type either \"picture,\" \"robot,\" or \"plush.\" Once you are done, type \"leave.\"")
               if investigateBasement == "picture":
                  Player.scene_choice(player.choice, "picture")
               elif investigateBasement == "robot":
                  if backyardQuest == False:   
                     Player.scene_choice(player.choice, "robot1")
                  elif backyardQuest == True:
                     Player.scene_choice(player.choice, "robot2")
                     print("\033[1m""Tip: Type \"i\" at any point to open your inventory.""\033[0m")
                     Player.scene_choice(player.choice, "exitBasement")
                     player.inventory.append(toyRobot)
                     Item.added_to_inventory(toyRobot)
                     locationText("Cynthia's Backyard")
                     return
               elif investigateBasement == "plush":
                  Player.scene_choice(player.choice, "plush")
               elif investigateBasement == "leave":
                  investigateBasement = "leave"
               elif investigateBasement == "i":
                  openInventory()
               else:
                  Player.scene_choice(player.choice, "invalid")
         if flowerPinwheel in player.inventory or toyRobot in player.inventory:          
            print("There is a lot of stuff scattered around the basement, among them you notice two things in particular. A framed picture and a large plush.")
            while investigateBasement != "leave":
               investigateBasement = input("\nWhich object do you want to look at? Type either picture or plush. Once you are done, type leave.")
               if investigateBasement == "picture":
                  Player.scene_choice(player.choice, "picture")
               elif investigateBasement == "plush":
                  Player.scene_choice(player.choice, "plush")
               elif investigateBasement == "leave":
                  investigateBasement = "leave"
               elif investigateBasement == "i":
                  openInventory()
               else:
                  Player.scene_choice(player.choice, "invalid")
         exitBasement = "Y"
         break
      if exitBasement != "N":
         Player.scene_choice(player.choice, "invalid")
         exitBasement = input("Would you like to leave the basement? (Y/N)")
   if exitBasement == "Y":
      Player.scene_choice(player.choice, "exitBasement")
      locationText("Cynthia's Backyard")

backyardQuest = False
cynthiasBasement(input("\nWould you like to leave the basement? (Y/N)"), backyardQuest)

#backyard sequence
print("After exiting the basement, you find yourself in your friend's backyard. She is outside watering her garden. As she finishes, she turns around and notices you.\n")
NPC.say_dialogue(cynthia.dialogue, "notice")
Player.say_dialogue(player.dialogue, "admit")
NPC.say_dialogue(cynthia.dialogue, "figured")
Player.say_dialogue(player.dialogue, "walk")
NPC.say_dialogue(cynthia.dialogue, "gardenEnd")

def cynthiasBackyard(backyardQuest):
   walkHome = False
   print("With just about an hour before you need to go to school, you have a few options.\n")
   while walkHome == False:
      gardenChoice = input("Do you want to walk home, talk to Cynthia, look at her garden, or go back to the basement? Type either \"walk,\" \"talk,\" \"garden,\" or \"basement.\"")
      if gardenChoice == "walk":
         confirmWalk = ""
         while confirmWalk != "Y":
            confirmWalk = input("If you walk home, you will not have the option to come back to Cynthia's backyard. Are you sure you want to walk home? (Y/N)")
            if confirmWalk == "Y":
               walkHome = True
               break
            elif confirmWalk == "N":
               Player.scene_choice(player.choice, "stay")
               break
            elif confirmWalk == "i":
               openInventory()
               print("")
            else:
               Player.scene_choice(player.choice, "invalid")
      elif gardenChoice == "talk":
         if backyardQuest == False:
            NPC.say_dialogue(cynthia.dialogue, "robotQuestAcceptC1")
            Player.say_dialogue(player.dialogue, "robotQuestAcceptP1")
            NPC.say_dialogue(cynthia.dialogue, "robotQuestAcceptC2")     
            Player.say_dialogue(player.dialogue, "robotQuestAcceptP2")
            NPC.say_dialogue(cynthia.dialogue, "robotQuestAcceptC3")
            print("\n\033[1m""Quest Accepted: Find Cynthia's Robot""\033[0m\n")
            backyardQuest = True
         elif toyRobot in player.inventory:
            player.inventory.remove(toyRobot)
            print("You give Cynthia her toy robot.")
            NPC.say_dialogue(cynthia.dialogue, "robotQuestCompletedC1")
            Player.say_dialogue(player.dialogue, "robotQuestCompletedP1")
            NPC.say_dialogue(cynthia.dialogue, "robotQuestCompletedC2")
            print("Cynthia hands you a hand-crafted flower pinwheel.")
            Item.added_to_inventory(flowerPinwheel)
            player.inventory.append(flowerPinwheel)
            print("A moment later, Cynthia makes a face as if she has remembered something. She pauses for a moment, trying to think of how to put it into words. A chill runs down your spine.")
            NPC.say_dialogue(cynthia.dialogue, "robotQuestCompletedC3")
            print("Your friend Sydney was at the party last night, but you have no memory of interacting with her after the first hour or so. The few interactions you do remember were casual conversations about topics such as the food and the atmosphere of the party. You cannot think of anything you said or did that might have upset her. Cynthia notices the confused look on your face.")
            NPC.say_dialogue(cynthia.dialogue, "robotQuestEnd")
            print("\n\033[1m""Quest Completed: Find Cynthia's Robot""\033[0m\n")
         else:
            NPC.say_dialogue(cynthia.dialogue, "flowersC")
            Player.say_dialogue(player.dialogue, "flowersP")
            print("Out of the corner of your eye, you can see her smiling.\n")
      elif gardenChoice == "garden":
         Player.scene_choice(player.choice, "garden")
      elif gardenChoice == "basement":
         locationText("Cynthia's Basement")
         cynthiasBasement("N", backyardQuest)
      elif gardenChoice == "i":
         openInventory()
         print("")
      else:
         Player.scene_choice(player.choice, "invalid")

cynthiasBackyard(backyardQuest)

#school sequence
print("You apologize one more time to Cynthia before thanking her and saying goodbye. After a short walk, you arive at your place. You take a shower, get into a fresh change of clothes, eat breakfast, and pack your backpack before heading off the school for the day.")
print("\n\033[1m""Some time later...""\033[0m")
locationText("English Class")
print("Before you know it, you have made it to your final class of the day; English. You take a seat in your usual spot next to Cynthia and wait for your teacher, Mrs. Catherine, to give instructions.\n")
NPC.say_dialogue(catherine.dialogue, "assignment")

def english():
   assignmentComplete = False
   wordleComplete = False
   if flowerPinwheel in player.inventory:
      print("You remember the flower pinwheel Cynthia gave you. You could probably use it for this assignment.\n")
      while assignmentComplete == False:
         classroomChoice = input("Would you like to show Mrs. Catherine the flower pinwheel, talk to Cynthia, or look around the classroom? Type either \"pinwheel,\" \"cynthia,\" or \"classroom.\"")
         if classroomChoice == "pinwheel":
            Player.scene_choice(player.choice, "pinwheel")
            NPC.say_dialogue(catherine.dialogue, "pinwheel")
            Player.say_dialogue(player.dialogue, "classroomThanks")
            assignmentComplete = True
         elif classroomChoice == "cynthia":
            NPC.say_dialogue(cynthia.dialogue, "wordleCy")
         elif classroomChoice == "classroom":
            Player.scene_choice(player.choice, "classroom")
         elif classroomChoice == "i":
            openInventory()
         else:
            Player.scene_choice(player.choice, "invalid")
   else:
      while assignmentComplete == False:
         classroomChoice = input("Would you like to do the Wordle, talk to Cynthia, or look around the classroom? Type either \"wordle,\" \"cynthia,\" or \"classroom.\"")
         if classroomChoice == "wordle":
            playGame(wordleComplete)
            Player.scene_choice(player.choice, "wordle")
            Player.say_dialogue(catherine.dialogue, "wordleCa")
            NPC.say_dialogue(player.dialogue, "classroomThanks")
            assignmentComplete = True
         elif classroomChoice == "cynthia":
            NPC.say_dialogue(cynthia.dialogue, "wordleCy")
         elif classroomChoice == "classroom":
            Player.scene_choice(player.choice, "classroom")
         elif classroomChoice == "i":
            openInventory()
         else:
            Player.scene_choice(player.choice, "invalid")

english()

print("\nYou wait out the remainder of the class. As the bell rings and you are getting ready to leave, you notice something odd. A chill runs down your spine. Despite previously never missing a day of school in her entire life, your friend Syndey's seat...")
print("\033[1m""is empty.""\033[0m")

print("\n\033[1m""To be continued.""\033[0m")