from itertools import permutations

perms = list(permutations('0123456789'))

# -------- OR --------

# def all_perms(elements):
#     if len(elements) <= 1:
#         return elements
#     else:
#         for perm in all_perms(elements[1:]):
#             for i in range(len(elements)):
#                 return perm[:i] + elements[0:1] + perm[i:]

# list = all_perms([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# for i in list:
#     print(list[i])

solution = ''.join(perms[999999])

print(solution)