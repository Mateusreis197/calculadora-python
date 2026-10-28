import os
from dotenv import load_dotenv

# Carrega as variáveis declaradas no arquivo .env (se existir)
load_dotenv()

APP_NAME = os.getenv("APP_NAME", "Calculadora Python")
PRECISAO = int(os.getenv("PRECISAO_DECIMAL", 2))

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("Não é possível dividir por zero.")
    return a / b

def exibir_menu():
    print("=" * 36)
    print(f"       {APP_NAME.upper()}       ")
    print("       Autor: Mateusreis197        ")
    print("=" * 36)
    print("1 - Adição (+)")
    print("2 - Subtração (-)")
    print("3 - Multiplicação (*)")
    print("4 - Divisão (/)")
    print("0 - Sair")
    print("=" * 36)

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == '0':
            print("\nEncerrando a calculadora. Até mais!")
            break

        if opcao in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))

                if opcao == '1':
                    resultado = somar(num1, num2)
                    simbolo = "+"
                elif opcao == '2':
                    resultado = subtrair(num1, num2)
                    simbolo = "-"
                elif opcao == '3':
                    resultado = multiplicar(num1, num2)
                    simbolo = "*"
                elif opcao == '4':
                    resultado = dividir(num1, num2)
                    simbolo = "/"

                print(f"\n=> Resultado: {num1} {simbolo} {num2} = {round(resultado, PRECISAO)}\n")

            except ValueError as erro:
                print(f"\n[Aviso] Entrada inválida ou erro matemático: {erro}\n")
        else:
            print("\n[Opção Inválida] Escolha um número de 0 a 4.\n")

if __name__ == "__main__":
    main()