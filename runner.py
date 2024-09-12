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
player = Player([], {"wakeUp":"You: \"Ugh, w-where am I? I must've fallen asleep in here. Hmm, I can't see a thing, I should probably look around for the light switch\"", "lightsOn":"You: \"I can finally see. How the hell did I end up in Cynthia's basement? Wait, that's right, she was the one hosting the party last night. I must've had too much to drink and stumbled down here before falling asleep. I should probably quit drinking so much... whatever, I'm gonna be late to school at this rate, I should get going.\"", "admit":"You: \"Sorry about that, I must've stumbled down there at some point last night. I hope you weren't too worried.\"", "walk": "You: \"Nah, It's alright. I can walk home, it's only 10 minutes anyways. Thank you for the offer though.\"", "robotQuestAcceptP1":"You: \"Go ahead.\"", "robotQuestAcceptP2":"You: \"Yeah that's fine, I'll look around for it. What does it look like?\"", "flowersP":"You: \"They're really beautiful. I can tell you take great care of them.\"", "robotQuestCompletedP1":"You: \"It was sitting in a corner of your basement.\"", "classroomThanks":"You: \"Thank you very much Mrs. Catherine.\""})
cynthia = NPC({"notice":"Cynthia: \"Oh, hey -----, so that's where you were.\"", "figured":"Cynthia: \"Don't stress about it, I figured something like that had probably happened. Classes start in about an hour, do you want me to drive you home?\"", "gardenEnd":"Cynthia: \"No problem. Well, I'm here if you need anything.\"\n", "robotQuestAcceptC1":"Cynthia: \"Actually -----, while you're still here, do you mind if I ask you something?\"", "robotQuestAcceptC2":"Cynthia: \"I lost one of my robots a few days ago, if you happen to see it could you let me know? I've already checked everywhere inside the house with no luck, I'm not really sure where else it could be.\"", "robotQuestAcceptC3": "Cynthia: \"Thank you so much, I really appreciate it. It has orange horns and is holding energy swords.\"", "flowersC":"Cynthia: \"Aren't the flowers pretty?\"", "robotQuestCompletedC1":"Cynthia: \"Oh, you found it! Thank you so much -----, where was it?\"", "robotQuestCompletedC2":"Cynthia: \"Huh, I wonder how it ended up down there? Regardless, I really appreciate the help. It is't much, but have this.\"", "robotQuestCompletedC3":"Cynthia: \"Um, by the way -----, you should probably apologize to Sydney the next time you see her.\"", "robotQuestEnd":"Cynthia: \"Oh, do you not rem... actually, forget I said anything. I'll see you at school -----.\"", "wordleCy":"Cynthia: \"Today's Wordle is really hard, I can't make any sense of it.\""})
catherine = NPC({"assignment":"Mrs. Catherine: \"Good afternoon class! I hope all of you have had a wonderful day so far. For today's assignment, you have two options. You can either complete the daily Wordle, or you can use our arts and crafts supplies in the back to create something of your choice. That is all for today, you may start working.\"", "pinwheel":"Mrs. Catherine: \"Oh -----, this looks beautiful. You earn full points for today. You can have free time for the rest of class.\"", "wordleCa":"Mrs. Catherine: \"Good job -----, you earn full points for today. You can have free time for the rest of class.\""})

#items
toyRobot = Item("Toy Robot", "A toy robot with orange horns and some cool looking energy swords.")
flowerPinwheel = Item("Flower Pinwheel", "A hand-crafted flower pinwheel given to you by Cynthia.")

#prints character dialogue
def sayDialogue(dialogue, trigger):
   print(dialogue[trigger])

#prints text every time location changes
def locationText(location):
   print("\n\033[1m" + location + "\033[0m\n")

#inventory function
def openInventory():
   exitInventory = False
   inventory = "Items: "
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
         print(toyRobot.description)
      elif flowerPinwheel in player.inventory and viewDescription == flowerPinwheel.name:
         print(flowerPinwheel.description)
      elif viewDescription == "close":
         exitInventory = True
      else:
         print("Invalid input.")

# intro sequence (multiple print statements are for formatting)
print("Welcome to ------------. Oh, are you not able to see that yet? Whatever, the name of this game isn't important. The date isn't important. Your name isn't important.")
print("What happened,\n \n \n \n \n\033[1mis important.\033[0m \n")
print("After a night of partying with classmates, a little too much drinking, and ir-ev-rs--le c-oi-e-, you find yourself lying down in a dark room, unsure of how you got there.")
print("Your adventure to rec-i-y your ---tak-s begins here.\n")
input("Type anything to continue.")

#first basement sequence
print("\n\033[1mMorning of the first day\033[0m")
locationText("Dark Room")
sayDialogue(player.dialogue, "wakeUp")

