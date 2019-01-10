import copy

class q1:
    
    def InitialState(self):
        return [[["a1","a2","b1","b2","c1","c2","d1","d2"] , [] , False], []]    
    
    def GoalState(self):
        return [[[] ,["a1","a2","b1","b2","c1","c2","d1","d2"] , True] , []]
    
    def CreateStates(self ,movement) :
        children = []
        
        if movement[0][2] :
            for person in movement[0][1] :
                move = []
                state = []
                temp =copy.deepcopy(movement[0])
                temp[0].append(person)
                temp[2] = False
                temp[1].remove(person)

                move.append(person)
                move.append("L")

                state.append(temp)
                state.append(move)
                children.append(state)
                for person2 in temp[1] :
                    state2 = copy.deepcopy(state)
                    temp2 = state2[0]
                    move2 = state2[1]
                    if person2[0] == person[0] and person2[1] != person[1] :
                        temp2[0].append(person2)
                        temp2[1].remove(person2)
                        if not self.alredyHave(children, temp2):
                            move2.remove("L")
                            move2.append(person2)
                            move2.append("L")
                            children.append(state2)
                    elif person2[0] != person[0] and person2[1] == person[1] :
                        temp2[0].append(person2)
                        temp2[1].remove(person2)
                        if not self.alredyHave(children, temp2):
                            move2.remove("L")
                            move2.append(person2)
                            move2.append("L")
                            children.append(state2)
        else :
            for person in movement[0][0] :
                move = []
                state = []
                temp =copy.deepcopy(movement[0])
                temp[1].append(person)
                temp[2] = True
                temp[0].remove(person)

                move.append(person)
                move.append("R")

                state.append(temp)
                state.append(move)
                children.append(state)
                for person2 in temp[0] :
                    state2 = copy.deepcopy(state)
                    temp2 = state2[0]
                    move2 = state2[1]
                    if person2[0] == person[0] and person2[1] != person[1] :
                        temp2[1].append(person2)
                        temp2[0].remove(person2)
                        if not self.alredyHave(children, temp2):
                            move2.remove("R")
                            move2.append(person2)
                            move2.append("R")
                            children.append(state2)
                    elif person2[0] != person[0] and person2[1] == person[1] :
                        temp2[1].append(person2)
                        temp2[0].remove(person2)
                        if not self.alredyHave(children, temp2):
                            move2.remove("R")
                            move2.append(person2)
                            move2.append("R")
                            children.append(state2)
        return children

    def IsGoalState(self ,state) :
        cnt = 0
        for person in state[0][1] :
            if person == "a1":
                cnt += 1
            if person == "a2":
                cnt += 1
            if person == "b1":
                cnt += 1
            if person == "b2":
                cnt += 1
            if person == "c1":
                cnt += 1
            if person == "c2":
                cnt += 1
            if person == "d1":
                cnt += 1
            if person == "d2":
                cnt += 1
        if cnt == 8 :
            return True
        else :
            return False   

    def alredyHave(self ,group , state) :
        for x in range (0 ,len(group)-1) :
            cnt = 0
            for person in group[x][0][1] :
                if person in state[1] :
                    cnt += 1
            if cnt == len(state[1]) :
                return True

    def MainAlredyHave(self, group , state) :
        for x in range (0 ,len(group)-1) :
            cnt = 0
            for person in group[x][0][1] :
                if person in state[0][1] :
                    cnt += 1
            if cnt == len(state[0][1]) and len(state[0][1]) == len(group[x][0][1]) and group[x][0][2] == state[0][2] :
                return True
        return False

    def repeatedStateIndex(self, group , state) :
        for x in range (0 ,len(group)-1) :
            cnt = 0
            for person in group[x][0][1] :
                if person in state[0][1] :
                    cnt += 1
            if cnt == len(state[0][1]) and len(state[0][1]) == len(group[x][0][1]) and group[x][0][2] == state[0][2] :
                return x
        return 10000