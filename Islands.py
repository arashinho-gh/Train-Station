from PathFinder import PathFinder

class Islands:

    islands = {}

    def __init__(self, graph, stations_bank):

        self.graph = graph
        self.stations_bank = stations_bank

    def findIslands(self):

        def dfs(node, visited):
            
            if node in visited: return

            visited.add(node)

            for neighbor in self.graph.adj_list[node]:
                
                if self.stations_bank[node]['zone'] == self.stations_bank[neighbor]['zone']:

                    dfs(neighbor, visited)

        v = set([])

        for node, neighbors in self.graph.adj_list.items():            
            
            if node not in v:

                self.islands[self.stations_bank[node]['zone']] = self.islands.get(self.stations_bank[node]['zone'], [])

                visited = set([])

                dfs(node, visited)

                self.islands[self.stations_bank[node]['zone']].append(list(visited))
                
                v = v.union(visited)

    def getPathToIsland(self):

        pathToIslands = {}

        for zone, Islands in self.islands.items():

            pathToIslands[zone] = pathToIslands.get(zone, {})

            for i in range(len(Islands) - 1):

                pathToIslands[zone][i] = pathToIslands[zone].get(i, {}) 

                for j in range(i + 1, len(Islands)):
                    

                    path_finder = PathFinder(self.graph, Islands[i][0])

                    path = path_finder.getPath(Islands[i][0], Islands[j][0])
                    Islands_path = set([])

                    for station in path:

                        station = str(station)

                        Islands_path.add(self.stations_bank[station]['zone'])

                    pathToIslands[zone][i][j] = {"zones_to_go_through": Islands_path }

        return pathToIslands



