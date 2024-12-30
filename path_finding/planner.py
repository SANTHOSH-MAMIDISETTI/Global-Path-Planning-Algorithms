import numpy as np
import yaml
import cv2 as cv

with open("params.yaml", "r") as f:
    params = yaml.safe_load(f)

method = params["method"]
start = params["start"]
goal = params["goal"]
map_name = params["map"]

if method == "astar":
    from astar import get_path
if method == "djikstras":
    from djikstras import get_path
if method == "rrt":
    from RRT import get_path

if __name__=="__main__":
    img = cv.imread(f"{map_name}.png", cv.IMREAD_GRAYSCALE)
    ret, map = cv.threshold(img,127,1,cv.THRESH_BINARY_INV)

    path = get_path(map)
    print(path)