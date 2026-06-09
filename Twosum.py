import sys

# Lê absolutamente tudo da entrada de uma vez só e separa por espaços
entrada = sys.stdin.read().split()

# Agora pegamos os valores pelas posições (índices) da lista 'entrada'
n = int(entrada[0])
k = int(entrada[1])

# O resto dos dados (do índice 2 em diante) são os saldos
# Já convertemos para int aqui para não precisar converter toda hora no while
dados = [int(x) for x in entrada[2:]]
cont = 0
input = sys.stdin.read
dados = input().split()
dados.sort()

esq = 0
dir = n-1

while esq < dir:
    conta = int(dados[esq]) + int(dados[dir])
    if conta == k:
        cont +=1
        dir-=1
        esq-=1
    elif conta < k:
        esq+=1
    elif conta > k:
        dir-=1

