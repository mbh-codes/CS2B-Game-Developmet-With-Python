# Dragon Realm

# import stuff
import random
import time
print()
# Global variables
score = 0
itemsOnPerson = {'Bare Hands': 'Flesh'} #These are the items our character will be carrying.
itemsInMainCave = {'Sword of a Thousand Truths': "Steal",'Magical Shield':'Magic','Recorder': 'Music'} #These are the items in the main cabin.
itemsOutside = {'Nothing': "Nothing"}
itemsInDeadEnd = {'Nothing': "Nothing"}
rooms = {'Main Cave': itemsInMainCave, 'Outside': itemsOutside, 'Dead End': itemsInDeadEnd}
currentRoomKey = 'Main Cave'
caveNumbers = {'1':'Main Cave','2':"Outside",'3':'Dead End'}

# Show Introduction
def show_intro():
    print('''You wake up dazed and confused in a dark cave. 
You stand up and see that there is tunnel that leads    
further into the cave and that there is a tunnel that leads outside. ''')

    print()

def choose_item():
    chosenItem = ''
    print('''You look around and you see:''')
    time.sleep(2)
    while chosenItem not in rooms[currentRoomKey]:
        for item in rooms[currentRoomKey]:
            print(item)
            time.sleep(1)
        print('What item do you pick up?')
        chosenItem = input()
    itemsOnPerson[chosenItem] = rooms[currentRoomKey][chosenItem]
    print('You have chosen:', chosenItem)
    return chosenItem


def show_phase1():
    print('''All of sudden you hear dragons roaring from far away. ''')
    time.sleep(1)
    print()
    choose_item()



def choose_cave():
    cave = ""
    while cave != "1" and cave != "2" and cave != "3":
        print("Where will you go? \n"
              "Run deeper into the cave: 1 \n"
              "Hide and hope the dragons don't find you: 2 \n"
              "Run outside of the cave while flailing your arms: 3 \n")
        cave = input()
    return cave



def check_cave(cave_chosen):
    global score
    if cave_chosen == "1":
        print("You approach the cave slowly...")
    time.sleep(2)
    print("Smells like dragon farts...")
    time.sleep(2)
    print("A big ol' DRAGON jumps out in front of you and opens its jaws and...")
    print()
    time.sleep(2)
    friendly_dragon = random.randint(1, 2)
    if cave_chosen == str(friendly_dragon):
        print("Gives you his treasure!")
        score += 1
    else:
        print("He farts on you.")
        if score >= 1:
            score -= 1

def play():
    stillPlaying = True
    while stillPlaying:
        show_intro()
        time.sleep(2)
        show_phase1()
        print("The roaring of the dragons becomes deafening! This must be their layer!")
        cave = choose_cave()
        check_cave(cave)
        print("Would you like to play again? (y to continue, q to quit)")
        choice = input()
        if choice == "q":
            stillPlaying = False
    print("Your score: " + str(score))
    print("Goodbye! Thanks for playin', naaamean?")

# Play the game!
play()

