import json

def load_data():
    with open("data/locations.json") as f:
        locations = json.load(f)
        print(f"Loaded {len(locations)} locations.")
    with open("data/time_windows.json") as f:
        time_windows = json.load(f)
        print(f"Loaded {len(time_windows)} time windows.")
    with open("data/demands.json") as f:
        demands = json.load(f)
        print(f"Loaded {len(demands)} demands.")
    with open("data/pickup_delivery_pairs.json") as f:
        pairs = json.load(f)
        print(f"Loaded {len(pairs)} pickup/delivery pairs.")

    return {
        "locations": locations,
        "time_windows": time_windows,
        "demands": demands,
        "pickup_delivery_pairs": pairs
    }