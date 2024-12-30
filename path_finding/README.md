# Global Path Planning Algorithms

This project involves implementing three global path planning algorithms: Dijkstra's Algorithm, A* Algorithm, and Rapidly Exploring Random Tree (RRT). The goal is to compute the shortest path in a 2D binary grid representing a complete map of the world.

## Objectives

* Implement Dijkstra's Algorithm for shortest path computation.
* Implement A* Algorithm with a Euclidean heuristic.
* Implement Rapidly Exploring Random Tree (RRT) for fast path planning.

## File Structure

```
path_finding
├── planner.py         # Driver file for testing algorithms
├── astar.py           # Implementation of A* Algorithm
├── djikstras.py       # Implementation of Dijkstra's Algorithm
├── RRT.py             # Implementation of RRT Algorithm
├── map1.png           # First test map
├── map2.png           # Second test map
└── params.yaml        # Configuration file with start, goal, and method details
```

## Requirements

* Python libraries: numpy, collections, os, math, matplotlib
* Each algorithm returns the path as a list of tuples from the start to the goal.
* Paths avoid obstacles but can touch walls.

## Implementation Details

### Dijkstra's Algorithm

* Computes the shortest path based on the cost to reach each node.
* Handles ties in cost randomly.
* Uses a priority queue sorted by cost.
* Distance to horizontal neighbors is 1; to diagonal neighbors is sqrt(2).

### A* Algorithm

* Builds upon Dijkstra's with an added heuristic (Euclidean distance) to guide the search.
* Distance metrics are the same as Dijkstra's.

### RRT

![RRT](images/rrt.png)

* Explores the space using a tree of random nodes.
* Terminates if a direct obstacle-free connection to the goal is found.
* Uses Euclidean distance to find the nearest node.

## Resources

* A*, Dijkstra's: [LaValle - Planning Algorithms](https://lavalle.pl/planning/ch2.pdf) (Sections 2.2.2 and 2.3.3)
* RRT Overview: [YouTube Video](https://www.youtube.com/watch?v=QR3U1dgc5RE&t=955s)
* RRT Visualized: [YouTube Video](https://www.youtube.com/watch?v=Ob3BIJkQJEw)
* RRT: [https://docs.ros.org/en/noetic/api/sensor_msgs/html/msg/LaserScan.html](https://www.youtube.com/watch?v=QR3U1dgc5RE&t=955s)

## Features

* Algorithms designed for large-scale grid maps.
* Modular implementation for easy testing and reuse.
* Visualization support with matplotlib.

## Final Notes

This repository reflects work focused on the implementation and testing of robust path planning algorithms. All components were developed and organized to facilitate future enhancements and broader applications in robotics and automation.
