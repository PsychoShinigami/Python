print("Welcome to the Dungeons!")
user=input("Type your display name for the game:")

def dungeon():
    dungeon=input('''Choose a dungeoon to explore:
                  (1)Abandoned Entrance 
                  (2)Spider Nest 
                  (3)Whispering Hall 
                  (4)Skeleton Crypt
                  (5)Poison Swamp Chamber
                  (6)Dark Maze 
                  (7)Frozen Prison
                  (8)Cursed Temple 
                  (9)Shadow King’s Domain
                  (10)Dragon’s Core
                  =>''')
    
    if dungeon=='1':
        print("You entered the Abandoned Entrance, a place filled with echoes of the past.\nThe air is thick with dust and the scent of decay. \nAs you step inside, you see remnants of old furniture and broken weapons scattered around.\nSuddenly, you hear a faint whisper coming from the shadows...")
        a1=input("The whisper grows louder, and you realize it's a ghostly voice warning you to leave. \nDo you choose to investigate the source of the whisper(1) or exit the dungeon?(2) =>")

        if a1=='2':
            print("You decide to heed the warning and exit the dungeon safely. \nMaybe you'll explore it another time.")
        elif a1=='1':
            b1=input("You follow the whisper deeper into the dungeon, and it leads you to a hidden chamber. \nInside, you find a treasure chest. \nWould you like to open it? (1)Yes (2)No =>")
            if b1=='yes' or b1=='1':
                print("You open the chest and find an old sword.\nCongratulations, you found a valuable item to add to your inventory!")
                print("While you were putting the sword in your backpack, you saw a black entity coming towards you. \nIt seems to be a ghostly figure, and it starts to approach you slowly.")
                c1=input("Do you choose to confront the entity (1) or try to escape (2)? => ")
                if c1=='1':
                    print("You tried to stab the entity with your sword, but it passed through it like a ghost. \nThe entity actually wanted to talk to you but after seeing you trying to attack it, it got angry and prisoned you in a cage. \nYou are now trapped in the dungeon forever, Game over!.")
                elif c1=='2':
                    print("You quickly turn around and run towards the exit, with the entity chasing you. \nBefore you could reach the exit, the entity catches up to you and saids, 'Why are you running? I just wanted to talk.' \nYou stop in your tracks, and the entity seems to calm down. \nIt tells you that it is a spirit of a former adventurer who got trapped in the dungeon and has been trying to find a way out for years. \nThe entity offers to help you escape if you promise to free it from the dungeon.")
                    d1=input("Do you agree to help the entity (1) or refuse (2)? =>")
                    if d1=='1':
                        print("You agreed to help the entity. \nThe entity tells you the method to free it from the curse, which involves finding a hidden artifact in the dungeon and using it to break the curse. \nYou set off on a quest to find the artifact, facing various challenges and obstacles along the way. \nAfter a long and perilous journey, you finally find the artifact and use it to break the curse, freeing the entity from its prison. \nThe entity thanks you for your help and offers to guide you out of the dungeon safely.")
                        print("You follow the entity's guidance and successfully escape the dungeon. \nAs you step outside, you feel a sense of relief and accomplishment. \nYou have not only escaped the dungeon but also helped a trapped spirit find freedom. \nCongratulations on your successful adventure!")
                    elif d1=='2':
                        print("You refused to help the entity, and it becomes angry. \nThe entity says, 'Little brat whom do you think you're refusing to help?' \nThe entity then attacks you, and cut you into pieces within a second. \nYou have died. Game over.") 
            elif b1=='no' or b1=='2':
                e1=input("You decide not to open the chest and continue ecploring the dungeon. \nAs you walk further, you found a hidden artifact.\nAs you pick it up, you see a black entity coming towards you. \nIt wanted to talk to you but after seeing you have the artifact in your hand, it shout at you, 'Give me that artifact! I need it to break the curse!' \nDo you choose to give the artifact to the entity (1) or keep it for yourself (2)? =>")
                if e1=='1':
                    print("You decided to give the artifact to the entity. \nThe entity takes the artifact and thanks you for your kindness. \nIt then uses the artifact to break the curse, freeing itself from the dungeon. \nThe entity offers to guide you out of the dungeon safely, and you follow its guidance to successfully escape. \nCongratulations on your successful adventure!")
                elif e1=='2':
                    print("You decided to keep the artifact for yourself. \nThe entity becomes angry and says, 'You selfish brat! I needed that artifact to break the curse!' \nThe entity then attacks you, and cut you into pieces within a second. \nYou have died. Game over.")
        else:
            print("Invalid choice. You had to choose either (1) or (2).")

while True:
    choice=input('''Choose an action:
                  (1)Explore a dungeon
                  (2)View inventory
                  (3)Check stats
                  (4)Exit game
                  =>''')
    if choice=='1':
        dungeon()
    elif choice=='4':
        print("Thanks for playing! Goodbye!")
        break
