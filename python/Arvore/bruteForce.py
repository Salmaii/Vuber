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

from itertools import permutations

# Obtem todas as permutações
perm = permutations(['a', 'b', 'c', 'd', 'e'])
cont = 0

# Imprime as permutações
for i in list(perm):
    cont = cont + 1
    print(f'{cont} -> {i}')
