### Print out everything on a single line unless its double pipes, then new line.

TILES = ('-', ' ', '-', ' ', '-', '||',
         '_', '|', '_', '|', '_', '|', '||',
         '&', ' ', '_', ' ', '||',
         ' ', ' ', ' ', '^', ' ', '||'
)
for tile in TILES:
    if tile != "||":
        print(tile, end="")
    else:
        print()