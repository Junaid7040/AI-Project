import networkx as nx
import queue
import copy
import matplotlib.pyplot as plt

# testGraph={
#     "1":["2","3","4","5"],
#     "2":["1","3"],
#     "3":["1","2","4"],
#     "4":["1","5","3"],
#     "5":["1","4"]
#     }

class Graph_bfs:

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


    def breadth_first_search(self,starts,goals):
        x=self.graph
        # Initialize an empty queue
        q = queue.Queue()
        # Initialize Visted List
        visited=[]
        #Append In Queue the Starting Node
        q.put([starts])

        while q:
            currentNode=q.get()
            neighbours= self.graph[currentNode[-1]]

            if(currentNode[-1] in goals):
                return currentNode,currentNode[-1]

            for neighbour in neighbours:
                if neighbour not in visited:
                    newList=copy.deepcopy(currentNode)
                    newList.append(neighbour)
                    q.put(newList)
            visited.append(currentNode[-1])

    def print_path(self,traced_path):
        self.G.add_nodes_from(traced_path)
        for i in range(len(traced_path)-1):
            self.G.add_edge(traced_path[i],traced_path[i+1])
        nx.draw(self.G, with_labels=True, node_color='lightblue', edge_color='gray')
        plt.show()

# x=Graph_bfs(False)
# traced,goal=x.breadth_first_search("2","5")
# x.print_path(traced)


