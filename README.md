## 🏋 BMI Calculator (Python + Tkinter)

A graphical BMI Calculator built with Python and Tkinter that allows users to:

Enter Name, Weight (kg), and Height (m)

Calculate BMI and determine the health category (Underweight, Normal, Overweight, Obese)

Store BMI records in a CSV file for historical tracking

Display a graph of past BMI values for all users using Matplotlib

# 📌 Features

✅ User-friendly GUI built with Tkinter
✅ Accurate BMI calculation using the formula:

BMI = weight (kg) / (height (m) ^ 2)

✅ Categorization into health ranges based on WHO standards
✅ CSV-based data storage for multiple users
✅ Historical graph visualization of BMI trends
✅ Error handling for invalid inputs
✅ Works for both beginners and advanced learners as per the project proposal


# 📂 File Structure

📁 BMI-Calculator
 ├── bmi_calculator.py   # Main program file
 ├── bmi_records.csv     # Auto-generated CSV file to store BMI history
 ├── README.md           # Project documentation


# 🛠 Requirements

Make sure you have Python 3.x installed along with the required library:

pip install matplotlib

(Tkinter comes pre-installed with Python on most systems)

# 🚀 How to Run

1. Clone the repository:git clone https://github.com/your-username/BMI-Calculator.git

2. Navigate to the project folder:cd BMI-Calculator

3. Run the program:python bmi_calculator.py

# 📊 Example Usage

1. Enter your name, weight, and height
2. Click "Calculate BMI" to see your result and category
3. Click "Show BMI History Graph" to view all saved BMI records plotted by name

# 📈 BMI Categories Used

Category	BMI Range

Underweight	< 18.5
Normal weight	18.5 – 24.9
Overweight	25 – 29.9
Obese	≥ 30
--

# 🏆 Project Proposal Fulfillment

This project meets all beginner and advanced requirements from the "Python Programming BMI Calculator Proposal" including:

User input validation

BMI calculation

Categorization into health ranges

GUI with Tkinter

CSV storage for multiple users

Historical data visualization

Error handling for invalid data
