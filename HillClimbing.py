import random

class hillClimbing:

    def simple(self , state , problem ) :
        maxMemory =0 
        expanded = 0
        visited = 0
        baseValue = problem.evaluation(state)
        current = state
        while True :
            queue = []
            expanded += 1
            for child in problem.CreateStates(current) :  
                value = problem.evaluation(child)
                queue.append([child,value])
                visited += 1
            if len(queue) > maxMemory : #keeping the maximum memory space used
                maxMemory = len(queue)
            for i in range(0, len(queue)):      #sort the queue from min cost to max cost
                j = i
                while j > 0 and queue[j-1][1] > queue[j][1]:
                    queue[j-1] , queue[j] = queue[j] , queue[j-1]
                    j -= 1

            if queue[0][1] < baseValue :
                current = queue[0][0]
                baseValue = queue[0][1]
            else :
                return { "currentState" : current ,"value" : baseValue ,"visitedNodes" : visited , "expandedNodes" : expanded , "memoryUsed" :maxMemory }

    def firstChoice(self , state , problem):
        maxMemory =0 
        expanded = 0
        visited = 0
        baseValue = problem.evaluation(state)
        current = state
        while True :
            queue = []
            expanded += 1
            for child in problem.CreateStatesRandom(current) : 
                value = problem.evaluation(child)
                queue.append([child,value])
            if len(queue) > maxMemory : #keeping the maximum memory space used
                maxMemory = len(queue)
            cnt=0
            for i in range(len(queue)):      
                visited += 1 #visited is number of nodes compared to current
                if queue[i][1] < baseValue :
                    current = queue[i][0]
                    baseValue = queue[i][1]
                    break
                else :
                    cnt += 1
            if cnt == len(queue) : #if no new better state was found eturn the last good one
                return { "currentState" : current ,"value" : baseValue ,"visitedNodes" : visited , "expandedNodes" : expanded , "memoryUsed" :maxMemory }


    def randomRestart(self , state , problem): 
        maxMemory =0 
        expanded = 0
        visited = 0
        queue = []
        value = problem.evaluation(state)
        queue.append([state , value])
        expanded += 1
        for child in problem.CreateStatesRandom(state) : 
            value = problem.evaluation(child)
            queue.append([child,value])
        results = []
        maxMemory = len(queue)
        while queue :
            current = queue.pop()[0]
            visited += 1
            results.append(self.simple(current,problem))

        for i in range(0, len(results)):      #sort the results from min cost to max cost
            j = i
            while j > 0 and results[j-1]["value"] > results[j]["value"]:
                results[j-1] , results[j] = results[j] , results[j-1]
                j -= 1
        maxMemory += len(results)
        result = results[0]
        result["visitedNodes"] += visited
        result["expandedNodes"] += expanded
        result["memoryUsed"] += maxMemory
        return result

    def stochastic(self , state , problem):
        maxMemory =0 
        expanded = 0
        visited = 0
        baseValue = problem.evaluation(state)
        current = state
        check = True
        while check :
            queue = []
            expanded += 1
            for child in problem.CreateStates(current) :
                value = problem.evaluation(child)
                if value < baseValue :
                    visited += 1 #number of nodes which their value compared with the basevalue
                    queue.append([child,value])
                    check = True
                else :
                    check = False
            if len(queue) > maxMemory : #keeping the maximum memory space used
                maxMemory = len(queue)
            if len(queue) > 0 :
                index = random.randint(0 ,len(queue))
                if index == len(queue):
                    index -= index
                
                current = queue[index][0]
                baseValue = queue[index][1]

        return { "currentState" : current ,"value" : baseValue ,"visitedNodes" : visited , "expandedNodes" : expanded , "memoryUsed" :maxMemory }


    
