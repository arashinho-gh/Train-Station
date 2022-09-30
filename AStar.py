class AStar:
    distance_bank = {}

    def __init__(self, graph, data, start, dest):
        self.graph = graph
        self.start = start
        self.dest = dest
        self.data = data
        self.index = int(start)

    def heurestic(self,current_node):
        longitude_start = float(self.data[self.index][1])
        longitude_current = float(self.data[int(current_node)][1])
        latitude_start = float(self.data[self.index][2])
        latitude_current = float(self.data[int(current_node)][2])
        H = (longitude_current-longitude_start)**2 + (latitude_current-latitude_start)**2
        return H
            
    def a_star_algorithm(self):
        open_list=set([self.start])
        closed_list=[]
        current_distance={}
        current_distance[self.start]=0
        adj={}
        adj[self.start]=self.start
        while len(open_list) > 0:
            n = None
            for v in open_list:
                if n == None or (current_distance[v] + self.heurestic(v) < current_distance[n] + self.heurestic(n)):
                    n=v
            if n == self.dest:
                reconst_path = []
                while adj[n] != n:
                    reconst_path.append(n)
                    n = adj[n]
                reconst_path.append(self.start)
                reconst_path.reverse()
                print("path found:")
                return reconst_path
            if n == None:
                print("Path doesn't exist")
                return None
            for m in self.graph.adj_list[str(n)]:
                if (m not in open_list )and (m not in closed_list):
                    open_list.add(m)
                    adj[m] = n
                    current_distance[m] = self.heurestic(n)
                else:
                    if current_distance[m] > current_distance[n]:
                        current_distance[m] = current_distance[n] + self.heurestic(n)
                        current_distance[m] = self.heurestic(n)
                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)
                            
            open_list.remove(n)
            closed_list.append(n)
        print("Path doesn't exist")
        return None