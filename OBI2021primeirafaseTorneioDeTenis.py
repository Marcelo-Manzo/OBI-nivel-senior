def main():
    lista = []
    for i in range(6):
        x = str(input())
        lista.append(x)
    print(equipe(lista))

def equipe(lista) -> int:
    vencedoras = 0
    for i in lista:
        if i == "V":
            vencedoras+=1
    match vencedoras:
        case 0: return -1
        case 1: return 3
        case 2: return 3
        case 3: return 2
        case 4: return 2
        case 5: return 1
        case 6: return 1

main()

