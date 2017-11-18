#!/usr/bin/python
# -*- coding: utf-8 -*-
import math as mp

def ordena(dados):
    return sorted(dados)

def amplitude_total(dados):
    xMin = dados[0] # ou min(dados)
    xMax = dados[-1] #ou lista[::-1][0] ou max(dados)
    return xMax - xMin

def intervalos(x):
    return  mp.ceil(mp.sqrt(x)) #ou K = 1 + 3,3logn (formula de Sturges)

def amplitude_das_classes(x,y):
    return x/y

def readArq():
    arquivo = open('dados.txt','r')
    vector = []
    while True:
        line = arquivo.readline()
        if len(line) == 0: #fim do arquivo
            break
        aux = line.split("-")
        for i in aux:
            vector.append(float(i))
    arquivo.close()
    return vector

def main():

    dados = readArq() #leitura do arquivo
    n = len(dados) #numero total de individuos
    dados = ordena(dados) #1 ordena-se os dados brutos (rol estatistico)
    AT = amplitude_total(dados) #2 determina-se a amplitude total dos dados (AT)
    K = intervalos(n) #3 determinar o nº de classes ou intervalos (K)
    h = amplitude_das_classes(AT,K) #4 calcula-se a amplitude das classes(h)
    print(AT)
    print("Rol", dados)
    print("AT = %.1f" %AT)
    print("K = %.1f" %K)
    print("h = %.2f" %h)

main()
