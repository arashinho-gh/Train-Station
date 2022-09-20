from GraphBuilder import GraphBuilder
from MetricsExtractor import Metrics_Extractor
from PathFinder import PathFinder




stations_attr, stations = Metrics_Extractor('./_dataset/london.stations.csv').metrics

bank = {}

for station in stations:

    for index, attr in enumerate(stations_attr):

        if index == 0:

            bank[station[0]] = {}

        bank[station[0]][attr] = station[index]
    

connections_attr, connections = Metrics_Extractor('./_dataset/london.connections.csv').metrics

graph = GraphBuilder(stations, connections)
print(graph.adj_list['300'])

path_finder = PathFinder(graph, '11')

# print(path_finder.distance_bank)
print(path_finder.getPath('11', '305'))


