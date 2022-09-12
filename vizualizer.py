from platform import python_branch
import pygame

from a_star import a_star

WIDTH = 800
# Set up the display size
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Pathfinding Algorithm")

# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GRAY = (128, 128, 128)
TURQUOISE = (64, 224, 208)


class Node:
    '''
    WHITE - a node that wasn't yet visited
    RED - it has been visited
    BLACK - a barrier
    ORANGE - the start node
    TORQUOISE - the end node
    PURPLE - path
    '''

    def __init__(self, row, col, node_width, total_rows):
        self.row = row
        self.col = col
        self.x = row * node_width
        self.y = col * node_width
        self.color = WHITE
        self.neighbors = []
        self.node_width = node_width
        self.total_rows = total_rows

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.color == RED

    def is_open(self):
        return self.color == GREEN

    def is_barrier(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == ORANGE

    def is_end(self):
        return self.color == TURQUOISE

    def reset(self):
        self.color = WHITE

    def make_closed(self):
        self.color = RED

    def make_open(self):
        self.color = GREEN

    def make_barrier(self):
        self.color = BLACK

    def make_start(self):
        self.color = ORANGE

    def make_end(self):
        self.color = TURQUOISE

    def make_path(self):
        self.color = PURPLE

    def draw(self, win):
        pygame.draw.rect(
            win, self.color, (self.y, self.x, self.node_width, self.node_width))

    def update_neighbors(self, grid):
        self.neighbors = []
        # First row and col are (0,0) so for ROWS = 50 the last row is 49
        # If the current node row(y) is at least one less then the last row (49) AND the next node down IS NOT a barrier:
        # DOWN
        if self.row < self.total_rows - 1 and not grid[self.row+1][self.col].is_barrier():
            # We add that node as the neighbor BELOW the current node
            self.neighbors.append(grid[self.row+1][self.col])
        # UP
        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():
            # We add that node as the neighbor ABOVE the current node
            self.neighbors.append(grid[self.row - 1][self.col])

        # RIGHT
        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier():
            # We add that node as the neighbor TO THE RIGHT of the current node
            self.neighbors.append(grid[self.row][self.col + 1])

        # LEFT
        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():
            # We add that node as the neighbor TO THE LEFT of the current node
            self.neighbors.append(grid[self.row][self.col - 1])

    def show_neighbors(self):
        for neingbor in self.neighbors:
            print("Pos:\n " + "row:" + str(neingbor.row) +
                  '  col: ' + str(neingbor.col))
        print(self.neighbors)

    def __lt__(self, other):
        # __lt__ - less than
        return False


def make_grid(rows, width):
    grid = []
    gap = width // rows
    cols = rows
    for row in range(rows):
        grid.append([])
        for col in range(cols):
            node = Node(row, col, gap, rows)
            grid[row].append(node)
    return grid


def draw_grid(win, rows, width):
    gap = width // rows
    for y in range(rows):
        # We draw horizontal lines
        pygame.draw.line(win, GRAY, (0, y * gap), (width, y * gap))
    for x in range(rows):
        # We draw vertical lines
        pygame.draw.line(win, GRAY, (x * gap, 0), (x * gap, width))


def draw(win, grid, rows, width):
    win.fill(WHITE)  # Make the background white

    # For each row in the grid, make every node draw itself
    for row in grid:
        for node in row:
            node.draw(win)
    draw_grid(win, rows, width)  # Draw the lines
    pygame.display.update()  # Update the screen


def get_clicked_pos(pos, rows, width):
    node_width = width // rows  # Ex. 800/50 = 16px
    x, y = pos
    col = x // node_width
    row = y // node_width

    return row, col


def main(win, width):
    ROWS = 50
    grid = make_grid(ROWS, WIDTH)

    start = None
    end = None

    run = True

    while run:
        draw(win, grid, ROWS, width)  # Redraw the screen at every frame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]:  # LEFT MOUSE BUTTON
                pos = pygame.mouse.get_pos()  # Get mouse pos

                # Rows - y, cols - x
                # Determine which row and which col the mouse click was at,
                row, col = get_clicked_pos(pos, ROWS, width)

                # We extract the node at certain row(y) and col(x)
                node = grid[row][col]

                # node.show_neighbors()
                if not start and node != end:
                    start = node
                    start.make_start()

                elif not end and node != start:
                    end = node
                    end.make_end()

                elif node != end and node != start:
                    node.make_barrier()

            elif pygame.mouse.get_pressed()[2]:  # RIGHT MOUSE BUTTON
                pos = pygame.mouse.get_pos()
                if node == start:
                    start = None
                elif node == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    # Update neighbors for all nodes
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)
                    a_star(lambda: draw(win, grid, ROWS, width),
                           grid, start, end)

                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid(ROWS, WIDTH)

    pygame.quit()


main(WIN, WIDTH)
