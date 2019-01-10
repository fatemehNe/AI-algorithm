import sys
import copy

class DFS:

    def DFS(self , start, problem ):
        visisitedNode = 0
        expandedNode = 0
        memory = 0
        stackMemory = 0
        stack = [[start , 0]] #start
        visited = []  # which nodes are visited
        path = [] #empty

        visited.append(start)                # mark start node as visited
        while stack:   #stack is not empty
            vertex = stack.pop()   #get first node to vertex 
            if problem.MainAlredyHave(path,vertex[0]) :   #node already in path
                continue #skip
            path.append(vertex[0])   #start adding node to path
            expandedNode += 1     #numer of expanded nodes
            for child in problem.CreateStates(vertex[0]):   #start exploring other node
                if not problem.MainAlredyHave(visited,child) :
                    move = copy.deepcopy(vertex[0][1])
                    for x in child[1]:
                        move.append(x)
                    child[1] = move
                    visited.append(child)  # mark node as visited
                    stack.append([child , vertex[1]+1])    #add neighbor node to stack
                if len(stack) > stackMemory : #keeping the maximum memory space used
                    stackMemory = len(stack)
                if problem.IsGoalState(child):
                    path.append(child)        # .........if target found stop
                    
                    visisitedNode = len(path)  #number of nodes visited in dfs
                    memory = len(path) + len(visited) +stackMemory #calculating the memory space used

                    return {"path" : child[1] ,"depth":vertex[1]+1 , "visisitedNode" : visisitedNode , "expandedNode" : expandedNode , "memoryUsed" :memory}
                    sys.exit(0)

        memory = len(path) + len(visited) +stackMemory
        visisitedNode = len(path)  #number of nodes visited in dfs            
        return {"no answer found" : 0 ,"depth":vertex[1] , "visisitedNode" : visisitedNode , "expandedNode" : expandedNode , "memoryUsed" :memory}
  
    def LDFS(self ,start, problem ,limit ):
        visisitedNode = 0
        expandedNode = 0
        memory = 0
        stackMemory = 0

        stack =[ [start,0] ]#start
        visited = []  # which nodes are visited
        path = [] #empty
        visited.append(start)                # mark start node as visited
        while stack:   #stack is not empty
            vertex = stack.pop()   #get first node to vertex 
            if problem.MainAlredyHave(path,vertex[0]) :   #node already in path
                continue #skip
            path.append(vertex[0])    #start adding node to path
            if vertex[1] < limit :
                expandedNode += 1         #numer of expanded nodes
                for child in problem.CreateStates(vertex[0]): #start exploring other node
                    if not problem.MainAlredyHave(visited,child) :
                        move = copy.deepcopy(vertex[0][1])
                        move.append(child[1])
                        child[1] = move
                        visited.append(child)  # mark node as visited
                        stack.append([child,vertex[1] +1])  #add neighbor node to stack and increment depth by 1
                    if len(stack) > stackMemory : #keeping the maximum memory space used
                        stackMemory = len(stack)
                    if problem.IsGoalState(child):
                        path.append(child)        # .........if target found stop

                        visisitedNode = len(path)  #number of nodes visited in ldfs
                        memory = len(path) + len(visited) +stackMemory #calculating the memory space used

                        return {"path" : child[1] ,"depth": vertex[1] +1 , "visisitedNode" : visisitedNode , "expandedNode" : expandedNode , "memoryUsed" :memory}
                        sys.exit(0)

        memory = len(path) + len(visited) +stackMemory
        visisitedNode = len(path)  #number of nodes visited in dfs            
        return {"depth is not enough for finding an answer" : 0  ,"depth": limit , "visisitedNode" : visisitedNode , "expandedNode" : expandedNode , "memoryUsed" :memory}


    def IterativeDeepening(self, start, problem):
        visisitedNode = 0
        expandedNode = 0
        stackMemory = 0
        visitedMemory = 0
        pathMemory =0
        totalMemory = 0
        stack =[ [start,0] ]                                #start
        visited = []                                        # which nodes are visited
        path = []                                           #empty
        visited.append(start)                               # mark start node as visited
        limit = 1
        while limit>0 :
            stack =[ [start,0] ]                            #start
            visited = []                                    # which nodes are visited
            path = []                                       #empty
            visited.append(start)                           # mark start node as visited
            while stack:                                    #stack is not empty
                vertex = stack.pop()                        #get first node to vertex 
                visisitedNode += 1
                if problem.MainAlredyHave(path,vertex[0]) :   #node already in path
                    continue                                #skip
                path.append(vertex[0])                      #start adding node to path
                if vertex[1] < limit :
                    expandedNode += 1
                    for child in problem.CreateStates(vertex[0]): #start exploring other node
                        if not problem.MainAlredyHave(visited,child) :
                            move = copy.deepcopy(vertex[0][1])
                            move.append(child[1])
                            child[1] = move
                            visited.append(child)           # mark node as visited
                            stack.append([child,vertex[1] +1]) #add neighbor node to stack and add increment depth by 1
                        if len(stack) > stackMemory : #keeping the maximum memory space used
                            stackMemory = len(stack)
                        if len(path) > pathMemory : #keeping the maximum memory space used
                            pathMemory = len(path)
                        if len(visited) > visitedMemory : #keeping the maximum memory space used
                            visitedMemory = len(visited)
                        visisitedNode += 1
                        if problem.IsGoalState(child):
                            path.append(child)              # .........if target found stop
                            totalMemory = visitedMemory + pathMemory + stackMemory
                            return {"path" : child[1] , "depth" :vertex[1]+1  , "visisitedNode" : visisitedNode , "expandedNode" : expandedNode , "memoryUsed" :totalMemory}
                            sys.exit(0)
            limit += 1     #increment limit for deeper iteration

        totalMemory = visitedMemory + pathMemory + stackMemory
        return {"no answer found" : 0 ,"depth": vertex[1] , "visisitedNode" : visisitedNode , "expandedNode" : expandedNode , "memoryUsed" :totalMemory}
                            