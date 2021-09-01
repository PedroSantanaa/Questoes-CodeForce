x = int(input())

step = 5
steps = 0
while True:
    if(x-step < 0):
        step -= 1
    elif(x-step > 0):
        x = x-step
        steps += 1
    else:
        steps += 1
        break

print(steps)
