# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
numero_1 = int(input("Digite o primeiro número: "))
numero_2 = int(input("Digite o segundo número: "))
print(numero_1 + numero_2)

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
numero_1 = int(input("Digite o primeiro número: "))
print(numero_1 % 5)

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
numero_1 = int(input("Digite o primeiro número: "))
numero_2 = int(input("Digite o segundo número: "))
print(numero_1 * numero_2)

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
try:
    numero_1 = int(input("Digite o primeiro número: "))
    numero_2 = int(input("Digite o segundo número: "))
    print(numero_1 // numero_2)
except ZeroDivisionError:
    print("Não é posível fazer divisão por zero ")
except KeyboardInterrupt:
    print("Você não inseriu um número ")

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
numero_1 = int(input("Digite o primeiro número: "))
print(numero_1 * numero_1)

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


# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação