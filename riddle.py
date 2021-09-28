from itertools import permutations
a = permutations(['a', 'b', 'a', 'b'], 4)
print(*sorted([''.join(Tuple) for Tuple in set(a)]), len(list(a)), sep='\n')
# count = 0
# for x in range(1, 11):
#     row = '#'*2**x
#     print(row)
#     count += len(row)
# print(count)