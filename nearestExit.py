from collections import deque
class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        """
        Algo:
        - this is straightforward application of finding a path to a valid boundary cell. 
        - Use BFS as we want to find the shortest exit.
        
        """
        maze_boundary = (len(maze),len(maze[0]))
        queue = deque()
        queue.append([entrance,0])
        print(queue)
        visited = {tuple(entrance)} # entrance is a list, we convert to tuple so we can use in a set
        
        while queue:
            current_cell, current_distance = queue.popleft()
            print('looking at ', current_cell, 'and visited', visited)
            #check if this is an exit
            current_row, current_column = current_cell[0], current_cell[1]
            # exits are when either row or column equal 0 or max value, we can't exit at entrance
            if (current_cell!=entrance) and ((current_row == maze_boundary[0]-1 or current_row==0) or (current_column==0 or current_column==maze_boundary[1]-1)):
                print('exit is at ',current_cell , 'with distance of ', current_distance)
                return current_distance
            # get the 4 possible neighbors up, down, left and right
            neighbors = [(current_row-1,current_column), (current_row+1,current_column),(current_row,current_column-1),(current_row,current_column+1)]
            for neighbor in neighbors:
                # check that this neighbor is not yet visited, is not a wall and is within the maze
                if (neighbor not in visited) and (neighbor[0] in range(maze_boundary[0])) and (neighbor[1] in range(maze_boundary[1])):
                    if (maze[neighbor[0]][neighbor[1]]!="+"):
                            visited.add(neighbor)
                            queue.append([neighbor,current_distance+1])
                            
        return -1


if __name__ == "__main__":
    solution=Solution()

    #test 1
    maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]]
    entrance = [1,2]
    result = solution.nearestExit(maze, entrance)
    assert result == 1

    #test2
    maze = [["+","+","+"],[".",".","."],["+","+","+"]]
    entrance = [1,0]
    assert solution.nearestExit(maze,entrance)== 2

    #test 3
    maze = [[".","+"]]
    entrance = [0,0]
    assert solution.nearestExit(maze,entrance) == -1