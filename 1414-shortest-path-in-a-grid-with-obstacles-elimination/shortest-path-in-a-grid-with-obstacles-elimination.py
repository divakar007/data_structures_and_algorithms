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
        
        # Special case: if we can eliminate enough obstacles to go straight
        if k >= n + m - 2:
            return n + m - 2
        
        # BFS with state: (row, col, obstacles_eliminated, steps)
        queue = deque([(0, 0, 0, 0)])
        
        # visited set to track (row, col, obstacles_used) to avoid cycles
        visited = set()
        visited.add((0, 0, 0))
        
        # Directions: right, down, up, left
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        while queue:
            row, col, obstacles_used, steps = queue.popleft()
            
            # Check if we reached the destination
            if row == n - 1 and col == m - 1:
                return steps
            
            # Explore all 4 directions
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                
                # Check if new position is within bounds
                if 0 <= new_row < n and 0 <= new_col < m:
                    # Calculate obstacles used if we move to this cell
                    new_obstacles_used = obstacles_used + grid[new_row][new_col]
                    
                    # Check if we can still eliminate obstacles and haven't visited this state
                    if new_obstacles_used <= k and (new_row, new_col, new_obstacles_used) not in visited:
                        visited.add((new_row, new_col, new_obstacles_used))
                        queue.append((new_row, new_col, new_obstacles_used, steps + 1))
        
        # No path found
        return -1

                
