Verificador de Palíndromo

def eh_palindromo(texto):
    limpo = texto.replace("", ""). lower()
    reyurn limpo == limpo[::-1]

#Exemplo de uso:
print(eh_palindromo("A base do teto desaba")) # True
