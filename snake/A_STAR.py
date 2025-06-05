from Algorithm import Algorithm


class A_STAR(Algorithm):
    def __init__(self, grid):
        super().__init__(grid)

    def run_algorithm(self, snake):
        # clear everything
        self.frontier = []
        self.explored_set = []
        self.path = []

        initialstate, goalstate = self.get_initstate_and_goalstate(snake)

        # open list
        self.frontier.append(initialstate)

        # while we have states in open list
        while len(self.frontier) > 0:
            min_index = 0
            for i in range(len(self.frontier)):
                if self.frontier[i].f < self.frontier[0].f:
                    min_index = i

            min_node = self.frontier.pop(min_index)

            if min_node.equal(goalstate):
                return self.get_path(min_node)

            self.explored_set.append(min_node)
            adjacent_nodes = self.get_neighbors(min_node)

            for adj in adjacent_nodes:
                if self.inside_body(snake, adj) or self.outside_boundary(adj) or adj in self.explored_set:
                    continue

                g = min_node.g + 1

                if adj not in self.frontier:
                    adj.h = self.manhattan_distance(goalstate, adj)
                    self.frontier.append(adj)
                    adj.parent = min_node
                    adj.g = g
                    adj.f = adj.g + adj.h
                elif g < adj.g:
                    adj.parent = min_node
                    adj.g = g
                    adj.f = adj.g + adj.h

        return None
