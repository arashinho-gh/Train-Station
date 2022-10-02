
class GraphBuilder:

    vertices = 0

    edges = 0

    adj_list = {}

    def __init__(self, vertices_data = None, edges = None):
        
        if vertices_data and edges:
            self.vertices_data = vertices_data
            self.vertices = vertices_data[1]

            self.edges = edges

            for edge in edges:

                station1 = edge[0]

                station2 = edge[1]

                line = edge[2]

                time = edge[3]

                self.add_edge(station1, station2, time, line) 

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

    def getNumberOfNodes(self): return len(self.vertices)

    def getNumberOfEdges(self): return len(self.edges)

    def getAverageNodeDegree(self): return (self.getNumberOfEdges())/(self.getNumberOfNodes())

    def getNodeData(self):
        
        node_data = {}
        for station in self.vertices:

            for index, attr in enumerate(self.vertices_data[0]):

                if index == 0:

                    node_data[station[0]] = {}

                node_data[station[0]][attr] = station[index]
    
        return node_data

    def getAdjList(self): return self.adj_list
        
    def getLongitude(self, node): return self.getNodeData()[node]['longitude']

    def getLatitude(self, node): return self.getNodeData()[node]['latitude']

    def getZone(self, node): return self.getNodeData()[node]['zone']

