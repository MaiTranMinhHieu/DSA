# bai19.py
import heapq

def shortest_path_grid(grid):
    rows, cols = len(grid), len(grid[0])
    dist = [[float('inf')] * cols for _ in range(rows)]
    dist[0][0] = grid[0][0]
    pq = [(grid[0][0], 0, 0)]
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while pq:
        d, r, c = heapq.heappop(pq)
        
        if d > dist[r][c]: continue
        if r == rows - 1 and c == cols - 1: return d
            
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                new_dist = d + grid[nr][nc]
                if new_dist < dist[nr][nc]:
                    dist[nr][nc] = new_dist
                    heapq.heappush(pq, (new_dist, nr, nc))
                    
    return -1

if __name__ == "__main__":
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    print(f"Chi phi nho nhat tren luoi: {shortest_path_grid(grid)}")