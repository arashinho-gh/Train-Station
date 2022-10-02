from GraphBuilder import GraphBuilder
from MetricsExtractor import Metrics_Extractor
from PathFinder import PathFinder
from Islands import Islands



stations_attr, stations = Metrics_Extractor('./_dataset/london.stations.csv').metrics
connections_attr, connections = Metrics_Extractor('./_dataset/london.connections.csv').metrics
graph = GraphBuilder(stations, connections)

islands = Islands(graph, bank)
islands.findIslands()
# print(islands.islands)
# print(islands.islands['1'][0][0])
# p = islands.getPathToIsland()
# print(p)

"""
path_finder = PathFinder(graph, '11')
print(path_finder.getPath('11', '43'))
print(path_finder.distance_bank['11'])
print(graph.adj_list["11"]["28"]["time"])
print(path_finder.distance_bank['28'])
print(graph.adj_list["28"]["107"]["time"])
print(path_finder.distance_bank['107'])
print(graph.adj_list["107"]["285"]["time"])
print(path_finder.distance_bank['285'])
print(graph.adj_list["285"]["279"]["time"])
print(path_finder.distance_bank['279'])
print(graph.adj_list["279"]["233"]["time"])
print(path_finder.distance_bank['233'])
print(graph.adj_list["233"]["157"]["time"])
print(path_finder.distance_bank['157'])
print(graph.adj_list["157"]["23"]["time"])
print(path_finder.distance_bank['23'])
print(graph.adj_list["23"]["41"]["time"])
print(path_finder.distance_bank['41'])
print(graph.adj_list["41"]["42"]["time"])
print(path_finder.distance_bank['42'])
print(graph.adj_list["42"]["183"]["time"])
print(path_finder.distance_bank['183'])
print(graph.adj_list["183"]["43"]["time"])
print(path_finder.distance_bank['43'])


print("///////")
"""
a_star = A_star("276", "43",bank, graph)
print("///////")

# print(a_star.getPath("276", "43"))
print(graph.adj_list['225'])
# print(a_star.bank['43'])

"""
print(a_star.bank['11'])
print(graph.adj_list["11"]["28"]["time"])
print(a_star.bank['28'])
print(graph.adj_list["28"]["192"]["time"])
print(a_star.bank['192'])
print(graph.adj_list["192"]["259"]["time"])
print(a_star.bank['259'])
print(graph.adj_list["259"]["126"]["time"])
print(a_star.bank['126'])
print(graph.adj_list["126"]["48"]["time"])
print(a_star.bank['48'])
print(graph.adj_list["48"]["250"]["time"])
print(a_star.bank['250'])
print(graph.adj_list["250"]["13"]["time"])
print(a_star.bank['13'])
print(graph.adj_list["13"]["225"]["time"])
print(a_star.bank['225'])
print(graph.adj_list["225"]["155"]["time"])
print(a_star.bank['155'])
print(graph.adj_list["155"]["284"]["time"])
print(a_star.bank['284'])
print(graph.adj_list["284"]["201"]["time"])
print(a_star.bank['201'])
print(graph.adj_list["201"]["27"]["time"])
print(a_star.bank['27'])
print(graph.adj_list["27"]["79"]["time"])
print(a_star.bank['79'])
print(graph.adj_list["79"]["43"]["time"])
print(a_star.bank['43'])

"""