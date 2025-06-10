import tkinter as tk
import time
import threading

# Initialize main window
root = tk.Tk()
root.title("🎮 Tic-Tac-Toe")
root.geometry("320x380")
root.configure(bg="#f0f0f0")
root.resizable(False, False)

current_player = "X"
board = [["" for _ in range(3)] for _ in range(3)]
buttons = []

BUTTON_STYLE = {
    "font": ("Helvetica", 24, "bold"),
    "width": 4,
    "height": 2,
    "bg": "#ffffff",
    "fg": "#000000",
    "activebackground": "#d0f0c0",
    "relief": "groove",
    "bd": 3
}

# Button click logic
def on_click(row, col):
    global current_player
    if board[row][col] == "":
        board[row][col] = current_player
        buttons[row][col].config(text=current_player, state="disabled", disabledforeground="#000000")
        if check_winner(current_player):
            show_custom_popup(f"🏆 Player {current_player} Wins!")
            disable_all_buttons()
        elif check_draw():
            show_custom_popup("🤝 It's a Draw!")
        else:
            current_player = "O" if current_player == "X" else "X"

# Check winner
def check_winner(player):
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

# Disable all buttons
def disable_all_buttons():
    for row in buttons:
        for btn in row:
            btn.config(state="disabled")

# Hover effects
def on_enter(e):
    if e.widget["state"] == "normal":
        e.widget["bg"] = "#e6f2ff"

def on_leave(e):
    if e.widget["state"] == "normal":
        e.widget["bg"] = "#ffffff"

# Custom popup with fade-in
def show_custom_popup(message):
    popup = tk.Toplevel(root)
    popup.geometry("280x150")
    popup.configure(bg="#fefae0")
    popup.title("🎉 Game Over")
    popup.attributes("-topmost", True)
    popup.resizable(False, False)
    popup.wm_attributes("-alpha", 0)  # Start transparent

    label = tk.Label(popup, text=message, font=("Helvetica", 18, "bold"), bg="#fefae0", fg="#2e2e2e")
    label.pack(pady=20)

    thanks = tk.Label(popup, text="Thanks for playing!", font=("Arial", 12), bg="#fefae0")
    thanks.pack()

    btn = tk.Button(popup, text="Close", command=root.quit, font=("Arial", 10, "bold"),
                    bg="#b5ead7", fg="black", relief="ridge", bd=2, width=10)
    btn.pack(pady=10)

    # Simulate fade-in effect
    def fade_in():
        for i in range(0, 11):
            popup.wm_attributes("-alpha", i / 10)
            time.sleep(0.03)

    threading.Thread(target=fade_in).start()

# Layout
frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=30)

for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(frame, **BUTTON_STYLE, command=lambda i=i, j=j: on_click(i, j))
        btn.grid(row=i, column=j, padx=5, pady=5)
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
        row.append(btn)
    buttons.append(row)

# Main loop
root.mainloop()
