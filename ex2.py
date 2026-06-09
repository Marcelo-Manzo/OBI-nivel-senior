import sys

entrada = sys.stdin.read().split()

n = int(entrada[0])
#lista de strings
dados = entrada[1:]
tupla = []

for i in range(0,len(dados)-1,2):
    tupla.append([int(dados[i]),int(dados[i+1])])
tupla.sort(key=lambda x: x[1])

cont = 1
fim_do_ultimo_escolhido = tupla[0][1]

# Começamos a olhar a partir do segundo filme (índice 1) até o final (n)
for i in range(1, n):
    # Se o início do filme atual for maior ou igual ao fim do último escolhido...
    if tupla[i][0] >= fim_do_ultimo_escolhido:
        cont += 1
        fim_do_ultimo_escolhido = tupla[i][1] # Atualiza o seu horário livre!










