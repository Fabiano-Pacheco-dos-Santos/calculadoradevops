# calc.py

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Erro: Divisão por zero!"
    return x / y


def remainder(x, y):
    return x % y


def main():
    print("Bem-vindo à Calculadora!")
    print("Escolha uma operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. resto")

    choice = input("Digite o número da operação desejada para calcular o resultado: ")

    if choice in ['1', '2', '3', '4', '5']:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        elif choice == '5':
            print(f"{num1} % {num2} = {remainder(num1, num2)}")
    else:
        print("Opção inválida, digite novamente")


if __name__ == "__main__":
    main()
