import copy
import random
from random import shuffle

class q5:
    
    def InitialState(self):
        return[ [[3,5,2,6,2,3,2,4,4],[1,1,5,5,5,2,3,1,3],[3,3,5,3,3,3,4,2,5],[6,5,1,1,1,6,6,5,6],[5,1,2,4,4,4,2,6,1],[1,2,4,2,6,4,4,6,6]],[]]        
    
    def CreateStates(self ,state) :
        children = []
        for surface in range(6):
            if surface == 0:
                #clockwise
                temp = copy.deepcopy(state)

                head = temp[surface][0]
                temp[surface][0] = temp[surface][6]
                temp[surface][6] = temp[surface][8]
                temp[surface][8] = temp[surface][2]
                temp[surface][2] = head
                
                head = temp[surface][1]
                temp[surface][1] = temp[surface][3]
                temp[surface][3] = temp[surface][7]
                temp[surface][7] = temp[surface][5]
                temp[surface][5] = head
                
                side = temp[1][0:3]
                temp[1][0:3] = temp[2][0:3]
                temp[2][0:3] = temp[3][0:3]
                row = temp[5][6:9]
                row.reverse()
                temp[3][0:3] = row
                side.reverse()
                temp[5][6:9] = side
                children.append([temp , ["surface1,90 degree clockwise"]])

                #unclockwise
                temp = copy.deepcopy(state)

                head = temp[surface][0]
                temp[surface][0] = temp[surface][2]
                temp[surface][2] = temp[surface][8]
                temp[surface][8] = temp[surface][6]
                temp[surface][6] = head
                
                head = temp[surface][1]
                temp[surface][1] = temp[surface][5]
                temp[surface][5] = temp[surface][7]
                temp[surface][7] = temp[surface][3]
                temp[surface][3] = head
                
                side = temp[1][0:3]
                row = temp[5][6:9]
                row.reverse()
                temp[1][0:3] = row
                row = temp[3][0:3]
                row.reverse()
                temp[5][6:9] = row
                temp[3][0:3] = temp[2][0:3]
                temp[2][0:3] = side
                children.append([temp , ["surface1,90 degree unclockwise"]])

            if surface == 1:
                # clockwise
                temp = copy.deepcopy(state)

                head = temp[surface][0]
                temp[surface][0] = temp[surface][6]
                temp[surface][6] = temp[surface][8]
                temp[surface][8] = temp[surface][2]
                temp[surface][2] = head
                
                head = temp[surface][1]
                temp[surface][1] = temp[surface][3]
                temp[surface][3] = temp[surface][7]
                temp[surface][7] = temp[surface][5]
                temp[surface][5] = head
                
                side = copy.deepcopy(temp[0])
                temp[0][0] = temp[5][0]
                temp[0][3] = temp[5][3]
                temp[0][6] = temp[5][6]

                temp[5][0] = temp[4][0]
                temp[5][3] = temp[4][3]
                temp[5][6] = temp[4][6]

                temp[4][0] = temp[2][0]
                temp[4][3] = temp[2][3]
                temp[4][6] = temp[2][6]

                temp[2][0] = side[0]
                temp[2][3] = side[3]
                temp[2][6] = side[6]
                children.append([temp , ["surface2,90 degree clockwise"]])

                # unclockwise
                temp = copy.deepcopy(state)

                head = temp[surface][0]
                temp[surface][0] = temp[surface][2]
                temp[surface][2] = temp[surface][8]
                temp[surface][8] = temp[surface][6]
                temp[surface][6] = head
                
                head = temp[surface][1]
                temp[surface][1] = temp[surface][5]
                temp[surface][5] = temp[surface][7]
                temp[surface][7] = temp[surface][3]
                temp[surface][3] = head
                
                side = copy.deepcopy(temp[0])
                temp[0][0] = temp[2][0]
                temp[0][3] = temp[2][3]
                temp[0][6] = temp[2][6]

                temp[2][0] = temp[4][0]
                temp[2][3] = temp[4][3]
                temp[2][6] = temp[4][6]

                temp[4][0] = temp[5][0]
                temp[4][3] = temp[5][3]
                temp[4][6] = temp[5][6]

                temp[5][0] = side[0]
                temp[5][3] = side[3]
                temp[5][6] = side[6]
                children.append([temp , ["surface2,90 degree unclockwise"]])

            if surface == 2:
                # clockwise
                temp = copy.deepcopy(state)

                head = temp[surface][0]
                temp[surface][0] = temp[surface][6]
                temp[surface][6] = temp[surface][8]
                temp[surface][8] = temp[surface][2]
                temp[surface][2] = head
                
                head = temp[surface][1]
                temp[surface][1] = temp[surface][3]
                temp[surface][3] = temp[surface][7]
                temp[surface][7] = temp[surface][5]
                temp[surface][5] = head
                
                side = copy.deepcopy(temp[0])
                temp[0][6] = temp[1][8]
                temp[0][7] = temp[1][5]
                temp[0][8] = temp[1][2]

                temp[1][2] = temp[4][0]
                temp[1][5] = temp[4][1]
                temp[1][8] = temp[4][2]

                temp[4][0] = temp[3][6]
                temp[4][1] = temp[3][3]
                temp[4][2] = temp[3][0]

                temp[3][0] = side[6]
                temp[3][3] = side[7]
                temp[3][6] = side[8]
                children.append([temp , ["surface3,90 degree clockwise"]])

                # unclockwise
                temp = copy.deepcopy(state)

                head = temp[surface][0]
                temp[surface][0] = temp[surface][2]
                temp[surface][2] = temp[surface][8]
                temp[surface][8] = temp[surface][6]
                temp[surface][6] = head
                
                head = temp[surface][1]
                temp[surface][1] = temp[surface][5]
                temp[surface][5] = temp[surface][7]
                temp[surface][7] = temp[surface][3]
                temp[surface][3] = head
                
                side = copy.deepcopy(temp[0])
                temp[0][6] = temp[3][0]
                temp[0][7] = temp[3][3]
                temp[0][8] = temp[3][6]

                temp[3][0] = temp[4][2]
                temp[3][3] = temp[4][1]
                temp[3][6] = temp[4][0]

                temp[4][0] = temp[1][2]
                temp[4][1] = temp[1][5]
                temp[4][2] = temp[1][8]

                temp[1][2] = side[8]
                temp[1][5] = side[7]
                temp[1][8] = side[6]
                children.append([temp , ["surface3,90 degree unclockwise"]])

            if surface == 3:
                # clockwise
                temp = copy.deepcopy(state)

                head = temp[surface][0]
                temp[surface][0] = temp[surface][6]
                temp[surface][6] = temp[surface][8]
                temp[surface][8] = temp[surface][2]
                temp[surface][2] = head
                
                head = temp[surface][1]
                temp[surface][1] = temp[surface][3]
                temp[surface][3] = temp[surface][7]
                temp[surface][7] = temp[surface][5]
                temp[surface][5] = head
                
                side = copy.deepcopy(temp[0])
                temp[0][8] = temp[2][8]
                temp[0][5] = temp[2][5]
                temp[0][2] = temp[2][2]

                temp[2][2] = temp[4][2]
                temp[2][5] = temp[4][5]
                temp[2][8] = temp[4][8]

                temp[4][2] = temp[5][2]
                temp[4][5] = temp[5][5]
                temp[4][8] = temp[5][8]

                temp[5][2] = side[2]
                temp[5][5] = side[5]
                temp[5][8] = side[8]
                children.append([temp ,[ "surface4,90 degree clockwise"]])

                # unclockwise
                temp = copy.deepcopy(state)

                head = temp[surface][0]
                temp[surface][0] = temp[surface][2]
                temp[surface][2] = temp[surface][8]
                temp[surface][8] = temp[surface][6]
                temp[surface][6] = head
                
                head = temp[surface][1]
                temp[surface][1] = temp[surface][5]
                temp[surface][5] = temp[surface][7]
                temp[surface][7] = temp[surface][3]
                temp[surface][3] = head
                

                side = copy.deepcopy(temp[0])
                temp[0][8] = temp[5][8]
                temp[0][5] = temp[5][5]
                temp[0][2] = temp[5][2]

                temp[5][2] = temp[4][2]
                temp[5][5] = temp[4][5]
                temp[5][8] = temp[4][8]

                temp[4][2] = temp[2][2]
                temp[4][5] = temp[2][5]
                temp[4][8] = temp[2][8]

                temp[2][2] = side[2]
                temp[2][5] = side[5]
                temp[2][8] = side[8]
                children.append([temp , ["surface4,90 degree unclockwise"]])

            if surface == 4:
                # clockwise
                temp = copy.deepcopy(state)

                head = temp[surface][0]
                temp[surface][0] = temp[surface][6]
                temp[surface][6] = temp[surface][8]
                temp[surface][8] = temp[surface][2]
                temp[surface][2] = head
                
                head = temp[surface][1]
                temp[surface][1] = temp[surface][3]
                temp[surface][3] = temp[surface][7]
                temp[surface][7] = temp[surface][5]
                temp[surface][5] = head
                
                side = copy.deepcopy(temp[2])
                temp[2][6] = temp[1][6]
                temp[2][7] = temp[1][7]
                temp[2][8] = temp[1][8]

                temp[1][6] = temp[5][2]
                temp[1][7] = temp[5][1]
                temp[1][8] = temp[5][0]

                temp[5][0] = temp[3][8]
                temp[5][1] = temp[3][7]
                temp[5][2] = temp[3][6]

                temp[3][6] = side[6]
                temp[3][7] = side[7]
                temp[3][8] = side[8]
                children.append([temp ,[ "surface5,90 degree clockwise"]])

                # unclockwise
                temp = copy.deepcopy(state)

                head = temp[surface][0]
                temp[surface][0] = temp[surface][2]
                temp[surface][2] = temp[surface][8]
                temp[surface][8] = temp[surface][6]
                temp[surface][6] = head
                
                head = temp[surface][1]
                temp[surface][1] = temp[surface][5]
                temp[surface][5] = temp[surface][7]
                temp[surface][7] = temp[surface][3]
                temp[surface][3] = head

                side = copy.deepcopy(temp[2])
                temp[2][6] = temp[3][6]
                temp[2][7] = temp[3][7]
                temp[2][8] = temp[3][8]

                temp[3][6] = temp[5][2]
                temp[3][7] = temp[5][1]
                temp[3][8] = temp[5][0]

                temp[5][0] = temp[1][8]
                temp[5][1] = temp[1][7]
                temp[5][2] = temp[1][6]

                temp[1][6] = side[6]
                temp[1][7] = side[7]
                temp[1][8] = side[8]
                children.append([temp ,[ "surface5,90 degree unclockwise"]])

            if surface == 5:
                # clockwise
                temp = copy.deepcopy(state)

                head = temp[surface][0]
                temp[surface][0] = temp[surface][6]
                temp[surface][6] = temp[surface][8]
                temp[surface][8] = temp[surface][2]
                temp[surface][2] = head
                
                head = temp[surface][1]
                temp[surface][1] = temp[surface][3]
                temp[surface][3] = temp[surface][7]
                temp[surface][7] = temp[surface][5]
                temp[surface][5] = head
                
                side = copy.deepcopy(temp[4])
                temp[4][6] = temp[1][0]
                temp[4][7] = temp[1][3]
                temp[4][8] = temp[1][6]

                temp[1][0] = temp[0][2]
                temp[1][3] = temp[0][1]
                temp[1][6] = temp[0][0]

                temp[0][0] = temp[3][2]
                temp[0][1] = temp[3][5]
                temp[0][2] = temp[3][8]

                temp[3][2] = side[8]
                temp[3][5] = side[7]
                temp[3][8] = side[6]
                children.append([temp , ["surface6,90 degree clockwise"]])

                # unclockwise
                temp = copy.deepcopy(state)

                head = temp[surface][0]
                temp[surface][0] = temp[surface][2]
                temp[surface][2] = temp[surface][8]
                temp[surface][8] = temp[surface][6]
                temp[surface][6] = head
                
                head = temp[surface][1]
                temp[surface][1] = temp[surface][5]
                temp[surface][5] = temp[surface][7]
                temp[surface][7] = temp[surface][3]
                temp[surface][3] = head
                
                side = copy.deepcopy(temp[4])
                temp[4][6] = temp[3][8]
                temp[4][7] = temp[3][5]
                temp[4][8] = temp[3][2]

                temp[3][8] = temp[0][2]
                temp[3][5] = temp[0][1]
                temp[3][2] = temp[0][0]

                temp[0][0] = temp[1][6]
                temp[0][1] = temp[1][3]
                temp[0][2] = temp[1][0]

                temp[1][0] = side[6]
                temp[1][3] = side[7]
                temp[1][6] = side[8]
                children.append([temp , ["surface6,90 degree unclockwise"]])

        return children
   

    def quality(self ,state) :
        value = 0
        wrongBlock = 0
        index = 0
        for surface in state:
            # print(state)
            index += 1
            for i in surface:
                if i != index:
                    wrongBlock += 1
        value = 6*9 - wrongBlock
        return value
       
    def AlredyHave(self, group , state) :
        for st in group :
            if st == state :
                return True


        