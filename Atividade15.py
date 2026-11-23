Sequencia de Fibonacci

def fibonacci(n):
    if n <= 0:
       return []
    if n == 1:
       return [0]

    seq = [0, 1] 
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq

# Exemplo de uso:
print(fibonacci(8)) # [0, 1, 1, 2, 3, 5, 8, 13]
