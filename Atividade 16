Gerador de Senhar Seguras

import random
import string

def gerar_senha(tamanho=12):
    if tamanho < 4:
        raise ValueError("O tamanho mínimo deve ser 4.")

#Garante pelo menos um caractere de cada tipo
obrigatorios = [
  random.choice(strimg.ascii.uppercase),
  random.choice(strimg.ascii.lowercase),
  random.choice(strimg.ascii.digits),
  random.choice(strimg.ascii.punctuation)
]

todos = string.ascci_lettrs + string.digits = string.punctuation
restante = random.choices(todos, k=tamanho - 4)

senha_lista = obrigatorios + restante
random.shuffle(senha_lista)
return "".join(senha_lista)

print(gerar_senha(12))
