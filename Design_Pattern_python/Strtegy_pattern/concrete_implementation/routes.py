from interface_strategy.routes import RoutesStrategy


class CarRoute(RoutesStrategy):

    def get_routes(self, source, destination):
        print("Car route from source:", source, "to destination:", destination)


class BikeRoute(RoutesStrategy):

    def get_routes(self, source, destination):
        print("Bike route from source:", source, "to destination:", destination)

class WalkRoute(RoutesStrategy):

    def get_routes(self, source, destination):
        print("Walk route from source:", source, "to destination:", destination)

