# -*- coding: utf-8 -*-
class Grid(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.f = 0
        self.g = 0
        self.h = 0
        self.parent = None

    def setGrid(self, parent, end):
        """Calculate g, h, f"""
        self.parent = parent
        if parent is not None:
            self.g = parent.g + 1
        else:
            self.g = 1
        self.h = abs(self.x - end.x) + abs(self.y - end.y)
        self.f = self.g + self.h


class AStar(object):
    def __init__(self, start, end, snake_body):
        self.start = start
        self.end = end
        self.open_list = [start]
        self.close_list = []
        self.snake_body = snake_body

    def aStarSearch(self):
        while len(self.open_list) > 0:
            # Set the square with the lowest f value to the current square
            current_grid = self.findMinGrid()
            # Removes the current square from self.open_list
            self.open_list.remove(current_grid)
            # Add the current square to the self.close_list
            self.close_list.append(current_grid)

            # Find the neighbor of the current grid
            neighbors = self.findNeighbors(current_grid)
            for grid in neighbors:
                if grid not in self.open_list:
                    # Unchecked, marked as father, added to self.open_list
                    grid.setGrid(current_grid, self.end)
                    self.open_list.append(grid)
            # The end is i=self.open_list, return~
            for grid in self.open_list:
                if (grid.x == self.end.x) and (grid.y == self.end.y):
                    return grid

        return None

    # The minimum f
    def findMinGrid(self):
        if self.open_list is None:
            self.open_list = []
        min_grid = self.open_list[0]
        for grid in self.open_list:
            if grid.f < min_grid.f:
                min_grid = grid

        return min_grid

    def findNeighbors(self, grid):
        if self.close_list is None:
            self.close_list = []
        if self.open_list is None:
            self.open_list = []

        neighbor_list = []
        if self.isValid(self.snake_body, grid.x, grid.y - 10):
            neighbor_list.append(Grid(grid.x, grid.y - 10))
        if self.isValid(self.snake_body, grid.x, grid.y + 10):
            neighbor_list.append(Grid(grid.x, grid.y + 10))
        if self.isValid(self.snake_body, grid.x - 10, grid.y):
            neighbor_list.append(Grid(grid.x - 10, grid.y))
        if self.isValid(self.snake_body, grid.x + 10, grid.y):
            neighbor_list.append(Grid(grid.x + 10, grid.y))

        return neighbor_list

    def isValid(self, snake_body: list[list], x: int, y: int) -> bool:
        if self.close_list is None:
            self.close_list = []
        if self.open_list is None:
            self.open_list = []

        if (x < -200 or x >= 200) or (y < -200 or y >= 200):
            return False
        if [x, y] in snake_body:
            return False
        if self.containGrid(self.open_list, x, y):
            return False
        if self.containGrid(self.close_list, x, y):
            return False

        return True

    @staticmethod
    def containGrid(grids: list, x: int, y: int) -> bool:
        for grid in grids:
            if (grid.x == x) and (grid.y == y):
                return True

        return False

    def pathFinding(self) -> list[list]:
        result_grid = self.aStarSearch()
        path = []
        while result_grid is not None:
            path.append([result_grid.x, result_grid.y])
            result_grid = result_grid.parent

        return path[::-1]
