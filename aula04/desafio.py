import back_end as be

def main():
    try:
        name = be.get_valid_name("Qual é o seu nome? ")
        wage = be.get_valid_type("Qual é o seu salário? ", float, valid_range=(1509, float('inf')))
        bonus = be.get_valid_type("Qual é a porcentagem do bônus? ", float, valid_range=(0, 1))

        be.validate_variables(name, wage, bonus)
        be.show_success(name, wage, bonus)
        be.show_bonus(name, be.calc_bonus(wage, bonus))

    except ValueError as e:
        print(f"\nERROR: {e}")

if __name__ == "__main__":
    main()
