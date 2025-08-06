# Simple Calculator

def main():
    print("Simple Calculator")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Choose operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    choice = input("Enter choice (1/2/3/4): ")

    if choice == '1' or choice == '+':
        result = num1 + num2
        op = '+'
    elif choice == '2' or choice == '-':
        result = num1 - num2
        op = '-'
    elif choice == '3' or choice == '*':
        result = num1 * num2
        op = '*'
    elif choice == '4' or choice == '/':
        if num2 == 0:
            print("Error: Division by zero!")
            return
        result = num1 / num2
        op = '/'
    else:
        print("Invalid choice.")
        return

    print(f"{num1} {op} {num2} = {result}")

if __name__ == "__main__":
    main()