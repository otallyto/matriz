import json


def verificaLampadaAcende(lampadas, entrada):
    with open('posicoes.json', 'r') as arquivo:
        data = arquivo.read()
        p = json.loads(data)
        if(lampadas[p[entrada-1]["l"]][p[entrada-1]["c"]] == 1):
            print("Lampada ja acesa")
        else:
            lampadas[p[entrada-1]["l"]][p[entrada-1]["c"]] = 1


def carregaMatrizInicial():
    with open('matrizInicial.json', 'r') as arquivo:
        data = arquivo.read()
        return json.loads(data)


def mostraMatriz(matriz):
    for i in range(3):
        print(matriz[i])


def menu(matriz):
    entrada = int(input("Digite qual lampada deseja acender? "))
    opcoes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    if(entrada in opcoes):
        if(entrada == 1):
            verificaLampadaAcende(matriz, entrada)
        elif entrada == 2:
            verificaLampadaAcende(matriz, entrada)
        elif entrada == 3:
            verificaLampadaAcende(matriz, entrada)
        elif entrada == 4:
            verificaLampadaAcende(matriz, entrada)
        elif entrada == 5:
            verificaLampadaAcende(matriz, entrada)
        elif entrada == 6:
            verificaLampadaAcende(matriz, entrada)
        elif entrada == 7:
            verificaLampadaAcende(matriz, entrada)
        elif entrada == 8:
            verificaLampadaAcende(matriz, entrada)
        elif entrada == 9:
            verificaLampadaAcende(matriz, entrada)
    else:
        print("Opcao invalida")
