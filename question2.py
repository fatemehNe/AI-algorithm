import random
import numpy as np
import copy

class q2:

    def InitialState(self):
        array =[]
        initial = [1,2,3,4,5,6,7,8,0]
        for i in range(3):
            row =[]
            while len(row) < 3 :
                r = random.randint(0,9)
                if r in initial :
                    row.append(str(r))
                    initial.remove(r)
            array.append(row)
        start = [np.array(array, np.str) ,[]]
        return start
        # return [np.array([["4","1","3"],["7","2","5"],["0","8","6"]]) ,[]]

    def CreateStates(self ,state) :
        children =[]
        i , j = np.where(state[0] =="0")
        curX = i[0]
        curY = j[0]
        for i in range(4):
            x = curX
            y = curY
            temp =copy.deepcopy(state[0])
            if i < 2 :
                x = x +(-1)**(i % 2)
                if x in range(3) :
                    temp[curX][curY] , temp[x][y] =  temp[x][y] , temp[curX][curY] 
                    if (i % 2) == 1 :
                        children.append([temp,"U"])
                    else :
                         children.append([temp,"D"])
            else :
                y = y +(-1)**(i % 2)
                if y in range(3) :
                    temp[curX][curY] , temp[x][y] =  temp[x][y] , temp[curX][curY] 
                    if (i % 2) == 1 :
                        children.append([temp,"L"])
                    else :
                         children.append([temp,"R"])
        return children

    def IsSolveble(self,state):
        check =[]
        inversion = 0
        for x in state[0] :
            for m in x :
                check.append(int( m))
        for i in check :
            if i != 0:
                for j in check :
                    if i < j and check.index(i) > check.index(j) and j != 0 :
                        inversion = inversion + 1
        if inversion % 2 == 0 :
            return True
        else :
            return False

    def IsGoalState(self ,state) :
        goal = np.array([["1","2","3",],["4","5","6"],["7","8","0"]])
        if np.array_equal(goal , state[0]) :
            return True
        else :
            return False

    def MainAlredyHave(self, group , state) :
        for st in group :
            if np.array_equal(st[0] , state[0]) :
                return True
    
    def Heuristic(self , child) :
        distance = 0
        matrix = child[0]
        for i in range(3):
            for j in range(3):
                if matrix[i][j] == "1" :
                    distance = distance + i + j
                elif matrix[i][j] == "2":
                    distance = distance + i + abs(j-1)
                elif matrix[i][j] == "3":
                    distance = distance + i + abs(j-2)
                elif matrix[i][j] == "4":
                    distance = distance + abs(i-1) + j
                elif matrix[i][j] == "5":
                    distance = distance + abs(i-1) + abs(j-1)
                elif matrix[i][j] == "6":
                    distance = distance + abs(i-1) + abs(j-2)
                elif matrix[i][j] == "7":
                    distance = distance + abs(i-2) + j
                elif matrix[i][j] == "8":
                    distance = distance + abs(i-2) + abs(j-1)
                elif matrix[i][j] == "0":
                    distance = distance + abs(i-2) + abs(j-2)
        return distance
