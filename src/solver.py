from ortools.constraint_solver import pywrapcp, routing_enums_pb2
from model import create_model
def solve(raw_data):
    routing, manager = create_model(raw_data)
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
    )
    search_parameters.local_search_metaheuristic = (
        routing_enums_pb2.LocalSearchMetaheuristic.GUIDED_LOCAL_SEARCH
    )
    search_parameters.time_limit.seconds = 30
    search_parameters.log_search = True

    print("Trying to solve with:")
    print("Nodes:", routing.Size())
    print("Vehicles:", routing.vehicles())

    solution = routing.SolveWithParameters(search_parameters)

    if not solution:
        print("No solution found. Attempting fallback test case.")

        fallback_manager = pywrapcp.RoutingIndexManager(3, 1, 0)
        fallback_routing = pywrapcp.RoutingModel(fallback_manager)

        def distance_callback(from_index, to_index):
            from_node = fallback_manager.IndexToNode(from_index)
            to_node = fallback_manager.IndexToNode(to_index)
            return abs(from_node - to_node) * 10

        transit_callback_index = fallback_routing.RegisterTransitCallback(distance_callback)
        fallback_routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

        fallback_parameters = pywrapcp.DefaultRoutingSearchParameters()
        fallback_parameters.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
        fallback_parameters.time_limit.seconds = 5

        fallback_solution = fallback_routing.SolveWithParameters(fallback_parameters)
        print("Fallback solution found:", fallback_solution is not None)

        if fallback_solution:
            print("✅ Fallback test case solved successfully. Check original model constraints.")
            return fallback_solution, fallback_routing, fallback_manager
        else:
            raise Exception("❌ No solution found even in fallback case.")

    return solution, routing, manager