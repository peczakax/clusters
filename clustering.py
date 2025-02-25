from collections import defaultdict
from geometry import is_point_in_circle, are_circles_adjacent

def find_clusters(circles):
    clusters = []
    visited = set()
    
    # Precompute adjacency list
    adjacency = defaultdict(list)
    for i, c1 in enumerate(circles):
        for j, c2 in enumerate(circles):
            if i != j and are_circles_adjacent(c1, c2):
                adjacency[i].append(j)
    
    def dfs(start_index):
        cluster = []
        stack = [start_index]
        
        while stack:
            idx = stack.pop()
            if idx not in visited:
                visited.add(idx)
                cluster.append(circles[idx])
                
                for neighbor in adjacency[idx]:
                    if neighbor not in visited:
                        stack.append(neighbor)
        return cluster
    
    for i, circle in enumerate(circles):
        if i not in visited:
            cluster = dfs(i)
            clusters.append(cluster)
    
    return clusters

def check_pair_cluster_intersection(point_pair, clusters):
    start, end = point_pair

    # Iterate over clusters: if both points are in ANY of the cluster's circles then return.
    for i, cluster in enumerate(clusters):
        if any(is_point_in_circle(start, circle) for circle in cluster) and \
        any(is_point_in_circle(end, circle) for circle in cluster):
            return [i]
    return []
