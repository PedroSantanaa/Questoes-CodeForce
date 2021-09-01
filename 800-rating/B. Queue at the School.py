n, t = [int(x) for x in input().split()]
Q = input()


for i in range(t):
    Q = Q.replace('BG', 'GB')


print(Q)
