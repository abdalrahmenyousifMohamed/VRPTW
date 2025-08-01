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
