def main():
    n = int(input())
    lista = []
    for i in range(n):
        lista.append(int(input()))
    soma(lista)

def soma(lista):
    listSoma = []
    soma = 0
    for i in lista:
        if i != 0:
            listSoma.append(i)
        else:
            listSoma.pop()
    
    soma = sum(listSoma)
    print(soma)
    
main()

