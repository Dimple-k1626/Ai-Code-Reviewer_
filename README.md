

# 🤖 AI Code Reviewer

An AI-powered Code Reviewer built using **Python** and **Streamlit** that automatically analyzes and improves code quality using industry-standard tools.

---

## 📌 Project Objective

To analyze Python code and automatically:
- Detect coding style issues
- Measure code complexity
- Improve code formatting
- Display before/after comparison
- Generate a downloadable analysis report

---

## 🛠️ Tools & Technologies Used

- **Python 3.x**
- **Streamlit** – User Interface
- **flake8** – Code style checker
- **black** – Code formatter
- **radon** – Code complexity analyzer
- **Visual Studio Code**

---

## 📂 Project Structure

AI_Code_Reviewer/
│
├── app.py # Main Streamlit application
├── sample_code.py # Sample Python code for testing
├── README.md # Project documentation
├── .venv/ # Virtual environment


---

## ⚙️ Installation & Setup (Step-by-Step)

### 1️⃣ Clone or Create Project Folder
```bash
mkdir AI_Code_Reviewer
cd AI_Code_Reviewer

2️⃣ Create Virtual Environment
python -m venv .venv


Activate it:

Windows

.venv\Scripts\activate

3️⃣ Install Required Libraries
pip install streamlit flake8 black radon

▶️ How to Run the Project

⚠️ Do NOT use python app.py

Run the Streamlit app using:

streamlit run app.py

🖥️ Application Features & Output

Paste Python code OR upload a .py file

Click Analyze Code

View:

Original code

flake8 style issues

Radon complexity report

Black formatted (improved) code

See summary of improvements

Download code analysis report

📄 Sample Output Sections

🧹 Style Issues (flake8)

📊 Code Complexity (radon)

✨ Improved Code (black)

✅ Summary of Improvements

📥 Downloadable Report

📦 Deliverables

Streamlit Web Application

Sample Code Analysis

Before & After Code Comparison

Downloadable Report (.txt)

README Documentation

🎓 Viva / Explanation (One Line)

“The AI Code Reviewer accepts Python code input, analyzes it using flake8, radon, and black, displays quality improvements, and exports a detailed report using a Streamlit-based UI.”

✅ Conclusion

This project demonstrates automated code quality analysis using modern Python tools and provides an interactive and user-friendly interface for developers to improve their code efficiently
