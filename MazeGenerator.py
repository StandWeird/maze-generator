import random

#Shows the grid
def showGrid(grid):
    for x in range(0, len(grid)):
        print(grid[x])

#Checks if all cells are empty
def emptycells(grid):
    emptycell = "false"
    for x in range(0, len(grid[0])):
        for m in range(0, len(grid)):
            if grid[x][m] == 0:
                emptycell = "true"
    return emptycell

#Checks if visited cell found has any connections
def connectionCheck(grid, x, y):
    check = "false"
    for emp in range(0, 3):
        if emp == 0:
            if y != 18:
                if grid[y+2][x] == 0:
                    check = "true"
        elif emp == 1:
            if y != 1:
                if grid[y-2][x] == 0:
                    check = "true"
        elif emp == 2:
            if x != 1:
                if grid[y][x-2] == 0:
                    check = "true"
        else:
            if x != 17:
                if grid[y][x+2] == 0:
                    check = "true"
    return check
        

#Creates a grid for the maze to work with.
def gridify(grid):
    smear = "true"
    for x in range(0, len(grid[0])):
        tempNumb = x
        while tempNumb > -2:
            tempNumb = tempNumb - 2
            if tempNumb == -1:
                tempNumb = -2
                smear = "false"
            elif tempNumb == -2:
                tempNumb = -2
                smear = "true"
            else:
                smear = "true"
        if smear == "true":
            for m in range(0, len(grid)):
                grid[x][m] = 1
    for x in range(0, len(grid)):
        tempNumb = x
        while tempNumb > -2:
            tempNumb = tempNumb - 2
            if tempNumb == -1:
                tempNumb = -2
                smear = "false"
            elif tempNumb == -2:
                tempNumb = -2
                smear = "true"
            else:
                smear = "true"
        if smear == "true":
            for m in range(0, len(grid[0])):
                grid[m][x] = 1
    showGrid(grid)
    for x in range(0, len(grid)):
        m = 0
    return grid

def huntandunalive(grid):
    foundUnvisitedCell = "false"
    count = 0
    cont = 0
    m, x = 0, 0
    while grid[x][m] != 0:
        for x in range(0, len(grid)-1):
            for m in range(0, len(grid)-1):
                #print("grid",grid[x][m])
                if grid[x][m] == 9:
                    if connectionCheck(grid, m, x) == "true":
                        currY = x
                        currX = m
                        foundUnvisitedCell = "true"
                        cont = 1
                        break
            if foundUnvisitedCell == "true":
                break
        if foundUnvisitedCell == "true":
            break
            if grid[x][m] == 0:
                currY = x
                currX = m
                break
    return currX, currY, cont
    
    
#Creates Connections Using HUNT AND KILL method
def generation(grid):
    currY = 1
    currX = 1
    cont = 1
    count = 0
    #1 stands for a maze wall
    #0 stands for an unvisited cell
    #6 stands for a broken wall
    #9 stands for a visited cell
    grid[currY][currX] = 9
    while cont == 1:
        x = currX
        y = currY
        r = random.randint(0,3)
        #print(r)
        #rand 0 = down
        #rand 1 = up
        #rand 2 = left
        #rand 3 = right
        if r == 0:
            if y != 17:
                if grid[y+2][x] == 0:
                    grid[y+2][x] = 9
                    grid[y+1][x] = 6
                    currY = y + 2
                    currX = x
        elif r == 1:
            if y != 1:
                if grid[y-2][x] == 0:
                    grid[y-2][x] = 9
                    grid[y-1][x] = 6
                    currY = y - 2
                    currX = x
        elif r == 2:
            if x != 1:
                if grid[y][x-2] == 0:
                    grid[y][x-2] = 9
                    grid[y][x-1] = 6
                    currY = y 
                    currX = x - 2
        else:
            if x != 17:
                if grid[y][x+2] == 0:
                    grid[y][x+2] = 9
                    grid[y][x+1] = 6
                    currY = y 
                    currX = x + 2
        count = count + 1
        if count == 10:
            print("Working")
            showGrid(grid)
            currX, currY, cont = huntandunalive(grid)
            count = 0
            #if all 0 cells are 9 (visited) stop the program and end it.
            
    print("escape")
    return grid
        
                
        
        
    

grid = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

grid = gridify(grid)
while emptycells(grid) == "true":
    grid = generation(grid)
    showGrid(grid)

#Bug, program cannot handle any random numbers if they exceed the array
#Bug, prints maze and ends in an error (not going to fix it)
