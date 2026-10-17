# Placement Readiness Data Explorer

An explainable, beginner-friendly Python data analysis project and interactive Streamlit web application to evaluate student placement readiness across technical, problem-solving, and communication dimensions.

> **Important Analytical Limitation:**  
> *This application uses synthetic student data and manually defined readiness rules for educational analysis. The readiness categories are not predictions of actual placement outcomes.*  
> This project does not claim to predict hiring decisions, salaries, placement probabilities, or real-world employment success.

---

## 1. Project Purpose & Problem Statement

In academic institutions, preparing students for campus placements requires understanding where each student stands across multiple skill areas:
- Core programming proficiency
- Problem-solving and aptitude test capability
- Communication and interpersonal skills
- Practical hands-on project experience
- Industry-recognized certifications

**The Placement Readiness Data Explorer** provides a clean, transparent, and explainable tool for educational data analysis. It analyzes a baseline batch of 40 students across three departments (**Computer Science**, **Information Technology**, and **Data Science**) targeting four popular career paths (**Software Developer**, **Data Analyst**, **Python Developer**, and **Business Analyst**).

Users can also **enter custom student records** directly through the web interface, save them to persistent CSV storage, and immediately see how those new records update every analysis table, chart, metric, and ranking across the application.

---

## 2. Key Features

1. **Dual Interface Options:**
   - **Streamlit Web Application (`app.py`)**: Professional web dashboard with tab navigation, summary metric cards, reactive filters, and native bar charts.
   - **Command-Line Program (`placement_readiness.py`)**: Fast terminal report with text-based visual charts (`#` and `*`).
2. **Student Data Entry System:**
   - Enter new student credentials with comprehensive input validation.
   - Validates unique Student ID, score bounds (0–100), and non-negative counts.
3. **Persistent CSV Data Storage:**
   - User-added records are safely persisted in `student_data.csv` using UTF-8 encoding.
   - Preserves baseline sample records without accidental overwriting.
   - Distinguishes record sources internally (`Sample` vs `User Added`).
4. **Data Management & Protection:**
   - Dedicated **Manage Student Data** tab to view saved records and delete user-added records with one click.
   - Baseline sample records (`STU001`–`STU040`) are permanently protected and cannot be deleted.
5. **Real-Time Integration Across All Analytics:**
   - Adding or removing a student automatically recalculates batch averages, department breakdowns, role distributions, readiness rankings, and stronger profile metrics.
6. **Department & Role Group Comparisons:**
   - Aggregated comparisons across departments and targeted job roles.
7. **Role-Wise Missing Competency Analysis:**
   - Explicit benchmark rules per job role to pinpoint specific skill gaps.
8. **Restrained, Professional Theme:**
   - Clean color palette configured via `.streamlit/config.toml` (Deep Navy `#0F172A`, Teal accent `#0D9488`, and Off-White background `#F8FAFC`).
9. **One-Click Windows Launcher (`run_app.bat`):**
   - Double-click batch file that auto-detects Python, checks virtual environments, validates dependencies, and launches the application.

---

## 3. Technologies Used

- **Python 3.x**: Core language (loops, functions, conditional branching, dictionaries, lists).
- **NumPy**: Numeric calculations and array operations (`np.mean`, `np.max`, `np.min`).
- **Pandas**: Structured DataFrames, grouping (`groupby`), sorting (`sort_values`), aggregation, and CSV handling.
- **Streamlit**: Web application framework (interactive metrics, tabs, tables, dropdown filters, forms, and native bar charts).

*Note: In strict accordance with project guidelines, no heavy third-party visualization libraries (Matplotlib, Seaborn, Plotly) or machine learning frameworks are used.*

---

## 4. Dataset Columns & Schema

| Column Name | Data Type | Range / Values | Description |
| :--- | :--- | :--- | :--- |
| `Student_ID` | String | e.g. `STU001`, `CS2026-01` | Unique student identifier |
| `Department` | String | Computer Science, Information Technology, Data Science | Academic department |
| `Programming_Skill` | Integer | 0 to 100 | Assessed coding competency |
| `Aptitude_Score` | Integer | 0 to 100 | Quantitative and logical aptitude test score |
| `Communication_Score` | Integer | 0 to 100 | Spoken, written, and interview communication score |
| `Projects` | Integer | $\ge 0$ | Count of completed technical projects |
| `Certifications` | Integer | $\ge 0$ | Count of verified certifications completed |
| `Preferred_Role` | String | Software Developer, Data Analyst, Python Developer, Business Analyst | Targeted career role |
| `Record_Source` | String | `Sample` or `User Added` | Internal origin tracker |

---

## 5. Readiness Scoring Formula & Classification Thresholds

### A. Explainable Weighted Formula

The readiness score is calculated on a 0–100 scale using a transparent weighted methodology:

$$\text{Readiness Score} = (\text{Prog} \times 0.30) + (\text{Apt} \times 0.25) + (\text{Comm} \times 0.20) + \text{Project Points} + \text{Certification Points}$$

Where:
- **Programming Skill (30% weight, max 30 points):**  
  $\text{Score} \times 0.30$. Programming forms the core technical foundation for entry-level tech roles.
- **Aptitude Score (25% weight, max 25 points):**  
  $\text{Score} \times 0.25$. Aptitude tests serve as the initial screening filter in recruitment rounds.
