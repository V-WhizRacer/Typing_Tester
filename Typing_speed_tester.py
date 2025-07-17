import tkinter as tk
from tkinter import ttk, messagebox
import random
import time

# Sample paragraphs
paragraphs = [
    "Typing is an essential skill today.\nKeep practicing every single day.\nAccuracy matters more than speed.",
    "Python is a fun language to learn.\nIt is widely used in AI and web.\nWrite clean and readable code.",
    "Focus on quality over quantity.\nMake each keystroke count.\nImprovement comes with practice."
]

class TypingSpeedTester:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Tester")
        self.root.geometry("950x620")
        self.root.resizable(False, False)
        self.font = ("Consolas", 16)
        self.dark_mode = False
        self.score_history = []
        self.setup_ui()
        self.reset()

    def setup_ui(self):
        title = ttk.Label(self.root, text="Typing Speed Tester", font=("Segoe UI", 24, "bold"))
        title.pack(pady=10)

        self.display_label = tk.Label(self.root, text="", font=self.font, bg="#f4f4f4", anchor="w", justify="left", width=100)
        self.display_label.pack(padx=20)

        self.entry = tk.Text(self.root, height=2, font=self.font, width=100)
        self.entry.pack(padx=20, pady=10)
        self.entry.bind("<KeyRelease>", self.track_typing)
        self.entry.bind("<Return>", self.handle_enter)

        self.stats_frame = ttk.Frame(self.root)
        self.stats_frame.pack(pady=5)

        self.timer_label = ttk.Label(self.stats_frame, text="Time: 60s", font=("Segoe UI", 12))
        self.wpm_label = ttk.Label(self.stats_frame, text="WPM: 0", font=("Segoe UI", 12))
        self.acc_label = ttk.Label(self.stats_frame, text="Accuracy: -", font=("Segoe UI", 12))
        self.wrong_label = ttk.Label(self.stats_frame, text="Wrong Keys: 0", font=("Segoe UI", 12))
        self.line_label = ttk.Label(self.stats_frame, text="Line: 1", font=("Segoe UI", 12))

        self.timer_label.grid(row=0, column=0, padx=10)
        self.wpm_label.grid(row=0, column=1, padx=10)
        self.acc_label.grid(row=0, column=2, padx=10)
        self.wrong_label.grid(row=0, column=3, padx=10)
        self.line_label.grid(row=0, column=4, padx=10)

        control_frame = ttk.Frame(self.root)
        control_frame.pack(pady=10)

        self.duration_cb = ttk.Combobox(control_frame, values=["30", "60", "90", "120"], width=5, state="readonly")
        self.duration_cb.set("60")
        self.duration_cb.grid(row=0, column=0, padx=5)

        ttk.Button(control_frame, text="Start Test", command=self.start_test).grid(row=0, column=1, padx=5)
        ttk.Button(control_frame, text="Reset", command=self.reset).grid(row=0, column=2, padx=5)
        ttk.Button(control_frame, text="Toggle Theme", command=self.toggle_theme).grid(row=0, column=3, padx=5)

        self.history_list = tk.Listbox(self.root, height=4, font=("Segoe UI", 12), width=90)
        self.history_list.pack(padx=20, pady=10)

        footer = ttk.Label(self.root, text="Made with ❤️ by Vageesh Pratap Singh", font=("Segoe UI", 10, "italic"))
        footer.pack(pady=5)


    def reset(self):
        self.all_lines = []
        for p in paragraphs:
            self.all_lines.extend(p.strip().split("\n"))
        random.shuffle(self.all_lines)

        self.line_pointer = 0
        self.current_line = self.all_lines[self.line_pointer]
        self.entry.delete("1.0", tk.END)
        self.update_display_line()
        self.start_time = None
        self.time_left = int(self.duration_cb.get())
        self.timer_label.config(text=f"Time: {self.time_left}s")
        self.line_label.config(text=f"Line: 1")
        self.timer_running = False
        self.correct_chars = 0
        self.total_chars = 0
        self.wrong_keys = 0
        self.line_count = 1
        self.wpm_label.config(text="WPM: 0")
        self.acc_label.config(text="Accuracy: -")
        self.wrong_label.config(text="Wrong Keys: 0")

    def update_display_line(self):
        self.display_label.config(text=self.current_line)

    def start_test(self):
        self.reset()
        self.timer_running = True
        self.start_time = time.time()
        self.countdown()
        self.entry.focus()

    def countdown(self):
        if self.timer_running and self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=f"Time: {self.time_left}s")
            self.root.after(1000, self.countdown)
        elif self.timer_running:
            self.evaluate_current_line()  # ← Evaluate final line even without pressing Enter
            self.finish_test()

    def handle_enter(self, event=None):
        if not self.timer_running:
            return "break"

        self.evaluate_current_line()
        self.line_pointer += 1
        self.line_count += 1

        if self.line_pointer >= len(self.all_lines):
            # Refill with more lines
            for p in paragraphs:
                self.all_lines.extend(p.strip().split("\n"))
            random.shuffle(self.all_lines)

        self.current_line = self.all_lines[self.line_pointer]
        self.update_display_line()
        self.line_label.config(text=f"Line: {self.line_count}")
        self.entry.delete("1.0", tk.END)
        return "break"

    def evaluate_current_line(self):
        typed = self.entry.get("1.0", "end-1c")
        expected = self.current_line
        correct = sum(1 for i, c in enumerate(typed) if i < len(expected) and c == expected[i])
        wrong = sum(1 for i, c in enumerate(typed) if i >= len(expected) or c != expected[i])
        self.correct_chars += correct
        self.wrong_keys += wrong
        self.total_chars += len(typed)
        self.wrong_label.config(text=f"Wrong Keys: {self.wrong_keys}")

    def track_typing(self, event=None):
        if not self.timer_running:
            return
        current = self.entry.get("1.0", "end-1c")
        expected = self.current_line
        self.entry.tag_remove("correct", "1.0", tk.END)
        self.entry.tag_remove("incorrect", "1.0", tk.END)

        for i, c in enumerate(current):
            tag = "correct" if i < len(expected) and c == expected[i] else "incorrect"
            start = f"1.0 + {i}c"
            end = f"1.0 + {i+1}c"
            self.entry.tag_add(tag, start, end)

        self.entry.tag_config("correct", foreground="green")
        self.entry.tag_config("incorrect", foreground="red")

    def finish_test(self):
        self.timer_running = False
        final_time = int(self.duration_cb.get())
        wpm = round((self.correct_chars / 5) / (final_time / 60))
        acc = round((self.correct_chars / self.total_chars) * 100, 2) if self.total_chars else 0
        result = f"WPM: {wpm} | Accuracy: {acc}% | Wrong Keys: {self.wrong_keys} | Duration: {final_time}s"
        self.wpm_label.config(text=f"WPM: {wpm}")
        self.acc_label.config(text=f"Accuracy: {acc}%")
        self.history_list.insert(0, result)
        messagebox.showinfo("Test Complete", result)

    def toggle_theme(self):
        self.dark_mode = not self.dark_mode
        bg = "#2e2e2e" if self.dark_mode else "#f4f4f4"
        fg = "white" if self.dark_mode else "black"
        self.display_label.config(bg=bg, fg=fg)
        self.entry.config(bg=bg, fg=fg, insertbackground=fg)
        self.history_list.config(bg=bg, fg=fg)
        self.root.configure(bg=bg)

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTester(root)
    root.mainloop()
