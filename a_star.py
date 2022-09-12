from queue import PriorityQueue
from tokenize import Triple
import pygame

'''
    The algorithm uses a PriorityQueue data structure which can be represented as the following loop:

    student = []
    student.append((5, 'Nick'))
    student.append((1, 'Rohan'))
    student.append((3, 'Jack'))
    student.sort(reverse=True)
    while student:
        t = student.pop()
        print(t)

    Output:  “ (1, 'Rohan') (3, 'Jack') (5, 'Nick')

    Instead of dequeuing the oldest element, PriorityQueue sorts and dequeues elements based on their priorities
    .get() method returns the element with the lowest priority
    In this case - f(n) score 
'''


def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()


def a_star(draw, grid, start, end):
    # 'count' keeps track of when nodes were inserted to the queue in case of when
    # we have two nodes in the queue with the same f(n) score
    # we can determine which node to take out when we have two nodes with the same f(n) score
    count = 0
    open_set = PriorityQueue()
    # .put() adds a note to the queue
    open_set.put(
        (0, count, start)  # We add a start node with f(n) = 0 to to open set
    )
    # came_from keeps track of after which node the current node came so we can determine the path
    came_from = {}
    g_score = {node: float("inf") for row in grid for node in row}
    g_score[start] = 0

    f_score = {node: float("inf") for row in grid for node in row}
    f_score[start] = h(start.get_pos(), end.get_pos())

    # This set hold the same data as the PriorityQueue(). It is needed becasue you can't check if an item is in the PriorityQueue and you can check it in a set
    open_set_hash = {start}

    # If the open set is empty it means that we considered every possible node and the algorithm hasn't found the path yet that means the path doesnt exist
    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # [2] gets the node object from the tuple (f, count, node)
        current = open_set.get()[2]
        # Synchronize the open_set_hash with open_set
        open_set_hash.remove(current)

        # If the current node is the end node then we found the shortest path
        if current == end:
            # Reconstruct the optimal path
            reconstruct_path(came_from, end, draw)
            end.make_end()
            return True

        for neighbor in current.neighbors:
            # g_score of neighbors is + 1 becasuse it is the g_score of current (distance from start to current) and in this case all of the neighbors are 1 block away from the current node
            temp_g_score = g_score[current] + 1
            # In the first step - if g_score[current] + 1 < inf
            # If for any of the neighbors, the temp_g_score - their assumed g_score is less then their actual g_score in the table then update their g_score cause we found a better path
            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                # Calculate the f_score from temp_g_score and h_score
                f_score[neighbor] = temp_g_score + \
                    h(neighbor.get_pos(), end.get_pos())
                # Add the neighbour to the set and on the next iteration the set will dequeue the node with the lowest f_score and consider it first
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()
        draw()

        if current != start:
            current.make_closed()

    return False


def h(p1, p2):
    # points will be tuples
    # Manhattan Distance
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)
