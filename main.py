# Code was written with Python 3.12
# Required libraries: matplotlib, numpy
# Author: Andrzej Pęczak

from input_handlers import get_number_of_transmitters_from_input, create_circles, create_points
from clustering import find_clusters, check_pair_cluster_intersection
from visualization import visualize

if __name__ == "__main__":
    clusters = find_clusters(create_circles(get_number_of_transmitters_from_input()))
    start, end = create_points(n=2)
    shared_cluster = check_pair_cluster_intersection((start, end), clusters)
    
    if shared_cluster:
        print("Safe flight is possible.")
    else:
        print("Safe flight is not possible.")
    
    visualize(clusters, (start, end, shared_cluster))
