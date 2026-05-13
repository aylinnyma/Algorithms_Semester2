word = "holamellamoaylinymiamigoayush"

a = 0
e = 0
i = 0
o = 0
u = 0

word.lower()
for x in word:
    if x == "a":
        a += 1 
    elif x == "e":
        e += 1
    elif x == "i":
        i += 1
    elif x == "o":
        o += 1
    elif x == "u":
        u += 1

print(f"A count: {a} \nE count: {e} \nI count: {i} \nO count: {o} \nU count: {u}")