import heapq
from pathfinder.PathFinder import PathFinder

class Dijkstra(PathFinder):

    nodes_data = {}

    def __init__(self, graph, source, destination):
        super().__init__()
        self.graph = graph
        self.source = source
        self.destination = destination

    def find_path(self):
        
        self.nodes_data = {
            self.source:{
                'cost': 0,
                'lines': [],
                'prev_node': None,
                'total_lines': 0
            }
        }

        visited_nodes = set()
        heap = [(0, self.source)]

        self.visited_nodes = 0
        self.relaxed_edges = 0

        while heap:
            current_source = heapq.heappop(heap)[1]
            if current_source in visited_nodes: continue 
            visited_nodes.add(current_source)
            for node in self.graph.getAdjList()[current_source]:
                self.visited_nodes += 1
                if node in visited_nodes:continue
                for weight in self.graph.adj_list[current_source][node]['time']:
                    weight = int(weight)
                    cost = int(self.nodes_data[current_source]['cost']) + weight
                    total_lines = 0

                    if len(set(self.nodes_data[current_source]['lines']).intersection(set(self.graph.adj_list[current_source][node]['time'][str(weight)]))) == 0 : total_lines = 1

                    if node not in self.nodes_data:
                        heapq.heappush(heap, (cost, node))
                        self.relaxed_edges +=1
                        if total_lines == 0:

                            self.nodes_data[node] = {
                                'cost': cost, 
                                'lines': set(self.nodes_data[current_source]['lines']).intersection(set(self.graph.adj_list[current_source][node]['time'][str(weight)])), 
                                'prev_node': current_source, 
                                'total_lines': self.nodes_data[current_source]['total_lines']
                                }
                        else:
                            
                            self.nodes_data[node] = {
                                'cost': cost, 
                                'lines': set(self.graph.adj_list[current_source][node]['time'][str(weight)]),
                                'prev_node': current_source, 
                                'total_lines': self.nodes_data[current_source]['total_lines'] + total_lines
                                }

                    else:

                        if cost <= int(self.nodes_data[node]['cost']) or (cost == int(self.nodes_data[node]['cost']) and self.nodes_data[current_source]['total_lines'] + total_lines < self.nodes_data[node]['total_lines']):
                            heapq.heappush(heap, (cost, node))
                            self.relaxed_edges += 1
                            self.nodes_data[node]['cost'] = cost
                            self.nodes_data[node]['prev_node'] = current_source
                            self.nodes_data[node]['total_lines'] = self.nodes_data[current_source]['total_lines'] + total_lines


        
    def get_path(self):

        path = []
        
        temp = self.destination

        path.append(temp)
        cost = 0
        while temp:

            path.append(self.nodes_data[temp]['prev_node'])
            temp = self.nodes_data[temp]['prev_node']

        return (path[::-1][1:])


