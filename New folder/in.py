import tkinter as tk

# --- Function to calculate total ---
def calculate():
    try:
        total = (
            int(e_2000.get() or 0) * 2000 +
            int(e_500.get() or 0) * 500 +
            int(e_200.get() or 0) * 200 +
            int(e_100.get() or 0) * 100 +
            int(e_50.get() or 0) * 50 +
            int(e_20.get() or 0) * 20 +
            int(e_10.get() or 0) * 10 +
            int(e_5.get() or 0) * 5 +
            int(e_2.get() or 0) * 2 +
            int(e_1.get() or 0) * 1
        )
        result_label.config(text=f"💰 Total: ₹{total}", fg="#00FF00")
    except Exception as e:
        result_label.config(text=f"❌ Error: {e}", fg="red")

# --- Main Window Setup ---
root = tk.Tk()
root.title("💸 Money Counter App")
root.geometry("350x600")
root.config(bg="#1c1c1c")
root.resizable(False, False)

tk.Label(
    root, text="💵 Cash Counter", 
    font=("Arial", 20, "bold"), 
    bg="#1c1c1c", fg="#00FFD1"
).pack(pady=15)

# --- Entry frame ---
frame = tk.Frame(root, bg="#1c1c1c")
frame.pack()

def make_input(label, color):
    tk.Label(frame, text=label, font=("Arial", 13), fg=color, bg="#1c1c1c").pack(pady=2)
    entry = tk.Entry(frame, font=("Arial", 13), bg="#2c2c2c", fg="white", justify='center', insertbackground='white')
    entry.pack(pady=3)
    return entry

# --- Note Input Fields ---
e_2000 = make_input("₹2000 Notes:", "#ff6666")
e_500  = make_input("₹500 Notes:", "#ff9966")
e_200  = make_input("₹200 Notes:", "#ffcc66")
e_100  = make_input("₹100 Notes:", "#99ff66")
e_50   = make_input("₹50 Notes:", "#66ffcc")
e_20   = make_input("₹20 Notes:", "#66ccff")
e_10   = make_input("₹10 Coins:", "#6699ff")
e_5    = make_input("₹5 Coins:", "#9966ff")
e_2    = make_input("₹2 Coins:", "#cc66ff")
e_1    = make_input("₹1 Coins:", "#ff66cc")

# --- Calculate Button ---
tk.Button(
    root, text="Calculate 💰", font=("Arial", 14, "bold"), 
    bg="#00cc66", fg="white", activebackground="#00ff99", 
    command=calculate
).pack(pady=20)

# --- Result Label ---
result_label = tk.Label(
    root, text="💰 Total: ₹0", 
    font=("Arial", 16, "bold"), 
    fg="white", bg="#1c1c1c"
)
result_label.pack(pady=10)

# --- Start the App ---
root.mainloop()
