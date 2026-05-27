# #o que eu tetei fazer:
# def main():
#     n = int(input())
#     lista = []
#     amigos = 0
#     for i in range(n):
#         x = str(input())
#         lista.append(x)
#     for i in lista:
#         if i[1] in amigos:
#             continue
#         else:
#             amigos+=1

#     TempoDeResposta(lista,amigos)

# def TempoDeResposta(lista,amigos):
#     TempoAmigos = []
#     for i in range(amigos):
#         TempoAmigos.append([])
#     for i in lista:
#         tempo = 0
#         for j in lista:
#             if(i[0] == "R" and j[0] == "E" and i[1] == j[1]):
#                 TempoAmigos.append(int(j[1]),tempo)
#                 lista.pop(i)
#                 lista.pop(j)
#                 break
#             if j[0] == "T":
#                 for z in range(len(TempoAmigos)):
#                     aux = TempoAmigos[z][1]
#                     aux += tempo
#                     TempoAmigos.pop(z)
#                     TempoAmigos.append(aux,z[1])
#     for i in TempoAmigos:
#         print(i)

# #LITSA: [R3, T5,E3]
# main()


# o que o chat fez: 
def resolver():
    n = int(input())
    eventos = []
    for _ in range(n):
        cmd, val = input().split()
        eventos.append((cmd, int(val)))

    # Dicionários para controlar o estado
    tempo_total = {}      # Soma dos tempos de resposta de cada amigo
    ultimo_recebido = {}  # Quando foi que o amigo X mandou a última mensagem (R)
    respondida = {}       # True se a última mensagem foi respondida, False se está pendente
    
    amigos = set()        # Para saber quais amigos existem no registro
    tempo_atual = 0       # Nosso cronômetro global

    for i in range(len(eventos)):
        cmd, x = eventos[i]
        
        if cmd == 'R':
            amigos.add(x)
            ultimo_recebido[x] = tempo_atual
            respondida[x] = False
            
        elif cmd == 'E':
            duracao = tempo_atual - ultimo_recebido[x]
            tempo_total[x] = tempo_total.get(x, 0) + duracao
            respondida[x] = True
            
        # Lógica do Tempo: Quanto tempo passa até o PRÓXIMO evento?
        if cmd == 'T':
            # Se o comando atual é T, o tempo já passou. 
            # Mas o enunciado diz que T indica o tempo entre o anterior e o próximo.
            # Já somamos isso no passo anterior ou somaremos agora.
            pass
        else:
            # Se o próximo registro for um T, usamos o valor de T.
            # Caso contrário, o padrão é passar 1 segundo.
            if i + 1 < n and eventos[i+1][0] == 'T':
                tempo_atual += eventos[i+1][1]
            else:
                # Só incrementa o tempo se não for o último evento
                if i + 1 < n:
                    tempo_atual += 1

    # Ordenar amigos para a saída
    for amigo in sorted(list(amigos)):
        if not respondida.get(amigo, True):
            print(f"{amigo} -1")
        else:
            print(f"{amigo} {tempo_total.get(amigo, 0)}")

resolver()
    