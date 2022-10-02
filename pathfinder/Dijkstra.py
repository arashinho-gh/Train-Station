from pathfinder.PathFinder import PathFinder

class Dijkstra(PathFinder):

    nodes_data = {}

    def __init__(self, graph, source, destination):

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

        visited_nodes = set([])
        current_source = self.source
        
        while len(visited_nodes) < len(self.graph.adj_list):
            visited_nodes.add(current_source)
            for node in self.graph.getAdjList()[current_source]:

                weight = int(sorted((self.graph.adj_list[current_source][node]['time']))[0])
                cost = int(self.nodes_data[current_source]['cost']) + weight
                total_lines = 0

                if len(set(self.nodes_data[current_source]['lines']).intersection(set(self.graph.adj_list[current_source][node]['time'][str(weight)]))) == 0 : total_lines = 1

                if node not in self.nodes_data:
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

                    if cost < int(self.nodes_data[node]['cost']) or (cost == int(self.nodes_data[node]['cost']) and self.nodes_data[current_source]['total_lines'] + total_lines < self.nodes_data[node]['total_lines']):

                        self.nodes_data[node]['cost'] = cost
                        self.nodes_data[node]['prev_node'] = current_source
                        self.nodes_data[node]['total_lines'] = self.nodes_data[current_source]['total_lines'] + total_lines

            temp_dist = None

            for k, v in self.nodes_data.items():

                if k not in visited_nodes:

                    if not temp_dist or int(v['cost']) < temp_dist:

                        temp_dist = int(v['cost'])

                        current_source = k

        
    def get_path(self):

        path = []
        
        temp = self.destination

        path.append(temp)
        cost = 0
        while temp:

            path.append(self.nodes_data[temp]['prev_node'])
            temp = self.nodes_data[temp]['prev_node']

        print("Total number of lines need to be taken: " + str(self.nodes_data[self.destination]['total_lines']))

        return (path[::-1][1:])
