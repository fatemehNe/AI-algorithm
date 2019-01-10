import sys
import copy


def BFS(start, problem ):
    visisitedNode = 0
    expandedNode = 0
    memory = 0
    totalMemory = 0
    visited = []                # which nodes are visited
    queue = []                  # which is the next node to visit
    path = []

    queue.append([start , 0])                  # enqueue start node
    visited.append(start)                # mark start node as visited
    while queue:                         # while queue is not empty
        current = queue.pop(0)            # ...get current node
        visisitedNode += 1        #number of nodes visited in bfs
        if problem.IsGoalState(current[0]):            # .........if target found stop
            totalMemory =  len(visited) +memory #calculating the memory space used
            return {"path" : current[0][1] ,"depth" : current[1] , "visisitedNode" : visisitedNode , "expandedNode" : expandedNode , "memoryUsed" :memory}
            sys.exit(0)
        expandedNode += 1        #numer of expanded nodes
        for child in problem.CreateStates(current[0]):        # ...for each neighbor of current[0]
            if not problem.MainAlredyHave(visited,child) :        # ......if neighbor not visited
                move = copy.deepcopy(current[0][1])
                for x in child[1]:
                    move.append(x)
                child[1] = move
                visited.append(child)       #     ...mark as visited
                queue.append([child , current[1]+1])         # .........add it to the queue
        if len(queue) > memory : #keeping the maximum memory space used
            memory = len(queue)
    totalMemory = len(visited) +memory #calculating the memory space used
    return {"no answer found" : 0 , "depth" : current[1] ,  "visisitedNode" : visisitedNode , "expandedNode" : expandedNode , "memoryUsed" :memory}
               


                
