import random
import ast
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

CELLS = [[0,0], [1,0], [2,0], [3,0], [4,0],
         [0,1], [1,1], [2,1], [3,1], [4,1],
         [0,2], [1,2], [2,2], [3,2], [4,2],
         [0,3], [1,3], [2,3], [3,3], [4,3],
         [0,4], [1,4], [2,4], [3,4], [4,4]]
### FINISHED AND FUNCTIONING - JUST FOR GAME OPENING - USED ONCE
def get_locations():
  monster = random.sample(CELLS, 1)
  door = random.sample(CELLS, 1)
  player = random.sample(CELLS, 1)
#  print("PLAYER = {}".format(player))
#  print("DOOR = {}".format(door))
#  print("MONSTER = {}".format(monster))
  return(player, monster, door) #return tuple

monster = get_locations()[1]
monster = monster[0]
print(monster)
door = get_locations()[2]
door = door[0]
print(door)
### FINISHED AND FUNCTIONING - JUST FOR GAME OPENING - USED ONCE
def get_locations():
  player = random.sample(CELLS, 1)
#  print("PLAYER = {}".format(player))
#  print("DOOR = {}".format(door))
#  print("MONSTER = {}".format(monster))
  return(player, monster, door) #return tuple

def move(player, moves):
  if len(player) == 1:
    player = player[0]
    
#  print("PLAYER IS {}".format(player))
#  print(type(player))
  if moves == 'QUIT':
    exit()
  elif moves == 'LEFT':
    player[0] -= 1
  elif moves == 'RIGHT':
    player[0] += 1
  elif moves == 'UP':
    player[1] -= 1
  elif moves == "DOWN":
    player[1] += 1
  else:
    "You can't make that move"
    game_loop(player)
  
  if player[0] < 0:
    print("You can't make that move.")
    player[0] += 1
  elif player[0] > 4:
    print("You can't make that move.")
    player[0] -= 1
  elif player[1] < 0:
    print("You can't make that move.")
    player[1] += 1
  elif player[1] > 4:
    print("You can't make that move.")
    player[1] -= 1
  
  game_loop(player)
#   if move = left, x-1
#   if move = right, x + 1
#   if move = up, y - 1
#   if move = down, y + 1
#

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
  
  ### FINISHED AND FUNCTIONING - USED FOR FIRST MOVE
def introduction():
  player = get_locations()[0]
  position = get_move(player[0])
  print("Welcome, you're current in room {}".format(player[0]))  # FILL WITH PLAYER POSITION
  print("You can move {}".format(position)) # FILL WITH AVAILABLE MOVES
  print("Enter QUIT to quit")
  
  moves = input("< ")
  moves = moves.upper()
  print(move)
  move(player, moves)
  
def game_loop(player):
#  print("THIS IS PLAYER IN GAME LOOP {}".format(player))
  position = get_move(player)
  if player == door:
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@ yay @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    exit()
  elif player == monster:
    print("CHOMP CHOMP CHOMP CHOMP CHOMP CHOMP CHOMP CHOMP CHOMP CHOMP CHOMP CHOMP ")
    print("CHOMP CHOMP CHOMP CHOMP CHOMP CHOMP CHOMP CHOMP CHOMP CHOMP CHOMP CHOMP ")
    print("CHOMP CHOMP CHOMP CHOMP CHOMP CHOMP CHOMP CHOMP CHOMP CHOMP CHOMP CHOMP ")
    print("CHOMP CHOMP CHOMP CHOMP CHOMP CHOMP CHOMP CHOMP CHOMP CHOMP CHOMP CHOMP ")
    print("CHOMP CHOMP CHOMP CHOMP CHOMP CHOMP CHOMP CHOMP CHOMP CHOMP CHOMP CHOMP ")
    print("CHOMP CHOMP CHOMP CHOMP CHOMP CHOMP CHOMP CHOMP CHOMP CHOMP CHOMP CHOMP ")
    print("CHOMP CHOMP CHOMP CHOMP CHOMP CHOMP CHOMP CHOMP CHOMP CHOMP CHOMP CHOMP ")
    print("...you die.")
    exit()
  else:
    print("You can move {}".format(position))
    print("Enter QUIT to quit")
    
  moves = input("< ")
  moves = moves.upper()
  move(player, moves)
    # Good move?  Change player position
    # Bad move? Let player know and don't change anything
    # Check for win
    # Check for loss
    # Otherwise, continue game loop
introduction()