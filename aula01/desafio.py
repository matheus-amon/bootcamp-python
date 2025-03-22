name = input("Qual é o seu nome? ")
wage = float(input("Qual é o seu salário? "))
bonus = float(input("Qual é o valor do bônus? "))

def calc_bonus(wage, bonus):
    total = 1000 + (wage * bonus)
    return total

def print_bonus(name, total):
    print(f"Olá {name}, o seu bônus é de R$ {total:.2f}")

print_bonus(name, calc_bonus(wage, bonus))
