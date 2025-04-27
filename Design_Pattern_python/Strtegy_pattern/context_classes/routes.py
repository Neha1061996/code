from interface_strategy.routes import RoutesStrategy


class RouteContext:

    def __init__(self, route_through: RoutesStrategy):
        self.route_through = route_through

    def set_route_through(self, route_through: RoutesStrategy):
        self.route_through = route_through

    def get_routes(self, source, destination):
        self.route_through.get_routes(
            source, destination
        )