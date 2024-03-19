from collections import deque

#Busca em largura para encontrar um vendedor de manga (estranho, mas foi o exemplo que encontrei)

def pesquisa(nome):
    fila_de_pesquisa = deque()
    fila_de_pesquisa += grafo["voce"]
    verificadas = []

    while fila_de_pesquisa:
        pessoa = fila_de_pesquisa.popleft()
        if not pessoa in verificadas:
            if pessoa_e_vendedor(pessoa):
                print(pessoa + " é um vendedor de manga")
                return True
            else:
                fila_de_pesquisa += grafo[pessoa]
                verificadas.append(pessoa)
    return False


def pessoa_e_vendedor(nome):
    return nome[-1] == 'm' #condicional adotado didaticamente

grafo = {}

grafo["voce"] = ["alice", "bob", "claire"]
grafo["bob"] = ["anuj", "peggy"]
grafo["alice"] = ["peggy"]
grafo["claire"] = ["thom", "jonny"]
grafo["anuj"] = []
grafo["peggy"] = []
grafo["thom"] = []
grafo["jonny"] = []

pesquisa("voce")


