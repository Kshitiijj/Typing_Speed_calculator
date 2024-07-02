import tkinter as tk #Used for Creating a GUI's
from tkinter import messagebox  #Displays message
import time   #this imports time, from which we will track our typing speed

class TypingSpeedCalculator:   #Created a class called TypingSpeedCalculator
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Calculator")

        self.prompt_text = "Myself Kshitij Surve, and I am happy to work with CodeClause."
        self.start_time = None

        self.setup_ui()

    def setup_ui(self):
        self.prompt_label = tk.Label(self.root, text=self.prompt_text, wraplength=300)
        self.prompt_label.pack(pady=10)

        self.text_area = tk.Text(self.root, height=5, width=40)
        self.text_area.pack(pady=10)
        self.text_area.bind('<FocusIn>', self.start_timer)

        self.submit_button = tk.Button(self.root, text="Submit", command=self.calculate_results)
        self.submit_button.pack(pady=10)

    def start_timer(self, event):
        self.start_time = time.time()

    def calculate_results(self):
        end_time = time.time()
        time_taken = end_time - self.start_time

        typed_text = self.text_area.get("1.0", tk.END).strip()
        word_count = len(typed_text.split())
        wpm = (word_count / time_taken) * 60

        accuracy = self.calculate_accuracy(typed_text)

        result_message = f"Typing Speed: {wpm:.2f} WPM\nAccuracy: {accuracy:.2f}%"
        messagebox.showinfo("Results", result_message)

    def calculate_accuracy(self, typed_text):
        prompt_words = self.prompt_text.split()
        typed_words = typed_text.split()

        correct_words = sum(1 for p, t in zip(prompt_words, typed_words) if p == t)
        total_words = len(prompt_words)

        accuracy = (correct_words / total_words) * 100
        return accuracy

if __name__ == "__main__": #implemented conditions
    root = tk.Tk()
    app = TypingSpeedCalculator(root)
    root.mainloop()
