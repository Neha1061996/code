from concrete_implementation.routes import CarRoute, BikeRoute, WalkRoute
from context_classes.routes import RouteContext


def make_route():
    context = RouteContext(CarRoute())
    context.get_routes("Home", "Office")

    context.set_route_through(BikeRoute())
    context.get_routes("home", "market")

    context.set_route_through(WalkRoute())
    context.get_routes("park", "home")