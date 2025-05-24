class Solution(object):
    def shortestPath(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not grid or not grid[0]:
            return -1
        
        n, m = len(grid), len(grid[0])
        
        if k >= n + m - 2:
            return n + m - 2
        
        queue = deque([(0, 0, 0, 0)])
        
        visited = set()
        visited.add((0, 0, 0))
        
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        while queue:
            row, col, obstacles_used, steps = queue.popleft()
            
            if row == n - 1 and col == m - 1:
                return steps
            
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                
                if 0 <= new_row < n and 0 <= new_col < m:
                    new_obstacles_used = obstacles_used + grid[new_row][new_col]
                    
                    if new_obstacles_used <= k and (new_row, new_col, new_obstacles_used) not in visited:
                        visited.add((new_row, new_col, new_obstacles_used))
                        queue.append((new_row, new_col, new_obstacles_used, steps + 1))
        return -1

                
