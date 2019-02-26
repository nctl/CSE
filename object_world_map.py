class Room(object):
    def __init__(self, name, north=None, south=None, east=None, west=None, description=None):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.description = description


"""
Example
R19A = Room("Mr. Wiebe's Room")
parking_lot = Room("The Parking Lot", None, R19A)
R19A.north = parking_lot
"""

library = Room("Library", None, None, None, None, "Desc.")
quad = Room("Name", None, None, None, None, "Desc.")
N40 = Room("N40", None, None, None, None, "Desc.")
gym_1 = Room("Main Gym", N40, None, None, None, "Desc.")
north_hall = Room("Northern Hall", None, quad, None, N40, "Desc.")
south_hall = Room("Southern Hall", quad, None, None, None, "Desc.")
cafe = Room("Cafeteria", library, None, south_hall, None, "Desc.")
office = Room("Office", gym_1, library, quad, None, "Desc.")  # You start here
bathroom = Room("Restroom", None, None, None, north_hall, "Desc.")

library.north = office
library.west = cafe
library.east = quad
quad.north = north_hall
quad.west = office
quad.south = south_hall
N40.south = gym_1
N40.east = north_hall
gym_1.south = office
north_hall.east = bathroom
south_hall.west = cafe


class Player(object):
    def __init__(self, starting_location):
        self.inventory = []
        self.current_location = starting_location

    def move(self, new_location):
        """

        :param new_location:
        """

    def find_room(self, direction):
        """

        :param direction:
        :return: north, south, east, west
        """
        return getattr(self.current_location, direction)


player = Player(None)


# Controller
directions = ["north", "south", "east", "west", "up", "down"]
playing = True
while playing:
    print(player.current_location.name)

    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command in directions:
        try:
            room_name = current_node["PATHS"][command]
            current_node = world_map[room_name]
        except KeyError:
            print("I can't go that way.")
    else:
        print("Command not recognized.")