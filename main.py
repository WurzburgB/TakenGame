#Wurzburg Brumaire

# Sample function showing the goal of the game and move commands
def show_instructions():
    # print a main menu and the commands
    print("Operation Taken Game")
    print("Collect 6 items to win the game, or you wife can't be saved.")
    print("Move commands: go South, go North, go East, go West")
    print("Add to Inventory: get 'item name'")
    print("-----------------------------------")


def show_state(inventory, rooms, state):
    print('Inventory: ', inventory)
    print('You see a ', rooms[state][0])
    print("--------------------------------")
    cmd, direction = input('Enter your move: ').split()  # cmd is go or get, ignoring it
    return direction


# A dictionary for the simplified Realm of the Undead Arena Game
# The dictionary links a room to other rooms.

rooms = {
    'Living Room': ['Blueprint', {'South': 'Utility Room'}],
    'Utility Room': ['Key', {'North': 'Living Room', 'East': 'Master Bedroom'}],
    'Master Bedroom': ['Gun', {'South': 'Living Room', 'West': 'Bathroom'}],
    'Bathroom': ['Bandage', {'West': 'Secured Room'}],
    'Secured Room': ['Wife']
}
# items = {
#    'Living Room': 'Blueprint',
#    'Utility Room': 'Key',
#    'Master Bedroom': 'Gun',
#    'Bathroom': 'Bandage',
#    'Secured Room': 'Wife'
# }

state = 'Living Room'
inventory = []


# function
def get_new_state(state, direction):
    new_state = state  # declaring
    for i in rooms:  # loop
        if i == state:  # if
            if direction in rooms[i][1]:  # if
                new_state = rooms[i][1][direction]  # assigning new_state

    return new_state  # return


show_instructions()
while 1:  # gameplay loop
    print('You are in the ', state)  # printing state
    if state == 'Secured Room':
        print('Free your wife!', end='')
        for i in range(50):
            for j in range(1000000):
                pass
            print(".", end='', flush=True)
        print()
        if len(inventory) == 4:
            print("Congratulations! You have collected all items and freed your wife!")
        else:
            print('You lost her...GAME OVER!')

        print("Thanks for playing the game. Hope you enjoyed it. ")
        break

    direction = show_state(inventory, rooms, state)
    # print ('Inventory: ', inventory)
    # print ('You see a ', items[state])
    # print ("--------------------------------")
    # cmd, direction = input('Enter your move: ').split()  # cmd is go or get, ignoring it
    if direction.lower() == rooms[state][0].lower():
        if rooms[state][0] not in inventory:
            inventory.append(rooms[state][0])
        continue
    direction = direction.capitalize()  # making first character capital remaining lower
    if direction == 'Exit':  # if
        exit(0)  # exit function
    if direction == 'East' or direction == 'West' or direction == 'North' or direction == 'South':  # if
        new_state = get_new_state(state, direction)  # calling function
        if new_state == state:  # if
            print('I think you should go another way!')  # print
        else:
            state = new_state  # changing state value to new_state
    else:
        print('Invalid direction!!')
