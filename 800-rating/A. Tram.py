n = int(input())
ni = 0

iin = []
for stops in range(n):
    o, i = [int(x) for x in input().split()]
    ni = ni + i - o
    iin.append(ni)


print(max(iin))
