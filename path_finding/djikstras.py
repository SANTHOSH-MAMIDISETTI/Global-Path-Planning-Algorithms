import numpy as np
import heapq
import yaml

def dijkstra_path(image, start, end):
    rows, cols = image.shape
    distances = np.full((rows, cols), float('inf'))
    distances[start] = 0
    
    visited = np.zeros((rows, cols), dtype=bool)
    priority_queue = [(0, start)]
    previous = {start: None}

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0),   
                  (1, 1), (1, -1), (-1, 1), (-1, -1)]  
    
    while priority_queue:
        current_distance, current = heapq.heappop(priority_queue)
        if visited[current]:
            continue
        visited[current] = True
        
        if current == end:
            break
        
        for direction in directions:
            neighbor = (current[0] + direction[0], current[1] + direction[1])
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and not visited[neighbor]:
                if image[neighbor] == 255:
                    distance = current_distance + 1
                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        previous[neighbor] = current
                        heapq.heappush(priority_queue, (distance, neighbor))

    path = []
    current = end
    while current:
        path.append(current)
        current = previous.get(current)
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

    out = out * 255
    with open("params.yaml", "r") as f:
        params = yaml.safe_load(f)

    start = tuple(params["start"])
    goal = tuple(params["goal"])

    path = dijkstra_path(out, start, goal)
    # raise NotImplementedError
    return path