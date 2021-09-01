l, b = [int(x) for x in input().split()]
cont = 1
while True:
    L = 3*l
    b = 2*b

    if L > b:
        break
    else:
        cont += 1

print(cont)
