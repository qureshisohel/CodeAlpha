import requests
import tkinter as tk
from tkinter import ttk

class CurrencyConverter:
    def __init__(self, url):
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']

    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        if from_currency != 'USD':
            amount = amount / self.currencies[from_currency]

        amount = round(amount * self.currencies[to_currency], 2)
        return amount

class App:
    def __init__(self, converter):
        self.root = tk.Tk()
        self.root.title("Currency Converter")
        self.root.geometry("400x500")
        self.root.configure(bg="#e0e0e0")

        # Create the labels and entry widgets
        self.from_label = ttk.Label(self.root, text="From:", font=("Helvetica", 14))
        self.from_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.from_currency = ttk.Combobox(self.root, width=15, values=list(converter.currencies.keys()), font=("Helvetica", 12))
        self.from_currency.grid(row=0, column=1, padx=10, pady=10)
        self.from_currency.current(0)

        self.amount_label = ttk.Label(self.root, text="Amount:", font=("Helvetica", 14))
        self.amount_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.amount_entry = ttk.Entry(self.root, width=15, font=("Helvetica", 12))
        self.amount_entry.grid(row=1, column=1, padx=10, pady=10)

        self.to_label = ttk.Label(self.root, text="To:", font=("Helvetica", 14))
        self.to_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.to_currency = ttk.Combobox(self.root, width=15, values=list(converter.currencies.keys()), font=("Helvetica", 12))
        self.to_currency.grid(row=2, column=1, padx=10, pady=10)
        self.to_currency.current(31)

        self.converted_label = ttk.Label(self.root, text="", font=("Helvetica", 14))
        self.converted_label.grid(row=3, column=1, padx=10, pady=10)

        # Create the convert button with custom style
        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 14), background="#2196F3", foreground="black")  # Blue button
        self.convert_button = ttk.Button(self.root, text="Convert", command=self.convert, style="TButton")
        self.convert_button.grid(row=4, column=1, padx=10, pady=10)

        self.converter = converter

    def convert(self):
        try:
            from_currency = self.from_currency.get()
            to_currency = self.to_currency.get()
            amount = float(self.amount_entry.get())
            converted_amount = self.converter.convert(from_currency, to_currency, amount)
            self.converted_label.config(text=str(converted_amount))

        except ValueError:
            self.converted_label.config(text="Invalid amount entered.")

    def run(self):
        self.root.mainloop()

url = 'https://api.exchangerate-api.com/v4/latest/USD'
converter = CurrencyConverter(url)

app = App(converter)
app.run()
