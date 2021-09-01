not_yet = []


for letter in input():
    if letter not in not_yet:
        not_yet.append(letter)


if (len(not_yet) % 2 == 0):
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')
