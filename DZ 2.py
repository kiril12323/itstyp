import random


def task1():
    name = input("Введіть ваше ім'я: ")
    age = int(input("Введіть ваш вік: "))
    print(f"Привіт {name}, тобі {age}!")


def task2():
    age = int(input("Введіть ваш вік: "))
    if age > 18:
        print("Вхід дозволено!")
    else:
        print("Вхід заборонено!")


def task3():
    number = random.randint(1, 10)
    attempts = 3
    print("Я загадав число від 1 до 10. Спробуй вгадати!")
    while attempts > 0:
        guess = int(input("Ваше число: "))
        if guess < number:
            print("Більше")
        elif guess > number:
            print("Менше")
        else:
            print("Ви вгадали!")
            return
        attempts -= 1
    print(f"На жаль, ви програли. Загадане число було {number}.")


def task4():
    start = int(input("Введіть початкове число: "))
    end = int(input("Введіть кінцеве число: "))
    for i in range(start, end + 1):
        print(i, end=" ")
    print()


def task5():
    n = int(input("Введіть число n: "))
    for i in range(n, 0, -1):
        if i % 2 == 0:
            print(i, end=" ")
    print()


def task6():
    n = int(input("Введіть число n для обчислення факторіалу: "))
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print(f"Факторіал числа {n} дорівнює {factorial}.")


def task7():
    score = int(input("Введіть кількість балів: "))
    if 0 <= score <= 49:
        print("Оцінка: незадовільно.")
    elif 50 <= score <= 69:
        print("Оцінка: задовільно.")
    elif 70 <= score <= 89:
        print("Оцінка: добре.")
    elif 90 <= score <= 100:
        print("Оцінка: відмінно.")
    else:
        print("Некоректна кількість балів.")


def task8():
    a = float(input("Введіть перше число (a): "))
    b = float(input("Введіть друге число (b): "))
    operation = input("Оберіть дію (+, -, *, /): ")
    if operation == "+":
        print(f"Результат: {a + b}")
    elif operation == "-":
        print(f"Результат: {a - b}")
    elif operation == "*":
        print(f"Результат: {a * b}")
    elif operation == "/":
        if b == 0:
            print("Ділення на нуль!")
        else:
            print(f"Результат: {a / b}")
    else:
        print("Некоректна операція.")


def main():
    while True:
        print("\nОберіть завдання:")
        print("1. Програма з ім'ям та віком")
        print("2. Перевірка віку")
        print("3. Гра 'Вгадай число'")
        print("4. Виведення чисел у діапазоні")
        print("5. Парні числа у зворотному порядку")
        print("6. Обчислення факторіалу")
        print("7. Визначення оцінки студента")
        print("8. Калькулятор")
        print("0. Вихід")

        choice = input("Ваш вибір: ")
        if choice == "1":
            task1()
        elif choice == "2":
            task2()
        elif choice == "3":
            task3()
        elif choice == "4":
            task4()
        elif choice == "5":
            task5()
        elif choice == "6":
            task6()
        elif choice == "7":
            task7()
        elif choice == "8":
            task8()
        elif choice == "0":
            print("До побачення!")
            break
        else:
            print("Некоректний вибір, спробуйте ще раз.")


if __name__ == "__main__":
    main()