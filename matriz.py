import funcoes
import os
import time

matriz = funcoes.carregaMatrizInicial()
while(1):
  funcoes.mostraMatriz(matriz)
  funcoes.menu(matriz)
  funcoes.mostraMatriz(matriz)
  time.sleep(3)
  os.system('cls' if os.name == 'nt' else 'clear')