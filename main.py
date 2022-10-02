from pathlib import Path
from GraphBuilder import GraphBuilder
from MetricsExtractor import Metrics_Extractor
from SortingAlgorithms.AStar import AStar
from SortingAlgorithms.PathFinder import PathFinder

stations_attr, stations = Metrics_Extractor(
    './_dataset/london.stations.csv').metrics

bank = {}

for station in stations:

    for index, attr in enumerate(stations_attr):

        if index == 0:

            bank[station[0]] = {}

        bank[station[0]][attr] = station[index]


connections_attr, connections = Metrics_Extractor(
    './_dataset/london.connections.csv').metrics

print(stations)
graph = GraphBuilder(stations, connections)
print(graph.adj_list['300'])
Path = PathFinder(graph, "11")

print("___________________________")
a_star = AStar(graph, stations, "11", "69")
print(a_star.a_star_algorithm())
print(Path.getPath("11", "69"))
