# calculator.py

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def main():
    print("Bem-vindo à Calculadora!")
    print("Escolha uma operação:")
    print("1. Adição")
    print("2. Subtração")

    choice = input("Digite o número da operação desejada: ")

    if choice in ['1', '2']:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
    else:
        print("Opção inválida")

if __name__ == "__main__":
    main()
