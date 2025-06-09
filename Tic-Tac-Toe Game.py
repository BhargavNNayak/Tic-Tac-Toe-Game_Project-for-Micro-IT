import tkinter as tk
from tkinter import messagebox

# Initialize main window
root = tk.Tk()
root.title("🎮 Tic-Tac-Toe")
root.geometry("300x350")
root.resizable(False, False)

# Game variables
current_player = "X"
board = [["" for _ in range(3)] for _ in range(3)]
buttons = []

# Function to handle clicks
def on_click(row, col):
    global current_player
    if board[row][col] == "":
        board[row][col] = current_player
        buttons[row][col].config(text=current_player, state="disabled")
        if check_winner(current_player):
            messagebox.showinfo("Game Over", f"🏆 Player {current_player} wins!")
            root.quit()
        elif check_draw():
            messagebox.showinfo("Game Over", "🤝 It's a draw!")
            root.quit()
        else:
            current_player = "O" if current_player == "X" else "X"

# Check winner
def check_winner(player):
    # Check rows, columns, diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Check draw
def check_draw():
    return all(board[i][j] != "" for i in range(3) for j in range(3))

# GUI layout
frame = tk.Frame(root)
frame.pack(pady=20)

for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(frame, text="", font=("Arial", 20), width=5, height=2,
                        command=lambda i=i, j=j: on_click(i, j))
        btn.grid(row=i, column=j, padx=5, pady=5)
        row.append(btn)
    buttons.append(row)

# Start GUI loop
root.mainloop()
