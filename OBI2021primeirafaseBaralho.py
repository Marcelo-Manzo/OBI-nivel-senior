def main():
    cartas = str(input())
    if cartas >= 3 and cartas <= 156:
        for i in range(0, len(cartas)-1, 3):
            cartas += " "
        cartas = cartas.split()
        VerificarRepitidas(cartas)

def VerificarRepitidas(cartas):
    repitidas = []
    copas = ""
    espadas = ""
    ouros = ""
    paus = ""
    for i,valor1 in cartas:
        for j,valor2 in cartas:
            if valor1== valor2 and i != j: 
                match valor1[2]:
                    case "C":
                        copas += "erro"
                    case "E":
                        espadas += "erro"
                    case "U":
                        ouros += "erro"
                    case "P":
                        paus += "erro"

    for i in cartas:
        

    
    

