print("Welcome to the Dungeons!")
user=input("Type your display name for the game:")

def dungeon():
    dungeon=input('''Choose a dungeon to explore:
                  (1)Abandoned Entrance 
                  (2)Dark Maze 
                  (3)Frozen Prison 
                  (4)Shadow King’s Domain
                  (5)Dragon’s Core
                  =>''')
    
    if dungeon=='1':
        print(f"{user}, you entered the Abandoned Entrance, a place filled with echoes of the past.\nThe air is thick with dust and the scent of decay. \nAs you step inside, you see remnants of old furniture and broken weapons scattered around.\nSuddenly, you hear a faint whisper coming from the shadows...")
        a1=input("The whisper grows louder, and you realize it's a ghostly voice warning you to leave. \nDo you choose to investigate the source of the whisper(1) or exit the dungeon?(2) =>")

        if a1=='2':
            print(f"{user}, you decide to heed the warning and exit the dungeon safely. \nMaybe you'll explore it another time.")
        elif a1=='1':
            b1=input("You follow the whisper deeper into the dungeon, and it leads you to a hidden chamber. \nInside, you find a treasure chest. \nWould you like to open it? (1)Yes (2)No =>")
            if b1=='yes' or b1=='1':
                print(f"{user}, you open the chest and find an old sword.")
                print("While you were putting the sword in your backpack, you saw a black entity coming towards you. \nIt seems to be a ghostly figure, and it starts to approach you slowly.")
                c1=input("Do you choose to confront the entity (1) or try to escape (2)? => ")
                if c1=='1':
                    print(f"{user}, you tried to stab the entity with your sword, but it passed through it like a ghost. \nThe entity actually wanted to talk to you but after seeing you trying to attack it, it got angry and imprisoned you in a cage. \nYou are now trapped in the dungeon forever, Game over!.")
                elif c1=='2':
                    print(f"{user}, you quickly turn around and run towards the exit, with the entity chasing you. \nBefore you could reach the exit, the entity catches up to you and said, 'Why are you running? I just wanted to talk.' \nYou stop in your tracks, and the entity seems to calm down. \nIt tells you that it is a spirit of a former adventurer who got trapped in the dungeon and has been trying to find a way out for years. \nThe entity offers to help you escape if you promise to free it from the dungeon.")
                    d1=input("Do you agree to help the entity (1) or refuse (2)? =>")
                    if d1=='1':
                        print(f"{user}, you agreed to help the entity. \nThe entity tells you the method to free it from the curse, which involves finding a hidden artifact in the dungeon and using it to break the curse. \nYou set off on a quest to find the artifact, facing various challenges and obstacles along the way. \nAfter a long and perilous journey, you finally find the artifact and use it to break the curse, freeing the entity from its prison. \nThe entity thanks you for your help and offers to guide you out of the dungeon safely.")
                        print(f"{user}, you follow the entity's guidance and successfully escape the dungeon. \nAs you step outside, you feel a sense of relief and accomplishment. \nYou have not only escaped the dungeon but also helped a trapped spirit find freedom. \nCongratulations on your successful adventure!")
                    elif d1=='2':
                        print(f"{user}, you refused to help the entity, and it becomes angry. \nThe entity says, 'Little brat whom do you think you're refusing to help?' \nThe entity then attacks you, and cut you into pieces within a second. \nYou have died. Game over.") 
            elif b1=='no' or b1=='2':
                e1=input("You decide not to open the chest and continue exploring the dungeon. \nAs you walk further, you found a hidden artifact.\nAs you pick it up, you see a black entity coming towards you. \nIt wanted to talk to you but after seeing you have the artifact in your hand, it shout at you, 'Give me that artifact! I need it to break the curse!' \nDo you choose to give the artifact to the entity (1) or keep it for yourself (2)? =>")
                if e1=='1':
                    print(f"{user}, you decided to give the artifact to the entity. \nThe entity takes the artifact and thanks you for your kindness. \nIt then uses the artifact to break the curse, freeing itself from the dungeon. \nThe entity offers to guide you out of the dungeon safely, and you follow its guidance to successfully escape. \nCongratulations on your successful adventure!")
                elif e1=='2':
                    print(f"{user}, you decided to keep the artifact for yourself. \nThe entity becomes angry and says, 'You selfish brat! I needed that artifact to break the curse!' \nThe entity then attacks you, and cut you into pieces within a second. \nYou have died. Game over.")
        else:
            print("Invalid choice. You had to choose either (1) or (2).")

    elif dungeon=='2':
        print(f"{user}, you entered the Dark Maze, a labyrinth filled with twists and turns. \nThe walls are covered in moss, and the air is damp and musty. \nAs you navigate through the maze, you hear strange noises echoing around you...")
        print("The voice was of the mystery man who is the boss of the maze. \nHe said, 'Welcome to my maze, adventurer. If you want to escape, you must find the hidden key and unlock the exit door. But be warned, there are many traps and monsters lurking in the maze, and I will be watching your every move.'")
        print(f"{user}, you start to explore the maze, trying to find the hidden key. \nAs you walk through the maze,you find a chest with golds and a sword in it. \nAs you open the chest and keep the loot, you encounter a group of goblins who are blocking your path. \nThey demand that you give them the loot you just found, or they will attack you.")
        a2=input("Do you choose to fight the goblins (1) or give them the loot (2)? =>")
        if a2=='1':
            print(f"{user}, you decide to fight the goblins. \nYou draw your sword which you had picked up from the chest, and engage in battle with the goblins. \nAfter a fierce fight, you manage to defeat the goblins and continue on your way. \nHowever, you are now injured and have lost some of your health.")
            print(f"{user}, you continue to explore the maze, and get lost in the twists and turns. \nAfter hours of wandering, you finally reach to the point where it was written one of the path has the key and one of the path gives you huge treasure. \nYou have to choose which path to take. \nDo you choose the key path (1) or the treasure path (2)? =>")
            b2=input("Do you choose the key path (1) or the treasure path (2)? =>")
            if b2=='1':
                print(f"{user}, you decide to take the key path. \nYou follow the path and fall into a trap, which causes you to lose all your health. \nYou have died. Game over. Sometimes you should be little greedy :)")
            elif b2=='2':
                print(f"{user}, you decide to take the treasure path. \nYou follow the path and find a room filled with gold and jewels. \nAlso you find the hidden key that you need to escape the maze. \nYou take the treasure and the key, and the hidden man appears and says, 'Ah… clever choice. Most fools chase the key like obedient puppets. But you… you chose greed. And greed is what this maze rewards.' \nCongratulations, {user}! You have successfully escaped the Dark Maze")
        
        elif a2=='2':
            print(f"{user}, you decide to give the goblins the loot. \nThe goblins snatch the loot from you and the sword too. \nThey then laugh at you and tore you apart.")
            print("You have died. Game over.")

    elif dungeon=='3':
        print(f"{user}, you entered the Frozen Prison, where you see many people trapped as slaves. \nThe air is freezing cold, and the walls are covered in ice. \nAs you explore the prison, you see a group of guards patrolling the area, and they seem to be looking for something...")
        a3=input("You hide behind a pillar and observe the guards. \nYou see that they are looking for a prisoner who has escaped from his cell. \nDo you choose to help the guards find the escaped prisoner (1) or try to find the prisoner yourself (2)? =>")
        if a3=='1':
            print(f"{user}, you decide to help the guards find the escaped prisoner. \nYou join the guards in their search, and after a while, you find the escaped prisoner hiding in a corner. \nThe guards thank you for your help and then kill the prisoner with ice bergs. \nThen you get to know that all the prisoners in the dungeon are actually innocent people who were captured and enslaved by the guards. \nYou feel guilty for helping the guards, and you decide to free the remaining prisoners. \nAfter getting rid of the guards, you explore the prison and find some good gears and weapons and the portal of the outside world. \nYou rush to free the prisoners but get caught by the guards.")
            b3=input("The guards say, 'You think you can free our slaves? You are just a weak adventurer! We will make an example out of you!' \nDo you choose to fight the guards (1) or surrender (2)?")
            if b3=='1':
                print(f"{user}, you decide to fight the guards. \nYou draw your weapon and engage in battle with the guards. \nBut they had the power of ice, and they easily overpower you. \nYou have died. Game over. Sometimes you should not rush :)")    
            elif b3=='2':
                print(f"{user}, you decide to surrender. \nThe guards laugh at you and say, 'You are a fool to surrender. You will be taken to our boss, and he will decide your fate.' \nYou are then taken to the boss of the prison, who is a powerful ice mage. \nYou then asked the boss to 1v1 you with the condition that if you win, he will free the prisoners or if you lose, you will be frozen in ice forever.")
                print(f"{user}, the boss agrees to your challenge and says, 'Very well, I will give you a chance to prove yourself. But be warned, I am a powerful ice mage, and I will not go easy on you.' \nThe battle begins, and you use all your skills and strategies to fight against the boss. \nAfter a long and intense battle, you manage to defeat the boss as it was a 1v1 match and free the prisoners. \nThe prisoners thank you for your bravery and help, and they offer you a share of the treasure they found.")
                c3=input("Do you choose to take the treasure (1) or decline the offer (2)? =>")
                if c3=='1':
                    print(f"{user}, you decide to take the treasure. \nYou take the treasure. \nThe prisoners are grateful for your help and offer to guide you out of the prison safely. \nCongratulations, {user}! You have successfully escaped the Frozen Prison and helped free innocent people in the process!")
                elif c3=='2':
                    print(f"{user}, you decide to decline the offer. \nYou thank the prisoners for their gratitude but say that you do not need any reward for helping them. \nBut the prisoners were a bunch of crazy people, and they all jump on you and kill you. \nYou have died. Game over. Sometimes you should just take the free stuff :)")
        elif a3=='2':
            print(f"{user}, you decide to try to find the prisoner yourself. \nYou sneak around the prison and eventually find the escaped prisoner. \nYou tried to help the prisoner escape, but guards caught you on way and killed both of you using ice powers. Game over you died!")

    elif dungeon=='4':
        print("You have entered the domain of the Shadow King!")
        print("When you step into this dark realm, you feel a chill run down your spine.\nThe atmosphere is red and rough, and the ground is covered in a layer of darkness.")
        print("Wherever you see, you notice a void entity everywhere with menacing eyes.")
        a4=input("You see a throne glowing with dark energy. Choose (1) to sit on it or (2) to ignore it and explore => ")
        if a4=='1':
            print('''You sit on the throne...
Power rushes through your body.
The Shadow King laughs:
"Fool... you are now my vessel."
You lose control of your body.
Game Over.''')
        elif a4=='2':
            print('''You ignore the throne and explore the domain.
While exploring, a whisper says:
'I can help you escape.. trust me.'
                  ''')
            b4=input("Do you choose to trust the whisper (1) or stay silent (2)? => ")
            if b4=='1':
                print('''The voice laughs and traps you in darkness forever.
Game Over.''')
            elif b4=='2':
                print('''You stay silent and continue exploring.
The shadow king appears:
"I will give you power beyond imagination…
or you can try to escape like a coward."''')
                c4=input("Do you choose to accept the Shadow King's offer (1) or try to escape (2)? => ")
                if c4=='1':
                    print('''You accept the Shadow King's offer.
You become the next Shadow King…
But lose your humanity.Game Over.''')
                elif c4=='2':
                    print('''As you try to escape, the Shadow King laughs:
"You think you can escape me? I am the darkness itself!"
But you hear that whisper again:
trust me, I can help you escape.''')
                    d4=input("Do you choose to trust the whisper (1) or try to escape on your own (2)? => ")
                    if d4=='1':
                        print(f'''You follow the whisper which said to jump into a portal of light.
which appears out of nowhere, and you escape the Shadow King's domain.
Congratulations, {user}! You have successfully escaped the Shadow King's domain!''')
                    elif d4=='2':
                        print('''You try to escape on your own, but the Shadow King is too powerful.
He catches you and says:
"You are no match for me. You will live inside my shadow forever."
Game Over.''')
    elif dungeon=='5':
        a5=input('''Are you sure you want to enter the Dragon’s Core?
This is the hardest dungeon.
1. Yes
2. No
=>''')
        if a5=='1':
            b5=input('''You step into the Dragon’s Core...
The ground shakes.
A massive dragon appears in front of you.
Its eyes glow with fire
1. Stand still
2. Run
=>''')
            if b5=='1':
                print(f'''The dragon looks at you...
Then suddenly- 
It sits down like a puppy and says:
Yoo I finally got my master back!
Congratulations, {user}! You have successfully completed the easiest dungeon xD! and befriended the dragon and become its master!''')
            elif b5=='2':
                print(f'''You try to run, but the dragon teleports you back to its side.
It sits down like a puppy and says:
Yoo I finally got my master back!
Congratulations, {user}! You have successfully completed the easiest dungeon xD! and befriended the dragon and become its master!''')
        elif a5=='2':
            print("You decide not to enter the Dragon’s Core. Maybe you'll explore it another time.")
    




        
while True:
    choice=input('''Choose an action:
                  (1)Explore a dungeon
                  (2)Exit game
                  =>''')
    if choice=='1':
        dungeon()
    elif choice=='2':
        print("Thanks for playing! Goodbye!")
        break

