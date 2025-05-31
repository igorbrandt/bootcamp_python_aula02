### Desafio - Refatorar o projeto da aula anterior evitando Bugs!

CONSTANTE_BONUS = 1000
# 1) Solicita ao usuário que digite seu nome
try:
    nome_usuario = input("Digite seu nome: ")

    # Verifica se o nome está vazio
    if len(nome_usuario) == 0:
        raise ValueError("O nome não pode ser vazio.")
    # Verifica se há números no nome
    elif any(char.isdigit() for char in nome_usuario):
        raise ValueError("O nome não pode conter números.")
    else: 
        print("Nome válido.")
except ValueError as e:
    print(f"Erro: {e}")

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
try:
    salario_usuario = float(input("Digite o valor do seu salario: "))
except ValueError:
    print("Você não digitou um valor.")

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
try:
    bonus_usuario = float(input("Digite o valor do seu bônus: "))
    if bonus_usuario < 0:
        raise ValueError("O valor não pode ser negativo")    
except ValueError as e:
    print(f"Erro: {e}")

# 4) Calcule o valor do bônus final
bonus_final = CONSTANTE_BONUS + salario_usuario * bonus_usuario

# 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
print(f"Nome: {nome_usuario}, Salário: R${salario_usuario:.2f}, Bônus Final: R${bonus_final:.2f}")

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?



