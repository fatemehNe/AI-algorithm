import numpy as np
import random
import copy
import matplotlib.pyplot as plt

import BFS 
import DFS 
import Astar
import UCS
import bidirectional

import HillClimbing
import SimulatedAnnealing
import Genetic

import question6
import question5
import question4
import question3
import question2
import question1

problem6 = question6.q6()
problem5 = question5.q5()
problem4 = question4.q4()
problem3 = question3.q3() 
problem2 = question2.q2()
problem1 = question1.q1()

dfs = DFS.DFS()
HC = HillClimbing.hillClimbing()

def p1(select) :
    
    start = problem1.InitialState()
    if select == "a" :
        print(BFS.BFS(start , problem1) , "BFS")

    if select == "b" :
        goal = problem1.GoalState()
        print(bidirectional.bidirectional( start,goal , problem1) , "bidirectional")

    if select == "c" :
        print(dfs.DFS(start , problem1) , "DFS")

def p2(select) :

    start = problem2.InitialState()
    if select == "a" :
        print(BFS.BFS(start , problem2) , "BFS")

    if select == "b" :
        print(dfs.DFS(start , problem2) , "DFS")

    if select == "c" :
        print(dfs.LDFS(start , problem2 , 15) , "LDFS")

    if select == "d" :
        print(Astar.Astar(start , problem2 ) , "A*")

def p3(select) :

    start = problem3.InitialState()
    if select == "a" :
        print(UCS.UCS(start , problem3) , "UCS")
    
    if select == "b" :
        print(dfs.IterativeDeepening(start , problem3) , "ITERATIVE")
    
def p4() :
     
    # the less the value the better
    start =problem4.InitialState(7)
    print(HC.stochastic(start,problem4) , "stochastic")
    print(HC.simple(start, problem4) , "simple")
    print(HC.firstChoice(start,problem4) , "firstchoice")
    print(HC.randomRestart(start,problem4) , "randomrestart")



def p5() :
    # the more the value the better and best is 54
    start = problem5.InitialState()
    print(SimulatedAnnealing.SA(start , problem5))
    
def p6() :
    condition = problem6.InitialState()
    output = Genetic.Genetic(condition , problem6)
    print(output["thecolors "])
    print(output["value"])
    print(output["generation"])
    xlist = range(len(output["bestG"]))
    plt.plot(xlist ,output["bestG"] , label="bestVals")
    plt.plot(xlist ,output["worstG"] , label="worstVals")
    plt.plot(xlist ,output["avgG"] , label="avgVals")
    plt.legend()
    plt.show()


