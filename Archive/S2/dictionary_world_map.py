# Current node = Current location
playing = True
world_map = {  # Please collapse this menu with [-]
    '#31': {
        'NAME': "",
        'DESCRIPTION': "",
        'PATHS': {
        }},

    '#21': {
        'NAME': "",
        'DESCRIPTION': "",
        'PATHS': {
        }},

    '#81': {
        'NAME': "",
        'DESCRIPTION': "",
        'PATHS': {
        }},

    '#753': {
        'NAME': "",
        'DESCRIPTION': "",
        'PATHS': {
        }},

    '#121': {
        'NAME': "",
        'DESCRIPTION': "",
        'PATHS': {
        }},

    '#69': {
        'NAME': "",
        'DESCRIPTION': "",
        'PATHS': {
        }},

    '#10': {
        'NAME': "",
        'DESCRIPTION': "",
        'PATHS': {
        }},

    '#234': {
        'NAME': "",
        'DESCRIPTION': "",
        'PATHS': {
        }},

    '#11': {
        'NAME': "",
        'DESCRIPTION': "",
        'PATHS': {
        }},

    '#12': {
        'NAME': "",
        'DESCRIPTION': "",
        'PATHS': {
        }},

    '#91': {
        'NAME': "",
        'DESCRIPTION': "",
        'PATHS': {
        }},

    '#30': {
        'NAME': "",
        'DESCRIPTION': "",
        'PATHS': {
        }}
 }

directions = ["NORTH", "SOUTH", "EAST", "WEST", "UP", "DOWN"]
current_node = {}
while playing:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
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
