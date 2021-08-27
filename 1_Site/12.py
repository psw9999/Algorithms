from itertools import permutations

arr = set(permutations([1,2,3,1], 2))

print(''.join(arr))