from pathfinder.PathFinderFactory import PathFinderFactory
from GraphBuilder import GraphBuilder
from MetricsExtractor import Metrics_Extractor
from salesman import Salesman

stations_data = Metrics_Extractor('./_dataset/london.stations.csv').metrics
connections_attr, connections = Metrics_Extractor('./_dataset/london.connections.csv').metrics

graph = GraphBuilder(stations_data, connections)
pathFinderFactory = PathFinderFactory()

# salesman = Salesman(graph,['1','2','3','4'] , '4')

# print(salesman.find_path())
# a_star = pathFinderFactory.initialize_pathFinder("A*", graph, "11", "43")
# dijkstra = pathFinderFactory.initialize_pathFinder("Dijkstra", graph, "11", "43")


print(graph.getAdjList()['11'])
print(graph.getAdjList()['83'])
print(graph.getAdjList()['193'])
print(graph.getAdjList()['18'])
print(graph.getAdjList()['186'])
print(graph.getAdjList()['122'])
print(graph.getAdjList()['99'])
print(graph.getAdjList()['236'])