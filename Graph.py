n = 6
Visited = [False] * n
Path = []
LetterPath = []


def hamilton(curr):
    Path.append(curr)
    if len(Path) == n:
        if A[Path[0]][Path[-1]] == 0:
            for path in Path:
                LetterPath.append(alf[path])
            return True
        else:
            Path.pop()
            return False
    Visited[curr] = True
    Visited[5] = True
    for next in range(n):
        if Visited[0] == Visited[1] == Visited[2] == Visited[3] == Visited[4] and next == 5:
            if A[curr][next] == 1 and hamilton(next):
                return True
        else:
            if A[curr][next] == 1 and not Visited[next] and hamilton(next):
                return True
    Visited[curr] = False
    Path.pop()
    return False


for k in range(n-1):
    alf = ["a", "b", "c", "d", "e"]
    B = [[0, 1, 0, 1, 0],
         [0, 0, 1, 0, 0],
         [1, 0, 0, 0, 1],
         [1, 1, 1, 0, 1],
         [1, 0, 0, 0, 0]]
    A = B
    for i in range(n-1):
        A[i].append(A[i][k])
    A.append(A[k])
    alf.append(alf[k])
    hamilton(k)
    if Path:
        print(LetterPath)
    A.clear()
    alf.clear()
    Path.clear()
    LetterPath.clear()
