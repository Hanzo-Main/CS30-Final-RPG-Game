# Course: CS 30
# Period: 1
# Date created: 21/03/01
# Date last modified: 21/03/01
# Name: Kira Gray
# Description: CS30 Final RPG game.

import title as ti
from classes import myPlayer
from game_map import zonemap
from game_map import print_map
global dest
global ask

# code for map
ZONENAME = ''
DESCRIPTION = 'description'
SEARCH = 'search'
SOLVED = False
UP = 'up', 'north',
DOWN = 'down', 'south',
LEFT = 'left', 'west',
RIGHT = 'right', 'east',


def print_location():
    """prints and moves where the player is on the map"""
    print('\n ' + myPlayer.location)
    print(zonemap[myPlayer.location][DESCRIPTION] + ' \n')


def move_player(destination):
    """prints where you have moved on the map"""
    print("\nYou have moved to the " + destination + ".")
    myPlayer.location = destination
    print_location()


def continuous(ans):
    """function that adds continuous gamplay"""
    while ans:
        print("""
          Do one of the following actions:
          -> Move
          -> Examine
          -> Attack
          -> Show Map
          -> Quit
          """)
        print("What would you like to do?")
        ans = input("> ")
        if ans.lower() == "quit":
            quit()
        elif ans.lower() == "move":
            move(ans)
        elif ans.lower() == "examine".lower():
            player_examine(ans)
        elif ans.lower() == "attack".lower():
            player_attack(ans)
        elif ans.lower() == "show map".lower():
            print_map()
        else:
            print("Invalid imput!")


def move(ans):
    """asks player where they want to move
    and helps move them there"""
    ask = "\nWhere would you like to go? \n> "
    dest = input(ask)
    if dest == 'left':
        destination = zonemap[myPlayer.location][LEFT]
        move_player(destination)
    elif dest == 'right':
        destination = zonemap[myPlayer.location][RIGHT]
        move_player(destination)
    else:
        print("Invalid direction, try using left, or right.\n")
        move(ans)


def player_examine(ans):
    """lets the player examine thier surroundings and
    travel up and down ladders"""
    if myPlayer.location == 'a1':
        ask = "\nWould you like to go up?\n"
        dest = input(ask)
        if dest == 'yes':
            destination = zonemap[myPlayer.location][UP]
            move_player(destination)
        else:
            continuous(ans)
    elif myPlayer.location == 'b4':
        ask = "\nWould you like to go up?\n> "
        dest = input(ask)
        if dest == 'yes':
            destination = zonemap[myPlayer.location][UP]
            move_player(destination)
    elif myPlayer.location == 'b2':
        ask = "\nWould you like to go down?\n> "
        dest = input(ask)
        if dest == 'yes':
            destination = zonemap[myPlayer.location][DOWN]
            move_player(destination)
    elif myPlayer.location == 'c2':
        ask = "\nWould you like to go down?\n> "
        dest = input(ask)
        if dest == 'yes':
            destination = zonemap[myPlayer.location][DOWN]
            move_player(destination)
        else:
            continuous(ans)
    else:
        print(zonemap[myPlayer.location][SEARCH] + '\n')


def player_attack(ans):
    """very basic attack function for the two enemys"""
    if myPlayer.location == 'b3':
        print("You shoot the pirate before he saw you!")
        continuous(ans)
    elif myPlayer.location == 'c4':
        print("You shot first!")
        print('\n You beat the game!')
        quit()


def main_game_loop():
    """Makes the game loop until it is beaten"""
    continuous(ans=True)


def setup_game():
    """prints starting text and map, also starts the game"""
    print('\nWelcome to The Hijack!\n')
    print('You have been hired to take back a cargo ship.')
    print('Only two pirates are involved. Good Luck!')
    print_map()
    main_game_loop()

ti.intro_text()
setup_game()
