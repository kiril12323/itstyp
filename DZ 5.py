def print_board(board):
    print("\n   0   1   2")
    for i, row in enumerate(board):
        print(f"{i}  " + " | ".join(row))
        if i < 2:
            print("  ---+---+---")
    print()

def check_win(board, player):
    for i in range(3):
        if all([cell == player for cell in board[i]]) or \
           all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def get_move(player):
    while True:
        try:
            move = input(f"Гравець {player}, введіть координати (рядок і стовпець): ")
            row, col = map(int, move.split())
            if row not in range(3) or col not in range(3):
                raise ValueError
            return row, col
        except ValueError:
            print("❌ Невірне введення. Введіть два числа від 0 до 2 через пробіл.")

def play_game():
    scores = {"X": 0, "O": 0}
    while True:
        board = [[" " for _ in range(3)] for _ in range(3)]
        current_player = "X"
        print("\n=== Нова гра 'Крестики-нолики' ===")
        print_board(board)

        while True:
            row, col = get_move(current_player)
            if board[row][col] != " ":
                print("⚠️ Клітинка зайнята!")
                continue
            board[row][col] = current_player
            print_board(board)

            if check_win(board, current_player):
                print(f"🎉 Гравець {current_player} переміг!")
                scores[current_player] += 1
                break
            if is_full(board):
                print("🤝 Нічия!")
                break

            current_player = "O" if current_player == "X" else "X"

        print(f"🔢 Рахунок: X = {scores['X']} | O = {scores['O']}")
        again = input("🔁 Зіграти ще раз? (так/ні): ").lower()
        if again != "так":
            print("🏁 Кінцевий рахунок:")
            print(f"X: {scores['X']} перемог")
            print(f"O: {scores['O']} перемог")
            print("Дякуємо за гру!")
            break

play_game()