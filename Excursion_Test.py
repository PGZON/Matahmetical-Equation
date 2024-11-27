import tkinter as tk
from tkinter import messagebox

class DataProcessor:
    def __init__(self):
        self.sets = [[], [], []]  # To hold three sets of values
        self.x_value = 0

    def input_values(self, values, x_value):
        self.sets = [values[:8], values[8:16], values[16:]]
        self.x_value = x_value

    def calculate_averages(self):
        averages = []
        for i in range(8):
            avg = (self.sets[0][i] + self.sets[1][i] + self.sets[2][i]) / 3
            averages.append(avg)
        return averages

    def apply_formula(self, averages):
        results = []
        for avg in averages:
            result = (avg / self.x_value) * 100
            results.append(result)
        return results

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Dynamic excursion balance measurement test")
        
        self.values = []
        self.entries = []

        # Create header label
        tk.Label(root, text="Dynamic excursion balance measurement test", font=("Arial", 16)).grid(row=0, column=0, columnspan=10, pady=10)

        # Create input fields for Set 1
        tk.Label(root, text="Set 1", font=("Arial", 14)).grid(row=1, column=0, columnspan=9)
        
        for j in range(8):
            label = tk.Label(root, text=f"{j+1}", borderwidth=1, relief="solid", width=5)
            label.grid(row=2, column=j, padx=5, pady=5)  # Column labels for Set 1
            entry = tk.Entry(root, width=10)
            entry.grid(row=3, column=j, padx=5, pady=5)  # Entry fields for Set 1
            self.entries.append(entry)

        # Create input fields for Set 2
        tk.Label(root, text="Set 2", font=("Arial", 14)).grid(row=4, column=0, columnspan=9)

        for j in range(8):
            label = tk.Label(root, text=f"{j+1}", borderwidth=1, relief="solid", width=5)
            label.grid(row=5, column=j, padx=5, pady=5)  # Column labels for Set 2
            entry = tk.Entry(root, width=10)
            entry.grid(row=6, column=j, padx=5, pady=5)  # Entry fields for Set 2
            self.entries.append(entry)

        # Create input fields for Set 3
        tk.Label(root, text="Set 3", font=("Arial", 14)).grid(row=7, column=0, columnspan=9)

        for j in range(8):
            label = tk.Label(root, text=f"{j+1}", borderwidth=1, relief="solid", width=5)
            label.grid(row=8, column=j, padx=5, pady=5)  # Column labels for Set 3
            entry = tk.Entry(root, width=10)
            entry.grid(row=9, column=j, padx=5, pady=5)  # Entry fields for Set 3
            self.entries.append(entry)

        # Label and entry for Leg Length
        tk.Label(root, text="Leg Length:", font=("Arial", 12)).grid(row=10, column=0, sticky='e', padx=(5))
        self.x_entry = tk.Entry(root)
        self.x_entry.grid(row=10, column=1, padx=(5))

        # Buttons to calculate and clear
        calculate_button = tk.Button(root, text="Calculate", command=self.calculate)
        calculate_button.grid(row=11, column=0)

        clear_button = tk.Button(root, text="Clear", command=self.clear_entries)
        clear_button.grid(row=11, column=1)

        # Result display area
        self.result_label = tk.Label(root, text="Results will be displayed here:", font=("Arial", 12), justify='left')
        self.result_label.grid(row=12, column=0, columnspan=10)

    def calculate(self):
        try:
            # Gather values from entries
            self.values = [float(entry.get()) for entry in self.entries]
            x_value = float(self.x_entry.get())
            
            processor = DataProcessor()
            processor.input_values(self.values, x_value)
            averages = processor.calculate_averages()
            results = processor.apply_formula(averages)

            result_text = "\n".join(f"Result in direction {i+1} :  {result:.2f}%" for i, result in enumerate(results))
            self.result_label.config(text=result_text)
        
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers.")

    def clear_entries(self):
        for entry in self.entries:
            entry.delete(0, tk.END)  # Clear each entry field
        self.x_entry.delete(0, tk.END)  # Clear the Leg Length entry field
        self.result_label.config(text="Results will be displayed here:")  # Reset result display

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()



#pyinstaller --onefile --windowed Excursion Test.py