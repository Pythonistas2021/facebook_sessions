def comb(N, k):
    factorial_N = 1
    factorial_k = 1
    factorial_Nk = 1

    for i in range(1, N+1):
        factorial_N = factorial_N*i
    
    for j in range(1, k+1):
        factorial_k = factorial_k*j

    for nk in range(1, N-k+1):
        factorial_Nk = factorial_Nk*nk

    combinatoria = int(factorial_N/(factorial_k*factorial_Nk))

    print(combinatoria)

N = int(input("N = "))
k = int(input("k = "))

comb(N, k)
