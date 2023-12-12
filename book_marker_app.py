import tkinter as tk

class PreUniMarker(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Marks Counter")

        self.create_widgets()

    def create_widgets(self):
        # total
        label_total = tk.Label(self, text="Enter the total: ", font=('Arial', 20))
        label_total.grid(row=0, column=0, padx=10, pady=10)

        self.entry_total = tk.Entry(self, font=('Arial', 20))
        self.entry_total.grid(row=0, column=1, padx=10, pady=10)

        # deductions
        label_deductions = tk.Label(self, text="Enter Deductions: ", font=('Arial', 20))
        label_deductions.grid(row=1, column=0, padx=10, pady=10)

        self.entry_deductions = tk.Entry(self, font=('Arial', 20))
        self.entry_deductions.grid(row=1, column=1, padx=10, pady=10)

        # calculate
        button_calculate = tk.Button(self, text="Calculate", font=('Arial', 20), command=self.get_total)
        button_calculate.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # mark
        self.label_mark = tk.Label(self, font=('Arial', 20))
        self.label_mark.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # percentage
        self.label_percentage = tk.Label(self, font=('Arial', 20))
        self.label_percentage.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        # Bind Tab and Enter keys
        self.entry_total.bind("<Tab>", lambda event: self.entry_deductions.focus_set())
        self.entry_deductions.bind("<Tab>", lambda event: self.entry_total.focus_set())
        self.bind("<Return>", lambda event: self.get_total())

    def get_deductions_total(self):
        deductions_str = self.entry_deductions.get()
        deductions = [int(num) for num in deductions_str.split()]
        return sum(deductions)

    def calculate_mark(self, total, deductions_total):
        mark = total - deductions_total
        return mark

    def calculate_percentage(self, total, mark):
        return float(mark / total) * 100

    def update_mark(self, mark, total):
        self.label_mark.config(text=f"Mark: {mark}/{total}")

    def update_percentage(self, percentage):
        self.label_percentage.config(text=f"Percentage: {percentage:.2f}%")

    def get_total(self, event=None):
        deductions_total = self.get_deductions_total()

        total = int(self.entry_total.get())
        mark = self.calculate_mark(total, deductions_total)
        percentage = self.calculate_percentage(total, mark)

        self.update_mark(mark, total)
        self.update_percentage(percentage)

if __name__ == "__main__":
    app = PreUniMarker()
    app.mainloop()
