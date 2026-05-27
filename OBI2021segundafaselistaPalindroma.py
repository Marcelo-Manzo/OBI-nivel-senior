import sys

def resolver():
    # Lê todas as entradas da memória de forma rápida
    input = sys.stdin.read
    dados = input().split()
    
    if not dados:
        return

    n = int(dados[0])
    # Converte os próximos N elementos para inteiros
    lista = [int(x) for x in dados[1:n+1]]
    
    # Inicializa os dois ponteiros nas pontas da lista
    esq = 0
    dir = n - 1
    operacoes = 0
    
    # Guarda os valores atuais das pontas para acumular as somas
    soma_esq = lista[esq]
    soma_dir = lista[dir]
    
    # Executa até os ponteiros se cruzarem
    while esq < dir:
        if soma_esq == soma_dir:
            # Valores iguais: avança ambos os ponteiros para dentro
            esq += 1
            dir -= 1
            soma_esq = lista[esq]
            soma_dir = lista[dir]
        elif soma_esq < soma_dir:
            # Esquerda menor: contrai/soma com o próximo vizinho da direita
            esq += 1
            soma_esq += lista[esq]
            operacoes += 1
        else:
            # Direita menor: contrai/soma com o próximo vizinho da esquerda
            dir -= 1
            soma_dir += lista[dir]
            operacoes += 1
            
    print(operacoes)

if __name__ == "__main__":
    resolver()
