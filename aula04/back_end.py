def calc_bonus(wage: float, bonus: float) -> float:
    return 1000 + (wage * bonus)

def show_bonus(name: str, total: float) -> float:
    print(f"\nOlá {name}, o seu bônus é de R$ {total:.2f}")

def validate_variables(name: str, wage: float, bonus: float):
    name = name.strip()
    if not name:
        raise ValueError("O nome não pode ser vazio.")
    if len(name) < 3:
        raise ValueError("O nome deve ter pelo menos 3 caracteres.")
    if len(name) > 50:
        raise ValueError("O nome deve ter no máximo 50 caracteres.")
    if not all(x.isalpha() or x.isspace() for x in name):
        raise ValueError("O nome deve conter apenas letras e espaços.")

    if not isinstance(wage, (int, float)):
        raise ValueError("O salário deve ser um número.")
    if wage < 1509:
        raise ValueError("O salário deve ser igual ou maior que R$ 1509.")

    if not isinstance(bonus, (int, float)):
        raise ValueError("A porcentagem do bônus deve ser um número.")
    if not (0 <= bonus <= 1):
        raise ValueError("A porcentagem do bônus deve estar entre 0 e 1.")

def show_success(name, wage, bonus):
    print("\nDados validados com sucesso!")
    print(f"Nome: {name}")
    print(f"Salário: R$ {wage:.2f}")
    print(f"Bônus: {bonus * 100:.2f}%")

def get_valid_name(prompt):
    while True:
        name = input(prompt).strip()
        if not all(x.isalpha() or x.isspace() for x in name):
            print("O nome deve conter apenas letras e espaços. Tente novamente.")
        elif len(name) < 3:
            print("O nome deve ter pelo menos 3 caracteres. Tente novamente.")
        else:
            return name

def get_valid_type(prompt, type_func, valid_range=None):
    while True:
        try:
            value = type_func(input(prompt).strip())
            if valid_range and not (valid_range[0] <= value <= valid_range[1]):
                print(f"O valor deve estar entre {valid_range[0]} e {valid_range[1]}. Tente novamente.")
            else:
                return value
        except ValueError:
            print(f"Valor inválido. Tente novamente.")
