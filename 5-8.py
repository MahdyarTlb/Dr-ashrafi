def solve_maze_simple(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    
    stack = [(start[0], start[1], [start])]
    visited = set([start])
    
    while stack:
        row, col, path = stack.pop()
        
        if (row, col) == end:
            return path
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if (0 <= new_row < rows and 0 <= new_col < cols and
                maze[new_row][new_col] == 0 and 
                (new_row, new_col) not in visited):
                
                visited.add((new_row, new_col))
                stack.append((new_row, new_col, path + [(new_row, new_col)]))
    
    return None