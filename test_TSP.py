from pathfinder.PathFinderFactory import PathFinderFactory
from GraphBuilder import GraphBuilder
from MetricsExtractor import Metrics_Extractor
from salesman import Salesman

stations_data = Metrics_Extractor('./_dataset/TSP.graph.stations.csv').metrics
connections_attr, connections = Metrics_Extractor('./_dataset/TSP.graph.connections.csv').metrics

graph = GraphBuilder(stations_data, connections)


def test_Tsp():
    salesman = Salesman(graph,['1','2','3','4'] , '1')
    assert salesman.find_path() == {"cost":80, "path":['1', '2', '4', '3', '1']}
    salesman = Salesman(graph,['1','2','3','4'] , '2')
    assert salesman.find_path() == {"cost":80, "path":['2', '1', '3', '4', '2']}
    salesman = Salesman(graph,['1','2','3','4'] , '3')
    assert salesman.find_path() == {"cost":80, "path":['3', '1', '2', '4', '3']}
    salesman = Salesman(graph,['1','2','3','4'] , '4')
    assert salesman.find_path() == {"cost":80, "path":['4', '2', '1', '3', '4']} 

