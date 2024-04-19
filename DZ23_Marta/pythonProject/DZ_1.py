import random as rnd


def random_arr(n):
    return [rnd.randint(0, 10) for i in range(n)]


l1 = random_arr(10)
l2 = random_arr(10)

# 1
l3 = l1 + l2

# 2
l4 = list(set(l3))

# 3
l5 = [i for i in l3 if i in l1 and i in l2]

# 4
l6 = [i for i in l1 if i not in l2] + [i for i in l2 if i not in l1]

# 5
a = sorted(l1)
b = sorted(l2)
l7 = [a[0], a[-1], b[0], b[-1]]

print(l1)
print(l2)
print(l3)
print(l4)
print(l5)
print(l6)
print(l7)