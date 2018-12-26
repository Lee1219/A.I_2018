count_BFS = 0
length = 0
time = 0
row = 0
col = 0

class position:
    def __init__(self, name, path):
        self.name = name
        self.path = path

def find_start(maze, row, col):
    for i in range(col):
        if maze[0][i] == '3':
            return tuple([0, i])
    return None

def find_end(maze, row, col):
    for i in range(col):
        if maze[row-1][i] == '4':
            return tuple([row-1, i])
    return None

def find_key(maze, row, col):
    for i in range(row):
        for j in range(col):
            if maze[i][j] == '6':
                return tuple([i, j])

def BFS(maze, start, end):
    global count_BFS, length, time
    q = []
    q.append(position(start, []))
    checked = list()

    while len(q) != 0:
        p = q.pop(0)
        checked.append(p.name)
        for adjspaces in get_adj(maze, p, checked, q):
            q.append(adjspaces)
            if end == adjspaces.name:
                return adjspaces.path, len(checked), len(adjspaces.path)

def get_adj(maze, p, checked, q):
    global row, col
    routes = list()
    x= p.name[0]
    y= p.name[1]

    if(x==0):
        if maze[x+1][y] != '1':
            routes.append((x+1, y))
        if maze[x][y-1] != '1':
            routes.append((x, y-1))
        if maze[x][y+1] != '1':
            routes.append((x, y+1))
    elif (x-1 >=0 and x+1 < row and y-1 >=0 and y+1 < col ):
        if maze[x-1][y] != '1':
            routes.append((x-1, y))
        if maze[x+1][y] != '1':
            routes.append((x+1, y))
        if maze[x][y-1] != '1':
            routes.append((x, y-1))
        if maze[x][y+1] != '1':
            routes.append((x, y+1))

    adj = list()
    for i in routes:
        if i not in checked and i not in [x.name for x in q]:
            adj.append(position(i, p.path + [p.name]))
    return adj

def write_path(maze, path, g):
    for i in range(len(maze)):
        if i>0:
            g.write('\n')
        for j in range(len(maze[0])):
            if tuple([i, j]) in path and maze[i][j] != '3' and maze[i][j] != '4' and maze[i][j] != '6':
                g.write('5' + " ")
            else:
                g.write(maze[i][j]+" ")
        print()

def first_floor():
    global count_BFS, length, row, col, time, length
    count_BFS = 0
    length = 0
    maps=list()
    f=open("first_floor_input.txt",'r')
    data = f.read().split('\n')
    mazeinfo=data[0].split(' ')
    row = int(mazeinfo[1])
    col = int(mazeinfo[2])

    for i in range(row):
        maps.append(data[i+1].split(' '))

    start = find_start(maps, row, col)
    key = find_key(maps, row, col)
    end = find_end(maps, row, col)
    path, time, length = BFS(maps, start, key)
    path2, time2, length2 = BFS(maps, key, end)
    g=open("first_floor_output.txt", 'w')
    write_path(maps, path+path2, g)
    g.write("\n" + "---" + "\n")
    g.write("length = " + str(length+length2) + "\n")
    g.write("time = " + str(time+time2))

    f.close()
    g.close()

def second_floor():
    global count_BFS, length, row, col, time, length
    count_BFS = 0
    length = 0
    maps = list()
    f = open("second_floor_input.txt", 'r')
    data = f.read().split('\n')
    mazeinfo = data[0].split(' ')
    row = int(mazeinfo[1])
    col = int(mazeinfo[2])

    for i in range(row):
        maps.append(data[i + 1].split(' '))

    start = find_start(maps, row, col)
    key = find_key(maps, row, col)
    end = find_end(maps, row, col)
    path, time, length = BFS(maps, start, key)
    path2, time2, length2 = BFS(maps, key, end)
    g = open("second_floor_output.txt", 'w')
    write_path(maps, path + path2, g)
    g.write("\n" + "---" + "\n")
    g.write("length = " + str(length + length2) + "\n")
    g.write("time = " + str(time + time2))

    f.close()
    g.close()

def third_floor():
    global count_BFS, length, row, col, time, length
    count_BFS = 0
    length = 0
    maps = list()
    f = open("third_floor_input.txt", 'r')
    data = f.read().split('\n')
    mazeinfo = data[0].split(' ')
    row = int(mazeinfo[1])
    col = int(mazeinfo[2])

    for i in range(row):
        maps.append(data[i + 1].split(' '))

    start = find_start(maps, row, col)
    key = find_key(maps, row, col)
    end = find_end(maps, row, col)
    path, time, length = BFS(maps, start, key)
    path2, time2, length2 = BFS(maps, key, end)
    g = open("third_floor_output.txt", 'w')
    write_path(maps, path + path2, g)
    g.write("\n" + "---" + "\n")
    g.write("length = " + str(length + length2) + "\n")
    g.write("time = " + str(time + time2))

    f.close()
    g.close()

def fourth_floor():
    global count_BFS, length, row, col, time, length
    count_BFS = 0
    length = 0
    maps = list()
    f = open("fourth_floor_input.txt", 'r')
    data = f.read().split('\n')
    mazeinfo = data[0].split(' ')
    row = int(mazeinfo[1])
    col = int(mazeinfo[2])

    for i in range(row):
        maps.append(data[i + 1].split(' '))

    start = find_start(maps, row, col)
    key = find_key(maps, row, col)
    end = find_end(maps, row, col)
    path, time, length = BFS(maps, start, key)
    path2, time2, length2 = BFS(maps, key, end)

    g = open("fourth_floor_output.txt", 'w')
    write_path(maps, path + path2, g)
    g.write("\n" + "---" + "\n")
    g.write("length = " + str(length + length2) + "\n")
    g.write("time = " + str(time + time2))

    f.close()
    g.close()

def fifth_floor():
    global count_BFS, length, row, col, time, length
    count_BFS = 0
    length = 0
    maps = list()
    f = open("fifth_floor_input.txt", 'r')
    data = f.read().split('\n')
    mazeinfo = data[0].split(' ')
    row = int(mazeinfo[1])
    col = int(mazeinfo[2])

    for i in range(row):
        maps.append(data[i + 1].split(' '))

    start = find_start(maps, row, col)
    key = find_key(maps, row, col)
    end = find_end(maps, row, col)
    path, time, length = BFS(maps, start, key)
    path2, time2, length2 = BFS(maps, key, end)
    g = open("fifth_floor_output.txt", 'w')
    write_path(maps, path + path2, g)
    g.write("\n" + "---" + "\n")
    g.write("length = " + str(length + length2) + "\n")
    g.write("time = " + str(time + time2))

    f.close()
    g.close()

def all_floor():
    first_floor()
    second_floor()
    third_floor()
    fourth_floor()
    fifth_floor()

def main():
    s = int(input("Press Number which floor you want to check : "))

    floor = {1: first_floor, 2: second_floor, 3: third_floor, 4:fourth_floor, 5: fifth_floor, 6: all_floor}
    try:
        floor[s]()
    except KeyError:
        print("floor Not Exist")

if __name__ == '__main__':
    main()
