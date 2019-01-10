

def Genetic(condition , problem  ) :
    graph = condition[0]
    colorNum = condition[1]
    edges = graph[2]
    maxFit = 0
    generationSize = 50
    populationSize = 50
    mutationRate = 0.01
    tournomentSize = 2

    bestfitnessVal = []
    worstfitnessVal = []
    avgfitnessVal = []
    generation = problem.CreatePopulation(condition , populationSize) #creating first population 
    for i in range(generationSize) : #times for creating new generation
        fitnessVal = []
        parents = problem.selectParents(generation ,tournomentSize ,edges) #tournomentSize for size of groups for choosing parents
        rawGeneration = problem.regeneration(parents ,populationSize) # creating new generation
        generation = problem.generationMutation(rawGeneration , colorNum ,mutationRate) #the mutated generation
        
        for person in generation :
            val = problem.fitness(person , edges)
            fitnessVal.append(val)
            if val == 1 :
                
                return {"thecolors " : person , "value" : val , "generation" : i+1 , "bestG" :bestfitnessVal, "worstG": worstfitnessVal ,"avgG": avgfitnessVal}

        fitnessVal.sort()
        bestfitnessVal.append(fitnessVal[len(fitnessVal)-1])
        worstfitnessVal.append(fitnessVal[0])
        avg = sum(fitnessVal)/ len(fitnessVal)
        avgfitnessVal.append(avg)

    for el in generation :
        value = problem.fitness(el , edges)
        if maxFit < value :
            maxFit = value
            selected = el

    
    return {"thecolors " : selected , "value" : maxFit , "generation" : i+1, "bestG" :bestfitnessVal, "worstG": worstfitnessVal ,"avgG": avgfitnessVal}