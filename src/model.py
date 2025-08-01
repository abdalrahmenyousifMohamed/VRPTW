from ortools.constraint_solver import pywrapcp
from distance_matrix import compute_euclidean_matrix

def create_model(data):
    print("Creating routing model...")
    print("Number of locations:", len(data["locations"]))
    print("Number of vehicles:", data["num_vehicles"])
    print("Depot location:", data["depot"])

    # ✅ FIXED: Don't add extra dummy nodes
    manager = pywrapcp.RoutingIndexManager(
        len(data["locations"]),
        data["num_vehicles"],
        data["depot"]
    )
    routing = pywrapcp.RoutingModel(manager)

    distance_matrix = compute_euclidean_matrix(data["locations"])

    def time_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return distance_matrix[from_node][to_node]

    transit_index = routing.RegisterTransitCallback(time_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_index)

    # Add Time Windows
    routing.AddDimension(
        transit_index,
        30,    # slack
        1000,   # maximum time per vehicle
        False,
        "Time")
    time_dimension = routing.GetDimensionOrDie("Time")
    for idx, (start, end) in enumerate(data["time_windows"]):
        index = manager.NodeToIndex(idx)
        time_dimension.CumulVar(index).SetRange(start, end)

    # Add Demand callback
    def demand_callback(from_index):
        from_node = manager.IndexToNode(from_index)
        return data["demands"][from_node]

    demand_index = routing.RegisterUnaryTransitCallback(demand_callback)
    routing.AddDimensionWithVehicleCapacity(
        demand_index,
        0,
        [data["vehicle_capacity"]] * data["num_vehicles"],
        True,
        "Capacity")

    # Pickup and Delivery
    # for pickup, delivery in data["pickup_delivery_pairs"]:
    #     pickup_index = manager.NodeToIndex(pickup)
    #     delivery_index = manager.NodeToIndex(delivery)
    #     routing.AddPickupAndDelivery(pickup_index, delivery_index)
    #     routing.solver().Add(
    #         routing.VehicleVar(pickup_index) == routing.VehicleVar(delivery_index))
    #     routing.solver().Add(
    #         time_dimension.CumulVar(pickup_index) <= time_dimension.CumulVar(delivery_index))
    # Pickup and Delivery (with validation)
    # for pickup, delivery in data["pickup_delivery_pairs"]:
    #     if pickup == delivery:
    #         print(f"❌ Skipping invalid pair: pickup = delivery = {pickup}")
    #         continue
    #     if pickup >= len(data["locations"]) or delivery >= len(data["locations"]):
    #         print(f"❌ Skipping out-of-range pair: ({pickup}, {delivery})")
    #         continue

    #     pickup_index = manager.NodeToIndex(pickup)
    #     delivery_index = manager.NodeToIndex(delivery)

    #     print(f"✅ Adding pickup/delivery pair: {pickup} → {delivery}")

    #     routing.AddPickupAndDelivery(pickup_index, delivery_index)
    #     routing.solver().Add(
    #         routing.VehicleVar(pickup_index) == routing.VehicleVar(delivery_index))
    #     routing.solver().Add(
    #         time_dimension.CumulVar(pickup_index) <= time_dimension.CumulVar(delivery_index))


    return routing, manager