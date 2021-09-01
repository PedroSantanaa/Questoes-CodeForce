vari = []
for x in input().split():
    vari.append(int(x))

price = 0
for i in range(1, vari[2]+1):
    price += i*vari[0]


borrow = vari[1]-price

if borrow < 0:
    print(abs(borrow))
else:
    print('0')
