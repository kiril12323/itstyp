import random


def display_rules():
    print("\nПравила игры 'Камень, ножницы, бумага':")
    print("1. Камень побеждает ножницы.")
    print("2. Ножницы побеждают бумагу.")
    print("3. Бумага побеждает камень.")
    print("4. Чтобы выйти из игры, введите 'выход'.")
    print("5. Игра состоит из нескольких раундов. Побеждает тот, кто наберет больше очков.")
    print()


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Ничья"
    elif (user_choice == "камень" and computer_choice == "ножницы") or \
            (user_choice == "ножницы" and computer_choice == "бумага") or \
            (user_choice == "бумага" and computer_choice == "камень"):
        return "Вы"
    else:
        return "Компьютер"


def play_rps():
    print("Добро пожаловать в улучшенную версию игры 'Камень, ножницы, бумага'!")
    display_rules()

    options = ["камень", "ножницы", "бумага"]
    user_score = 0
    computer_score = 0
    round_number = 1

    while True:
        print(f"\nРаунд {round_number}:")
        print(f"Счет: Вы - {user_score}, Компьютер - {computer_score}")
        user_choice = input("Ваш выбор (камень, ножницы, бумага): ").lower()

        if user_choice == "выход":
            print("\nВы завершили игру. Подсчет окончательных результатов...")
            break

        if user_choice not in options:
            print("Неверный ввод. Пожалуйста, выберите 'камень', 'ножницы' или 'бумага'.")
            continue

        computer_choice = random.choice(options)
        print(f"Компьютер выбрал: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)

        if winner == "Ничья":
            print("Ничья в этом раунде!")
        elif winner == "Вы":
            print("Вы выиграли этот раунд!")
            user_score += 1
        else:
            print("Компьютер выиграл этот раунд!")
            computer_score += 1

        round_number += 1

    print("\nИтоговый счет:")
    print(f"Вы - {user_score}, Компьютер - {computer_score}")

    if user_score > computer_score:
        print("Поздравляем! Вы выиграли игру!")
    elif user_score < computer_score:
        print("Компьютер победил в игре. Удачи в следующий раз!")
    else:
        print("Игра закончилась вничью!")
    print("Спасибо за игру!")


if __name__ == "__main__":
    play_rps()