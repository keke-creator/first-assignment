import tkinter as tk
from tkinter import ttk
import math

class Shape:
    def __init__(self, unit='cm'):
        self.unit = unit

    def to_cm(self, value):
        if self.unit == 'in':
            return value * 2.54
        return value

    def get_area(self):
        raise NotImplementedError("Subclasses should implement this method.")

class AreaCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Area Calculator")

        self.unit_var = tk.StringVar(value='cm')
        self.shape_var = tk.StringVar(value='square')

        self.create_widgets()

    def create_widgets(self):
        # Shape selection
        ttk.Label(self.root, text="Choose the shape:").grid(row=0, column=0, padx=10, pady=10)
        shapes = ['square', 'rectangle', 'triangle', 'circle']
        shape_menu = ttk.Combobox(self.root, textvariable=self.shape_var, values=shapes)
        shape_menu.grid(row=0, column=1, padx=10, pady=10)
        shape_menu.bind("<<ComboboxSelected>>", self.update_form)

        # Unit selection
        ttk.Label(self.root, text="Choose the unit:").grid(row=1, column=0, padx=10, pady=10)
        unit_menu = ttk.Combobox(self.root, textvariable=self.unit_var, values=['cm', 'in'])
        unit_menu.grid(row=1, column=1, padx=10, pady=10)

        # Input fields
        self.input_frame = ttk.Frame(self.root)
        self.input_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # Calculate button
        ttk.Button(self.root, text="Calculate", command=self.calculate_area).grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # Result display
        self.result_label = ttk.Label(self.root, text="")
        self.result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        self.update_form()

if __name__ == "__main__":
    root = tk.Tk()
    app = AreaCalculatorApp(root)
    root.mainloop()















