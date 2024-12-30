import numpy as np
import math
import random
import yaml


class Node:
    """Class to store the RRT graph"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.parent = None

def dist_and_angle(x1, y1, x2, y2):
    dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    angle = math.atan2(y2 - y1, x2 - x1)
    return dist, angle

def nearest_node(nodes, x, y):
    distances = [dist_and_angle(node.x, node.y, x, y)[0] for node in nodes]
    return nodes[np.argmin(distances)]

def collision(binary_array, x1, y1, x2, y2):
    """Check for collision between two points in the binary array."""
    x = np.linspace(x1, x2, num=100)
    y = np.linspace(y1, y2, num=100)
    for i in range(len(x)):
        xi, yi = int(round(x[i])), int(round(y[i]))
        if binary_array[yi][xi] == 0:  # 0 indicates an obstacle
            return True
    return False

def rrt(binary_array, start, goal, step_size=10, max_iter=1000):
    height, width = binary_array.shape
    nodes = [Node(start[0], start[1])]

    for _ in range(max_iter):
        # Random point generation
        rand_x = random.randint(0, width - 1)
        rand_y = random.randint(0, height - 1)
        nearest = nearest_node(nodes, rand_x, rand_y)
        
        # Steer towards random point
        _, theta = dist_and_angle(nearest.x, nearest.y, rand_x, rand_y)
        new_x = int(nearest.x + step_size * math.cos(theta))
        new_y = int(nearest.y + step_size * math.sin(theta))

        if new_x < 0 or new_y < 0 or new_x >= width or new_y >= height:
            continue  # Ignore points outside bounds
        
        if not collision(binary_array, nearest.x, nearest.y, new_x, new_y):
            new_node = Node(new_x, new_y)
            new_node.parent = nearest
            nodes.append(new_node)

            # Check if goal is reached
            if not collision(binary_array, new_x, new_y, goal[0], goal[1]):
                goal_node = Node(goal[0], goal[1])
                goal_node.parent = new_node
                nodes.append(goal_node)
                return nodes

    return None  # Return None if no path is found

def extract_path(goal_node):
    path = []
    current = goal_node
    while current:
        path.append((current.x, current.y))
        current = current.parent
    path.reverse()
    return path


def get_path(grid: np.ndarray) -> list :

    out = []
    for i in grid:
        a = []
        for j in i:
            if j == 0:
                a.append(1)
            else:
                a.append(0)
        out.append(a)
    
    out = np.array(out)

    with open("params.yaml", "r") as f:
        params = yaml.safe_load(f)

    start = tuple(params["start"])
    goal = tuple(params["goal"])


    path = []

    nodes = rrt(out, start, goal, step_size=10)

    if nodes:
        goal_node = nodes[-1]
        path = extract_path(goal_node)
    
    return path
