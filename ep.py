##### EP - GIT ###
# Ao implementar uma função, dê commit no github usando os comandos vistos no workshop!
# Implemente uma função de cada vez, e dê commit em uma função por vez.
# NOME: Thiago Martins de Andrade Machado

import statistics

def minimo(arr):
    # retorna o menor valor do array
    return min(arr)

def maximo(arr):
    # retorna o maior valor do array
    return max(arr)

def meio(arr):
    # retorna o valor exatamente ao meio do array
    if (len(arr) == 0):
        return 0

    if (len(arr) % 2 == 1):
        return arr[len(arr)//2]

    return (arr[len(arr)//2] + arr[len(arr)//2 - 1])/2

def media(arr):
    # retorna a media dos valores do array
    if (len(arr) == 0):
        return 0
    return sum(arr) / len(arr)


def moda(arr):
    # retorna o valor que mais se repete no array
    return statistics.mode(arr)

def soma(arr, n = 1):
    # soma n a todos os valores do array e retorna o novo array
    # exemplo
    # entrada: arr = [1, 1, 1], n = 5
    # saida: arr = [6, 6, 6]
    for i in range(len(arr)):
        arr[i] = arr[i] + n 
    return arr


def subtracao(arr, n):
    # subtrai n em todos os valores do array e retorna o novo array
    # exemplo
    # entrada: arr = [1, 1, 1], n = 5
    # saida: arr = [-4, -4, -4]
    return soma(arr, n * (-1))

def soma_arr(arr1, arr2):
    # soma de dois arrays elemento-a-elemento e retorna
    arr3 = []
    for i in range(len(arr1)):
        arr3.append(arr1[i] + arr2[i])
    return arr3


def produto_interno(arr1, arr2):
    # retorna o produto interno entre dois vetores
    return