switch = False
while switch == False:
   wallCheck = input("\nWhich wall would you like to check? Type either \"front,\" \"behind,\" \"left,\" or \"right.\"")
   if wallCheck == "front":
      print("You try to check the wall in front of you for the light switch, however it seems to be completely blocked off by a row of what feels like cardboard boxes.")
   elif wallCheck == "behind":
      print("You make your way to the wall behind you. After feeling around for the light switch, you conclude it must be somewhere else.")
   elif wallCheck == "left":
      print("You make your way to the wall on your left. After feeling around for a moment, you locate the light switch and turn it on.")
      switch == True
      break
   elif wallCheck == "right":
      print("You try to make your way to the wall on your right, however you trip over something on the floor. After tripping over various objects a few more times, you decide it isn't worth it and go back.")
   elif wallCheck == "i":
      openInventory()
   else:
      print("Invalid input.")

#second basement sequence
locationText("Cynthia's Basement")
sayDialogue(player.dialogue, "lightsOn")

def cynthiasBasement(exitBasement, backyardQuest):
   investigateBasement = ""
   while exitBasement != "Y":
      if exitBasement == "N":
         print("You decide to look around the basement for a bit.\n")
         if flowerPinwheel not in player.inventory and toyRobot not in player.inventory:
            print("There is a lot of stuff scattered around the basement, among them you notice three things in particular. A framed picture, a toy robot, and a large plush.")
            while investigateBasement != "leave":
               investigateBasement = input("\nWhich object do you want to look at? Type either \"picture,\" \"robot,\" or \"plush.\" Once you are done, type \"leave.\"")
               if investigateBasement == "picture":
                  print("You take a look at the framed picture. It contains a cute bunny with a suspiciously feline face.")
               elif investigateBasement == "robot":
                  if backyardQuest == False:   
                     print("You take a look at the toy robot. It has orange horns and some cool looking energy swords.")
                  elif backyardQuest == True:
                     print("This is probably the robot Cynthia is looking for. You pick up the toy robot. Toy Robot was added to your inventory.")
                     print("\033[1m""Tip: Type \"i\" at any point to open your inventory.""\033[0m")
                     print("You make your way to the stairs and exit the basement.")
                     player.inventory.append(toyRobot)
                     locationText("Cynthia's Backyard")
                     return
               elif investigateBasement == "plush":
                  print("You take a look at the large plush. It seems to be a monster made of flesh and bones.")
               elif investigateBasement == "leave":
                  investigateBasement = "leave"
               elif investigateBasement == "i":
                  openInventory()
               else:
                  print("Invalid input.")
         if flowerPinwheel in player.inventory or toyRobot in player.inventory:          
            print("There is a lot of stuff scattered around the basement, among them you notice two things in particular. A framed picture and a large plush.")
            while investigateBasement != "leave":
               investigateBasement = input("\nWhich object do you want to look at? Type either picture or plush. Once you are done, type leave.")
               if investigateBasement == "picture":
                  print("You take a look at the framed picture. It contains a cute bunny with a suspiciously feline face. ")
               elif investigateBasement == "plush":
                  print("You take a look at the large plush. It seems to be a monster made of flesh and bones.")
               elif investigateBasement == "leave":
                  investigateBasement = "leave"
               elif investigateBasement == "i":
                  openInventory()
               else:
                  print("Invalid input.")
         exitBasement = "Y"
         break
      if exitBasement != "N":
         print("Invalid input.\n")
         exitBasement = input("Would you like to leave the basement? (Y/N)")
   if exitBasement == "Y":
      print("You make your way to the stairs and exit the basement.")
      locationText("Cynthia's Backyard")

backyardQuest = False
cynthiasBasement(input("\nWould you like to leave the basement? (Y/N)"), backyardQuest)

