# =======================================================
# Projeto: Calculadora Python
# Desenvolvedor: Mateusreis197
# GitHub: https://github.com/Mateusreis197
# =======================================================

# 1. Definição das funções para cada operação
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: Divisão por zero não é permitida!"
    return a / b

# 2. Exibição do menu
print("================================")
print("       CALCULADORA PYTHON       ")
print("  Desenvolvido por: Mateusreis197")
print("================================")
print("Escolha a operação desejada:")
print("1 - Adição (+)")
print("2 - Subtração (-)")
print("3 - Multiplicação (*)")
print("4 - Divisão (/)")
print("================================")

# 3. Leitura da escolha
opcao = input("Digite a opção (1, 2, 3 ou 4): ")

# 4. Verificação e cálculo
if opcao in ['1', '2', '3', '4']:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if opcao == '1':
        resultado = somar(num1, num2)
        print(f"\nResultado: {num1} + {num2} = {resultado}")
    elif opcao == '2':
        resultado = subtrair(num1, num2)
        print(f"\nResultado: {num1} - {num2} = {resultado}")
    elif opcao == '3':
        resultado = multiplicar(num1, num2)
        print(f"\nResultado: {num1} * {num2} = {resultado}")
    elif opcao == '4':
        resultado = dividir(num1, num2)
        print(f"\nResultado: {num1} / {num2} = {resultado}")
else:
    print("\nOpção inválida! Escolha um número de 1 a 4.")
