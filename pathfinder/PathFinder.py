from abc import ABC, abstractmethod

class PathFinder(ABC):

    @abstractmethod
    def find_path(self):
        pass 

    @abstractmethod
    def get_path(self):
        pass



