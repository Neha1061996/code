from abc import ABC, abstractmethod

class RoutesStrategy(ABC):

    @abstractmethod
    def get_routes(self, source, destination):
        pass