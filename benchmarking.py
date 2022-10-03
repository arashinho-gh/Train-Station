from pathfinder.PathFinderFactory import PathFinderFactory
from GraphBuilder import GraphBuilder
from Utils.MetricsExtractor import Metrics_Extractor
import random

pathFinderFactory = PathFinderFactory()
print("------- A* v.s Dijkstra -------")

# Connected Graph
print("------- Start and End are connected -------")
stations_data = Metrics_Extractor('./_dataset/benchMarking1.graph.stations.csv').metrics
connections_attr, connections = Metrics_Extractor('./_dataset/benchMarking1.graph.connections.csv').metrics

graph_1 = GraphBuilder(stations_data, connections)

a_star = pathFinderFactory.initialize_pathFinder("A*", graph_1, "1", "6")
dijkstra = pathFinderFactory.initialize_pathFinder("Dijkstra", graph_1, "1", "6")

a_star.find_path()
dijkstra.find_path()
print("-- A*")
print("Number of nodes visited:", a_star.visited_nodes)
print("Numbers of edges relaxed:", a_star.relaxed_edges)
print()
print("-- Dijkstra")
print("Number of nodes visited:",dijkstra.visited_nodes)
print("Numbers of edges relaxed:", dijkstra.relaxed_edges)

# Not Connected
print("------- Start and End are NOT connected -------")
stations_data = Metrics_Extractor('./_dataset/benchMarking2.graph.stations.csv').metrics
connections_attr, connections = Metrics_Extractor('./_dataset/benchMarking2.graph.connections.csv').metrics

graph_2 = GraphBuilder(stations_data, connections)

a_star = pathFinderFactory.initialize_pathFinder("A*", graph_2, "1", "7")
dijkstra = pathFinderFactory.initialize_pathFinder("Dijkstra", graph_2, "1", "7")

a_star.find_path()
dijkstra.find_path()
print("-- A*")
print("Number of nodes visited:", a_star.visited_nodes)
print("Numbers of edges relaxed:", a_star.relaxed_edges)
print()
print("-- Dijkstra")
print("Number of nodes visited:",dijkstra.visited_nodes)
print("Numbers of edges relaxed:", dijkstra.relaxed_edges)


# Start and End is the same
print("------- Start and End are the same -------")

ations_data = Metrics_Extractor('./_dataset/benchMarking1.graph.stations.csv').metrics
connections_attr, connections = Metrics_Extractor('./_dataset/benchMarking1.graph.connections.csv').metrics

graph_3 = GraphBuilder(stations_data, connections)

a_star = pathFinderFactory.initialize_pathFinder("A*", graph_3, "1", "1")
dijkstra = pathFinderFactory.initialize_pathFinder("Dijkstra", graph_3, "1", "1")

a_star.find_path()
dijkstra.find_path()
print("-- A*")
print("Number of nodes visited:", a_star.visited_nodes)
print("Numbers of edges relaxed:", a_star.relaxed_edges)
print()
print("-- Dijkstra")
print("Number of nodes visited:",dijkstra.visited_nodes)
print("Numbers of edges relaxed:", dijkstra.relaxed_edges)


# One path from start to end
print("------- No edges to Relax -------")

stations_data = Metrics_Extractor('./_dataset/benchMarking3.graph.stations.csv').metrics
connections_attr, connections = Metrics_Extractor('./_dataset/benchMarking3.graph.connections.csv').metrics

graph_4 = GraphBuilder(stations_data, connections)

a_star = pathFinderFactory.initialize_pathFinder("A*", graph_3, "1", "6")
dijkstra = pathFinderFactory.initialize_pathFinder("Dijkstra", graph_3, "1", "6")

a_star.find_path()
dijkstra.find_path()
print("-- A*")
print("Number of nodes visited:", a_star.visited_nodes)
print("Numbers of edges relaxed:", a_star.relaxed_edges)
print()
print("-- Dijkstra")
print("Number of nodes visited:",dijkstra.visited_nodes)
print("Numbers of edges relaxed:", dijkstra.relaxed_edges)

# london
print("------- Random London Test -------")

stations_data = Metrics_Extractor('./_dataset/london.stations.csv').metrics
connections_attr, connections = Metrics_Extractor('./_dataset/london.connections.csv').metrics

graph_5 = GraphBuilder(stations_data, connections)

start = str(random.randint(1,302))
end = str(random.randint(1,302))

a_star = pathFinderFactory.initialize_pathFinder("A*", graph_5, start, end)
dijkstra = pathFinderFactory.initialize_pathFinder("Dijkstra", graph_5, start, end)

a_star.find_path()
dijkstra.find_path()
print("-- A*")
print("Number of nodes visited:", a_star.visited_nodes)
print("Numbers of edges relaxed:", a_star.relaxed_edges)
print()
print("-- Dijkstra")
print("Number of nodes visited:",dijkstra.visited_nodes)
print("Numbers of edges relaxed:", dijkstra.relaxed_edges)

