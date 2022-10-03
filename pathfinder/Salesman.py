from pathfinder.PathFinderFactory import PathFinderFactory
from GraphBuilder import GraphBuilder

class Salesman():

    def __init__(self, graph, stations_to_monitor, start_station):

        self.graph = graph
        self.station_to_monitor = stations_to_monitor
        self.start_station = start_station

    def find_path(self):

        graph_subset = {}
        nodes_data = {}

        for station in self.station_to_monitor:

            graph_subset[station] = graph_subset.get(station, {})

            for neighbor_station in self.graph.getAdjList()[station]:

                if neighbor_station in self.station_to_monitor:
                    
                    graph_subset[station][neighbor_station] = self.graph.getAdjList()[station][neighbor_station]

        
        for station in self.station_to_monitor:

            pathFinderFactory = PathFinderFactory()

            graph = GraphBuilder()

            graph.adj_list = graph_subset

            dijkstra = pathFinderFactory.initialize_pathFinder("Dijkstra", graph, station, station)

            dijkstra.find_path()

            nodes_data[station] = dijkstra.nodes_data

        station_order = [self.start_station]

        valid_permutations = []

        def getPermutation(lst):

            if len(lst) == 0:
                return []
            elif len(lst) == 1:
                return [lst]
            else:
                l = []
                for i in range(len(lst)):
                    x = lst[i]
                    xs = lst[:i] + lst[i+1:]
                    for p in getPermutation(xs):
                        l.append([x] + p)
                return l
        
        for p in getPermutation(self.station_to_monitor):
            
            if p[0] == self.start_station:
                
                p.append(self.start_station)
                valid_permutations.append(p)

        path = None
        lowest_cost = None

        for perm in valid_permutations:
            
            cost = 0

            for i in range(len(perm) - 1):

                cost += nodes_data[perm[i]][perm[i + 1]]['cost']

            if not lowest_cost or cost < lowest_cost:

                lowest_cost = cost

                path = perm


        return {"path": path, "cost":lowest_cost}