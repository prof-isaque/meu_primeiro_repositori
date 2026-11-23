Buscador de Caminhos (BFS em labirinto)

Python
from collections import deque

def resolver_labirinto(labirinto):
    linhas, colunas = len(labirinto), len(labirinto[0])
    inicio = None
    
    # Encontra a posição inicial 'S'
    for r in range(linhas):
        for c in range(colunas):
            if labirinto[r][c] == 'S':
                inicio = (r, c)
                break

    fila = deque([(inicio, [inicio])])  # (posição_atual, caminho_percorrido)
    visitados = {inicio}
    direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Cima, Baixo, Esquerda, Direita

    while fila:
        (r, c), caminho = fila.popleft()
        
        if labirinto[r][c] == 'E':
            return caminho
            
        for dr, dc in direcoes:
            nr, nc = r + dr, c + dc
            if (0 <= nr < linhas and 0 <= nc < colunas and 
                labirinto[nr][nc] != 1 and (nr, nc) not in visitados):
                visitados.add((nr, nc))
                fila.append(((nr, nc), caminho + [(nr, nc)]))
                
    return None
