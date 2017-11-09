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
