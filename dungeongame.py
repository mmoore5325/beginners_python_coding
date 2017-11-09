import random

# draw a grid(4x4, 5x5)
# pick a random location for player
# pick a random location for exit door
# draw a player in grid
# take input for movement
# move player unless move is not valid
# check for win or loss
# clear screen and redraw grid on every move

#def gridSize_def():
#    global gridSize
#    while True:
#        try:
#            gridSize = int(input("input grid length and width\n"))
#            if gridSize<2:
#                print ("invalid int")
#            else:
#                break
#        except ValueError:
#            print ("invalid input") 
#    grids = [[] for _ in range (gridSize)]
#    for i in range(0,gridSize):
#        grids[i-1]=[0 for _ in range(gridSize)]
#    return grids
#
#def grid_def():
#  x = []
#  for i in range (0,gridSize):
#    x.append(grids[i-1])      
#  print(x)
##  print(x[2][1])
#grids = gridSize_def()
#grid_def()

CELLS = [(0,0), (1,0), (2,0), (3,0), (4,0),
         (0,1), (1,1), (2,1), (3,1), (4,1),
         (0,2), (1,2), (2,2), (3,2), (4,2),
         (0,3), (1,3), (2,3), (3,3), (4,3),
         (0,4), (1,4), (2,4), (3,4), (4,4)]
random_starting_spot = random.sample(CELLS, 1)
print(random_starting_spot)
print(random_starting_spot[0])
x = random_starting_spot
def get_locations():
  monster = random.sample(CELLS, 1)
  door = random.sample(CELLS, 1)
  player = random.sample(CELLS, 1)
  print("PLAYER = {}".format(player))
  print("DOOR = {}".format(door))
  print("MONSTER = {}".format(monster))
  return(player, monster, door) #return tuple

def move(player, move):
  # get location
  
  # if move = left, x-1
  # if move = right, x + 1
  # if move = up, y - 1
  # if move = down, y + 1
  return player

def get_move(player):
  move = ["LEFT", "RIGHT", "UP", "DOWN"]
  if player[0] == 0 and player[1] == 0:
    return(move[1:5:2])
  elif player[0] == 4 and player[1] == 4:
    return(move[0:4:2])
  elif player[0] == 4 and player[1] == 0:
    return(move[0:5:3])
  elif player[0] == 0 and player[1] == 4:
    return(move[1:3:1])
  elif player[0] == 0:
    return(["RIGHT", "UP", "DOWN"])
  elif player[0] == 4:
    return(["LEFT", "UP", "DOWN"])
  elif player[1] == 4:
    return(["LEFT", "RIGHT", "UP"])
  elif player[1] == 0:
    return(["DOWN", "LEFT", "RIGHT"])
  else:
    return(move[:])
#   y == 0, can move up
#   y == 4, cant move down
  # x == 4, cant move right
  # x == 0, cant move left
  
while True:
  player = get_locations()[0]
  monster = get_locations()[1]
  door = get_locations()[2]
  position = get_move(player[0])
  print("Welcome, you're current in room {}".format(player[0]))  # FILL WITH PLAYER POSITION
  print("You can move {}".format(position)) # FILL WITH AVAILABLE MOVES
  print("Enter QUIT to quit")
#  
  move = input("< ")
  move = move.upper()
  
  
  if move == 'QUIT':
    break
  
  

    # Good move?  Change player position
    # Bad move? Let player know and don't change anything
    # Check for win
    # Check for loss
    # Otherwise, continue game loop