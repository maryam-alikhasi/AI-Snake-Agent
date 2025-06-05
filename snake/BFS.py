from collections import deque
from Utility import Node
from Algorithm import Algorithm


class BFS(Algorithm):
    def __init__(self, grid):
        super().__init__(grid)

    def run_algorithm(self, snake):
        # start clean
        self.frontier = deque([])
        self.explored_set = []
        self.path = []

        initialstate, goalstate = self.get_initstate_and_goalstate(snake)

        # open list
        self.frontier.append(initialstate)

        # while we have states in open list
        while len(self.frontier) > 0:
            current_node = self.frontier.popleft()
            self.explored_set.append(current_node)

            for adjacent in self.get_neighbors(current_node):
                if self.inside_body(snake, adjacent) or self.outside_boundary(adjacent):
                    self.explored_set.append(adjacent)
                    continue

                if adjacent not in self.frontier and adjacent not in self.explored_set:
                    adjacent.parent = current_node
                    self.explored_set.append(adjacent)
                    self.frontier.append(adjacent)

                    if adjacent.equal(goalstate):
                        return self.get_path(adjacent)

        return None
