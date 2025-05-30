# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
numero_1 = int(input("Digite o primeiro número: "))
numero_2 = int(input("Digite o segundo número: "))
resultado = numero_1 + numero_2
print(resultado)

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
numero_1 = int(input("Digite um número: "))
resultado = numero_1 % 5
print(resultado)

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
numero_1 = int(input("Digite o primeiro número: "))
numero_2 = int(input("Digite o segundo número: "))
resultado = numero_1 * numero_2
print(resultado)

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
try:
    numero_1 = int(input("Digite o primeiro número: "))
    numero_2 = int(input("Digite o segundo número: "))
    resultado = numero_1 // numero_2
    print(resultado)
except ZeroDivisionError:
    print("Não é posível fazer divisão por zero ")
except KeyboardInterrupt:
    print("Você não inseriu um número ")

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
num = int(input("Digite um número: "))
resultado = num ** 2
print(resultado)

# #### Números de Ponto Flutuante (`float`)
# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
numero_1 = float(input("Digite o primeiro número: "))
numero_2 = float(input("Digite o segundo número: "))
print(numero_1 + numero_2)
# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
numero_1 = float(input("Digite o primeiro número: "))
numero_2 = float(input("Digite o segundo número: "))
print((numero_1 + numero_2)/2)
# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
numero_1 = float(input("Digite o primeiro número: "))
numero_2 = float(input("Digite o segundo número: "))
print(numero_1 ** numero_2)
# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
numero_1 = float(input("Digite a temperatura em Celsius: "))
print(numero_1 * 1.8 + 32)
# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
raio = float(input("Digite o raio do círculo: "))
area = 3.14159265 * (raio ** 2)
print(f"A área do círculo é: {area}")
      
# #### Strings (`str`)
# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
string = input("Escreva uma palavra: ")
print(string.upper())
# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
string = input("Escreva seu nome completo: ")
print(string.lower())
# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
string = input("Escreva uma frase: ")
print(string.strip())
# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
string = input("Digite uma data no formato 'dd/mm/aaaa': ")
print(string.split("/"))
# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
str_1 = input("Escreva uma palavra: ")
str_2 = input("Escreva outra palavra: ")
resultado = print(str_1 + str_2)
print(resultado)

# #### Booleanos (`bool`)
# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
expressao_1 = True
expressao_2 = False
resultado = expressao_1 and expressao_2
print(f"O resultado do AND lógico é {resultado}")

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
expressao_1 = True
expressao_2 = False
resultado = expressao_1 or expressao_2
print(f"O resultado do OR lógico é {resultado}")

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
expressao = input("Insira True ou False: ")
resultado = expressao.lower() == "true"
invertido = not resultado
print(invertido)

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
numero_1 = float(input("Digite um número: "))
numero_2 = float(input("digite outro número: "))
resultado_diferenca = numero_1 == numero_2
print(resultado_diferenca)

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
numero_1 = float(input("Digite um número: "))
numero_2 = float(input("digite outro número: "))
resultado_diferenca = numero_1 != numero_2
print(resultado_diferenca)

# #### try-except e if
# 21: Conversor de Temperatura
try:
    temperatura_celcius = float(input("Digite uma tempertura em graus Celcius: "))
    temperatura_far = (temperatura_celcius * 1.8) + 32
    print(temperatura_far)
except ValueError as e:
    print(e)
except:
    print("Algo deu errado")

# 22: Verificador de Palíndromo
entrada = input("Digite uma palavra ou frase: ")
if isinstance(entrada, str):
    entrada_formatada = entrada.replace(" ", "").lower()
    if entrada_formatada == entrada_formatada[::-1]:
        print("É um palídromo")
    else:
        print("Não é um palídromo")
    
# 23: Calculadora Simples
try:
    num_1 = float(input("Digite um número: "))
    num_2 = float(input("Digite outro número: "))
    operador = (input("Escolha um operador, (+, -, * e /) : "))
    if operador == "+":
        resultado = num_1 + num_2
    elif operador == "-":
        resultado = num_1 - num_2
    elif operador == "*":
        resultado = num_1 * num_2
    elif operador == "/":
        resultado = num_1 / num_2
    else:
        print("Operador inválido ou divisão por zero.")
    print(f"O resultado é: {resultado}")
except:
    print("Erro: entrada inválida.")

# 24: Classificador de Números
try:
    num = int(input("Digite um número inteiro: "))
    if num % 2 == 0:
        print("O num é par")
    else:
        print("O num é ímpar")
    if num > 0:
        print("O num é positivo")
    elif num == 0:
        print("O num é zero")
    else:
        print("O num é negativo")
except:
    print("Você não digitou um número inteiro")
    
# 25: Conversão de Tipo com Validação
entrada = input("Digite uma sequência de números inteiros separados por vírgula: ")
entrada_split = entrada.split(",")
num_int = []
try:
    for num in entrada_split:
        num_int.append(int(num.strip()))
    print(f"Lista de números inteiros: {num_int}")
except ValueError:
    print("Erro: certifique-se de que todos os elementos são números inteiros válidos.")
