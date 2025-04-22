import tkinter as tk
from tkinter import messagebox
import random

class HangmanGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game")
        self.master.geometry("500x550")
        self.master.resizable(False, False)

        self.word_list = ["PYTHON", "JAVA", "JAVASCRIPT", "HTML", "CSS", "RUBY", "PHP"]
        self.max_attempts = 6

        # Game Title
        tk.Label(master, text="Hangman Game", font=("Helvetica", 28, "bold")).pack(pady=10)

        # Word display
        self.word_label = tk.Label(master, font=("Courier", 28), fg="darkblue")
        self.word_label.pack(pady=20)

        # Input Frame
        self.input_frame = tk.Frame(master)
        self.input_frame.pack(pady=10)

        self.input_entry = tk.Entry(self.input_frame, font=("Helvetica", 18), width=5, justify="center")
        self.input_entry.pack(side=tk.LEFT, padx=10)
        self.input_entry.focus()

        self.submit_button = tk.Button(self.input_frame, text="Guess", font=("Helvetica", 14), command=self.guess_letter)
        self.submit_button.pack(side=tk.LEFT)

        # Attempts
        self.remaining_attempts_label = tk.Label(master, font=("Helvetica", 16))
        self.remaining_attempts_label.pack(pady=5)

        # Hangman ASCII Display
        self.hangman_label = tk.Label(master, font=("Courier", 14), justify="left")
        self.hangman_label.pack(pady=10)

        self.hangman_images = [
            """\n-----\n|   |\n|\n|\n|\n|""",
            """\n-----\n|   |\n|   O\n|\n|\n|""",
            """\n-----\n|   |\n|   O\n|   |\n|\n|""",
            """\n-----\n|   |\n|   O\n|  /|\n|\n|""",
            """\n-----\n|   |\n|   O\n|  /|\\\n|\n|""",
            """\n-----\n|   |\n|   O\n|  /|\\\n|  /\n|""",
            """\n-----\n|   |\n|   O\n|  /|\\\n|  / \\\n|"""
        ]

        # Start game
        self.reset_game()

    def get_display_word(self):
        return " ".join([letter if letter in self.guessed_letters else "_" for letter in self.word])

    def guess_letter(self):
        letter = self.input_entry.get().strip().upper()
        self.input_entry.delete(0, tk.END)
        self.input_entry.focus()

        if letter.isalpha() and len(letter) == 1:
            if letter not in self.guessed_letters:
                self.guessed_letters.add(letter)
                if letter not in self.word:
                    self.attempts_left -= 1
                self.update_display()

                if "_" not in self.get_display_word():
                    self.end_game(True)
            else:
                messagebox.showwarning("Duplicate", f"You've already guessed '{letter}'.")
        else:
            messagebox.showwarning("Invalid Input", "Please enter a single alphabet letter.")

    def update_display(self):
        self.word_label.config(text=self.get_display_word())
        self.remaining_attempts_label.config(text=f"Attempts Left: {self.attempts_left}")
        self.hangman_label.config(text=self.hangman_images[self.max_attempts - self.attempts_left])

        if self.attempts_left == 0:
            self.end_game(False)

    def end_game(self, won):
        if won:
            msg = f"🎉 You guessed it right! The word was '{self.word}'."
        else:
            msg = f"😢 You lost! The word was '{self.word}'."

        if messagebox.askyesno("Game Over", msg + "\n\nDo you want to play again?"):
            self.reset_game()
        else:
            self.master.quit()

    def reset_game(self):
        self.word = random.choice(self.word_list)
        self.guessed_letters = set()
        self.attempts_left = self.max_attempts
        self.update_display()

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
