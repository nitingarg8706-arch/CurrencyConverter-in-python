import requests
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Function to convert currency
def convert(event=None):
    try:
        from_currency = entry_from.get().upper()
        to_currency = entry_to.get().upper()
        amount = float(entry_amount.get())

        url = f"https://open.er-api.com/v6/latest/{from_currency}"

        response = requests.get(url)
        data = response.json()

        if data.get("result") != "success":
            messagebox.showerror("Error", "Invalid base currency")
            return

        if to_currency not in data["rates"]:
            messagebox.showerror("Error", "Invalid target currency")
            return

        rate = data["rates"][to_currency]
        result = amount * rate

        label_result.config(
            text=f"{amount} {from_currency} = {result:.2f} {to_currency}"
        )

    except ValueError:
        messagebox.showerror("Error", "Enter valid number")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# GUI Window
root = tk.Tk()
root.title("Currency Converter")
root.geometry("600x450")
root.resizable(False, False)

# Background Image (JPG)
bg = Image.open("D:/python/currency/background.jpg")
bg = bg.resize((600,450))
bg_image = ImageTk.PhotoImage(bg)

bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Title
title = tk.Label(root, text="Currency Converter", font=("Arial",20,"bold"))
title.pack(pady=10)

# From Currency
tk.Label(root, text="From Currency (USD, INR, EUR)" , font=("Arial",16,"bold")).pack()
entry_from = tk.Entry(root)
entry_from.pack()

# To Currency
tk.Label(root, text="To Currency (USD, INR, EUR)", font=("Arial",16,"bold")).pack()
entry_to = tk.Entry(root)
entry_to.pack()

# Amount
tk.Label(root, text="Amount", font=("Arial",16,"bold")).pack()
entry_amount = tk.Entry(root)
entry_amount.pack()

# Convert Button
tk.Button(root, text="Convert", command=convert, font=("Arial",16,"bold"), bg="lightblue").pack(pady=10)

# # Result Label
label_result = tk.Label(root, text= '', font=("Arial",17,"bold"), bg="lightgrey") 
label_result.pack(pady=20)

# Press Enter to convert
root.bind("<Return>", convert)

root.mainloop()