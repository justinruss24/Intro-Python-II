from room import Room
from player import Player
from item import Item
import sys
import textwrap

item = {
    "bag": Item("bag", "should be good for carrying all your things"),
    "sword": Item("sword", "its very sharp"),
    "hat": Item("hat", "very fashionable"),
    "trophy": Item("trophy", "congratulations! you've completed the search and found the trophy!")
}

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# adding items to rooms
room['foyer'].items[0] = item['bag']
room['narrow'].items[0] = item['sword']
room['overlook'].items[0] = item['hat']
room['treasure'].items[0] = item['trophy']

def hasItem():
    if(player.location.items):
        pickup = input("Looks like there's a %s, would you like to pick it up? Type 'y' for yes, and 'n' for no." % (player.location.items[0]))
        if(pickup == 'y'):
            player.inventory.append(item)
            print("good choice! can't believe someone left this behind.")
            player.location.items.clear()
        elif(pickup == 'n'):
            print("ok, if you say so.")
        else:
            print("that command doesn't do anything")
    else:
        print("looks like the room is empty.")




# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.




# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
is_started = True
is_playing = False
while is_started:
    player_name = input("Welcome to the adventure game! What is your name?: ")
    player = Player(player_name, room['outside'])
    print("Awesome,", player.name, ", you are currently", player.location,
          ". To go anywhere, use 'n', 's', 'e', and 'w'. For help, type 'help', and to quit at any time, type 'q'!")
    is_playing = True
    while is_playing:
        action = input("What would you like to do?: ").split(' ')
        # print(action[0])
        if str(action[0]) == 'help':
            print(player.location)
        elif str(action[0]) == 'q':
            print("we hate to see you go so soon, but good luck on all future endeavors.")
            is_playing = False
        elif str(action[0]) == 'n':
            if player.location.n_to:
                player.location = player.location.n_to
                print(player.location)
                hasItem()
                print(player.location)
            else:
                print("there is nothing in that direction..")
        elif str(action[0]) == 's':
            if player.location.s_to:
                player.location = player.location.s_to
                print(player.location)
                hasItem()
                print(player.location)
            else:
                print("there is nothing in that direction..")
        elif str(action[0]) == 'w':
            if player.location.w_to:
                player.location = player.location.w_to
                print(player.location)
                hasItem()
                print(player.location)
            else:
                print("there is nothing in that direction..")
        elif str(action[0]) == 'e':
            if player.location.e_to:
                player.location = player.location.e_to
                print(player.location)
                hasItem()
                print(player.location)
            else:
                print("there is nothing in that direction..")
        else:
            print("That command won't do you any good.. Try again!")
