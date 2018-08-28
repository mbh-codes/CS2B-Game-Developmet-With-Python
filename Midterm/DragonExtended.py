# DragonQuest
# A prequel to Dragon Realm By Aaron Hobson

# import stuff
import time
print()
# Global variables
score = 0
itemsOnPerson = {} #These are the items our character will be carrying.
itemsInMainCave = {'Sword of a Thousand Truths': "Steal",'Magical Shield':'Magic','Recorder': 'Music'} #These are the items in the main cabin.
itemsOutside = {'Nothing': "Nothing"} #Here you can add more items to have alternate endings
itemsInDeadEnd = {'Nothing': "Nothing"} #Here you can add more items to have alternate endings
rooms = {'Main Cave': itemsInMainCave, 'Outside': itemsOutside, 'Dead End': itemsInDeadEnd}
currentRoomKey = 'Main Cave'
caveNumbers = {"1":'Dead End',"2":"Outside","3":'Main Cave'}

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
            print(" "+item)
            time.sleep(1)
        print()
        print('What item do you pick up?')
        chosenItem = input()
    itemsOnPerson[chosenItem] = rooms[currentRoomKey][chosenItem]
    chosenItem = ''
    while chosenItem not in rooms[currentRoomKey]:
        for item in rooms[currentRoomKey]:
            print(" "+item)
            time.sleep(1)
        print("What item do you pick up?")
        chosenItem = input()
    itemsOnPerson[chosenItem] = rooms[currentRoomKey][chosenItem]
    print('Items on person:', itemsOnPerson)
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
              "     1: Run deeper into the cave\n"
              "     2: Run outside of the cave while charging\n"
              "     3: Hide and hope the dragons don't find you\n")
        cave = input()
    return cave


def fire_ending():
    print('The Dragon turns around and opens its jaws and ...')
    time.sleep(2)
    print("Unleashed a fiery attack on you and turns you into ashes!")

def check_room(room):
    global score
    if room == "Main Cave": #This will consist of three alternate endings in the Main Cave room
        print("You slip behind a rock as the dragons walk in.")
        time.sleep(2)
        print('The dragon enters the cave and heads deeper into tunnel.')
        time.sleep(2)
        if "Sword of a Thousand Truths" in itemsOnPerson:
            print('Clink clink')
            time.sleep(2)
            print('Your  brushes against the wall.')
            time.sleep(2)
            fire_ending()
            time.sleep(2)
            print("FATALITY!")
            if score >= 1:
                score -= 1
        elif "Magical Shield" in itemsOnPerson:
            print("Clink clink")
            time.sleep(2)
            print('Your shield brushes against the wall.')
            time.sleep(2)
            fire_ending()
            print('The Dragon turns around and continues deeper into the cave....')
            time.sleep(2)
            print('You open your eyes and your still alive!!!')
            time.sleep(2)
            print("The Magical Shield protected you from the Dragon's fire")
            time.sleep(2)
            print("You escaped alive!")
            score += 1
        elif "Recorder" in itemsOnPerson:
            print("The Dragon continues walking deeper into the cave and you escape.")
            score += 1
    elif room == "Dead End":#This will consist of three alternate endings in the Dead End room
        print("The ground begins to shake as the Dragon begins to enter the cave.")
        time.sleep(3)
        print("You run deeper into the cave....")
        time.sleep(3)
        print("and it's a dead end!")
        time.sleep(2)
        print("A big ol' DRAGON jumps into the cave and opens its jaw and..")
        time.sleep(2)
        if "Sword of a Thousand Truths" in itemsOnPerson:
            print("Stops to look at your sword")
            time.sleep(2)
            print("You take out your sword and begin charging towards the Dragon's belly")
            time.sleep(2)
            print("It steps on you.")
            time.sleep(2)
            print('BRUTALITY!')
            if score >= 1:
                score -= 1
        elif "Magical Shield" in itemsOnPerson:
            print("Begins to shoot fire..")
            time.sleep(2)
            print("BUT!!!")
            time.sleep(2)
            print("Your shield bounces the fires back towards the eyes of the Dragon and blinds it.")
            time.sleep(2)
            print("You escaped the cave.")
            score += 1
        elif "Recorder" in itemsOnPerson:
            print("You start playing the recorder.")
            time.sleep(2)
            print("The big ol' DRAGON lowers his head and points towards a riding saddle.")
            time.sleep(2)
            print("You fly away on the DRAGON playing the recorder.")
            score += 1
    elif room == 'Outside':
        print("The ground begins to shake as the Dragon lands outside of the cave.")
        time.sleep(2)
        print("You charge outside of the cave and ...")
        time.sleep(2)
        if "Sword of a Thousand Truths" in itemsOnPerson:
            print("You slay the beast!")
            time.sleep(2)
            print("but another big ol' Dragon flies in, picks you up, and releases you from an incredible height")
            time.sleep(2)
            print("BRUTALITY")
            if score >= 1:
                score -= 1
        elif "Magical Shield" in itemsOnPerson:
            print("You aim your shield to reflect the Dragon's breath right back at them.")
            time.sleep(2)
            print("You notice that you are on a mountain and you begin sprinting down the mountain.")
            time.sleep(2)
            print("More Dragons begin showing up, but they still can't damage you.")
            time.sleep(2)
            print("Dragons and their mommas begin showing up and still no damage is done to you.")
            time.sleep(2)
            print("You turn around in awe of how many Dragons there are and...")
            time.sleep(2)
            print("You trip on a pebble and the shield falls out of your hands.")
            time.sleep(3)
            print("BRUTALITY!!!")
            if score >= 1:
                score -= 1
        elif "Recorder" in itemsOnPerson:
            print("You begin playing the recorder.")
            time.sleep(2)
            print("The big ol' Dragon begins to dance in mid air.")
            time.sleep(2)
            print("More Dragons and their Mommas begin to show up and dance in mid air.")
            time.sleep(2)
            print("You become worshipped by the Dragon Civilization and you will be known in Dragon History as the Mother of Dragons")
            score += 1

def play():
    stillPlaying = True
    while stillPlaying:
        show_intro()
        time.sleep(2)
        show_phase1()
        print("The roaring of the dragons becomes deafening! This must be their layer!")
        cave = choose_cave()
        currentRoomKey = caveNumbers[cave]
        check_room(currentRoomKey)
        print("Would you like to play again? (y to continue, q to quit)")
        choice = input()
        if choice == "q":
            stillPlaying = False
        itemsOnPerson.clear()
    print("Your score: " + str(score))
    print("Goodbye! Thanks for playin', naaamean?")

# Play the game!
play()

