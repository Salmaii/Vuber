from math import inf
from itertools import product


def floyd_warshall(n, edge):
    rn = range(n)
    dist = [[inf] * n for i in rn]
    nxt = [[0] * n for i in rn]
    for i in rn:
        dist[i][i] = 0
    for u, v, w in edge:
        dist[u - 1][v - 1] = w
        nxt[u - 1][v - 1] = v - 1
    for k, i, j in product(rn, repeat=3):
        sum_ik_kj = dist[i][k] + dist[k][j]
        if dist[i][j] > sum_ik_kj:
            dist[i][j] = sum_ik_kj
            nxt[i][j] = nxt[i][k]
    print("    pair        dist     path")
    for i, j in product(rn, repeat=2):
        if i != j:
            path = [i]
            while path[-1] != j:
                path.append(nxt[path[-1]][j])
            print("%3d → %3d  %4d       %s"
                  % (i + 1, j + 1, dist[i][j],
                     ' → '.join(str(p + 1) for p in path)))
    
if __name__ == '__main__':
    floyd_warshall(5, [
        [1, 2, 4], 
        [1, 3, 8], 
        [1, 4, 15], 
        [1, 5, 24],
        [2, 1, 4],
        [2, 3, 300],
        [2, 4, 15],
        [2, 5, 20],
        [3, 1, 8],
        [3, 2, 300],
        [3, 4, 8],
        [3, 5, 14],
        [4, 1, 15],
        [4, 2, 15],
        [4, 3, 8],
        [4, 5, 6],
        [5, 1, 24],
        [5, 2, 20],
        [5, 3, 14],
        [5, 4, 6]])




#Bota o link ae -> https://www.youtube.com/watch?v=7yrmrKE1tgA
#cuzin<<<<<<<--------------
#https://www.youtube.com/watch?v=fdqxetN9YPA


"""
    pair        dist     path
  1 →   2     4       1 → 2
  1 →   3     8       1 → 3
  1 →   4    15       1 → 4
  1 →   5    21       1 → 4 → 5
  2 →   1     4       2 → 1
  2 →   3    12       2 → 1 → 3
  2 →   4    15       2 → 4
  2 →   5    20       2 → 5
  3 →   1     8       3 → 1
  3 →   2    12       3 → 1 → 2
  3 →   4     8       3 → 4
  3 →   5    14       3 → 5
  4 →   1    15       4 → 1
  4 →   2    15       4 → 2
  4 →   3     8       4 → 3
  4 →   5     6       4 → 5
  5 →   1    21       5 → 4 → 1
  5 →   2    20       5 → 2
  5 →   3    14       5 → 3
  5 →   4     6       5 → 4
"""


"""
    pair        dist     path

  1 →   2     4       1 → 2 // 
  1 →   3     8       1 → 3
  1 →   4    15       1 → 4
  1 →   5    21       1 → 4 → 5

  2 →   1     4       2 → 1
  2 →   3    12       2 → 1 → 3
  2 →   4    15       2 → 4 
  2 →   5    20       2 → 5 //

  3 →   1     8       3 → 1
  3 →   2    12       3 → 1 → 2
  3 →   4     8       3 → 4
  3 →   5    14       3 → 5

  4 →   1    15       4 → 1
  4 →   2    15       4 → 2
  4 →   3     8       4 → 3 //
  4 →   5     6       4 → 5

  5 →   1    21       5 → 4 → 1
  5 →   2    20       5 → 2
  5 →   3    14       5 → 3
  5 →   4     6       5 → 4 //


"""