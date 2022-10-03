import heapq
from math import radians, cos, sin, asin, sqrt
from pathfinder.PathFinder import PathFinder

class A_Star(PathFinder):

    nodes_data = {}

    def __init__(self, graph, source, destination):
        super().__init__()
        self.graph = graph
        self.source = source
        self.destination = destination

    def find_path(self):
        heuristic = self.calc_distance(
                    {"longitude": self.graph.getLongitude(self.source), "latitude": self.graph.getLatitude(self.source)},
                    {"longitude": self.graph.getLongitude(self.destination), "latitude": self.graph.getLatitude(self.destination)}
                    )

        self.nodes_data = {
            self.source: {
                "cost_from_source": 0,
                "heuristic_distance": heuristic,
                "f": 0 + heuristic,
                "prev_vertex": None
            }
        }
        heap = [(heuristic, self.source)]
        visited = []
        self.visited_nodes = 0
        self.relaxed_edges = 0
        current_node = self.source

        while current_node != self.destination and heap:

            visited.append(current_node) 

            for neighbor in self.graph.adj_list[current_node]:
                self.visited_nodes += 1
                cost = int(self.nodes_data[current_node]["cost_from_source"]) + int(sorted(self.graph.adj_list[neighbor][current_node]["time"].keys())[0])
                heuristic = self.calc_distance(                    
                    {"longitude": self.graph.getLongitude(neighbor), "latitude": self.graph.getLatitude(neighbor)},
                    {"longitude": self.graph.getLongitude(self.destination), "latitude": self.graph.getLatitude(self.destination)}
                    )
                f = cost + heuristic
            
                if (neighbor not in self.nodes_data) or (cost < self.nodes_data[neighbor]["cost_from_source"] ):
                    heapq.heappush(heap, (f, neighbor))
                    self.relaxed_edges += 1
                    self.nodes_data[neighbor] = {
                        "cost_from_source": cost,
                        "heuristic_distance": heuristic,
                        "f": f,
                        "prev_vertex": current_node
                    }

            while current_node in visited and heap:
                current_node = heapq.heappop(heap)[1]
            

    def get_path(self):
        prev_node = self.nodes_data[self.destination]["prev_vertex"]
        cost = self.nodes_data[self.destination]["cost_from_source"]
        path = [self.destination]

        while prev_node:

            path.append(prev_node)
            prev_node = self.nodes_data[prev_node]["prev_vertex"]

        return path[::-1]

    def calc_distance(self, point_one, point_two):

        lon1 = radians(float(point_one["longitude"]))
        lon2 = radians(float(point_two["longitude"]))
        lat1 = radians(float(point_one["latitude"]))
        lat2 = radians(float(point_two["latitude"]))


        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    
        c = 2 * asin(sqrt(a))
        
        r = 6371
        
        return(c * r)






        





