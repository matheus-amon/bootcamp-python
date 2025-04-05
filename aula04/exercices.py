# 1. Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
for i in range(1, 11):
    print(i ** 2)

# 2. Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".
langs: list = ["Python", "Java", "C++", "JavaScript"]
langs.remove("C++")
langs.append("Ruby")

# 3. Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.
livro: dict = {
    "title": "Jornada de Dados",
    "author": "Luciano",
    "publication_year": 2023
}

keys: list = list(livro.keys())
for i in keys:
    print(f"{i}: {livro[i]}")

# 4. Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
def contar_caracteres(s):
    '''Essa eu peguei do gabarito pois não consegui interpretar o exercício'''
    contagem = {}
    for caractere in s:
        contagem[caractere] = contagem.get(caractere, 0) + 1
    return contagem

print(contar_caracteres("engenharia de dados"))

# 5. Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.
fruits = ["maçã", "banana", "cereja"]
fruits_prices = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
prices: list = []
for fruit in fruits:
    price = fruits_prices[fruit]
    prices.append(price)

print(sum(prices))

# 6. Eliminação de Duplicatas
# Objetivo: Dada uma lista de emails, remover todos os duplicados.

# 7. Filtragem de Dados
# Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.

# 8. Ordenação Personalizada
# Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.

# 9. Agregação de Dados
# Objetivo: Dado um conjunto de números, calcular a média.

# 10. Divisão de Dados em Grupos
# Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.

# Exercícios com Dicionários

# 11. Atualização de Dados
# Objetivo: Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.

# 12. Fusão de Dicionários
# Objetivo: Dados dois dicionários, fundi-los em um único dicionário.

# 13. Filtragem de Dados em Dicionário
# Objetivo: Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.

# 14. Extração de Chaves e Valores
# Objetivo: Dado um dicionário, criar listas separadas para suas chaves e valores.

# 15. Contagem de Frequência de Itens
# Objetivo: Dada uma string, contar a frequência de cada caractere usando um dicionário.

# 16. Soma de Números
# Escreva uma função que receba uma lista de números e retorne a soma de todos os números.

# 17. Verificação de Número Primo
# Crie uma função que receba um número como argumento e retorne True se o número for primo e False caso contrário.

# 18. Reversão de String
# Desenvolva uma função que receba uma string como argumento e retorne essa string revertida.

# 19. Combinação de Pares com Soma
# Implemente uma função que receba dois argumentos: uma lista de números e um número. 
# A função deve retornar todas as combinações de pares na lista que somem ao número dado.

# 20. Ordenação de Chaves de Dicionário
# Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas.
