from data_loader import load_data
from solver import solve
from visualizer import plot_routes

def main():
    raw_data = load_data()
    raw_data["num_vehicles"] = 6
    raw_data["depot"] = 0
    raw_data["vehicle_capacity"] = 30

    solution, routing, manager = solve(raw_data)

    if solution is None or routing.Size() < 5:
        print("❌ Could not find a valid solution or fallback used. Skipping plotting.")
        return

    try:
        plot_routes(raw_data, routing, manager, solution)
    except Exception as e:
        print("❌ Error during plotting or extracting solution:", str(e))

if __name__ == "__main__":
    main()