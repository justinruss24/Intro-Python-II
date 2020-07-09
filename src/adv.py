from room import Room
from player import Player
from item import Item
import sys
import textwrap

item = {
    "bag": Item("bag", "should be good for carrying all your things"),
    "sword": Item("sword", "its very sharp"),
    "hat": Item("hat", "very fashionable"),
    "treasure": Item("treasure", "congratulations! you've completed the search and found the treasure!")
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
room['outside'].items[0] = item['bag']
room['outside'].items.pop()

room['foyer'].items[0] = item['sword']
room['foyer'].items.pop()

room['overlook'].items[0] = item['hat']
room['overlook'].items.pop()


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


player1 = Player("Justin", room["outside"])

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
has_started = True
is_playing = False
while has_started:
    player_name = input("welcome to the game! to get started, please state your name: ")
    print("if you'd like to quit at any time, type 'q' to exit")
    player = Player(player_name, room['outside'])
    is_playing = True
    while is_playing:
        print("your current location is %s" % player.location)
        action = input("the choice is yours, where would you like to go? move your character by typing 'n' for north, 's' for south, 'e' for east, and 'w' for west. for clues, type 'help': ").split(' ')
        if str(action[0].lower() == 'help'):
            print(player.location.description)
        elif str(action[0].lower() == 'n'):
            if player.current_room.n_to:
                player.current_room = player.current_room.n_to
                pass
            else:
                print('not a valid option, try again')
        elif str(action[0].lower() == 'w'):
            if player.current_room.w_to:
                player.current_room = player.current_room.w_to
                pass
            else:
                print('not a valid option, try again')
        elif str(action[0].lower() == 'e'):
            if player.current_room.e_to:
                player.current_room = player.current_room.e_to
                pass
            else:
                print('not a valid option, try again')
        elif str(action[0].lower() == 's'):
            if player.current_room.s_to:
                player.current_room = player.current_room.s_to
                pass
            else:
                print('not a valid option, try again')
        elif str(action[0].lower() == 'q'):
            has_started = is_playing = False
        elif str(action[0]).lower() == 'look':
            if len(player.location.items) > 0:
                for x in player.location.items:
                    print('you can see a %s' % (x.name))
                item_action = input(
                    'would you like to take one of the items? type [get] [item name]: ').split(' ')
                if str(item_action[1]).lower() == 'treasure':
                    player.pick_up(player.location.items[0])
                    print('youve found the treasure! you win!')
                    is_playing, is_started = False, False
                elif str(player.location.items[0]) == str(item_action[1]).lower():
                    player.inventory.append(player.location.items[0])
                    player.location.items.remove(
                        player.location.items[0])
                elif len(player.location.items) > 1:
                    if str(player.location.items[1] == item_action[1]):
                        player.pick_up(player.location.items[1])
                    else:
                        pass
            else:
                print(
                    'besides the door you just came in from there doesnt seem to be anything')
        elif str(action[0]).lower() == 'drop':
            if len(action) == 1:
                print('what item do you want to drop?')
            elif len(action) > 1:
                for i in player.inventory:
                    if i.name == str(action[1]).lower():
                        player.drop_item(i)
                        pass
                    else:
                        print('you dont have that item')
                        pass
        elif str(action[0]).lower() == 'inventory':
            for j in player.inventory:
                print(j.name)
        elif player.location.current.lower() == 'treasure':
            print(
                'you found the mad gods treasure! congratulations take your trophy and escape')
            is_playing = False
            is_started = False
        elif str(action[0]).lower() == "command":
            print('[n] [e] [s] [w] [help] [look] [q] [inventory] [drop]')
        else:
            print('not a valid option')