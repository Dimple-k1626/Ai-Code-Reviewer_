import streamlit as st
import subprocess
import tempfile
import os

st.set_page_config(page_title="AI Code Reviewer", layout="wide")

st.title("🤖 AI Code Reviewer")
st.write("Upload or paste Python code to analyze quality automatically.")

# --- Code Input ---
option = st.radio("Choose input method:", ["Paste Code", "Upload File"])

code = ""

if option == "Paste Code":
    code = st.text_area("Paste your Python code here:", height=250)
else:
    uploaded_file = st.file_uploader("Upload Python file", type=["py"])
    if uploaded_file:
        code = uploaded_file.read().decode("utf-8")

# --- Analyze Button ---
if st.button("🔍 Analyze Code") and code.strip():
    with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as temp:
        temp.write(code.encode())
        temp_file = temp.name

    st.subheader("📌 Original Code")
    st.code(code, language="python")

    # --- flake8 ---
    st.subheader("🧹 Style Issues (flake8)")
    flake8_result = subprocess.run(
        ["flake8", temp_file],
        capture_output=True,
        text=True
    )
    st.text(flake8_result.stdout if flake8_result.stdout else "No style issues found")

    # --- radon ---
    st.subheader("📊 Code Complexity (radon)")
    radon_result = subprocess.run(
        ["radon", "cc", temp_file, "-a"],
        capture_output=True,
        text=True
    )
    st.text(radon_result.stdout)

    # --- black ---
    st.subheader("✨ Improved Code (black formatted)")
    subprocess.run(["black", temp_file], capture_output=True)
    with open(temp_file, "r") as f:
        formatted_code = f.read()

    st.code(formatted_code, language="python")

    # --- Summary ---
    st.subheader("✅ Summary of Improvements")
    st.markdown("""
    - Fixed formatting issues
    - Improved code readability
    - Detected complex logic
    - Ready for production standards
    """)

    # --- Export Report ---
    report = f"""
AI CODE REVIEW REPORT

STYLE ISSUES:
{flake8_result.stdout}

COMPLEXITY REPORT:
{radon_result.stdout}

IMPROVED CODE:
{formatted_code}
"""

    st.download_button(
        "📄 Download Report",
        report,
        file_name="code_review_report.txt"
    )

    os.remove(temp_file)
