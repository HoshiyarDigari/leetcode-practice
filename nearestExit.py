from collections import deque
class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        """
        Algo:
        - this is straightforward application of finding a path to a valid boundary cell. 
        - Use BFS as we want to find the shortest exit.
        
        """
        maze_rows = len(maze)
        maze_columns = len(maze[0])
        queue = deque()
        queue.append(entrance)
        print(queue, maze_rows , 'x', maze_columns)
        visited = {tuple(entrance)}
        while queue:
            current_cell = queue.popleft()
            print('looking at ', current_cell, 'and visited', visited)
            #check if this is an exit
            row, column = current_cell[0], current_cell[1]
            if (row == maze_rows-1 or row==0) or (column==0 or column==maze_columns-1):
                print('exit is at ',current_cell)
                break
            # get the 4 possible neighbors up, down, left and right
            neighbors = [(row-1,column), (row+1,column),(row,column-1),(row,column+1)]
            for neighbor in neighbors:
                if (neighbor not in visited) and (maze[neighbor[0]][neighbor[1]]!="+") and (neighbor[0]<maze_rows) and (neighbor[1] < maze_columns):
                            visited.add(neighbor)
                            queue.append(list(neighbor))



if __name__ == "__main__":
    solution=Solution()
    maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]]
    entrance = [1,2]
    result = solution.nearestExit(maze, entrance)
    assert result == 1