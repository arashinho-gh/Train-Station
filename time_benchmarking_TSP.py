import pyperf, random
from pathfinder.PathFinderFactory import PathFinderFactory
from GraphBuilder import GraphBuilder
from Utils.MetricsExtractor import Metrics_Extractor
from pathfinder.Salesman import Salesman

stations_data = Metrics_Extractor('./_dataset/TSP.graph.stations.csv').metrics
connections_attr, connections = Metrics_Extractor('./_dataset/TSP.graph.connections.csv').metrics

graph = GraphBuilder(stations_data, connections)

runner = pyperf.Runner()

# start at 1
salesman = Salesman(graph,['1','2','3','4'] , '1')
runner.bench_func("TSP_1", salesman.find_path)

# start at 2
salesman = Salesman(graph,['1','2','3','4'] , '2')
runner.bench_func("TSP_2", salesman.find_path)

# start at 3
salesman = Salesman(graph,['1','2','3','4'] , '3')
runner.bench_func("TSP_3", salesman.find_path)

# start at 4
salesman = Salesman(graph,['1','2','3','4'] , '4')
runner.bench_func("TSP_4", salesman.find_path)

# run with: python time_benchmarking_TSP.py -o time_benchmarking_TSP.json