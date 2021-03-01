def print_map():
    print("""╔════════════╦════════════╦═════════════╦════════════╗
             ║   Latter   ║ Cargo Left ║ Cargo Right ║ Hyperdrive ║
             ║ (2nd  lvl) ║  (*start)  ║  (and map)  ║    Room    ║
             ╠════════════╬════════════╬═════════════╬════════════╣
             ║    Crew    ║   Latter   ║ Living Area ║   Latter   ║
             ║  Quarters  ║ (to start) ║             ║ (3rd  lvl) ║
             ╠════════════╬════════════╬═════════════╬════════════╣
             ║  Captains  ║   Latter   ║ Locked Room ║  Cockpit   ║
             ║  Quarters  ║ (2nd  lvl) ║             ║            ║
             ╚════════════╩════════════╩═════════════╩════════════╝
          """)

ZONENAME = ''
DESCRIPTION = 'description'
SEARCH = 'search'
SOLVED = False
UP = 'up', 'north',
DOWN = 'down', 'south',
LEFT = 'left', 'west',
RIGHT = 'right', 'east',

solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False,
                 'b1': False, 'b2': False, 'b3': False, 'b4': False,
                 'c1': False, 'c2': False, 'c3': False, 'c4': False,
                 }

zonemap = {
    'a1': {
        ZONENAME: 'Latter up',
        DESCRIPTION: 'There is a latter going up.',
        SEARCH: 'The start is to the right.',
        UP: 'b2',
        DOWN: '',
        LEFT: '',
        RIGHT: 'a2',
    },
    'a2': {
        ZONENAME: 'Cargo left',
        DESCRIPTION: """This is the start. cargo containers are piled high
        """,
        SEARCH: """There is more cargo on the right and a latter going up on the left
        """,
        UP: '',
        DOWN: '',
        LEFT: 'a1',
        RIGHT: 'a3',
    },
    'a3': {
        ZONENAME: 'Cargo right',
        DESCRIPTION: 'More cargo containers',
        SEARCH: """Theres a door to the right and the other side of the cargo hold on the left
        """,
        UP: '',
        DOWN: '',
        LEFT: 'a2',
        RIGHT: 'a4',
    },
    'a4': {
        ZONENAME: 'Hyperdrive room',
        DESCRIPTION: 'locked',
        SEARCH: 'the only way is to the cargo hold on the left',
        UP: '',
        DOWN: '',
        LEFT: 'a3',
        RIGHT: '',
    },
    'b1': {
        ZONENAME: 'Crew Quarters',
        DESCRIPTION: """there is a table and beds. There are two pirates""",
        SEARCH: 'the only way is right to the latter going down',
        UP: '',
        DOWN: '',
        LEFT: '',
        RIGHT: 'b2',
    },
    'b2': {
        ZONENAME: 'Latter down',
        DESCRIPTION: 'Latter that goes down',
        SEARCH: """Crew Quarters are to the left and the living area
        to the right""",
        UP: '',
        DOWN: 'a1',
        LEFT: 'b1',
        RIGHT: 'b3',
    },
    'b3': {
        ZONENAME: 'Living area',
        DESCRIPTION: """typical living arrangements. There is one pirates""",
        SEARCH: """the latter going down on the left and a latter
        going up on the right. You found a key card!""",
        UP: '',
        DOWN: '',
        LEFT: 'b2',
        RIGHT: 'b4',
    },
    'b4': {
        ZONENAME: 'Latter up',
        DESCRIPTION: 'There is a latter going up.',
        SEARCH: 'The living area is to the left.',
        UP: 'c2',
        DOWN: '',
        LEFT: 'b3',
        RIGHT: '',
    },
    'c1': {
        ZONENAME: 'Captains Quarters',
        DESCRIPTION: 'locked',
        SEARCH: 'There is a latter going down to the right',
        UP: '',
        DOWN: '',
        LEFT: '',
        RIGHT: 'c2',
    },
    'c2': {
        ZONENAME: 'Latter down',
        DESCRIPTION: 'Latter that goes down.',
        SEARCH: """The captains quarters is on the left and a
        locked room on the right.""",
        UP: '',
        DOWN: 'b4',
        LEFT: 'c1',
        RIGHT: 'c3',
    },
    'c3': {
        ZONENAME: 'Locked room',
        DESCRIPTION: """You use the key card! There is nothing in the room,
        it's just a room leading to the cockpit.""",
        SEARCH: """The latter going down is on the left and the
        cockpit is to the right.""",
        UP: '',
        DOWN: '',
        LEFT: 'c2',
        RIGHT: 'c4',
    },
    'c4': {
        ZONENAME: 'Cockpit',
        DESCRIPTION: """The captain,
        everything else is normal""",
        SEARCH: """the only way is to the left back to the locked room""",
        UP: '',
        DOWN: '',
        LEFT: 'c3',
        RIGHT: '',
    },
}