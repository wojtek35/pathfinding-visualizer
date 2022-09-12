A pathfinding visualizer app in Python.

The program utilizes the A\* algorithm to find the shortest path between two points with obstacles between them.
A\* is an informed search algorithm with means the algorithm doesn't only brute-force every single path but utilizes a heuristic function that helps to guide the algorithm. The algorithm considers only the most optimal (the shortest path).

H(n) score - a guess of the path distance based on the distance between the 'n' node and the end node.
Heuristic function - it is only a guess based because there can be all sorts of obstacles in the path that we won't know until the algorithm is finished.
In this case, the distance will be estimated based on the 'Manhattan distance' which is the sum of absolute values of differences on the end node s x and y coordinates and the current node x and y coordinates
h = abs(current_node.x - end_node.x) + abs(current_node.y - end_node.y)
This heuristic function should only be used then we are allowed to move in only four directions (right, left, top, bottom) which fits this example perfectly)

G(n) - the current shortest path from the start node to the 'n' node
\n
F(n) = G(n) + H(n)
What does F(n) represent? Let's consider 3 points A, B and C. A is the starting node. C is the ending node and B is the node in between them. F(B) represents a 'score' composed of two components. We have already gone X blocks from A to B (G(B)) and from this node, we guess (based on the H(n)) that the path to the C node is Y blocks. If instead of node B we had many nodes - the algorithm would choose the node with the lowest F(n) score as the next node.

1. First left mouse click will add the start node on the screen (orange)
2. Second left mouse click will add the end mode on the screen (turquoise)
3. After that left mouse clicks will add the barriers
4. You can delete the nodes with right mouse click
5. Start the algorithm by hitting SPACE
6. Clear the grid by hitting the C key

![](https://github.com/wojtek35/pathfinding-visualizer/blob/master/video.gif)
