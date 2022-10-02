from pathfinder.A_Star import A_Star
from pathfinder.Dijkstra import Dijkstra

class PathFinderFactory():

    @staticmethod
    def initialize_pathFinder(algo_name, graph, source, destination):
        try:
            if algo_name == "A*":
                return A_Star(graph, source, destination)
            elif algo_name == "Dijkstra":
                return Dijkstra(graph, source, destination)
            raise AssertionError("Invalid Algorithm name!")
        except AssertionError as e:
            print(e)

                
            