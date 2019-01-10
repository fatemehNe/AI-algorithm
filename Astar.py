import sys
import question1
import copy


def Astar(start, problem ):
    visisitedNode = 0
    expandedNode = 0
    memory = 0
    totalMemory = 0
    visited = []                # which nodes are visited
    queue = []                  # which is the next node to visit

    queue.append([start,problem.Heuristic(start) , 0])                  # enqueue start node
    visited.append(start)                # mark start node as visited
    while queue:                         # while queue is not empty
        cur = queue.pop(0)            # ...get current node
        current = cur[0]
        visisitedNode += 1        #number of nodes visited in A*
        if problem.IsGoalState(current) or problem.Heuristic(current) == 0:            # .........if target found stop
            totalMemory = len(visited) +memory #calculating the memory space used
            return {"path" : current[1] ,  "cost" : cur[1],"depth" : cur[2] ,"visisitedNode" : visisitedNode , "expandedNode" : expandedNode , "memoryUsed" :memory}
            sys.exit(0)

        expandedNode += 1        #numer of expanded nodes
        for child in problem.CreateStates(current):        # ...for each neighbor of current
            if not problem.MainAlredyHave(visited,child) :        # ......if neighbor not visited
                move = copy.deepcopy(current[1])
                for x in child[1]:
                    move.append(x)
                child[1] = move
                visited.append(child)       #     ...mark as visited
                cost = len(current[1]) + problem.Heuristic(child)
                queue.append([child, cost , cur[2]+1])         # .........add it to the queue
        for i in range(0, len(queue)):      #sort the queue from min cost to max cost
            j = i
            while j > 0 and queue[j-1][1] > queue[j][1]:
                queue[j-1] , queue[j] = queue[j] , queue[j-1]
                j -= 1
        if len(queue) > memory : #keeping the maximum memory space used
            memory = len(queue)

    
    totalMemory =  len(visited) +memory #calculating the memory space used
    return {"path not found" : 0 ,  "cost" : cur[1], "depth" : cur[2],"visisitedNode" : visisitedNode , "expandedNode" : expandedNode , "memoryUsed" :memory}
            


                
