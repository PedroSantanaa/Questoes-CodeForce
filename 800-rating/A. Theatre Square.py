import math
n, m, a = [int(x) for x in input().split()]

min = math.ceil(m/a)*math.ceil(n/a)
print(min)
