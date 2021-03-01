# Course: CS 30
# Period: 1
# Date created: 21/03/01
# Date last modified: 21/03/01
# Name: Kira Gray
# Description: CS30 Final RPG game. All input must be
# lowercase

# Course: CS 30
# Period: 1
# Date created: 21/02/28
# Date last modified: 21/03/01
# Name: Kira Gray
# Description: RPG game with classes, no addition files yet
# Ill be doing that for the final game though

import title as ti
from classes import myPlayer
from classes import player
from map import zonemap
import map
global dest
global ask

ZONENAME = ''
DESCRIPTION = 'description'
SEARCH = 'search'
SOLVED = False
UP = 'up', 'north',
DOWN = 'down', 'south',
LEFT = 'left', 'west',
RIGHT = 'right', 'east',


def print_location():
    print('\n' + ('#' * (4 + len(myPlayer.location))))
    print('# ' + myPlayer.location + ' #')
    print('# ' + zonemap[myPlayer.location][DESCRIPTION] + ' #')
    print('\n' + ('#' * (4 + len(myPlayer.location))))


def move(myAction):
    ask = "Where would you like to "+myAction+" to?\n> "
    dest = input(ask)
    if dest == 'left':
        destination = zonemap[myPlayer.location][LEFT]
        move_player(destination)
    elif destination == 'right':
        destination = zonemap[myPlayer.location][RIGHT]
        move_player(destination)
    else:
        print("Invalid direction, try using left, or right.\n")
        move(myAction)


def move_player(destination):
    print("\nYou have moved to the " + destination + ".")
    myPlayer.location = destination
    print_location()



def continuous(ans):
    while ans:
        print("""
          Do one of the following actions:
          -> Move
          -> Explore
          -> Attack
          -> Quit
          """)
        print("What would you like to do?")
        ans = input("> ")
        if ans.lower() == "quit":
            break
        elif ans.lower() == "left":
            player.move(ans.lower())
            print("You go left.")
        elif ans.lower() == "right".lower():
            player.move(ans.lower())
            print("You go right.")
        elif ans.lower() == "Explore".lower():
            player.explore(ans.lower())
            print("You look around.")
        elif ans.lower() == "attack".lower():
            player.attack(ans.lower())
            print("You attack.")
        else:
            print("Invalid imput!")

def play_examine(ans):
    if zonemap[myPlayer.location] == 'a1' or 'b4':
        ask = "Would you like to go up?\n> "
        dest = input(ask)
        if dest == 'yes':
            destination = zonemap[myPlayer.location][UP]
            move_player(destination)
        else:
            continuous(ans)
    elif zonemap[myPlayer.location] == 'b2' or 'c2':
        ask = "Would you like to go down?\n> "
        dest = input(ask)
        if dest == 'yes':
            destination = zonemap[myPlayer.location][DOWN]
            move_player(destination)
        else:
            continuous(ans)
    else:
        zonemap[myPlayer.location][SEARCH]


def main_game_loop():
    while myPlayer.won is False:
        continuous(ans=True)


def setup_game():
    print('\nWelcome to The Hijack!\n')
    print('You have been hired to take back a cargo ship.')
    print('Only two pirates are involved. Good Luck!')
    main_game_loop()

ti.intro_text()
setup_game()
