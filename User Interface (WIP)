import tkinter as tk
from tkinter import ttk
import pandas as pd
import run

class MyGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Dwayne's BlackJack Simulator")
        self.master.geometry("800x600")

        # Player selection dropdown
        self.player_label = tk.Label(self.master, text="Select player:")
        self.player_label.pack()

        self.player_options = ["Player 1", "Player 2", "Player 3", "Player 4", "Player 5", "Player 6", "Player 7"]
        self.player_var = tk.StringVar(self.master)
        self.player_var.set(self.player_options[0]) # default value
        self.player_menu = tk.OptionMenu(self.master, self.player_var, *self.player_options)
        self.player_menu.pack()

        # Iteration input
        self.iter_label = tk.Label(self.master, text="Enter number of iterations:")
        self.iter_label.pack()

        self.iter_entry = tk.Entry(self.master)
        self.iter_entry.pack()

        # Run button
        self.run_button = tk.Button(self.master, text="RUN", command=self.run_backend)
        self.run_button.pack(side=tk.LEFT)

        # Data display window
        self.display_frame = tk.Frame(self.master)
        self.display_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.display_label = tk.Label(self.display_frame, text="Data display:")
        self.display_label.pack()

        self.data_text = tk.Label(self.display_frame, wraplength=400, height=10, relief=tk.SOLID)
        self.data_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Download button
        self.download_button = tk.Button(self.master, text="CSV", command=self.download_csv)
        self.download_button.pack()

    def run_backend(self):
        # Get user input
       # player = self.player_var.get()
        iterations = int(self.iter_entry.get())

        # Call backend function with user input
        data = run.rungame(iterations)
        self.data_text.config(text=data) # display new data

    def download_csv(self):
        # Get data from display window
        data = pd.read_csv(pd.compat.StringIO(self.data_text.cget('text')))
       
        # Save data as CSV file
        file_path = "data.csv"
        data.to_csv(file_path, index=False)

if __name__ == "__main__":
    root = tk.Tk()
    gui = MyGUI(root)
    root.mainloop()

