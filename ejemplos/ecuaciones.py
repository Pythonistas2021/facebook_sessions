print("Resuelve la siguiente ecuación lineal")
ecuation = "2x - 3 = x + 2"
terms = ecuation.split()
left = []
right = []

for term in terms:
    print(term)
    if term.find("x") in (0,1):
        left.append(term)
    elif term != "=":
        right.append(term)

left = " ".join(left)
right = " ".join(right)
