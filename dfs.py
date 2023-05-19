import networkx as nx
import copy
import matplotlib.pyplot as plt


class Graph_dfs:

    #Constructor
    # 1. Directed - True | Directed  : False | UnDirected
    def __init__(self,directed):
        self.directed=directed;
        self.graph={}

        if  self.directed:
            self.DG = nx.DiGraph()
        else:
            self.G = nx.Graph()


    def add_edge(self,node1,node2):
        if node1 in self.graph:
           self.graph[node1].append(node2)
           if not self.directed:
               if node2 in self.graph:
                   self.graph[node2].append(node1)
               else:
                   self.graph.__setitem__(node2, [node1])
        else:
            self.graph.__setitem__(node1,[node2])
            if not self.directed:
                if node2 in self.graph:
                    self.graph[node2].append(node1)
                else:
                    self.graph.__setitem__(node2, [node1])


    def depth_first_search(self,starts,goals):
        x=self.graph
        # Initialize an empty queue
        stack=[]
        # Initialize Visted List
        visited=[]
        #Append In Queue the Starting Node
        stack.append([starts])

        while stack:
            currentNode=stack.pop()
            neighbours= self.graph[currentNode[-1]]

            if(currentNode[-1] in goals):
                return currentNode,currentNode[-1]

            for neighbour in neighbours:
                if neighbour not in visited:
                    newList=copy.deepcopy(currentNode)
                    newList.append(neighbour)
                    stack.append(newList)
            visited.append(currentNode[-1])

    def print_path(self,traced_path):
        self.G.add_nodes_from(traced_path)
        for i in range(len(traced_path)-1):
            self.G.add_edge(traced_path[i],traced_path[i+1])
        nx.draw(self.G, with_labels=True, node_color='lightblue', edge_color='gray')
        plt.show()



