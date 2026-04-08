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
                  (10)Dragon’s Core''')
    if dungeon=='1':
        print("You entered the Abandoned Entrance, a place filled with echoes of the past.\nThe air is thick with dust and the scent of decay. \nAs you step inside, you see remnants of old furniture and broken weapons scattered around.\nSuddenly, you hear a faint whisper coming from the shadows...")

while True:
    choice=input('''Choose an action:
                  (1)Explore a dungeon
                  (2)View inventory
                  (3)Check stats
                  (4)Exit game''')
    if choice=='1':
        dungeon()
    elif choice=='4':
        print("Thanks for playing! Goodbye!")
        break
