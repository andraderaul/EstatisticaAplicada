#!/usr/bin/python
# -*- coding: utf-8 -*-
import math as mp

#leitura do arquivo
def readArq():
    arquivo = open('dados.txt','r')
    vector = []

    line = arquivo.readline()
    while len(line) is not 0:
        aux = line.split('-')
        for i in aux:
            vector.append(float(i))
        line = arquivo.readline()

    arquivo.close()
    return vector

#MEDIA = Soma de todos elementos dividido pelo total de elementos
def media(vector):
    n = len (vector)
    s = sum(dados) # somatorio i = 1 ... n; sum += x[i]
    print("Soma = %.2f N = %d " %(s,n), end="")
    return s/n

#MODA = valor que ocorre com maior frequencia. A moda ponde nao existir(AMODAL), Pode nao ser unica (bimodal ou multimodal)
def moda(vector):
    maior = 0
    resto = []
    for i in vector:
        item = vector.count(i) #apariçoes
        if maior < item:
            maior = item #pegando o que mais apareceu
        else:
            resto.append(i) #salvando o restante

    cont = 0
    for i in resto:
        item = resto.count(i)
        if item == maior: #quantos mais apareceram igual ao maior
            cont += 1

    mo = []
    #maior = 1 apareceu cada um somente uma vez
    #maior = n apareceu todas as vezes
    #maior+cont = n todos simbolos apareceram igualmente
    if maior == 1 or maior == len(vector) or (cont+maior) == len(vector):
        mo.append("Amodal")
        return mo
    else:
        for i in vector:
            item = vector.count(i)
            if item == maior and i not in mo:
                mo.append(i)
        return mo

#MEDIANA = É o valor central que divide o conjunto de dados em partes proporcionais
def mediana(vector):
    vector.sort() #ordena-se
    print("Ordenado: ", vector)
    n = len(vector)
    if n%2: #impar
        i = (n+1)//2
        return vector[i-1] #pq o vetor n começa de 1
    else:#par
        j = (n//2) #aqui seria (n/2)+1 pq o vetor começa de 0
        i = (n//2)-1 #aqui seria (n/2) pq o vetor começa de 0
        return (vector[i] + vector[j])/2


if __name__ == '__main__':

    dados = readArq()
    print("Media = %.2f" %media(dados))
    print("Mediana = %.2f" %mediana(dados))
    print("Moda = ", moda(dados))
