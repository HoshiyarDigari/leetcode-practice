class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        pass


if __name__ == "__main__":
    solution=Solution()
    maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]]
    entrance = [1,2]
    result = solution.nearestExit(maze, entrance)
    assert result == 1