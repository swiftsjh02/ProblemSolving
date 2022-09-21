#matrix chain multiplication

def MCM(p, n):
    m = [[0 for x in range(n)] for x in range(n)]
    s = [[0 for x in range(n)] for x in range(n)]
    for i in range(1, n):
        m[i][i] = 0
    for r in range(2, n):
        for i in range(1, n-r+1):
            j = i + r - 1
            m[i][j] = 999999999
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    return m, s

def print_optimal_parens(s, i, j):
    if i == j:
        print("A", i, sep="", end="")
    else:
        print("(", end="")
        print_optimal_parens(s, i, s[i][j])
        print_optimal_parens(s, s[i][j]+1, j)
        print(")", end="")

if __name__ == "__main__":
    p = [30, 35, 15, 5, 10, 20, 25]
    n = len(p)
    m, s = MCM(p, n)
    print(m[1][n-1])
    print_optimal_parens(s, 1, n-1)
    