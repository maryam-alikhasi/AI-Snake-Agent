from abc import ABC, abstractmethod
from Constants import NO_OF_CELLS, BANNER_HEIGHT
from Utility import Node
import math


class Algorithm(ABC):

    def __init__(self, grid):
        self.grid = grid
        self.frontier = []
        self.explored_set = []
        self.path = []

    def get_initstate_and_goalstate(self, snake):
        return Node(snake.get_x(), snake.get_y()), Node(snake.get_fruit().x, snake.get_fruit().y)

    def manhattan_distance(self, nodeA, nodeB):
        x1, y1 = nodeA.x, nodeA.y
        x2, y2 = nodeB.x, nodeB.y
        answer = abs(x1 - x2) + abs(y1 - y2)
        return answer

    def euclidean_distance(self, nodeA, nodeB):
        x1, y1 = nodeA.x, nodeA.y
        x2, y2 = nodeB.x, nodeB.y
        answer = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        return answer

    @abstractmethod
    def run_algorithm(self, snake):
        pass

    def get_path(self, node):
        if node.parent == None:
            return node

        while node.parent.parent != None:
            self.path.append(node)
            node = node.parent
        return node

    def inside_body(self, snake, node):
        for body in snake.body:
            if body.x == node.x and body.y == node.y:
                return True
        return False

    def outside_boundary(self, node):
        if not 0 <= node.x < NO_OF_CELLS:
            return True
        elif not BANNER_HEIGHT <= node.y < NO_OF_CELLS:
            return True
        return False

    def get_neighbors(self, node):
        i = int(node.x)
        j = int(node.y)

        neighbors = []
        # left [i-1, j]
        if i > 0:
            neighbors.append(self.grid[i-1][j])
        # right [i+1, j]
        if i < NO_OF_CELLS - 1:
            neighbors.append(self.grid[i+1][j])
        # top [i, j-1]
        if j > 0:
            neighbors.append(self.grid[i][j-1])

        # bottom [i, j+1]
        if j < NO_OF_CELLS - 1:
            neighbors.append(self.grid[i][j+1])

        return neighbors
