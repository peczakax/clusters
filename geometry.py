from collections import namedtuple

# Define a Point named tuple
Point = namedtuple('Point', ['x', 'y'])

# Define a Circle named tuple
Circle = namedtuple('Circle', ['x', 'y', 'r'])

def is_point_in_circle(point, circle):
    px, py = point.x, point.y
    dx = px - circle.x
    dy = py - circle.y
    return dx * dx + dy * dy <= circle.r * circle.r

def are_circles_adjacent(circle1, circle2):
    dx = circle2.x - circle1.x
    dy = circle2.y - circle1.y
    sum_radii = circle1.r + circle2.r
    return dx * dx + dy * dy <= sum_radii * sum_radii

def calculate_cluster_boundaries(clusters):    
    # Initialize with first circle's bounds
    first_circle = clusters[0][0]
    min_x = first_circle.x - first_circle.r
    max_x = first_circle.x + first_circle.r
    min_y = first_circle.y - first_circle.r
    max_y = first_circle.y + first_circle.r
    
    # Find min/max considering all circles
    for cluster in clusters:
        for circle in cluster:
            min_x = min(min_x, circle.x - circle.r)
            max_x = max(max_x, circle.x + circle.r)
            min_y = min(min_y, circle.y - circle.r)
            max_y = max(max_y, circle.y + circle.r)
    
    return (min_x, max_x, min_y, max_y)

def calculate_points_boundaries(point1, point2):
    # Get coordinates from the processed point tuple
    start_x, start_y = point1.x, point1.y
    end_x, end_y = point2.x, point2.y
    
    # Find min/max for both points
    min_x = min(start_x, end_x)
    max_x = max(start_x, end_x)
    min_y = min(start_y, end_y)
    max_y = max(start_y, end_y)
    
    return (min_x, max_x, min_y, max_y)

def combine_boundaries(bounds1, bounds2):
    min_x1, max_x1, min_y1, max_y1 = bounds1
    min_x2, max_x2, min_y2, max_y2 = bounds2
    
    min_x = min(min_x1, min_x2)
    max_x = max(max_x1, max_x2)
    min_y = min(min_y1, min_y2)
    max_y = max(max_y1, max_y2)
    
    # Add 10% padding
    width = max_x - min_x
    height = max_y - min_y
    padding_x = width * 0.1
    padding_y = height * 0.1
    
    return (min_x - padding_x, max_x + padding_x, 
            min_y - padding_y, max_y + padding_y)
