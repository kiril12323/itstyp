a = float(input("Введите первое число: "))
op = input("Выберите операцию (+, -, *, /): ")
b = float(input("Введите второе число: "))

if op == '+':
    print("Результат:", a + b)
elif op == '-':
    print("Результат:", a - b)
elif op == '*':
    print("Результат:", a * b)
elif op == '/':
        print("Результат:", a / b)