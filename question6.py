import copy
import random
from random import shuffle

class q6:
    
    def InitialState(self):
        graph = []
        edges = [[0,2], [0, 15], [1, 2], [1, 4], [3, 2], [3,14],[3,13], [3,15], [4,5] ,[4,12], [5,12],[5,6],[6,11],[6,7],[7,8],[8,11],[8,9],[8,10],[10,11],[10,12],[10,15],[13,12],[11,12]]
        graph = [16 , 23 , edges] # num of vertexes , num of edges , edges
        return [graph , 4] #graph , number of colors
    
    def colorTheGraph(self , colorNumber , vertexNumber) :
        coloredGraph = []
        for i in range(vertexNumber) :
            coloredGraph.append(random.randint(1,colorNumber))
        return coloredGraph

    def CreatePopulation(self ,condition , populationSize) :
        population = []
        graph = condition[0]
        colorNumbers = condition[1]
        for i in range(populationSize) :
            population.append(self.colorTheGraph(colorNumbers , graph[0]))
        return population

    def createChild(self ,individual1 ,individual2) :
        child = []
        for i in range(len(individual1)):
            if (int(100 * random.random()) < 50):
                child.append(individual1[i])
            else:
                child.append(individual2[i])
        return child

    def selectParents(self , generation , tournomentSize , edges):
        selected = []
        selectedIndividuals = []
        while generation :
            group = []
            for i in range(tournomentSize): 
                if generation :
                    sample = random.choice(generation)
                    generation.remove(sample)
                    group.append(sample)
            maxFit = 0
            for el in group :
                value = self.fitness(el , edges)
                if maxFit < value :
                    maxFit = value
                    selected = el
            selectedIndividuals.append(selected)
        random.shuffle(selectedIndividuals)
        return selectedIndividuals

    def regeneration(self , selectedIndividuals , generationSize): #maybe change it 
        newGeneration = []
        for i in range(generationSize) :
            individual1 =random.choice(selectedIndividuals)
            individual2 =random.choice(selectedIndividuals)
            child = self.createChild(individual1, individual2)
            newGeneration.append(child)
        return newGeneration

    def fitness(self ,individual , edges) :
        score = 0
        for edge in edges :
            if individual[edge[0]] != individual[edge[1]] :
                score += 1
        return score/len(edges)

    def mutation(self , individual ,colorNum) :
        index = random.randint(0 ,len(individual)-1)
        individual[index] = random.randint(1,colorNum)
        return individual

    def generationMutation(self , generation , colorNum, mutationRate) :
        for ind in generation :
            if random.random() < mutationRate :
                ind = self.mutation(ind , colorNum)
        return generation
        