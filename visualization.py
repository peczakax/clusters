import matplotlib.pyplot as plt
import numpy as np
from geometry import calculate_cluster_boundaries, calculate_points_boundaries, combine_boundaries

def plot_clusters(clusters):
    colors = plt.cm.Set3(np.linspace(0, 1, len(clusters)))
    for i, cluster in enumerate(clusters):
        for circle in cluster:
            plt.gca().add_patch(plt.Circle((circle.x, circle.y), circle.r, color=colors[i], fill=True, alpha=0.3))
            plt.gca().add_patch(plt.Circle((circle.x, circle.y), circle.r, color=colors[i], fill=False, linewidth=2))

def plot_point_pair(point_data):
    start, end, shared_cluster = point_data
    start_x, start_y = start.x, start.y
    end_x, end_y = end.x, end.y
    
    # Determine marker style and prepare annotation text
    MARKER_STYLE = '+' 
    cluster_text = f" (same cluster: {shared_cluster})" if shared_cluster else " (different clusters)"
    
    # Plot points with black borders
    base_size = 10
    plt.plot(start_x, start_y, MARKER_STYLE, color='black', markersize=base_size+4, markeredgewidth=4)
    plt.plot(end_x, end_y, MARKER_STYLE, color='black', markersize=base_size+4, markeredgewidth=4)
    plt.plot(start_x, start_y, MARKER_STYLE, color='lightgreen', markersize=base_size+3, markeredgewidth=3)
    plt.plot(end_x, end_y, MARKER_STYLE, color='red', markersize=base_size+3, markeredgewidth=3)
    
    MARKER_STYLE = 'o'
    # Add annotations
    plt.annotate(f'Start{cluster_text}', xy=(start_x, start_y), 
                xytext=(7, 7), textcoords='offset points', 
                color='black')
    plt.annotate(f'End{cluster_text}', xy=(end_x, end_y), 
                xytext=(7, 7), textcoords='offset points', 
                color='black')

def visualize(clusters, processed_points):
    # Set up plot boundaries
    cluster_bounds = calculate_cluster_boundaries(clusters)
    point1, point2, shared_cluster = processed_points
    point_bounds = calculate_points_boundaries(point1, point2)
    min_x, max_x, min_y, max_y = combine_boundaries(cluster_bounds, point_bounds)
        
    # Configure plot
    plt.figure(figsize=(10, 10)) 
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xlim(min_x, max_x)
    plt.ylim(min_y, max_y)
    plt.grid(True, linestyle='--', alpha=0.7)
    title = f'Clusters (Total: {len(clusters)})'
    
    # Add information about flight safety to the title
    if shared_cluster:
        title += ' - Safe Flight Possible'
    else:
        title += ' - Safe Flight Not Possible'
    
    plt.title(title)

    # Plot elements
    plot_clusters(clusters)
    plot_point_pair(processed_points)

    plt.show()
