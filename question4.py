import copy
import random
from random import shuffle

class q4:
    
    def InitialState(self, K):
        queue = []
        for i in range(3*K):
            r = random.randint(0,9)
            queue.append(r)
        return queue
    
    def CreateStates(self ,state) :
        children = []
        for i in range(len(state)) :
            j = i +3 
            if j < len(state) :
                for x in range(j , len(state)):
                    temp = copy.deepcopy(state)
                    temp[i] , temp[x] = temp[x] , temp[i]
                    children.append(temp)
        
        return children

    def CreateStatesRandom(self , state):
        children = []
        for i in range(10) :
            temp =copy.deepcopy(state)
            shuffle(temp)
            if not self.AlredyHave(children,state):
                children.append(temp)
        return children

    def evaluation(self ,state) :
        array = []
        sum = 0
        cnt = 0
        for i in range(len(state)):
            sum += state[i]
            cnt+=1
            if cnt == 3 :
                array.append(sum)
                sum = 0
                cnt = 0
        maximum = array[0]
        for i in range(0, len(array)):      #sort the array from min cost to max cost
            if maximum < array[i] :
                maximum = array[i]
        return maximum
    
    def AlredyHave(self, group , state) :
        for st in group :
            if st == state :
                return True


        