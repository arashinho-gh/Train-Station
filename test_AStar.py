from pathfinder.PathFinderFactory import PathFinderFactory
from GraphBuilder import GraphBuilder
from MetricsExtractor import Metrics_Extractor

stations_data = Metrics_Extractor('./_dataset/aStar.graph.stations.csv').metrics
connections_attr, connections = Metrics_Extractor('./_dataset/aStar.graph.connections.csv').metrics

graph = GraphBuilder(stations_data, connections)
pathFinderFactory = PathFinderFactory()

bank = {(1, 1): ['1'], (1, 2): ['1', '2'], (1, 3): ['1', '3'], (1, 4): ['1', '2', '4'], (1, 5): ['1', '3', '5'], (1, 6): ['1', '2', '4', '6'], (2, 1): ['2', '1'], (2, 2): ['2'], (2, 3): ['2', '1', '3'], (2, 4): ['2', '4'], (2, 5): ['2', '1', '3', '5'], (2, 6): ['2', '4', '6'], (3, 1): ['3', '1'], (3, 2): ['3', '1', '2'], (3, 3): ['3'], (3, 4): ['3', '1', '2', '4'], (3, 5): ['3', '5'], (3, 6): ['3', '1', '2', '4', '6'], (4, 1): ['4', '2', '1'], (4, 2): ['4', '2'], (4, 3): ['4', '2', '1', '3'], (4, 4): ['4'], (4, 5): ['4', '5'], (4, 6): ['4', '6'], (5, 1): ['5', '3', '1'], (5, 2): ['5', '4', '2'], (5, 3): ['5', '3'], (5, 4): ['5', '4'], (5, 5): ['5'], (5, 6): ['5', '6'], (6, 1): ['6', '4', '2', '1'], (6, 2): ['6', '4', '2'], (6, 3): ['6', '4', '2', '1', '3'], (6, 4): ['6', '4'], (6, 5): ['6', '5'], (6, 6): ['6']}

def test_AStar():
    for i in range(1, 7):
        for j in range(1, 7):
            a_star = pathFinderFactory.initialize_pathFinder("A*", graph, str(i), str(j))
            a_star.find_path()
            assert a_star.get_path() == bank[(i,j)] 



