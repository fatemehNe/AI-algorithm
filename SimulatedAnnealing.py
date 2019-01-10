import random
import math
import copy

def probability(oldCost, newCost, Temprature) :
        p = math.exp((newCost-oldCost)/Temprature)
        return p

def SA(state , problem):
    maxMemory = 0
    expanded = 0
    visited = 0
    T0 = 1.7  #initial temperature
    k = 1   #step of cooling temperature
    beta = 100
    temprature = 2 
    alpha = 0.87    
    current = state
    oldCost = problem.quality(state[0])
    newState = True
    while temprature > 0.00001 :
        queue = []
        for i in range (50) :
            if newState :
                expanded +=1 #counting number of expanded nodes
                for ch in problem.CreateStates(current[0]) : #adding neighbors of the current state to th queue
                    move = copy.deepcopy(current[1])
                    for x in ch[1]:
                        move.append(x)
                    ch[1] = move
                    queue.append(ch)
                newState = False

            if len(queue) > maxMemory : #keeping the maximum memory space used
                maxMemory = len(queue)
                
            index =  random.randint(0 , len(queue)) #choosing one of the neighbors randomly
            if index == len(queue) : 
                index -= 1
            temp = queue.pop(index)
            newCost = problem.quality(temp[0])
            visited += 1     #counting number of visited nodes
            if newCost > oldCost :   
                current = temp
                oldCost = newCost
                newState = True
                queue = []
            elif probability(oldCost , newCost, temprature) > random.random() :
                current = temp
                oldCost = newCost
                newState = True
                queue = []
            elif len(queue) == 0 :
                current = temp
                oldCost = newCost
                newState = True
                queue = []
            
        newState = True
            #exponential cooling 
        temprature = alpha*temprature
            #linear cooling 
        # temprature -= 0.1
            #logarithmic cooling
        # temprature = T0/(1 + beta*math.log10(1+k))
        # k += 1
    return {"currentState" : current[0] ,"movements": current[1] , "stateQuality" : oldCost ,"visitedNodes" : visited , "expandedNodes" : expanded ,"memoryUsed" :maxMemory }



