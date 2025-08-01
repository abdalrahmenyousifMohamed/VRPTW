import matplotlib.pyplot as plt

def plot_routes(data, routing, manager, solution):
    routes = []
    for vehicle_id in range(data["num_vehicles"]):
        index = routing.Start(vehicle_id)
        route = []
        while not routing.IsEnd(index):
            node = manager.IndexToNode(index)
            route.append(node)
            index = solution.Value(routing.NextVar(index))
        route.append(manager.IndexToNode(index))
        routes.append(route)

    colors = ['r', 'g', 'b', 'c', 'm']
    for i, route in enumerate(routes):
        coords = [data["locations"][node] for node in route]
        xs, ys = zip(*coords)
        plt.plot(xs, ys, marker='o', label=f"Vehicle {i}", color=colors[i % len(colors)])
    plt.legend()
    plt.title("Vehicle Routes")
    plt.savefig("results/route_plot.png")
    plt.show()
