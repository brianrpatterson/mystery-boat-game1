
from termcolor import cprint

# create class for room attributes
class Room():
    def __init__(self, name, description=None, person=None):
        self.name = name
        self.N = None
        self.S = None
        self.E = None
        self.W = None
        self.description = description
        self.person = person
    
# class for people
class Person():
    def __init__(self, name, speech1, speech2, speech3):
        self.name = name
        self.speech1 = speech1
        self.speech2 = speech2
        self.speech3 = speech3
        self.speechcount = 1
    def dialogue(self, speechcount):
        if speechcount == 1:
            cprint(self.speech1, 'green')
            self.speechcount += 1
        elif speechcount == 2:
            cprint(self.speech2, 'green')
            self.speechcount += 1
        else:
            cprint(self.speech3, 'green')
            self.speechcount = 1

# default room when there is no room in the cardinal direction
noRoom = Room('noRoom')

# function to define which rooms are in each cardinal direction from a given room
# necessary because we can't refer to a nonexistent room when creating each room
def room_relationships(room: Room, north=noRoom, south=noRoom, east=noRoom, west=noRoom):
    room.N = north
    room.S = south
    room.E = east
    room.W = west

# create the person characters
terry = Person('Terry', 'Shame what happened to Kevin. Can\'t say I\'ll miss his dessert hoarding though.', 'I\'m on my way to a pest control convention. I work as a sales rep for a chemical company.', 'After I went to bed last night I heard an awful rukus coming from the deck. You weren\'t attacked were you?')
miguel = Person('Miguel', 'Crazy to think. We knew Kevin for such little time and now all we have to remember him by is the memory of his idiocy.', 'When we get to land I will probably get some more red paint to decorate this bird.', 'I\'m not sure anyone else noticed but when we found Kevin his hair was soaking wet.')
jack = Person('Jack','It\'s so exciting! A real murder! In person! This is great research for my book!', 'I am writing a murder mystery that takes place in a medieval castle. The killer is going to commit the crime with a candlestick.', 'I was in my room all night except for when you asked me for a towel.')

kevinroom = Room('Kevin\'s Cabin', 'In the room there is little more than a portrait of the most beautiful woman you have ever seen.')
terryroom = Room('Terry\'s Cabin', 'Terry is lounging on the bed and you observe an unopened container of rat poison, a lab coat, and rubber gloves.', terry)
miguelroom = Room('Miguel\'s Cabin', 'Miguel is whittling a small bird. His room contains a several knives, blocks of wood, and red stained cutting gloves.', miguel)
jackroom = Room('Jack\'s Cabin', 'Jack is typing furiously on a typewriter at his desk. There are manuscripts, antique candlesticks, and miniature castles in the room.', jack)
deck = Room('The Deck', 'A nice place when the weather is good. There are wet footprints running from the Galley going into your room.')
franklinroom = Room('Franklin\'s Cabin', 'Your own room. There is an empty wallet, some books, and an address book on the desk.')
salon = Room('The Salon', 'On the table there are playing cards from an unfinished game and several empty beer bottles.')
galley = Room('The Galley', 'A small, fairly plain kitchen. Nothing seems out of place apart from some wet footprints')
head = Room('The Head', 'A cramped ship\'s bathroom. There is a lot of water all over the sink and floor.')

room_relationships(kevinroom, west=terryroom, south=franklinroom)
room_relationships(terryroom, noRoom, deck, kevinroom, miguelroom)
room_relationships(miguelroom, east=terryroom, south=jackroom)
room_relationships(jackroom, miguelroom, head, deck)
room_relationships(deck, terryroom, galley, franklinroom, jackroom)
room_relationships(franklinroom, kevinroom, salon, noRoom, deck)
room_relationships(salon, franklinroom, west=galley)
room_relationships(galley, deck, noRoom, salon, head)
room_relationships(head, jackroom, east=galley)

cprint('Welcome!', 'red')
cprint('''You(Francis) are a passenger on a boat bound for another country.
      Things were going well with you and your fellow travelers until one of them, Kevin, was found dead. You have been designated as the detective. Your job is to interview the other passengers, inspect the ship, and determine who the murderer is.''', 'blue')
print('To list controls type "help" when prompted.')

# movement logic
current_room = kevinroom
move_counter = 1

def changeroom(newroom, oldroom):
    if newroom != noRoom:
        print(f'You move into the {newroom.name} room. {newroom.description}')
        global move_counter
        move_counter += 1
        return newroom
    else:
        print('You have reached the edge of the boat that direction.')
        return oldroom

def endgame():
    print('Welcome to the conclusion. As you are likely aware it appears you are the killer. Unfortunately for you the other people on the boat realized this and tie you up. As soon as you land, police come onboard and arrest you. Now you wait in jail for your sentencing wishing you had dried all the water better.')

while True:
    user_command = input('Please enter a command. > ')
    if user_command == 'help':
        print('''The available commands are:
            "Bow" - move to the room closer to the bow of current if available
            "Starboard" - move to the room starboard of current if available
            "Stern" - move to the room closer to the stern of current if available
            "Port" - move to the room port of current if available
            "look" - observe the contents of the current room
            "talk" - speak with whoever is currently in the room, this command can be repeated to get more dialogue
            "help" - prints this menu
            "end_game" - use to end the game and read the conclusion when you are ready
            ''')
    elif user_command.upper() == 'BOW':
        current_room = changeroom(current_room.N, current_room)
    elif user_command.upper() == 'STARBOARD':
        current_room = changeroom(current_room.E, current_room)
    elif user_command.upper() == 'STERN':
        current_room = changeroom(current_room.S, current_room)
    elif user_command.upper() == 'PORT':
        current_room = changeroom(current_room.W, current_room)
    elif user_command.upper() == 'LOOK':
        print(current_room.description)
    elif user_command.upper() == 'TALK':
        if current_room.person != None:
            current_room.person.dialogue(current_room.person.speechcount)
        else:
            print('There is nobody here to talk to.')
    elif user_command.upper() == 'END_GAME':
        endgame()
        break
    else:
        print('Sorry that isn\'t a recognized command. Please try again or type "help" for a list of possible commands')


