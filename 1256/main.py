'''

RULES:

1) M is always a prime number (e.g.: 7, 13 ...)

'''

N = int(input())

# Executing N loops
for _ in range(N):
    M, C = str(input()).split(' ')

    # Casting
    M = int(M)
    C = int(C)

    # Reading Keys
    aux = str(input()).split(' ')
    size = len(aux)

    for i in range(size):
        # Hash value
        hash_value = C % M
        
    
