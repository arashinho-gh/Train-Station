from pathfinder.PathFinderFactory import PathFinderFactory
from GraphBuilder import GraphBuilder
from MetricsExtractor import Metrics_Extractor

stations_data = Metrics_Extractor('./_dataset/dijkstra.graph.stations.csv').metrics
connections_attr, connections = Metrics_Extractor('./_dataset/dijkstra.graph.connections.csv').metrics

graph = GraphBuilder(stations_data, connections)
pathFinderFactory = PathFinderFactory()

bank = {
    1: {'1': {'cost': 0, 'lines': [], 'prev_node': None, 'total_lines': 0}, '2': {'cost': 1, 'lines': {'2'}, 'prev_node': '1', 'total_lines': 1}, '3': {'cost': 3, 'lines': {'1'}, 'prev_node': '1', 'total_lines': 1}, '4': {'cost': 2, 'lines': {'2'}, 'prev_node': '2', 'total_lines': 1}, '5': {'cost': 7, 'lines': {'1'}, 'prev_node': '3', 'total_lines': 2}, '6': {'cost': 9, 'lines': {'2'}, 'prev_node': '4', 'total_lines': 1}},
    2: {'2': {'cost': 0, 'lines': [], 'prev_node': None, 'total_lines': 0}, '1': {'cost': 1, 'lines': {'2'}, 'prev_node': '2', 'total_lines': 1}, '4': {'cost': 1, 'lines': {'2'}, 'prev_node': '2', 'total_lines': 1}, '3': {'cost': 4, 'lines': {'1'}, 'prev_node': '1', 'total_lines': 2}, '5': {'cost': 7, 'lines': {'1'}, 'prev_node': '4', 'total_lines': 2}, '6': {'cost': 8, 'lines': {'2'}, 'prev_node': '4', 'total_lines': 1}},
    3: {'3': {'cost': 0, 'lines': [], 'prev_node': None, 'total_lines': 0}, '1': {'cost': 3, 'lines': {'1'}, 'prev_node': '3', 'total_lines': 1}, '5': {'cost': 4, 'lines': {'3'}, 'prev_node': '3', 'total_lines': 1}, '2': {'cost': 4, 'lines': {'2'}, 'prev_node': '1', 'total_lines': 2}, '4': {'cost': 5, 'lines': {'2'}, 'prev_node': '2', 'total_lines': 2}, '6': {'cost': 12, 'lines': {'1'}, 'prev_node': '4', 'total_lines': 2}},
    4: {'4': {'cost': 0, 'lines': [], 'prev_node': None, 'total_lines': 0}, '2': {'cost': 1, 'lines': {'2'}, 'prev_node': '4', 'total_lines': 1}, '5': {'cost': 6, 'lines': {'1'}, 'prev_node': '4', 'total_lines': 1}, '6': {'cost': 7, 'lines': {'2'}, 'prev_node': '4', 'total_lines': 1}, '1': {'cost': 2, 'lines': {'2'}, 'prev_node': '2', 'total_lines': 1}, '3': {'cost': 5, 'lines': {'1'}, 'prev_node': '1', 'total_lines': 2}},
    5: {'5': {'cost': 0, 'lines': [], 'prev_node': None, 'total_lines': 0}, '3': {'cost': 4, 'lines': {'3'}, 'prev_node': '5', 'total_lines': 1}, '4': {'cost': 6, 'lines': {'1'}, 'prev_node': '5', 'total_lines': 1}, '6': {'cost': 9, 'lines': {'1'}, 'prev_node': '5', 'total_lines': 1}, '1': {'cost': 7, 'lines': {'1'}, 'prev_node': '3', 'total_lines': 2}, '2': {'cost': 7, 'lines': {'2'}, 'prev_node': '4', 'total_lines': 2}},
    6: {'6': {'cost': 0, 'lines': [], 'prev_node': None, 'total_lines': 0}, '4': {'cost': 7, 'lines': {'2'}, 'prev_node': '6', 'total_lines': 1}, '5': {'cost': 9, 'lines': {'1'}, 'prev_node': '6', 'total_lines': 1}, '2': {'cost': 8, 'lines': {'2'}, 'prev_node': '4', 'total_lines': 1}, '1': {'cost': 9, 'lines': {'2'}, 'prev_node': '2', 'total_lines': 1}, '3': {'cost': 12, 'lines': {'1'}, 'prev_node': '1', 'total_lines': 2}}
}


def test_Dijkstra():
    for i in range(1, 7):
        dijkstra = pathFinderFactory.initialize_pathFinder("Dijkstra", graph, str(i), '6')
        dijkstra.find_path()
        assert dijkstra.nodes_data == bank[i]

