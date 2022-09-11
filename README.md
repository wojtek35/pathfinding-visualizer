A pathfinding vizualizer app in Python.

The program utilizes the A\* algorithm to find the shortest path between two points with obstacles between them.
A\* is an informed search algorithm with means the algorithm doesn't onlyt brute-force every single path but it utilizes a heuristic function that helps to guide the algorithm. The algorithm considers only the most optimal (the shortest path).

H(n) score - absolute distance
G(n) - current shortest distance
F(n) = G(n) + H(n)

| Node          | F             | G          | H           | Last           |
| ------------- | ------------- | -----------| ----------- | -----------    |
| A             | Content Cell  |            |             |                |
| B             | Content Cell  |            |             |                |
| C             | Content Cell  |            |             |                |
