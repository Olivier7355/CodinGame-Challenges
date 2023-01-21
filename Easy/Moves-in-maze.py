# https://www.codingame.com/ide/puzzle/moves-in-maze
# Does not pass validator test 6

maze = []
goals = []
alphabet = ['0','1','2','3','4','5','6','7','8','9','A','B',
            'C','D','E','F','G','H','I','J','K','L','M','N',
            'O','P','Q','R','S','T','W','X','Y','Z']
offsets = {
    "right": (1, 0),
    "left": (-1,0),
    "up": (0,-1),
    "down": (0,1)
}

def is_legal_pos(maze, pos):
    i, j = pos
    return maze[j][i] != "#"

def get_path(predecessors, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = predecessors[current]
    path.append(start)
    path.reverse()
    return path

def bfs(maze, start, goal):
    queue = [] # Create the queue
    queue.append(start) # Add the start position to the queue
    predecessors = {start: None} # The dict will contains all the paths 

    while queue:
        current_cell = queue[0] # First element of the queue
        del queue[0] # delete first element of the queue
        
        # The path has been found
        if current_cell == goal:
            return get_path(predecessors, start, goal)
        
        for direction in ["up", "right", "down", "left"]:
            row_offset, col_offset = offsets[direction]
            
            if (current_cell[0] + col_offset > w-1) :
                neighbour = ((current_cell[0] + col_offset) - w, current_cell[1] + row_offset)                
            elif (current_cell[0] + col_offset < 0) :
                neighbour = ((current_cell[0] + col_offset) + w, current_cell[1] + row_offset)  
            elif (current_cell[1] + row_offset > h-1) :
                neighbour = (current_cell[0] + col_offset, (current_cell[1] + row_offset) - h)
            elif (current_cell[1] + row_offset < 0) :
                neighbour = (current_cell[0] + col_offset, (current_cell[1] + row_offset) + h)
            else :
                neighbour = (current_cell[0] + col_offset, current_cell[1] + row_offset)
            
            if is_legal_pos(maze, neighbour) and neighbour not in predecessors:
                queue.append(neighbour)
                predecessors[neighbour] = current_cell
    return None

w, h = [int(i) for i in input().split()]
for i in range(h):
    row = list(input())
    maze.append(row)

for y in range(h):
    for x in range(w):

        # Search the X,Y of the start position
        if maze[y][x] == 'S' : start_pos = (x, y)

        # Search the X,Y of all the goals (.)
        elif maze[y][x] == '.' : goals.append((x,y))

for pos in goals:
    goal_pos = pos
    result = bfs(maze, start_pos, goal_pos)
    if result : maze[goal_pos[1]][goal_pos[0]] = alphabet[(len(result)-1)]
    else : maze[goal_pos[1]][goal_pos[0]] = '.'

maze[start_pos[1]][start_pos[0]] = '0'
for i in range(len(maze)) :
    print(''.join(maze[i]))
