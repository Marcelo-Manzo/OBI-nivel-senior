import sys

# 1. Lendo os dados padrão OBI
entrada = sys.stdin.read().split()
if entrada:
    n = int(entrada[0])
    peso_maximo = int(entrada[1])

    dados = entrada[2:]
    tupla = []
    for i in range(0, len(dados) - 1, 2):
        # Guardamos como inteiros: [peso, valor]
        tupla.append([int(dados[i]), int(dados[i+1])])

    # Criamos uma função para testar os caminhos (a partir da pedra 'i')
    def testar_caminho(i, peso_atual, valor_atual):
        # Se o peso estourou o limite, esse caminho deu errado (retorna 0)
        if peso_atual > peso_maximo:
            return 0
        
        # Se já olhamos todas as pedras, devolvemos o valor que conseguimos juntar
        if i == n:
            return valor_atual

        # Pegamos os dados da pedra atual
        peso_pedra = tupla[i][0]
        valor_pedra = tupla[i][1]

        # SEU PENSAMENTO LÓGICO AQUI:
        # Caminho A: O que acontece se eu PEGAR essa pedra?
        caminho_pegar = testar_caminho(i + 1, peso_atual + peso_pedra, valor_atual + valor_block) # (Nota: valor_pedra)
        
        # Caminho B: O que acontece se eu PULAR essa pedra e olhar as próximas?
        caminho_pular = testar_caminho(i + 1, peso_atual, valor_atual)

        # O Python vai seguir os dois caminhos e nos devolver o que der mais dinheiro!
        return max(caminho_pegar, caminho_pular)

    # Mandamos o computador começar a testar a partir da pedra 0, com peso 0 e valor 0
    maior_valor_encontrado = testar_caminho(0, 0, 0)
    print(maior_valor_encontrado)