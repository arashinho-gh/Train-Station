import pyperf, random
from pathfinder.PathFinderFactory import PathFinderFactory
from GraphBuilder import GraphBuilder
from Utils.MetricsExtractor import Metrics_Extractor
from pathfinder.Islands import Islands

runner = pyperf.Runner()

stations_data = Metrics_Extractor('./_dataset/Islands.graph.stations.csv').metrics
connections_attr, connections = Metrics_Extractor('./_dataset/Islands.graph.connections.csv').metrics

graph = GraphBuilder(stations_data, connections)

islands = Islands(graph)

runner.bench_func("Find Islands", islands.findIslands)
runner.bench_func("Find Paths", islands.getPathToIsland)

# run with: python time_benchmarking_Islands.py -o time_benchmarking_Islands.json