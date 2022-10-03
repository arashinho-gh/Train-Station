from pathfinder.PathFinderFactory import PathFinderFactory

class Islands:

    islands = {}

    def __init__(self, graph):

        self.graph = graph

    def findIslands(self):

        def dfs(node, visited):
            
            if node in visited: return

            visited.add(node)

            for neighbor in self.graph.getAdjList()[node]:
                
                if self.graph.getZone(node) == self.graph.getZone(neighbor):

                    dfs(neighbor, visited)

        v = set([])

        for node, neighbors in self.graph.getAdjList().items():            
            
            if node not in v:

                self.islands[self.graph.getZone(node)] = self.islands.get(self.graph.getZone(node), [])

                visited = set([])

                dfs(node, visited)

                self.islands[self.graph.getZone(node)].append(sorted(list(visited)))
                
                v = v.union(visited)

    def getPathToIsland(self):

        pathToIslands = {}


        for node in self.graph.getAdjList().keys():

            pathToIslands[node] = {}

            dijkstra = PathFinderFactory.initialize_pathFinder("Dijkstra", self.graph, node, node)

            dijkstra.find_path()

            for neighbor in dijkstra.nodes_data.keys():
                
                dijkstra.destination = neighbor
                path = dijkstra.get_path()
                zones = set()
                for n in path:
                    zones.add(self.graph.getZone(n))

                pathToIslands[node][neighbor] = {"path": path, "zones": zones}

                

        return pathToIslands
