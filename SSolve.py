board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def solution(b):
    f = find_empty(b)
    if not f:
        return True
    else:
        r, c = f
        for i in range(1, 10):
            if check(i, (r, c), b):
                b[r][c] = i
                if solution(b):
                    return True

                b[r][c] = 0
        return False


def check(num, pos, b):
    # for row
    for i in range(len(b[0])):
        if num == b[pos[0]][i] and pos[1] != i:
            return False

    # for col
    for i in range(len(b)):
        if num == b[i][pos[1]] and pos[0] != i:
            return False

    # for box
    rbox = pos[0] // 3
    cbox = pos[1] // 3
    for i in range(rbox * 3, rbox * 3 + 3):
        for j in range(cbox * 3, cbox * 3 + 3):
            if b[i][j] == num and (i, j) != pos:
                return False
    return True


def display_table(b):
    for i in range(len(b)):
        print("")
        if i % 3 == 0 and i != 0:
            print("")
        for j in range(len(b[i])):
            if j % 3 == 0 and j != 0:
                print("  ", end="")

            print(str(b[i][j]) + " ", end="")


def find_empty(b):
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] == 0:
                return (i, j)  # row and col

    return None


display_table(board)
solution(board)
print("\n\n")
display_table(board)
