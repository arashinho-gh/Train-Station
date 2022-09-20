class PathFinder:

    distance_bank = {}

    def __init__(self, graph, source):

        self.distance_bank = {

            source: {'cost': 0, 'lines': [], 'prev_node': None, 'total_lines': 0}

        }

        visited_nodes = set([])

        current_source = source
        
    
        while len(visited_nodes) < len(graph.adj_list):

            visited_nodes.add(current_source)

            for node in graph.adj_list[current_source]:

                weight = int(sorted((graph.adj_list[current_source][node]['time']))[0])

                cost = int(self.distance_bank[current_source]['cost']) + weight

                total_lines = 0

                if len(set(self.distance_bank[current_source]['lines']).intersection(set(graph.adj_list[current_source][node]['time'][str(weight)]))) == 0 : total_lines = 1

                if node not in self.distance_bank:

                    if total_lines == 0:

                        self.distance_bank[node] = {
                            'cost': cost, 
                            'lines': set(self.distance_bank[current_source]['lines']).intersection(set(graph.adj_list[current_source][node]['time'][str(weight)])), 
                            'prev_node': current_source, 
                            'total_lines': self.distance_bank[current_source]['total_lines']
                            }
                    else:
                        
                        self.distance_bank[node] = {
                            'cost': cost, 
                            'lines': set(graph.adj_list[current_source][node]['time'][str(weight)]),
                            'prev_node': current_source, 
                            'total_lines': self.distance_bank[current_source]['total_lines'] + total_lines
                            }

                else:

                    if cost < int(self.distance_bank[node]['cost']) or (cost == int(self.distance_bank[node]['cost']) and self.distance_bank[current_source]['total_lines'] + total_lines < self.distance_bank[node]['total_lines']):

                        self.distance_bank[node]['cost'] = cost
                        self.distance_bank[node]['prev_node'] = current_source
                        self.distance_bank[node]['total_lines'] = self.distance_bank[current_source]['total_lines'] + total_lines

            temp_dist = None

            for k, v in self.distance_bank.items():

                if k not in visited_nodes:

                    if not temp_dist or int(v['cost']) < temp_dist:

                        temp_dist = int(v['cost'])

                        current_source = k

        
    def getPath(self, source, dest):

        path = []
        
        temp = dest

        path.append(temp)

        while temp:

            path.append(self.distance_bank[temp]['prev_node'])

            temp = self.distance_bank[temp]['prev_node']

        print("Total number of lines need to be taken: " + str(self.distance_bank[dest]['total_lines']))

        return (path[::-1][1:])
