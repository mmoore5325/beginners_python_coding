import random

# draw a grid(4x4, 5x5)
# pick a random location for player
# pick a random location for exit door
# draw a player in grid
# take input for movement
# move player unless move is not valid
# check for win or loss
# clear screen and redraw grid on every move

def gridSize_def():
   global gridSize
   while True:
       try:
           gridSize = int(input("input grid length and width\n"))
           if gridSize<2:
               print ("Too Small")
           else:
               break
       except ValueError:
           print ("invalid input") 
   grids = [[] for _ in range (gridSize)]
   for i in range(0,gridSize):
       grids[i-1]=[0 for _ in range(gridSize)]
   return grids

def grid_def():
 x = []
 for i in range (0,gridSize):
   x.append(grids[i-1])      
 print(x)


CELLS = [(0,0), (1,0), (2,0), (3,0), (4,0),
         (0,1), (1,1), (2,1), (3,1), (4,1),
         (0,2), (1,2), (2,2), (3,2), (4,2),
         (0,3), (1,3), (2,3), (3,3), (4,3),
         (0,4), (1,4), (2,4), (3,4), (4,4)]

def get_locations():
  monster = None
  door = None
  player = None
  
  return(monster, door, player) #return tuple

def move(player, move):
  # get location
  # if move = left, x-1
  # if move = right, x + 1
  # if move = up, y - 1
  # if move = down, y + 1
  return player

def get_move(player):
  move = ["LEFT", "RIGHT", "UP", "DOWN"]
  # y == 0, can move up
  # y == 4, cant move down
  # x == 4, cant move right
  # x == 0, cant move left
  
while True:
  print("Welcome, you're current in room {}").format()  # FILL WITH PLAYER POSITION
  print("You can move {}") # FILL WITH AVAILABLE MOVES
  print("Enter QUIT to quit")
  
  move = input("< ")
  move = move.upper()
  
  if move == 'QUIT':
    break