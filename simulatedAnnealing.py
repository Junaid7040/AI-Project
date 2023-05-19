import networkx as nx
import queue
import copy
import matplotlib.pyplot as plt
import random
import math
import six
import sys
sys.modules['sklearn.externals.six'] = six
import mlrose


# testGraph={
#     "A":[("B",11),("C",14),("D",7)],
#     "B":[("A",11),("E",15)],
#     "C":[("A",14),("E",8),("D",18),("F",10)],
#     "D":[("C",18),("A",7),("F",25)],
#     "E":[("B",15),("H",9),("C",8)],
#     "F":[("C",10),("D",25),("G",20)],
#     "G":[("H",10),("F",20)],
#     "H":[("G",10)]}



class Graph_SimulatedAnnealing:


    #Constructor
    # 1. Directed - True | Directed  : False | UnDirected
    def __init__(self,directed):
        self.directed=directed;
        self.graph={}
        # self.heurisitcsDict = {
        #     "A": 40,
        #     "B": 32,
        #     "C": 25,
        #     "D": 35,
        #     "E": 19,
        #     "F": 17,
        #     "G": 0,
        #     "H": 10
        # }

        if  self.directed:
            self.DG = nx.DiGraph()
        else:
            self.G = nx.Graph()


    def add_edge(self,node1,node2,weight):
        if node1 in self.graph:
           self.graph[node1].append((node2,weight))
           if not self.directed:
               if node2 in self.graph:
                   self.graph[node2].append((node1,weight))
               else:
                   self.graph.__setitem__(node2, [(node1,weight)])
        else:
            self.graph.__setitem__(node1,[(node2,weight)])
            if not self.directed:
                if node2 in self.graph:
                    self.graph[node2].append((node1,weight))
                else:
                    self.graph.__setitem__(node2, [(node1,weight)])


    def simulated_annealing(self,starts,goals):
        #Copies The Graph to X
        #self.graph=testGraph
        X=self.graph
        #initializes a priority Queue
        pq = queue.PriorityQueue()
        #mlrose Schedule for Time decay
        schedule = mlrose.ExpDecay(init_temp=10, exp_const=0.05, min_temp=1)
        #Best Cost Initialization
        bestCost = -1
        #Enqueuing the First Node into a Queue
        pq.put(( self.heurisitcsDict[starts], [(starts,0)] ))
        #Initializing the Temprature
        temprature = 10
        #visited
        visited=[]
        #counter to break Annealing
        counter=0

        while pq:
            current=pq.get()
            currCost,currentNode=current
            x=currentNode[-1][0]

            #if Current Node is One of the Goals
            if(currentNode[-1][0] in goals):
                cost=0
                for i in range(len(currentNode)):
                    cost+=currentNode[i][1]
                return currentNode,cost,currentNode[-1][0]   #traced_path5, cost4, goal


            neighbours = self.graph[currentNode[-1][0]]
            randomNode=neighbours[random.randint(0,(len(neighbours)-1))]
            randomCost=self.heurisitcsDict[randomNode[0]]

            deltaEnergy = randomCost - currCost                 #ΔE = E_new - E_current
            #ΔE is the delta energy.
            #E_new is the energy of the new state or solution being evaluated.
            #E_current is the energy of the current state or solution
            probab = math.exp(-(deltaEnergy) / temprature)

            if deltaEnergy <= 0:
                newList = copy.deepcopy(currentNode)
                newList.append((randomNode))
                pq.put((randomCost,newList))
            elif math.exp(-(deltaEnergy) / temprature) > 0.5 and math.exp(-(deltaEnergy) / temprature) < 1:
                newList = copy.deepcopy(currentNode)
                newList.append((randomNode))
                pq.put((randomCost, newList))
                counter=0
            else:
                pq.put(current)
                counter=counter+1
            if counter==1000:
                break;
                return "Not Found Results"

            temprature=schedule.evaluate(1)


    def print_path(self,traced_path):
        self.G.add_nodes_from(traced_path)
        for i in range(len(traced_path)-1):
            self.G.add_edge(traced_path[i],traced_path[i+1])
        nx.draw(self.G, with_labels=True, node_color='lightblue', edge_color='gray')
        plt.show()

    def set_heurisitcs(self,heuristicDict):
        self.heurisitcsDict=heuristicDict;

# x=Graph_SimulatedAnnealing(False)
# traced,goal,cost=x.simulated_annealing("A",["G"]) #traced_path5, cost4, goal
# x.print_path(traced)


