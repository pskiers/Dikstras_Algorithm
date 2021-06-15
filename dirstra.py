
def extract_minimum(queue, cost):
    co_q = {cost[x][y]: (x, y) for x, y in queue}
    return co_q[min(co_q.keys())]



def dikstra(graph):
    height = len(graph)
    width = len(graph[0])
    nodes_checked = []      # if nodes_checked[n][m] == 1 then and only then node (n,m) was already checked
    path = []               # path[n][m] represents from which node (like a clock 12-from node above, 3-from node on the right, 6 from node below, 9-from node on the left) do you get to this node if you follow the shortest way.
    cost = []

    for _ in range(height):
        row = [False for _ in range(width)]
        nodes_checked.append(row)
        row_pth = [0 for _ in range(width)]
        path.append(row_pth)
        rows_costs = [-1 for _ in range(width)]
        cost.append(rows_costs)

    starting = (0,0)
    queue = []
    for i in range(height):
        for j in range(width):
            if int(graph[i][j]) == 0:
                starting = (i,j)
                queue = [(i,j)]
                cost[i][j] = 0
                break
        if len(queue) != 0:
            break

    while len(queue) != 0:
        i,j = extract_minimum(queue, cost)
        to_relax = [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]
        for node in to_relax:
            m, n = node
            if height > m >= 0 and width > n >= 0:
                if cost[m][n] == -1 or cost[m][n] > cost[i][j] + int(graph[m][n]):
                    cost[m][n] = cost[i][j] + graph[m][n]
                    path[m][n] = i, j
                    if nodes_checked[m][n] is False:
                        queue.append((m,n))
        nodes_checked[i][j] = True
        queue.remove((i, j))

    best_path = []
    end_of_path = (-1, -1)
    for _ in range(height):
        row = [False for _ in range(width)]
        best_path.append(row)
    for i in range(height):
        for j in range(width):
            if int(graph[i][j]) == 0 and (i, j) != starting:
                end_of_path = (i,j)
                break
        if end_of_path != (-1, -1):
            break
    best_path[starting[0]][starting[1]] = True
    while end_of_path != 0:
        i, j = end_of_path
        best_path[i][j] = True
        end_of_path = path[i][j]

    to_print = ''
    for i in range(height):
        for j in range(width):
            if best_path[i][j] is True:
                to_print += str(graph[i][j])
                to_print += ' '
            else:
               to_print += '  '
        to_print += '\n'
    return to_print


gr = [[1,1,1,1,2,2],[1,0,4,1,2,2],[9,4,2,1,1,1],[9,9,6,4,1,1],[9,9,0,4,1,1],[9,9,1,1,1,1]]
print(dikstra(gr))
