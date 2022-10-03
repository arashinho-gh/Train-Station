import pyperf, random
from pathfinder.PathFinderFactory import PathFinderFactory
from GraphBuilder import GraphBuilder
from Utils.MetricsExtractor import Metrics_Extractor

pathFinderFactory = PathFinderFactory()

runner = pyperf.Runner()

# small graph
connections_attr_1, connections_1 = Metrics_Extractor('./_dataset/benchMarking1.graph.connections.csv').metrics
stations_data_1 = Metrics_Extractor('./_dataset/benchMarking1.graph.stations.csv').metrics
graph_1 = GraphBuilder(stations_data_1, connections_1)

# large graph
connections_attr_2, connections_2 = Metrics_Extractor('./_dataset/london.connections.csv').metrics
stations_data_2 = Metrics_Extractor('./_dataset/london.stations.csv').metrics
graph_2 = GraphBuilder(stations_data_2, connections_2)

# random start and end
start_1 = str(random.randint(1, graph_1.getNumberOfNodes()))
end_1 = str(random.randint(1, graph_1.getNumberOfNodes()))
start_2 = str(random.randint(1, graph_2.getNumberOfNodes()))
end_2 = str(random.randint(1, graph_2.getNumberOfNodes()))

# Dijikstra
dijkstra1 = pathFinderFactory.initialize_pathFinder("Dijkstra", graph_1, start_1, end_1)
runner.bench_func("Dijikstra Small Graph", dijkstra1.find_path)
dijkstra2 = pathFinderFactory.initialize_pathFinder("Dijkstra", graph_2, start_2, end_2)
runner.bench_func("Dijikstra Large Graph", dijkstra2.find_path)

# A* 
a_star1 = pathFinderFactory.initialize_pathFinder("A*", graph_1, start_1, end_1)
runner.bench_func("A* Small Graph", a_star1.find_path)
a_star2 = pathFinderFactory.initialize_pathFinder("A*", graph_2, start_2, end_2)
runner.bench_func("A* Large Graph", a_star2.find_path)

# run with: python time_benchmarking.py -o time_benchmarking.json