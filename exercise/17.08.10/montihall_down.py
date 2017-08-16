import random

def populate_doors():  # put a car behind one door
    door = ['goat', 'goat', 'goat']
    door[random.randint(0, 2)] = 'car'
    return door

wins = 0
losses = 0
# playing the game 100,000 times:
for x in range(100000):
    doors = populate_doors()
    first_choice = random.randint(0, 2)  # choose a random door
    if doors[first_choice] == 'car':
        wins = wins + 1  # contestant switched to losing door
    else:
        losses = losses + 1  # contestant switched to winning door

print("바꾸지 않았을 때")
print("Wins:", wins)
print("Losses:", losses)

wins=0
losses=0
for x in range(100000):
    doors = populate_doors()
    select_choice=[0,1,2]
    first_choice = random.randint(0, 2)  # choose a random door
    del select_choice[first_choice]
    if doors[select_choice[0]]=='goat':
        del select_choice[0]
    else:
        del select_choice[1]
    if doors[select_choice[0]] == 'car':
        wins = wins + 1  # contestant switched to losing door
    else:
        losses = losses + 1  # contestant switched to winning door

print("바꿨을 때")
print("Wins:", wins)
print("Losses:", losses)
