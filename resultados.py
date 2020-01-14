'''
Modulo para trabalharmos com os resultados de provas. E obter os alunos aprovados.
'''

# -*- coding: utf-8 -*-

import pandas as pd


def search_bin(lista1, lista2):
    '''
    Função que compara duas listas e retorna nomes semelhantes.
    testando o método de busca binário
    :param lista1: variável do tipo list com nomes, consideramos essa como sendo a lista
                    com alguns nomes que podem ser de seu interesse.
    :param lista2: variável do tipo list com nomes alunos, consideramos essa sendo a lista
                    de nomes que são de seu interesse
    :return: dicionário de nomes semelhantes e número de repetições na lista1

    Exemplo de aplicação:

    > lista_A = [João, Guilherme, Maria, Vicente de Paula, Luís Guimarães]
    > lista_B = [Maria, Luís Guimarães, Joao]
    > resultado = search_bin(lista_A, lista_B)
    > print(resultado)
    > {Maria: 1, Luís Guimarães:1}

    Observe que se você tiver mais de  um nome em comum na lista1 o valor retornado pela 
    chave (nome), será o número de vezes que ele aparece na lista1.

    Exemplo2:

    > lista_A = ["João", "Guilherme", "Maria", "João", "Vicente de Paula", "Maria", "Luís Guimarães"]
    > lista_B = ["Maria", "Luís Guimarães", "Joao"]
    > resultado = search_bin(lista_A, lista_B)
    > print(resultado)
    > {Maria: 2, Luís Guimarães:1}
   
    Nota: Para encontrar um nome ele deve ser exatamente igual em ambas as listas. Como no
    exemplo acima vemos que o nome João não é considerado por ele não ter o acento na lista_B,
    para encontrar os nomes em casos semelhantes, tente passar as listas na função acentos antes
    de usar a busca.
    '''
    iguais = {}
    lista1.sort()
    lista2.sort()
    #Aqui pegamos o tamanho da lista de aprovados no vestibular para podemos divir a lista em partes
    lista_tempor = lista1
    #Agora vamos comparar os alunos de ambas as listas
    for aluno in lista1:
        while True:
            indice = int(len(lista_tempor)/2)
            if len(lista_tempor) % 2 == 0:
                if len(lista_tempor)==2:
                    if aluno == lista_tempor[0]:
                        iguais[aluno] = iguais.get(aluno,0) +1
                        break
                    if aluno == lista_tempor[1]:
                        iguais[aluno] = iguais.get(aluno,0) +1
                        break
                    else: break
                if aluno < lista_tempor[indice]:
                    lista_tempor = lista_tempor[:indice]
                elif aluno > lista_tempor[indice-1]:
                    lista_tempor = lista_tempor[indice:]
            else:
                if len(lista_tempor) == 1:
                    if aluno == lista_tempor[0]:
                        iguais[aluno] = iguais.get(aluno, 0) +1
                        break
                    else: break
                if aluno < lista_tempor[indice]:
                    lista_tempor = lista_tempor[: indice+1]
                elif aluno > lista_tempor[indice]:
                    lista_tempor = lista_tempor[indice:]
    return iguais

def search_lin(lista1, lista2):
    '''
    Essa função faz uma pesquisa linear dos alunos, essa é ideal por encontrar mais de um valor
    na segunda lista, diferentemente da função search_bin() que apenas encontra repetições na lista1.
    :param lista1: variável do tipo list com nomes, consideramos essa como sendo a lista
                    com alguns nomes que podem ser de seu interesse.
    :param lista2: variável do tipo list com nomes alunos, consideramos essa sendo a lista
                    de nomes que são de seu interesse
    :return: dicionário de nomes com o número de vezes que o nome é encontrado em ambas listas
    
    Exemplo de aplicação:

    > lista_A = ["João", "Guilherme", "Maria", "Vicente de Paula", "Luís Guimarães"]
    > lista_B = ["Maria", "Luís Guimarães", "Joao"]
    > resultado = search_lin(lista_A, lista_B)
    > print(resultado)
    > {Maria: 1, Luís Guimarães:1}

    Observe que se você tiver mais de  um nome em comum na lista1 ou lista2 o valor retornado pela 
    chave (nome), será o número de vezes que ele aparece na lista1 ou lista2.

    Exemplo2:

    > lista_A = ["João", "Guilherme", "Maria", "João","Vicente de Paula", "Maria","Luís Guimarães"]
    > lista_B = ["Maria", "Luís Guimarães", "Joao", "Maria"]
    > resultado = search_lin(lista_A, lista_B)
    > print(resultado)
    > {Maria: 4, Luís Guimarães: 1}
   
    Nota: Para encontrar um nome ele deve ser exatamente igual em ambas as listas. Como no
    exemplo acima vemos que o nome João não é considerado por ele não ter o acento na lista_B,
    para encontrar os nomes em casos semelhantes, tente passar as listas na função acentos antes
    de usar a busca.

    '''
    iguais = {}
    for aprovado in lista1:
        for aluno in lista2:
            if aprovado == aluno:
                iguais[aluno] = iguais.get(aluno, 0) +1
    return iguais

def acentos(palavra):
    '''
    A função retorna o parâmetro sem acentos
    '''
    acentos = {"á": "A", "â": "A", "à": "A", "ã": "A", "ä": "A", "é": "E", "ê": "E", \
               "è": "E", "ë": "E", "í": "I", "î": "I", "ì": "I", "ï": "I", "ó": "O", \
               "ô": "O", "ò": "O", "õ": "O", "ö": "O", "ú": "U", "ù": "U", "û": "U", \
               "ü": "U", "Â": "A", "À": "A", "Á": "A", "Ã": "A", "Ä": "A", "È": "E", \
               "É": "E", "Ê": "E", "Ë": "E", "Ì": "I", "Í": "I", "Î": "I", "Ò": "O", \
               "Ó": "O", "Ô": "O", "Õ": "O", "Ö": "O", "Ù": "U", "Ú": "U", "Û": "U", \
               "Ü": "U", "ç": "C", "Ç": "C", "ñ": "N", "Ñ": "N"
               }

    for letra in palavra:
        if letra in acentos:
            x = palavra.find(letra)
            palavra = list(palavra)
            palavra[x] = acentos.get(letra)
            palavra = "".join(palavra)

    return palavra
