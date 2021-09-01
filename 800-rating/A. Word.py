word = input()
upper = 0
lower = 0

for x in word:
    if x.isupper():
        upper += 1
    else:
        lower += 1

if (upper == lower) or (upper < lower):
    word = word.lower()
else:
    word = word.upper()


print(word)
