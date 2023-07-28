# Problem: Given M and N, calculate S = 1*1 + 1*2 + ... + 1*10 + 2*1 + 2*2 + ... + ... + M*N

def calcS(M, N):
    S = 0

    for i in range(1, M+1):
        for j in range(1, N+1):
            S += i*j

    return S

# Enter input
m = int(input('Enter M: '))
n = int(input('Enter N: '))

# Print output
print(f'S = ', calcS(m, n))