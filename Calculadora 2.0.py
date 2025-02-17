import math

# Funções de operações científicas
def adicionar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro! Divisão por zero."

def potencia(x, y):
    return x ** y

def raiz(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return "Erro! Raiz quadrada de número negativo."

def seno(x):
    return math.sin(math.radians(x))

def cosseno(x):
    return math.cos(math.radians(x))

def tangente(x):
    return math.tan(math.radians(x))

def logaritmo(x):
    if x > 0:
        return math.log(x)
    else:
        return "Erro! Logaritmo de número não positivo."

def exponencial(x):
    return math.exp(x)

# Função para o menu
def menu():
    print("\nCalculadora Científica")
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Potência")
    print("6. Raiz Quadrada")
    print("7. Seno")
    print("8. Cosseno")
    print("9. Tangente")
    print("10. Logaritmo Natural")
    print("11. Exponencial")
    print("0. Sair")

# Função principal da calculadora
def calculadora():
    while True:
        menu()
        escolha = input("Digite o número da operação (0 para sair): ")

        if escolha == '0':
            print("Saindo da calculadora...")
            break

        if escolha in ('1', '2', '3', '4', '5'):
            num1 = float(input("Digite o primeiro número: "))

            if escolha != '6' and escolha != '7' and escolha != '8' and escolha != '9' and escolha != '10' and escolha != '11':
                num2 = float(input("Digite o segundo número: "))
            
            if escolha == '1':
                print(f"{num1} + {num2} = {adicionar(num1, num2)}")
            elif escolha == '2':
                print(f"{num1} - {num2} = {subtrair(num1, num2)}")
            elif escolha == '3':
                print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
            elif escolha == '4':
                print(f"{num1} / {num2} = {dividir(num1, num2)}")
            elif escolha == '5':
                print(f"{num1} ^ {num2} = {potencia(num1, num2)}")

        elif escolha == '6':
            num1 = float(input("Digite o número para calcular a raiz quadrada: "))
            print(f"Raiz quadrada de {num1} = {raiz(num1)}")

        elif escolha == '7':
            num1 = float(input("Digite o ângulo (em graus) para calcular o seno: "))
            print(f"Seno de {num1}° = {seno(num1)}")

        elif escolha == '8':
            num1 = float(input("Digite o ângulo (em graus) para calcular o cosseno: "))
            print(f"Cosseno de {num1}° = {cosseno(num1)}")

        elif escolha == '9':
            num1 = float(input("Digite o ângulo (em graus) para calcular a tangente: "))
            print(f"Tangente de {num1}° = {tangente(num1)}")

        elif escolha == '10':
            num1 = float(input("Digite o número para calcular o logaritmo natural: "))
            print(f"Logaritmo de {num1} = {logaritmo(num1)}")

        elif escolha == '11':
            num1 = float(input("Digite o número para calcular a exponencial: "))
            print(f"Exponencial de {num1} = {exponencial(num1)}")

        else:
            print("Opção inválida! Tente novamente.")

# Chama a função da calculadora
calculadora()
