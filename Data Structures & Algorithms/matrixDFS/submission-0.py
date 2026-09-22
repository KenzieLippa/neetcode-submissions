class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        visited = set()
        ROW = len(grid)
        COL = len(grid[0])
        def visit(r,c):
            #base case out of bounds
            if min(r,c) < 0 or r == ROW or c == COL or grid[r][c] ==1 or (r,c) in visited:
                return 0
            #success case
            if r == ROW-1 and c == COL-1:
                return 1
            
            count = 0
            visited.add((r,c))
            count += visit(r+1, c)
            count += visit(r-1, c)
            count += visit(r, c+1)
            count += visit(r, c-1)
            visited.remove((r,c))
            return count


        return visit(0,0)
        