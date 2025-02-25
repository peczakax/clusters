from geometry import Point, Circle

def get_input_mode_from_input(item_type):
    while True:
        mode = input(f"Choose input mode for {item_type} (1 for random, 2 for manual): ").strip()
        if mode in ['1', '2']:
            return mode
        print("Please enter either 1 or 2")

def get_number_of_transmitters_from_input():
    while True:
        try:
            n = int(input("Enter the number of transmitters: "))
            if 1 <= n:
                return n
            print("Please enter a number greater or equal 1")
        except ValueError:
            print("Please enter a valid integer")

def get_point_coordinates_from_input(point_name):
    print(f"\nEnter coordinates for {point_name} point:")
    x = get_valid_float_from_input("X coordinate: ")
    y = get_valid_float_from_input("Y coordinate: ")
    return Point(x, y)

def get_points_from_input(n):
    points = []
    for i in range(n):
        point = get_point_coordinates_from_input(f"point {i+1}")
        points.append(point)
    return points

def get_valid_float_from_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if 0 <= value:
                return value
            print(f"Please enter a value greater or equal 0")
        except ValueError:
            print("Please enter a valid number")

def get_transmitter_parameters_from_input(circle_num):
    print(f"\nEnter parameters for transmitter {circle_num}:")
    x = get_valid_float_from_input("X coordinate: ")
    y = get_valid_float_from_input("Y coordinate: ")
    p = get_valid_float_from_input("Power: ")
    return Circle(x, y, p)

def generate_random_circles(n):
    import random
    circles = []
    for _ in range(n):
        x = random.uniform(10, 90)
        y = random.uniform(10, 90)
        r = random.uniform(1, 10)
        circles.append(Circle(x, y, r))
    return circles

def generate_random_points(n):
    import random
    points = []
    for _ in range(n):
        x = random.uniform(10, 90)
        y = random.uniform(10, 90)
        points.append(Point(x, y))
    return points

def create_circles(n):
    mode = get_input_mode_from_input("transmitter")
    return generate_random_circles(n) if mode == '1' else [get_transmitter_parameters_from_input(i + 1) for i in range(n)]

def create_points(n):
    mode = get_input_mode_from_input("points")
    return generate_random_points(n) if mode == '1' else get_points_from_input(n)
