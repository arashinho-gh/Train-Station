from abc import ABC, abstractmethod

class PathFinder(ABC):

    def __init__(self):
        self.relaxed_edges = 0
        self.visited_nodes = 0

    @abstractmethod
    def find_path(self):
        pass 

    @abstractmethod
    def get_path(self):
        pass