- **Communication Score (20% weight, max 20 points):**  
  $\text{Score} \times 0.20$. Crucial for interviews, managerial rounds, and team collaboration.
- **Project Experience (15% weight, max 15 points):**  
  Each project completed contributes **3.0 points**, capped at a maximum of **15.0 points** (for 5 or more projects).
- **Certifications (10% weight, max 10 points):**  
  Each verified certification contributes **2.5 points**, capped at a maximum of **10.0 points** (for 4 or more certifications).

$$\text{Maximum Possible Score} = 30 + 25 + 20 + 15 + 10 = 100.0$$

### B. Classification Thresholds

Students are classified using straightforward `if-elif-else` conditions:

- **Strong ($\ge 75.0$):** High overall readiness across multiple competencies, solid projects, and foundational certifications.
- **Moderate ($60.0 \le \text{Score} < 75.0$):** Satisfactory baseline preparation with potential in 1 or 2 specific areas that need strengthening.
- **Developing ($< 60.0$):** Foundational stage requiring prioritized faculty mentoring, portfolio building, and core skill practice.

---

## 6. Role-Based Missing Competency Identification

Explicit benchmark thresholds were defined for each role to identify skill gaps:

| Preferred Role | Min. Programming | Min. Aptitude | Min. Communication | Min. Projects | Min. Certifications |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Software Developer** | 75 | 65 | 60 | 2 | 1 |
| **Data Analyst** | 65 | 75 | 65 | 2 | 1 |
| **Python Developer** | 80 | 65 | 55 | 2 | 1 |
| **Business Analyst** | 50 | 70 | 80 | 2 | 1 |

For each student targeting a role, the system checks whether their scores fall below these benchmarks and tabulates the total occurrences per role.

---

## 7. How to Run the Application

### Option A: One-Click Windows Launcher (Easiest)

Simply double-click the **`run_app.bat`** file located in the project root folder.  
The batch script will:
1. Verify Python installation.
2. Activate a virtual environment if present (`venv` or `.venv`).
3. Check required packages (`streamlit`, `pandas`, `numpy`).
4. Automatically start the Streamlit web application.

### Option B: Manual Command-Line Launch

Open your terminal or PowerShell in the project directory:
```bash
cd "Placement-Readiness-Data-Explorer"
```
Install dependencies if not already installed:
```bash
pip install -r requirements.txt
```
Launch the web application:
```bash
python -m streamlit run app.py
```
*(Or `streamlit run app.py` if Python Scripts is in your system PATH).*

When started, open **`http://localhost:8501`** in any web browser.

### Option C: Run the Terminal CLI Version

To run the terminal analysis report with text bar charts:
```bash
python placement_readiness.py
```

---

## 8. Student Data Entry & Management Guide

### Adding a Student
1. Open the web app and select **Add Student** from the sidebar.
2. Enter the **Student ID** (e.g. `STU101` or `CS-01`).
3. Select the **Department** and **Preferred Role**.
4. Set the **Programming Skill**, **Aptitude Score**, and **Communication Score** (0–100).
5. Specify the count of **Projects** and **Certifications**.
6. Click **Add Student**.
7. The system validates the input, calculates readiness, appends the record to `student_data.csv`, and immediately updates all analysis sections.

### Managing and Deleting Records
1. Select **Student Records** from the sidebar.
2. Open the **Manage Added Records** expander below the main table.
3. Review the list of student-added entries.
4. Select an ID from the dropdown and click **Delete Record**.
5. The record is removed from storage and all views refresh automatically.
6. Baseline sample records (`STU001`–`STU040`) are protected from accidental deletion.

---

## 9. Project Structure

```text
Placement-Readiness-Data-Explorer/
│
├── .streamlit/
│   └── config.toml          # Streamlit theme configuration (Teal & Navy)
├── app.py                   # Streamlit web application with 9 tabs
├── placement_readiness.py   # Command-line program & shared calculation functions
├── student_data.csv         # Persistent CSV storage for user-added student records
├── run_app.bat              # Windows batch launcher (double-click to run)
├── requirements.txt         # Minimal dependencies (streamlit, numpy, pandas)
├── README.md                # Project documentation & user guide
└── .gitignore               # Ignores bytecode, virtual environments, and local data
```

---

## 10. Analytical Limitations

1. **Synthetic Nature of Baseline Data:** The baseline dataset is synthetically compiled for educational data analysis and does not represent actual institutional records.
2. **Deterministic Heuristic Rules:** Readiness scores and levels are calculated based on fixed, transparent weights and thresholds rather than predictive machine learning models.
3. **No Employment Prediction:** A "Strong" level does not guarantee hiring, nor does a "Developing" level indicate future failure. Actual placement depends on external market forces, company hiring criteria, and interview performance.

---

## 11. GitHub & Data Privacy

- **Data Privacy**: The `.gitignore` file includes `student_data.csv` so that any personal student records entered locally on your machine remain private and are not accidentally uploaded to a public repository.
- **Safe Initialization**: If `student_data.csv` is absent when someone clones your repository, the application initializes safely with the 40 baseline sample records.
- **No Secrets**: No API keys, passwords, or cloud credentials are required or included.

### Publishing to GitHub:
```bash
cd "Placement-Readiness-Data-Explorer"
git add .
git commit -m "Upgrade: Add student data entry, persistent storage, and batch launcher"
git push origin main
```
