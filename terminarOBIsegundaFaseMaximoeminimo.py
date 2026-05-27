import sys

def resolver():
    # Lê todas as entradas da memória de forma rápida
    dados = []
    for i in range(3):
        dados.append(int(input()))

    primeiro = 0
    cont = dados[1]

    while primeiro == 0:
        soma = 0
        digitos = [int(d) for d in str(cont)]
        for i in digitos:
            soma += i
        if soma == dados[0]:
            primeiro = cont
        cont+=1


    segundo = 0
    cont2 = dados[2]
    while segundo==0:
        soma = 0
        digitos = [int(d) for d in str(cont2)]
        for i in digitos:
            soma += i
        if soma == dados[0]:
            segundo = cont2
        cont-=1
    print(primeiro)
    print(segundo)


if __name__ == "__main__":
    resolver()
