def comb(N, k):
    factorial_N = 1
    factorial_k = 1
    factorial_Nk = 1

    for i in range(1, N):
        factorial_N = factorial_N*i
    
    for j in range(1, k):
        factorial_k = factorial_k*j

    for nk in range(1, N-k):
        factorial_Nk = factorial_Nk*nk

    combinatoria = factorial_N/(factorial_k*factorial_Nk)

    print(f"La combinatoria de N={N} y k={k} es:", combinatoria)

N = int(input("N = "))
k = int(input("k = "))

comb(N, k)

