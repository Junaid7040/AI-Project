import depthLimitedDepthFirstSearch as dp

import networkx as nx
import queue
import copy
import matplotlib.pyplot as plt


#
# testGraph={
#     "A":[("B",11),("C",14),("D",7)],
#     "B":[("A",11),("E",15)],
#     "C":[("A",14),("E",8),("D",18),("F",10)],
#     "D":[("C",18),("A",7),("F",25)],
#     "E":[("B",15),("H",9),("C",8)],
#     "F":[("C",10),("D",25),("G",20)],
#     "G":[("H",10),("F",20)],
#     "H":[("G",10)]}



class Graph_iterativeDeepeningSearch:
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
            self.G = nx.DiGraph()
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

    def ids(self,root, goal, depth):
        cost=0
        dps=dp.Graph_depthLimitedDepthFirstSearch(False)
        dps.graph=self.graph
        for i in range(depth):
            GoalState = dps.depthLimitedSearch(root, goal, i+1)
            if (GoalState != None):
                return GoalState;
        return GoalState

    def print_path(self,traced_path):
        self.G.add_nodes_from(traced_path)
        for i in range(len(traced_path)-1):
            self.G.add_edge(traced_path[i],traced_path[i+1])
        nx.draw(self.G, with_labels=True, node_color='lightblue', edge_color='gray')
        plt.show()

    def set_heurisitics(self,heuristicDict):
        self.heurisitcsDict=heuristicDict;

# x=Graph_iterativeDeepeningSearch(False)
# traced=x.ids("A",["G"],3) #traced_path, cost
# x.print_path(traced[0])
