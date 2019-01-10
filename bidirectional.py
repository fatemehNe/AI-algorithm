import sys
import copy

def reverseAction(path):
    movement =[]
    while path :
        movement.append(path.pop())
    return movement

def bidirectional(start,goal ,problem):
    depth = 0

    visisitedNode1 = 0
    expandedNode1 = 0
    visisitedNode2 = 0
    expandedNode2 = 0
    memory1 = 0
    memory2= 0
    totalMemory = 0
    check = 0

    visited1 = []                # which nodes are visited
    queue1 = []                  # which is the next node to visit
    path1 = []

    visited2 = []                # which nodes are visited
    queue2 = []                  # which is the next node to visit
    path2 = []

    queue1.append([start , 0])                  # enqueue start node
    visited1.append(start)                # mark start node as visited

    queue2.append([goal , 0])                  # enqueue goal node
    visited2.append(goal)                # mark goal node as visited
    
    while queue1 or queue2:
        if queue1:                         # while queue is not empty
            current = queue1.pop(0)            # ...get current node
            path1.append(current[0])
            visisitedNode1 += 1        #number of nodes visited in Bidirectional
            if problem.IsGoalState(current[0]) : # if target found stop or intersection
                return {"move" : current[0][1] ,"depth" : current[1] , "visisitedNode" : visisitedNode1 + visisitedNode2 , "expandedNode" : expandedNode1 + expandedNode2 , "memoryUsed" :totalMemory}
                sys.exit(0)
            elif problem.MainAlredyHave(path2 , current[0]):
                check = 1
            expandedNode1 += 1        #numer of expanded nodes
            for child in problem.CreateStates(current[0]):        # ...for each neighbor of current[0]
                if not problem.MainAlredyHave(visited1,child) :        # ......if neighbor not visited
                    move = copy.deepcopy(current[0][1])
                    for x in child[1]:
                        move.append(x)
                    child[1] = move
                    visited1.append(child)       # .........mark as visited
                    queue1.append([child , current[1]+1])         # .........add it to the queue
            
        if len(queue1) > memory1 : #keeping the maximum memory space used
            memory1 = len(queue1)

        if queue2:                         # while queue is not empty
            current2 = queue2.pop(0)            # ...get current2 node
            path2.append(current2[0])
            visisitedNode2 += 1        #number of nodes visited in Bidirectional
            if problem.MainAlredyHave(path1,current2[0]):            # .........if target found stop
                check = 2
                
            expandedNode2 += 1        #numer of expanded nodes
            for child in problem.CreateStates(current2[0]):        # ...for each neighbor of current
                if not problem.MainAlredyHave(visited2,child) :        # ......if neighbor not visited
                    move2 = copy.deepcopy(current2[0][1])
                    for x in child[1]:
                        move2.append(x)
                    child[1] = move2
                    visited2.append(child)       # .........mark as visited 
                    queue2.append([child , current2[1]+1])         # .........add it to the queue
        
        if len(queue2) > memory2 : #keeping the maximum memory space used
            memory2 = len(queue2)
        
        if check == 1 or check ==2 :
            move = current[0][1]
            i  = problem.repeatedStateIndex(path2 , current[0])
            move.append(reverseAction(path2[i][1]))
            if check == 1 :
                depth = current[1]
            if check == 2 :
                depth = current2[1]
            totalMemory = memory1 + memory2 + len(path1) + len(path2) + len(visited1) + len(visited2)
            return {"move" : move ,"depth" : depth , "visisitedNode" : visisitedNode1 + visisitedNode2 , "expandedNode" : expandedNode1 + expandedNode2 , "memoryUsed" :totalMemory}
               
            sys.exit(0)
    return "no answer found"

                
