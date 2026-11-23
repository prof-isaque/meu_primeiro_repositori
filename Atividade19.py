 Validador de Parênteses Balanceados

Python
def validar_parenteses(s):
    pilha = []
    pares = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in pares.values():
            pilha.append(char)
        elif char in pares.keys():
            if not pilha or pilha.pop() != pares[char]:
                return False
                
    return len(pilha) == 0

# Exemplos de uso:
print(validar_parenteses("{[()]}"))  # True
print(validar_parenteses("{[(])}"))  # False
