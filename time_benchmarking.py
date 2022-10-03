import pyperf, random
from pathfinder.PathFinderFactory import PathFinderFactory
from GraphBuilder import GraphBuilder
from MetricsExtractor import Metrics_Extractor

pathFinderFactory = PathFinderFactory()

runner = pyperf.Runner()

# build small graph
connections_attr_1, connections_1 = Metrics_Extractor('./_dataset/benchMarking1.graph.connections.csv').metrics
stations_data_1 = Metrics_Extractor('./_dataset/benchMarking1.graph.stations.csv').metrics
graph_1 = GraphBuilder(stations_data_1, connections_1)

# build large graph
connections_attr_2, connections_2 = Metrics_Extractor('./_dataset/london.connections.csv').metrics
stations_data_2 = Metrics_Extractor('./_dataset/london.stations.csv').metrics
graph_2 = GraphBuilder(stations_data_2, connections_2)

# randomize start and end
smallStart = str(random.randint(1, graph_1.getNumberOfNodes()))
smallEnd = str(random.randint(1, graph_1.getNumberOfNodes()))
largeStart = str(random.randint(1, graph_2.getNumberOfNodes()))
largeEnd = str(random.randint(1, graph_2.getNumberOfNodes()))

# Dijikstra results
dijkstra1 = pathFinderFactory.initialize_pathFinder("Dijkstra", graph_1, smallStart, smallEnd)
runner.bench_func("Dijikstra Small Graph", dijkstra1.find_path)
dijkstra2 = pathFinderFactory.initialize_pathFinder("Dijkstra", graph_2, largeStart, largeEnd)
runner.bench_func("Dijikstra Large Graph", dijkstra2.find_path)

# A* results
a_star1 = pathFinderFactory.initialize_pathFinder("A*", graph_1, smallStart, smallEnd)
runner.bench_func("A* Small Graph", a_star1.find_path)
a_star2 = pathFinderFactory.initialize_pathFinder("A*", graph_2, largeStart, largeEnd)
runner.bench_func("A* Large Graph", a_star2.find_path)

# run with: python time_benchmarking.py -o time_benchmarking.json