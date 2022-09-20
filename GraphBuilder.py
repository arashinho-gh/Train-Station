
class GraphBuilder:

    vertices = 0

    edges = 0

    adj_list = {}

    def __init__(self, vertices, edges):
        
        self.vertices = len(vertices)

        self.edges = len(edges)

        for edge in edges:

            station1 = edge[0]

            station2 = edge[1]

            line = edge[2]

            time = edge[3]

            self.add_edge(station1, station2, time, line) # time = 0, line = 1

    def add_edge(self, v, w, time, line):

        if v not in self.adj_list:

            self.adj_list[v] = {}

        if w not in self.adj_list:

            self.adj_list[w] = {}

        if w not in self.adj_list[v]:

            self.adj_list[v][w] = {'time': {}}
        
        if v not in self.adj_list[w]:

            self.adj_list[w][v] = {'time': {}}

        if time not in self.adj_list[v][w]['time']:

            self.adj_list[v][w]['time'][time] = [] 

        if time not in self.adj_list[w][v]['time']:

            self.adj_list[w][v]['time'][time] = []


        self.adj_list[w][v]['time'][time].append(line) 
        self.adj_list[v][w]['time'][time].append(line)



        

