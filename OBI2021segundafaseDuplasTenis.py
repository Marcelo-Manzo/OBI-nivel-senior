lista = []
for i in range(4):
    lista.append(int(input()))
for i in range(len(lista)):
    for j in range(len(lista)-1):
        if lista[j] < lista[j+1]:
            aux = lista[j]
            lista[j] = lista[j+1]
            lista[j+1] = aux
            
x = (lista[0]+lista[3])-(lista[1]+lista[2])
if x<0:
    x = -x
print(x)