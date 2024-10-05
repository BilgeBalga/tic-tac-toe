import tkinter as tk
from game import TicTacToe

class TicTacToeGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.master.configure(bg="#e0e0e0")  # Background color
        self.game = TicTacToe()
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_widgets()
        self.update_status()

    def create_widgets(self):
        for row in range(3):
            for col in range(3):
                button = tk.Button(
                    self.master,
                    text=' ',
                    font='Arial 40 bold',
                    width=5,
                    height=2,
                    bg="#ffffff",  # Button color
                    activebackground="#ffcc00",  # Color on click
                    command=lambda r=row, c=col: self.on_button_click(r, c)
                )
                button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
                self.buttons[row][col] = button
        
        self.status_label = tk.Label(self.master, text="", font='Arial 16 bold', bg="#e0e0e0")
        self.status_label.grid(row=3, column=0, columnspan=3)

        # Create a reset button
        self.reset_button = tk.Button(
            self.master,
            text="Tekrar Oyna",
            command=self.reset_game,
            font='Arial 14 bold',
            bg="#007bff",
            fg="#ffffff"
        )
        self.reset_button.grid(row=4, column=0, columnspan=3, pady=10)

        # Grid weights for responsive design
        for i in range(3):
            self.master.grid_rowconfigure(i, weight=1)
            self.master.grid_columnconfigure(i, weight=1)

    def on_button_click(self, row, col):
        if self.game.current_player == 1 and self.game.make_move(row, col):
            self.buttons[row][col].config(text='X', fg="#ff0000")  # X color
            winner = self.game.check_winner()
            if winner:
                self.show_winner(winner)
            elif self.game.is_draw():
                self.show_winner("Beraberlik!")
            else:
                self.game.current_player *= -1  # Switch to AI
                self.update_status()
                self.master.after(1000, self.ai_turn)  # Delay AI's turn by 1 second

    def ai_turn(self):
        if self.game.current_player == -1:  # Check if it's AI's turn
            self.game.ai_move()
            for row in range(3):
                for col in range(3):
                    if self.game.board[row][col] == 'O':
                        self.buttons[row][col].config(text='O', fg="#0000ff")  # O color
            winner = self.game.check_winner()
            if winner:
                self.show_winner(winner)
            elif self.game.is_draw():
                self.show_winner("Beraberlik!")
            else:
                self.game.current_player *= -1  # Switch back to human
                self.update_status()

    def update_status(self):
        self.status_label.config(text=f"Sıra: {'X (İnsan)' if self.game.current_player == 1 else 'O (Yapay Zeka)'}")

    def show_winner(self, winner):
        self.status_label.config(text=f"{winner} kazandı!")
        self.master.configure(bg="#28a745")  # Green background color for win
        for row in self.buttons:
            for button in row:
                button.config(state='disabled')  # Disable buttons after game ends

    def reset_game(self):
        self.game.reset_game()
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text=' ', state='normal')
        self.master.configure(bg="#e0e0e0")  # Reset background color
        self.update_status()

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeGUI(root)
    root.mainloop()