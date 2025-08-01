import math

def compute_euclidean_matrix(locations):
    matrix = []
    for from_node in locations:
        row = []
        for to_node in locations:
            dist = math.hypot(
                from_node[0] - to_node[0],
                from_node[1] - to_node[1]
            )
            row.append(int(dist))
        matrix.append(row)
    return matrix