#backyard sequence
print("After exiting the basement, you find yourself in your friend's backyard. She is outside watering her garden. As she finishes, she turns around and notices you.\n")
sayDialogue(cynthia.dialogue, "notice")
sayDialogue(player.dialogue, "admit")
sayDialogue(cynthia.dialogue, "figured")
sayDialogue(player.dialogue, "walk")
sayDialogue(cynthia.dialogue, "gardenEnd")

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
               print("You decide to stay for a little bit longer.\n")
               break
            elif confirmWalk == "i":
               openInventory()
               print("")
            else:
               print("Invalid input.\n")
      elif gardenChoice == "talk":
         if backyardQuest == False:
            sayDialogue(cynthia.dialogue, "robotQuestAcceptC1")
            sayDialogue(player.dialogue, "robotQuestAcceptP1")
            sayDialogue(cynthia.dialogue, "robotQuestAcceptC2")     
            sayDialogue(player.dialogue, "robotQuestAcceptP2")
            sayDialogue(cynthia.dialogue, "robotQuestAcceptC3")
            print("\n\033[1m""Quest Accepted: Find Cynthia's Robot""\033[0m\n")
            backyardQuest = True
         elif toyRobot in player.inventory:
            player.inventory.remove(toyRobot)
            print("You give Cynthia her toy robot.")
            sayDialogue(cynthia.dialogue, "robotQuestCompletedC1")
            sayDialogue(player.dialogue, "robotQuestCompletedP1")
            sayDialogue(cynthia.dialogue, "robotQuestCompletedC2")
            print("Cynthia hands you a flower pinwheel. Flower Pinwheel was added to your inventory.")
            player.inventory.append(flowerPinwheel)
            print("A moment later, Cynthia makes a face as if she has remembered something. She pauses for a moment, trying to think of how to put it into words. A chill runs down your spine.")
            sayDialogue(cynthia.dialogue, "robotQuestCompletedC3")
            print("Your friend Sydney was at the party last night, but you have no memory of interacting with her after the first hour or so. The few interactions you do remember were casual conversations about topics such as the food and the atmosphere of the party. You cannot think of anything you said or did that might have upset her. Cynthia notices the confused look on your face.")
            sayDialogue(cynthia.dialogue, "robotQuestEnd")
            print("\n\033[1m""Quest Completed: Find Cynthia's Robot""\033[0m\n")
         else:
            sayDialogue(cynthia.dialogue, "flowersC")
            sayDialogue(player.dialogue, "flowersP")
            print("Out of the corner of your eye, you can see her smiling.\n")
      elif gardenChoice == "garden":
         print("You take a look at Cynthia's garden. It contains a wide variety of beautiful flowers, all of which smell amazing.\n")
      elif gardenChoice == "basement":
         locationText("Cynthia's Basement")
         cynthiasBasement("N", backyardQuest)
      elif gardenChoice == "i":
         openInventory()
         print("")
      else:
         print("Invalid input.\n")

cynthiasBackyard(backyardQuest)

#school sequence
print("You apologize one more time to Cynthia before thanking her and saying goodbye. After a short walk, you arive at your place. You take a shower, get into a fresh change of clothes, eat breakfast, and pack your backpack before heading off the school for the day.")
print("\n\033[1m""Some time later...""\033[0m")
locationText("English Class")
print("Before you know it, you have made it to your final class of the day; English. You take a seat in your usual spot next to Cynthia and wait for your teacher, Mrs. Catherine, to give instructions.\n")
sayDialogue(catherine.dialogue, "assignment")

def english():
   assignmentComplete = False
   wordleComplete = False
   if flowerPinwheel in player.inventory:
      print("\nYou remember the flower pinwheel Cynthia gave you. You could probably use it for this assignment.")
      while assignmentComplete == False:
         classroomChoice = input("\nWould you like to show Mrs. Catherine the flower pinwheel, talk to Cynthia, or look around the classroom? Type either \"pinwheel,\" \"cynthia,\" or \"classroom.\"")
         if classroomChoice == "pinwheel":
            print("You wait for about 10 minutes to make it seem like you made the flower pinwheel yourself. You walk up to Mrs. Catherine and show her the pinwheel.\n")
            sayDialogue(catherine.dialogue, "pinwheel")
            sayDialogue(player.dialogue, "classroomThanks")
            assignmentComplete = True
         elif classroomChoice == "cynthia":
            sayDialogue(cynthia.dialogue, "wordleCy")
         elif classroomChoice == "classroom":
            print("You take a look around the classroom. There are bookshelves filled to the brim with novels, pictures of old students, and a few motivational posters.")
         elif classroomChoice == "i":
            openInventory()
         else:
            print("Invalid input.")
   else:
      while assignmentComplete == False:
         classroomChoice = input("\nWould you like to do the Wordle, talk to Cynthia, or look around the classroom? Type either \"wordle,\" \"cynthia,\" or \"classroom.\"")
         if classroomChoice == "wordle":
            playGame(wordleComplete)
            print("\nYou show Mrs. Catherine the completed Wordle.")
            sayDialogue(catherine.dialogue, "wordleCa")
            sayDialogue(player.dialogue, "classroomThanks")
            assignmentComplete = True
         elif classroomChoice == "cynthia":
            sayDialogue(cynthia.dialogue, "wordleCy")
         elif classroomChoice == "classroom":
            print("You take a look around the classroom. There are bookshelves filled to the brim with novels, pictures of old students, and a few motivational posters.")
         elif classroomChoice == "i":
            openInventory()
         else:
            print("Invalid input.")

english()

print("\nYou wait out the remainder of the class. As the bell rings and you are getting ready to leave, you notice something odd. A chill runs down your spine. Despite previously never missing a day of school in her entire life, your friend Syndey's seat...")
print("\033[1m""is empty.""\033[0m")

print("\n\033[1m""To be continued.""\033[0m")