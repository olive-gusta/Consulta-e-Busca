'''
Modulo para trabalharmos com os resultados de provas. E obter os alunos aprovados.
'''

# -*- coding: utf-8 -*-

def search_bin(lista1, lista2):
    '''
    Função que compara duas listas e retorna nomes semelhantes.
    testando o método de busca binário
    :param lista1: variável do tipo list com nomes, vestibular
    :param lista2: variável do tipo list com nomes alunos
    :return: dicionário de nomes
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
    :param lista1: variável do tipo list com nomes, vestibular
    :param lista2: variável do tipo list com nomes alunos
    :return: dicionário de nomes com o número de vezes que o nome é encontrado
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
               "ü": "U", "Â": "A", "À": "A", "Á": "A", "Ã": "A", "Ä": "A", "È": "E", "É": "E", \
               "Ê": "E", "Ë": "E", "Ì": "I", "Í": "I", "Î": "I", "Ò": "O", "Ó": "O", \
               "Ô": "O", "Õ": "O", "Ö": "O", "Ù": "U", "Ú": "U", "Û": "U", "Ü": "U", \
               "ç": "C", "Ç": "C", "ñ": "N", "Ñ": "N"
               }

    for letra in palavra:
        if letra in acentos:
            x = palavra.find(letra)
            palavra = list(palavra)
            palavra[x] = acentos.get(letra)
            palavra = "".join(palavra)

    return palavra
