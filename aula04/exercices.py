# 1. Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
for i in range(1, 11):
    print(i ** 2)

# 2. Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".
langs: list = ["Python", "Java", "C++", "JavaScript"]
langs.remove("C++")
langs.append("Ruby")
print(langs)

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
emails = [
    'matheus.amon@outlook.com', 'mathesamon@gmail.com', 'amoncpbi@gmail.com',
    'matheus.amon@singlesoftware.com', 'mathesamon@gmail.com', 'amoncpbi@gmail.com'
]

def remove_emails_duplicates(emails: list) -> list:
    return list(set(emails))

print(remove_emails_duplicates(emails=emails))

# 7. Filtragem de Dados
# Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.
ages: list = [
    12, 13, 12, 56, 43, 57, 34, 23, 12, 65, 97, 12, 75, 42, 46, 35, 23, 17, 16,
    13, 14, 15, 16, 2, 5, 9, 2, 6, 8, 0, 10, 35, 86, 35, 23, 54, 76, 45, 15, 14
]

def filter_ages(ages: list) -> list:
    return [age for age in ages if age >= 18]

filtered_ages: list = filter_ages(ages=ages)
print(filtered_ages)

# 8. Ordenação Personalizada
# Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.
'''Essa eu peguei do gabarito pois não consegui elaborar a lógica do exercício'''
persons = [
    {"nome": "Alice", "idade": 30},
    {"nome": "Bob", "idade": 25},
    {"nome": "Carol", "idade": 20}
]
persons.sort(key=lambda pessoa: pessoa["nome"])

print(persons)

# 9. Agregação de Dados
# Objetivo: Dado um conjunto de números, calcular a média.
numbers = [10, 20, 30, 40, 50]

def calc_avg_list(numbers: list) -> float:
    total = sum(numbers)
    size = len(numbers)
    avg = total / size
    return avg

print(calc_avg_list(numbers=numbers))

# 10. Divisão de Dados em Grupos
# Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.
values: list = [
    12, 13, 12, 56, 43, 57, 34, 23, 12, 65, 97, 12, 75, 42, 46, 35, 23, 17, 16,
    13, 14, 15, 16, 2, 5, 9, 2, 6, 8, 0, 10, 35, 86, 35, 23, 54, 76, 45, 15, 14
]

evens: list = [even for even in values if not even % 2]
odds: list = [odd for odd in values if odd % 2]

print(odds, evens)

# 11. Atualização de Dados
# Objetivo: Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.
products: list = [
    {"id": 1, "nome": "Teclado", "preço": 100},
    {"id": 2, "nome": "Mouse", "preço": 80},
    {"id": 3, "nome": "Monitor", "preço": 300}
]

for product in products:
    if product['id'] == 2:
        product['preço'] = 90

print(products)

# 12. Fusão de Dicionários
# Objetivo: Dados dois dicionários, fundi-los em um único dicionário.
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

dict3 = {**dict1, **dict2}

print(dict3)

# 13. Filtragem de Dados em Dicionário
# Objetivo: Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.
stock = {"Teclado": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}
stock = {product: qt for product, qt in stock.items() if qt > 0}

print(stock)

# 14. Extração de Chaves e Valores
# Objetivo: Dado um dicionário, criar listas separadas para suas chaves e valores.
example: dict = {"a": 1, "b": 2, "c": 3}
keys: list = list(example.keys())
values: list = list(example.values())

print(keys, values)

# 15. Contagem de Frequência de Itens
# Objetivo: Dada uma string, contar a frequência de cada caractere usando um dicionário.
text: str = 'matheus amon cunha figueiredo marçal'
frequency: dict = {}
for i in text:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1

print(frequency)

# 16. Soma de Números
# Escreva uma função que receba uma lista de números e retorne a soma de todos os números.
def list_sum(numbers: list):
    return numbers.sum()

# 17. Verificação de Número Primo
# Crie uma função que receba um número como argumento e retorne True se o número for primo e False caso contrário.
def is_cousin(number: int) -> bool:
    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True

# 18. Reversão de String
# Desenvolva uma função que receba uma string como argumento e retorne essa string revertida.
def reverse_string(string: str) -> str:
    return string[::-1]

# 19. Combinação de Pares com Soma
# Implemente uma função que receba dois argumentos: uma lista de números e um número. 
# A função deve retornar todas as combinações de pares na lista que somem ao número dado.
def find_pairs(numbers: list, target: int) -> list:
    pairs: list = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                pairs.append((numbers[i], numbers[j]))
    return pairs

# 20. Ordenação de Chaves de Dicionário
# Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas.
def sort_dict_keys(d: dict) -> list:
    return sorted(d.keys())
