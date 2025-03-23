### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.
quantidade = 10
preco = 20.0

if quantidade > 0 and preco > 0:
    print("Dados válidos")
else:
    print("Dados inválidos")

### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
temp = 25.0

if temp < 15:
    status = "Baixa"
elif 15 <= temp <= 30:
    status = "Normal"
else:
    status = "Alta"

print(f"Temperatura: {temp}°C - Status: {status}")

### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.
log = {
    'timestamp': '2021-06-23 10:00:00',
    'level': 'ERROR',
    'message': 'Falha na conexão'
}

if log['level'] == 'ERROR':
    print(f"{log['timestamp']} - {log['level']}: {log['message']}")
else:
    print("Nenhum erro encontrado")

### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.
age = 25
email = "nome@gmail.com"
valid_email = "@" in email and "." in email.split("@")[-1]
valid_age = 18 <= age <= 65

if valid_age and valid_email:
    print("Dados de usuário válidos")
else:
    if not valid_age:
        print("Idade inválida. Deve estar entre 18 e 65 anos.")
    if not valid_email:
        print("Email inválido. Deve conter '@' e '.'")

### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.
transacao = {
    'valor': 12000,
    'hora': 20
}

if transacao['valor'] > 10000 or transacao['hora'] < 9 or transacao['hora'] > 18:
    print("Transação suspeita")
else:
    print("Transação normal")

### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.
texto = "Python é uma linguagem de programação. Python é fácil de aprender."

palavras = texto.lower().replace('.', '').split()
contagem = {}

for palavra in palavras:
    if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1

### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.
lista_numeros = [10, 20, 30, 40, 50]
minimo = min(lista_numeros)
maximo = max(lista_numeros)
normalizados = [(num - minimo) / (maximo - minimo) for num in lista_numeros]

### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico 
#faltando
dicionarios = [
    {'nome': 'Alice', 'idade': 25},
    {'nome': 'Bob', 'idade': None},
    {'nome': 'Charlie', 'idade': 30}
]
usuarios_validos = [usuario for usuario in dicionarios if usuario['idade'] is not None]

print("Usuários válidos:", usuarios_validos)

### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.
lista_numeros = [1, 2, 3, 4, 5, 6]
numeros_pares = [num for num in lista_numeros if num % 2 == 0]

### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.
data = [
    {'categoria': 'eletrônicos', 'valor': 100},
    {'categoria': 'roupas', 'valor': 50},
    {'categoria': 'eletrônicos', 'valor': 200},
]
vendas_por_categoria = {}
for registro in data:
    categoria = registro['categoria']
    valor = registro['valor']
    if categoria in vendas_por_categoria:
        vendas_por_categoria[categoria] += valor
    else:
        vendas_por_categoria[categoria] = valor
print("Vendas por categoria:", vendas_por_categoria)

### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.
data = []
while True:
    entrada = input("Digite um valor (ou 'sair' para encerrar): ")
    if entrada.lower() == "sair":
        break
    data.append(entrada)
print("Dados lidos:", data)

### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.
entrada_valida = False
while not entrada_valida:
    try:
        numero = int(input("Digite um número entre 1 e 10: "))
        if 1 <= numero <= 10:
            entrada_valida = True
        else:
            print("Número fora do intervalo. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")

### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.
json_data = [
    {'pagina': 1, 'dados': [1, 2, 3]},
    {'pagina': 2, 'dados': [4, 5, 6]},
    {'pagina': 3, 'dados': []}  # Página vazia indica fim
]
pagina = 0
while pagina < len(json_data):
    dados = json_data[pagina]['dados']
    if not dados:  # Se a página estiver vazia, encerra o loop
        break
    print(f"Processando dados da página {pagina + 1}: {dados}")
    pagina += 1

### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.
reconexoes = 0
max_tentativas = 5
while reconexoes < max_tentativas:
    try:
        print(f"Tentativa de conexão {reconexoes + 1}")
        raise ConnectionError("Falha na conexão")
    except ConnectionError as e:
        print(e)
        reconexoes += 1
        if reconexoes == max_tentativas:
            print("Máximo de tentativas atingido. Encerrando.")
        else:
            print("Tentando novamente...")

### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.
data = [1, 2, 3, 4, 5, 'parar', 6, 7]
for item in data:
    if item == 'parar':
        print("Processamento interrompido.")
        break
    print(f"Processando item: {item}")
