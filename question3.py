import random
import numpy as np
import copy

class q3:

    def randomLoc(self) :
        i = random.randint(0,7)
        j = random.randint(0,7)

        if (i == 6 and j == 0) or (i == 7 and j == 4) or (i == 2 and j == 1) or (i == 3 and j == 5) or (i == 4 and j == 3) or (i == 5 and j == 4) :
            return self.randomLoc()
        else :
            return [i,j]

    def InitialState(self):
        start = np.zeros((8,8) , np.int8)
        start[6][0] = 2
        start[7][4] = 2
        start[2][1] = -1
        start[3][5] = -1
        start[4][3] = -1
        start[5][4] = -1

        loc = self.randomLoc()
        start[loc[0]][loc[1]] = 1
        state =  [start ,[[loc[0],loc[1]]]]
        return state

    def CreateStates(self ,state) :
        children =[]
        i , j = np.where(state[0] == 1)
        curX = i[0]
        curY = j[0]
        for i in range(8):
            x = curX
            y = curY
            temp =copy.deepcopy(state[0])
            if i == 0 :
                x = x + 1
                y = y + 2
                if x in range(8) and y in range(8) and temp[x][y] != -1:
                    temp[x][y] = 1
                    temp[curX][curY] = 0
                    children.append([temp , [x,y]])
            elif i == 1 :
                x = x + 1
                y = y - 2
                if x in range(8) and y in range(8) and temp[x][y] != -1:
                    temp[x][y] = 1
                    temp[curX][curY] = 0
                    children.append([temp , [x,y]])
            elif i == 2 :
                x = x - 1
                y = y + 2
                if x in range(8) and y in range(8) and temp[x][y] != -1:
                    temp[x][y] = 1
                    temp[curX][curY] = 0
                    children.append([temp , [x,y]])
            elif i == 3 :
                x = x - 1
                y = y - 2
                if x in range(8) and y in range(8) and temp[x][y] != -1:
                    temp[x][y] = 1
                    temp[curX][curY] = 0
                    children.append([temp , [x,y]])
            elif i == 4 :
                x = x + 2
                y = y + 1
                if x in range(8) and y in range(8) and temp[x][y] != -1:
                    temp[x][y] = 1
                    temp[curX][curY] = 0
                    children.append([temp , [x,y]])
            elif i == 5 :
                x = x + 2
                y = y - 1
                if x in range(8) and y in range(8) and temp[x][y] != -1:
                    temp[x][y] = 1
                    temp[curX][curY] = 0
                    children.append([temp , [x,y]])
            elif i == 6 :
                x = x - 2
                y = y + 1
                if x in range(8) and y in range(8) and temp[x][y] != -1:
                    temp[x][y] = 1
                    temp[curX][curY] = 0
                    children.append([temp , [x,y]])
            elif i == 7 :
                x = x - 2
                y = y - 1
                if x in range(8) and y in range(8) and temp[x][y] != -1:
                    temp[x][y] = 1
                    temp[curX][curY] = 0
                    children.append([temp , [x,y]])
        return children




    def IsGoalState(self ,state) :
        i , j = np.where(state[0] == 1)
        if ( i == 6 and j == 0 ) or ( i == 7 and j == 4 ) :
            return True
        else :
            return False
        

    def MainAlredyHave(self, group , state) :
        for st in group :
            if np.array_equal(st[0] , state[0]) :
                return True
        
    
    # def Heuristic(self , child) :
        
    