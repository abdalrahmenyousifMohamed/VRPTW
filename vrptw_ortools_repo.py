# Directory structure (as Python comments)

# vrptw-capacity-pickup-delivery/
# ├── README.md
# ├── requirements.txt
# ├── .gitignore
# ├── data/
# │   ├── locations.json
# │   ├── time_windows.json
# │   ├── demands.json
# │   └── pickup_delivery_pairs.json
# ├── src/
# │   ├── main.py
# │   ├── data_loader.py
# │   ├── distance_matrix.py
# │   ├── model.py
# │   ├── solver.py
# │   └── visualizer.py
# ├── results/
# │   ├── routes_output.json
# │   ├── solution_summary.txt
# │   └── route_plot.png
# └── notebooks/
#     └── test_instance.ipynb

# ======================
# data/locations.json
# ======================
[
  [30, 40], [35, 45], [20, 60], [50, 30], [55, 20],
  [25, 65], [60, 25], [45, 50], [40, 60], [30, 30]
]

# ======================
# data/time_windows.json
# ======================
[
  [0, 300], [30, 100], [50, 150], [60, 180], [80, 200],
  [40, 120], [90, 220], [70, 160], [85, 190], [100, 240]
]

# ======================
# data/demands.json
# ======================
[0, -5, -6, -4, -3, 6, 5, 4, 3, 5]

# ======================
# data/pickup_delivery_pairs.json
# ======================
[
  [1, 5], [2, 6], [3, 7], [4, 8], [9, 5]
]

# ======================
# README.md
# ======================
# Vehicle Routing Problem with Time Windows and Pickups/Deliveries

This project solves a **Vehicle Routing Problem (VRP)** with the following constraints:
- **Time Windows**: Each customer must be serviced within a specific time range.
- **Vehicle Capacities**: Each vehicle can only carry a limited load.
- **Pickup & Delivery**: Each pickup node must precede its delivery, and both must be served by the same vehicle.

## 📁 Folder Structure
```
vrptw-capacity-pickup-delivery/
├── data/                 # Input data in JSON
├── results/              # Output routes, plots, summary
├── src/                  # Python source code
├── notebooks/            # Jupyter experiments
├── README.md
├── requirements.txt
```

## ⚙️ How It Works
- Data is read from JSON files: node locations, time windows, demands, and pickup-delivery pairs.
- Euclidean distances are computed as travel times.
- Google OR-Tools is used to:
  - Register callbacks for distance and demand
  - Add time and capacity dimensions
  - Enforce pickup-before-delivery
- The solution is visualized using matplotlib.

## ▶️ Run the Solver
```bash
pip install -r requirements.txt
python src/main.py
```

## 📦 Requirements
```
ortools
matplotlib
```

## 📈 Output
- **`route_plot.png`** shows the vehicle routes on a 2D map.
- **`solution_summary.txt`** (to be generated) will contain readable route info.

## 🔗 References
- [Google OR-Tools Routing Guide](https://developers.google.com/optimization/routing)
