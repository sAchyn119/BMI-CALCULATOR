import tkinter as tk
from tkinter import messagebox
import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt

CSV_FILE = "bmi_records.csv"

# BMI category ranges
def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# Ensure CSV file has correct header
def ensure_csv_header():
    if not os.path.isfile(CSV_FILE):
        with open(CSV_FILE, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Name", "Weight(kg)", "Height(m)", "BMI", "Category"])
    else:
        with open(CSV_FILE, mode="r") as file:
            first_line = file.readline().strip()
        if first_line != "Date,Name,Weight(kg),Height(m),BMI,Category":
            with open(CSV_FILE, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Date", "Name", "Weight(kg)", "Height(m)", "BMI", "Category"])

# Save BMI record to CSV
def save_bmi_record(name, weight, height, bmi, category):
    ensure_csv_header()
    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M"), name, weight, height, round(bmi, 2), category])

# Show historical BMI graph with names on X-axis
def show_history_graph():
    ensure_csv_header()

    names = []
    bmis = []

    with open(CSV_FILE, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                bmis.append(float(row["BMI"]))
                names.append(row["Name"])
            except ValueError:
                pass

    if not bmis:
        messagebox.showinfo("No Data", "No BMI history found.")
        return

    plt.figure(figsize=(8, 5))
    plt.plot(names, bmis, marker='o', linestyle='-', color='blue')
    plt.xticks(rotation=45, ha='right')
    plt.xlabel("Name")
    plt.ylabel("BMI")
    plt.title("BMI History (All Users)")
    plt.tight_layout()
    plt.show()

# Calculate BMI and display result
def calculate_bmi():
    name = entry_name.get().strip()
    weight = entry_weight.get().strip()
    height = entry_height.get().strip()

    if not name:
        messagebox.showerror("Input Error", "Please enter your name.")
        return

    try:
        weight = float(weight)
        height = float(height)
        if weight <= 0 or height <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid positive numbers for weight and height.")
        return

    bmi = weight / (height ** 2)
    category = get_bmi_category(bmi)
    result_label.config(text=f"BMI: {bmi:.2f} ({category})")

    save_bmi_record(name, weight, height, bmi, category)

# Tkinter window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x350")
root.resizable(False, False)

# Labels and inputs
tk.Label(root, text="Name:").pack(pady=5)
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Weight (kg):").pack(pady=5)
entry_weight = tk.Entry(root)
entry_weight.pack()

tk.Label(root, text="Height (m):").pack(pady=5)
entry_height = tk.Entry(root)
entry_height.pack()

# Buttons
tk.Button(root, text="Calculate BMI", command=calculate_bmi, bg="lightgreen").pack(pady=10)
tk.Button(root, text="Show BMI History Graph", command=show_history_graph, bg="lightblue").pack(pady=5)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

# Run GUI
root.mainloop()