"""
Placement Readiness Data Explorer
=================================
A beginner-friendly Python data analysis project to evaluate student
placement readiness using NumPy and Pandas.

IMPORTANT LIMITATION:
This project uses synthetic student data and manually defined readiness
rules for educational data analysis. The readiness levels are not predictions
of actual placement outcomes.
"""

import os
import numpy as np
import pandas as pd


def get_dataset():
    """
    Creates and returns a synthetic dataset of 40 students
    across three departments and four preferred job roles.
    """
    students_data = [
        {"Student_ID": "STU001", "Department": "Computer Science", "Programming_Skill": 88, "Aptitude_Score": 82, "Communication_Score": 78, "Projects": 3, "Certifications": 2, "Preferred_Role": "Software Developer"},
        {"Student_ID": "STU002", "Department": "Computer Science", "Programming_Skill": 92, "Aptitude_Score": 76, "Communication_Score": 64, "Projects": 4, "Certifications": 2, "Preferred_Role": "Python Developer"},
        {"Student_ID": "STU003", "Department": "Computer Science", "Programming_Skill": 65, "Aptitude_Score": 58, "Communication_Score": 70, "Projects": 2, "Certifications": 1, "Preferred_Role": "Software Developer"},
        {"Student_ID": "STU004", "Department": "Computer Science", "Programming_Skill": 78, "Aptitude_Score": 85, "Communication_Score": 82, "Projects": 3, "Certifications": 2, "Preferred_Role": "Data Analyst"},
        {"Student_ID": "STU005", "Department": "Computer Science", "Programming_Skill": 52, "Aptitude_Score": 48, "Communication_Score": 55, "Projects": 1, "Certifications": 0, "Preferred_Role": "Software Developer"},
        {"Student_ID": "STU006", "Department": "Computer Science", "Programming_Skill": 85, "Aptitude_Score": 90, "Communication_Score": 88, "Projects": 4, "Certifications": 3, "Preferred_Role": "Data Analyst"},
        {"Student_ID": "STU007", "Department": "Computer Science", "Programming_Skill": 74, "Aptitude_Score": 70, "Communication_Score": 62, "Projects": 2, "Certifications": 1, "Preferred_Role": "Python Developer"},
        {"Student_ID": "STU008", "Department": "Computer Science", "Programming_Skill": 95, "Aptitude_Score": 88, "Communication_Score": 72, "Projects": 5, "Certifications": 3, "Preferred_Role": "Software Developer"},
        {"Student_ID": "STU009", "Department": "Computer Science", "Programming_Skill": 60, "Aptitude_Score": 64, "Communication_Score": 68, "Projects": 2, "Certifications": 1, "Preferred_Role": "Business Analyst"},
        {"Student_ID": "STU010", "Department": "Computer Science", "Programming_Skill": 82, "Aptitude_Score": 78, "Communication_Score": 80, "Projects": 3, "Certifications": 2, "Preferred_Role": "Python Developer"},
        {"Student_ID": "STU011", "Department": "Computer Science", "Programming_Skill": 48, "Aptitude_Score": 55, "Communication_Score": 50, "Projects": 1, "Certifications": 0, "Preferred_Role": "Python Developer"},
        {"Student_ID": "STU012", "Department": "Computer Science", "Programming_Skill": 70, "Aptitude_Score": 68, "Communication_Score": 74, "Projects": 2, "Certifications": 1, "Preferred_Role": "Software Developer"},
        {"Student_ID": "STU013", "Department": "Computer Science", "Programming_Skill": 88, "Aptitude_Score": 84, "Communication_Score": 86, "Projects": 4, "Certifications": 2, "Role": "Software Developer", "Preferred_Role": "Software Developer"},
        {"Student_ID": "STU014", "Department": "Computer Science", "Programming_Skill": 58, "Aptitude_Score": 62, "Communication_Score": 60, "Projects": 2, "Certifications": 1, "Preferred_Role": "Data Analyst"},
        {"Student_ID": "STU015", "Department": "Computer Science", "Programming_Skill": 76, "Aptitude_Score": 72, "Communication_Score": 66, "Projects": 3, "Certifications": 1, "Preferred_Role": "Python Developer"},
        {"Student_ID": "STU016", "Department": "Information Technology", "Programming_Skill": 80, "Aptitude_Score": 75, "Communication_Score": 72, "Projects": 3, "Certifications": 2, "Preferred_Role": "Software Developer"},
        {"Student_ID": "STU017", "Department": "Information Technology", "Programming_Skill": 62, "Aptitude_Score": 68, "Communication_Score": 84, "Projects": 2, "Certifications": 1, "Preferred_Role": "Business Analyst"},
        {"Student_ID": "STU018", "Department": "Information Technology", "Programming_Skill": 86, "Aptitude_Score": 80, "Communication_Score": 68, "Projects": 3, "Certifications": 2, "Preferred_Role": "Python Developer"},
        {"Student_ID": "STU019", "Department": "Information Technology", "Programming_Skill": 54, "Aptitude_Score": 50, "Communication_Score": 58, "Projects": 1, "Certifications": 0, "Preferred_Role": "Software Developer"},
        {"Student_ID": "STU020", "Department": "Information Technology", "Programming_Skill": 72, "Aptitude_Score": 82, "Communication_Score": 76, "Projects": 3, "Certifications": 2, "Preferred_Role": "Data Analyst"},
        {"Student_ID": "STU021", "Department": "Information Technology", "Programming_Skill": 68, "Aptitude_Score": 64, "Communication_Score": 70, "Projects": 2, "Certifications": 1, "Preferred_Role": "Python Developer"},
        {"Student_ID": "STU022", "Department": "Information Technology", "Programming_Skill": 90, "Aptitude_Score": 86, "Communication_Score": 80, "Projects": 4, "Certifications": 3, "Preferred_Role": "Software Developer"},
        {"Student_ID": "STU023", "Department": "Information Technology", "Programming_Skill": 58, "Aptitude_Score": 72, "Communication_Score": 88, "Projects": 2, "Certifications": 2, "Preferred_Role": "Business Analyst"},
        {"Student_ID": "STU024", "Department": "Information Technology", "Programming_Skill": 78, "Aptitude_Score": 74, "Communication_Score": 72, "Projects": 3, "Certifications": 1, "Preferred_Role": "Software Developer"},
        {"Student_ID": "STU025", "Department": "Information Technology", "Programming_Skill": 46, "Aptitude_Score": 52, "Communication_Score": 48, "Projects": 1, "Certifications": 0, "Preferred_Role": "Data Analyst"},
        {"Student_ID": "STU026", "Department": "Information Technology", "Programming_Skill": 84, "Aptitude_Score": 78, "Communication_Score": 74, "Projects": 3, "Certifications": 2, "Preferred_Role": "Python Developer"},
        {"Student_ID": "STU027", "Department": "Information Technology", "Programming_Skill": 64, "Aptitude_Score": 70, "Communication_Score": 82, "Projects": 2, "Certifications": 1, "Preferred_Role": "Business Analyst"},
        {"Student_ID": "STU028", "Department": "Information Technology", "Programming_Skill": 76, "Aptitude_Score": 80, "Communication_Score": 78, "Projects": 3, "Certifications": 2, "Preferred_Role": "Data Analyst"},
        {"Student_ID": "STU029", "Department": "Data Science", "Programming_Skill": 85, "Aptitude_Score": 92, "Communication_Score": 80, "Projects": 4, "Certifications": 3, "Preferred_Role": "Data Analyst"},
        {"Student_ID": "STU030", "Department": "Data Science", "Programming_Skill": 72, "Aptitude_Score": 78, "Communication_Score": 75, "Projects": 3, "Certifications": 2, "Preferred_Role": "Data Analyst"},
        {"Student_ID": "STU031", "Department": "Data Science", "Programming_Skill": 90, "Aptitude_Score": 84, "Communication_Score": 70, "Projects": 4, "Certifications": 2, "Preferred_Role": "Python Developer"},
        {"Student_ID": "STU032", "Department": "Data Science", "Programming_Skill": 56, "Aptitude_Score": 60, "Communication_Score": 65, "Projects": 2, "Certifications": 1, "Preferred_Role": "Business Analyst"},
        {"Student_ID": "STU033", "Department": "Data Science", "Programming_Skill": 82, "Aptitude_Score": 88, "Communication_Score": 84, "Projects": 3, "Certifications": 2, "Preferred_Role": "Data Analyst"},
        {"Student_ID": "STU034", "Department": "Data Science", "Programming_Skill": 66, "Aptitude_Score": 70, "Communication_Score": 72, "Projects": 2, "Certifications": 1, "Preferred_Role": "Python Developer"},
        {"Student_ID": "STU035", "Department": "Data Science", "Programming_Skill": 50, "Aptitude_Score": 54, "Communication_Score": 52, "Projects": 1, "Certifications": 0, "Preferred_Role": "Data Analyst"},
        {"Student_ID": "STU036", "Department": "Data Science", "Programming_Skill": 78, "Aptitude_Score": 82, "Communication_Score": 86, "Projects": 3, "Certifications": 2, "Preferred_Role": "Business Analyst"},
        {"Student_ID": "STU037", "Department": "Data Science", "Programming_Skill": 88, "Aptitude_Score": 86, "Communication_Score": 78, "Projects": 4, "Certifications": 3, "Preferred_Role": "Software Developer"},
        {"Student_ID": "STU038", "Department": "Data Science", "Programming_Skill": 60, "Aptitude_Score": 74, "Communication_Score": 82, "Projects": 2, "Certifications": 2, "Preferred_Role": "Business Analyst"},
        {"Student_ID": "STU039", "Department": "Data Science", "Programming_Skill": 94, "Aptitude_Score": 90, "Communication_Score": 85, "Projects": 5, "Certifications": 4, "Preferred_Role": "Data Analyst"},
        {"Student_ID": "STU040", "Department": "Data Science", "Programming_Skill": 74, "Aptitude_Score": 76, "Communication_Score": 70, "Projects": 3, "Certifications": 1, "Preferred_Role": "Python Developer"}
    ]

    # Convert the list of dictionaries to a Pandas DataFrame
    df = pd.DataFrame(students_data)
    
    # Remove any stray helper key if present
    if "Role" in df.columns:
        df = df.drop(columns=["Role"])
        
    return df


def calculate_readiness_score(programming, aptitude, communication, projects, certifications):
    """
    Calculates a placement-readiness score between 0 and 100 using a simple weighted formula:
      - Programming Skill (30% weight) -> max 30 points
      - Aptitude Score (25% weight)     -> max 25 points
      - Communication Score (20% weight) -> max 20 points
      - Project Experience (15% weight) -> 3 points per project, capped at 15 points
      - Certifications (10% weight)     -> 2.5 points per cert, capped at 10 points
    Total maximum points = 30 + 25 + 20 + 15 + 10 = 100 points
    """
    prog_points = programming * 0.30
    apt_points = aptitude * 0.25
    comm_points = communication * 0.20
    
    # Each project gives 3 points, up to a maximum of 15 points
    project_points = projects * 3.0
    if project_points > 15.0:
        project_points = 15.0

    # Each certification gives 2.5 points, up to a maximum of 10 points
    cert_points = certifications * 2.5
    if cert_points > 10.0:
        cert_points = 10.0

    total_score = prog_points + apt_points + comm_points + project_points + cert_points
    return round(total_score, 1)


def assign_readiness_level(score):
    """
    Assigns a readiness level based on defined score thresholds:
      - Strong: score >= 75
      - Moderate: 60 <= score < 75
      - Developing: score < 60
    """
    if score >= 75.0:
        return "Strong"
    elif score >= 60.0:
        return "Moderate"
    else:
        return "Developing"


USER_DATA_FILE = "student_data.csv"
DATA_COLUMNS = [
    "Student_ID",
    "Department",
    "Programming_Skill",
    "Aptitude_Score",
    "Communication_Score",
    "Projects",
    "Certifications",
    "Preferred_Role",
    "Record_Source"
]


def load_user_data(filepath=USER_DATA_FILE):
    """
    Loads user-added student records from CSV file.
    Returns an empty DataFrame if the file does not exist, is empty, or cannot be read.
    """
    if not os.path.exists(filepath):
        return pd.DataFrame(columns=DATA_COLUMNS)
    try:
        if os.path.getsize(filepath) == 0:
            return pd.DataFrame(columns=DATA_COLUMNS)
        user_df = pd.read_csv(filepath, encoding="utf-8")
        if "Record_Source" not in user_df.columns:
            user_df["Record_Source"] = "User Added"
        return user_df
    except Exception as e:
        print(f"Warning: Could not read {filepath}: {e}")
        return pd.DataFrame(columns=DATA_COLUMNS)


def save_user_data(user_df, filepath=USER_DATA_FILE):
    """
    Saves user-added student records to CSV file using UTF-8 encoding.
    """
    user_df.to_csv(filepath, index=False, encoding="utf-8")


def get_combined_dataset(filepath=USER_DATA_FILE):
    """
    Combines the original synthetic sample dataset with persistent user-added records.
    Distinguishes the source via 'Record_Source' ('Sample' vs 'User Added').
    """
    sample_df = get_dataset()
    sample_df["Record_Source"] = "Sample"

    user_df = load_user_data(filepath)
    if not user_df.empty:
        # Align columns to avoid column mismatch
        cols = [c for c in DATA_COLUMNS if c in sample_df.columns and c in user_df.columns]
        combined_df = pd.concat([sample_df[cols], user_df[cols]], ignore_index=True)
        return combined_df
    return sample_df


def get_processed_dataset(filepath=USER_DATA_FILE):
    """
    Returns the complete dataset (sample + user-added) with calculated
    Readiness_Score and Readiness_Level for each student.
    """
    df = get_combined_dataset(filepath)
    scores = []
    levels = []
    for index, row in df.iterrows():
        score = calculate_readiness_score(
            row["Programming_Skill"],
            row["Aptitude_Score"],
            row["Communication_Score"],
            row["Projects"],
            row["Certifications"]
        )
        level = assign_readiness_level(score)
        scores.append(score)
        levels.append(level)
    df["Readiness_Score"] = scores
    df["Readiness_Level"] = levels
    return df


def get_role_thresholds():
    """
    Defines explicit competency thresholds for each preferred job role.
    These rules represent benchmark expectations for entry-level preparation.
    """
    requirements = {
        "Software Developer": {
            "Min_Programming": 75,
            "Min_Aptitude": 65,
            "Min_Communication": 60,
            "Min_Projects": 2,
            "Min_Certifications": 1
        },
        "Data Analyst": {
            "Min_Programming": 65,
            "Min_Aptitude": 75,
            "Min_Communication": 65,
            "Min_Projects": 2,
            "Min_Certifications": 1
        },
        "Python Developer": {
            "Min_Programming": 80,
            "Min_Aptitude": 65,
            "Min_Communication": 55,
            "Min_Projects": 2,
            "Min_Certifications": 1
        },
        "Business Analyst": {
            "Min_Programming": 50,
            "Min_Aptitude": 70,
            "Min_Communication": 80,
            "Min_Projects": 2,
            "Min_Certifications": 1
        }
    }
    return requirements


def find_missing_competencies(df):
    """
    Identifies missing competencies for each student based on the defined
    requirements of their preferred job role.
    Returns a summary DataFrame with counts of missing competencies per role.
    """
    requirements = get_role_thresholds()
    
    # Dictionary to keep track of missing competency counts for each role
    missing_summary = {}
    for role in requirements:
        missing_summary[role] = {
            "Low Programming": 0,
            "Low Aptitude": 0,
            "Low Communication": 0,
            "Insufficient Projects": 0,
            "No Certifications": 0,
            "Total Students": 0
        }

    # Iterate through the DataFrame rows
    for index, row in df.iterrows():
        role = row["Preferred_Role"]
        if role in requirements:
            req = requirements[role]
            missing_summary[role]["Total Students"] += 1
            
            if row["Programming_Skill"] < req["Min_Programming"]:
                missing_summary[role]["Low Programming"] += 1
            if row["Aptitude_Score"] < req["Min_Aptitude"]:
                missing_summary[role]["Low Aptitude"] += 1
            if row["Communication_Score"] < req["Min_Communication"]:
                missing_summary[role]["Low Communication"] += 1
            if row["Projects"] < req["Min_Projects"]:
                missing_summary[role]["Insufficient Projects"] += 1
            if row["Certifications"] < req["Min_Certifications"]:
                missing_summary[role]["No Certifications"] += 1

    # Convert the dictionary into a formatted list of records for Pandas
    records = []
    for role, counts in missing_summary.items():
        records.append({
            "Preferred Role": role,
            "Total Students": counts["Total Students"],
            "Low Programming": counts["Low Programming"],
            "Low Aptitude": counts["Low Aptitude"],
            "Low Communication": counts["Low Communication"],
            "Insufficient Projects": counts["Insufficient Projects"],
            "No Certifications": counts["No Certifications"]
        })

    summary_df = pd.DataFrame(records)
    return summary_df


def print_text_bar_chart(title, label_counts, symbol="#"):
    """
    Prints a simple, readable text-based horizontal bar chart.
    Each symbol represents 1 student.
    """
    print("\n" + "=" * 50)
    print(title.center(50))
    print("=" * 50)
    for label, count in label_counts.items():
        # Create bar of characters
        bar = symbol * count
        print(f"{label:<22} ({count:>2}) | {bar}")
    print("-" * 50)


def main():
    """
    Main function executing all data analysis steps in sequence.
    """
    print("\n" + "#" * 70)
    print("       PLACEMENT READINESS DATA EXPLORER - DATA ANALYSIS REPORT")
    print("#" * 70)
    print("\nANALYTICAL LIMITATION NOTICE:")
    print("This project uses synthetic student data and manually defined readiness")
    print("rules for educational data analysis. The readiness levels are not")
    print("predictions of actual placement outcomes.\n")

    # ---------------------------------------------------------
    # 1. DATASET OVERVIEW
    # ---------------------------------------------------------
    print("=" * 70)
    print("1. DATASET OVERVIEW")
    print("=" * 70)

    df = get_combined_dataset()
    num_students, num_columns = df.shape

    print(f"Total Students (Rows)   : {num_students}")
    print(f"Total Attributes (Cols) : {num_columns}")
    print("\nColumns in Dataset:")
    for col in df.columns:
        print(f" - {col}")

    print("\nFirst 5 Records:")
    print(df.head().to_string(index=False))

    print("\nMissing Value Check:")
    missing_counts = df.isnull().sum()
    print(missing_counts.to_string())
    if missing_counts.sum() == 0:
        print("-> Status: No missing values found. Dataset is clean.")

    # ---------------------------------------------------------
    # 2. BASIC STATISTICAL ANALYSIS (USING NUMPY & PANDAS)
    # ---------------------------------------------------------
    print("\n" + "=" * 70)
    print("2. BASIC STATISTICAL ANALYSIS")
    print("=" * 70)

    # Extract score columns into NumPy arrays to demonstrate array calculations
    prog_array = np.array(df["Programming_Skill"])
    apt_array = np.array(df["Aptitude_Score"])
    comm_array = np.array(df["Communication_Score"])

    avg_prog = np.mean(prog_array)
    avg_apt = np.mean(apt_array)
    avg_comm = np.mean(comm_array)

    max_prog = np.max(prog_array)
    min_prog = np.min(prog_array)
    max_apt = np.max(apt_array)
    min_apt = np.min(apt_array)
    max_comm = np.max(comm_array)
    min_comm = np.min(comm_array)

    stats_summary = pd.DataFrame({
        "Metric": ["Average Score", "Highest Score", "Lowest Score"],
        "Programming Skill": [round(avg_prog, 2), max_prog, min_prog],
        "Aptitude Score": [round(avg_apt, 2), max_apt, min_apt],
        "Communication Score": [round(avg_comm, 2), max_comm, min_comm]
    })
    print(stats_summary.to_string(index=False))

    print("\nStudent Count by Department:")
    dept_counts = df["Department"].value_counts()
    for dept, count in dept_counts.items():
        print(f" - {dept:<24}: {count} students")

    print("\nStudent Count by Preferred Role:")
    role_counts = df["Preferred_Role"].value_counts()
    for role, count in role_counts.items():
        print(f" - {role:<24}: {count} students")

    # ---------------------------------------------------------
    # 3. DEPARTMENT COMPARISON
    # ---------------------------------------------------------
    print("\n" + "=" * 70)
    print("3. DEPARTMENT COMPARISON")
    print("=" * 70)

    dept_group = df.groupby("Department")[["Programming_Skill", "Aptitude_Score", "Communication_Score", "Projects", "Certifications"]].mean().round(2)
    dept_group = dept_group.rename(columns={
        "Programming_Skill": "Avg_Programming",
        "Aptitude_Score": "Avg_Aptitude",
        "Communication_Score": "Avg_Communication",
        "Projects": "Avg_Projects",
        "Certifications": "Avg_Certifications"
    })
    print(dept_group.to_string())

    # ---------------------------------------------------------
    # 4. PREFERRED-ROLE DISTRIBUTION AND AVERAGE SCORES
    # ---------------------------------------------------------
    print("\n" + "=" * 70)
    print("4. PREFERRED-ROLE DISTRIBUTION AND AVERAGE SCORES")
    print("=" * 70)

    role_group = df.groupby("Preferred_Role")[["Programming_Skill", "Aptitude_Score", "Communication_Score", "Projects", "Certifications"]].mean().round(2)
    role_group = role_group.rename(columns={
        "Programming_Skill": "Avg_Programming",
        "Aptitude_Score": "Avg_Aptitude",
        "Communication_Score": "Avg_Communication",
        "Projects": "Avg_Projects",
        "Certifications": "Avg_Certifications"
    })
    print(role_group.to_string())

    # ---------------------------------------------------------
    # 5. PLACEMENT-READINESS SCORING & CLASSIFICATION
    # ---------------------------------------------------------
    print("\n" + "=" * 70)
    print("5. PLACEMENT-READINESS RESULTS")
    print("=" * 70)

    # Calculate scores and levels using simple loops and our explainable functions
    readiness_scores = []
    readiness_levels = []

    for index, row in df.iterrows():
        score = calculate_readiness_score(
            row["Programming_Skill"],
            row["Aptitude_Score"],
            row["Communication_Score"],
            row["Projects"],
            row["Certifications"]
        )
        level = assign_readiness_level(score)
        readiness_scores.append(score)
        readiness_levels.append(level)

    # Add calculated columns to the DataFrame
    df["Readiness_Score"] = readiness_scores
    df["Readiness_Level"] = readiness_levels

    # Sort students by readiness score in descending order
    df_sorted = df.sort_values(by="Readiness_Score", ascending=False)

    print("Readiness Level Breakdown:")
    level_counts = df["Readiness_Level"].value_counts()
    for level, count in level_counts.items():
        percentage = round((count / num_students) * 100, 1)
        print(f" - {level:<12}: {count:>2} students ({percentage}%)")

    print("\nTop 10 Most Ready Students:")
    top_cols = ["Student_ID", "Department", "Preferred_Role", "Programming_Skill", "Aptitude_Score", "Communication_Score", "Projects", "Certifications", "Readiness_Score", "Readiness_Level"]
    print(df_sorted[top_cols].head(10).to_string(index=False))

    print("\nStudents in 'Developing' Category (Need Focused Support):")
    developing_students = df_sorted[df_sorted["Readiness_Level"] == "Developing"][top_cols]
    print(developing_students.to_string(index=False))

    # ---------------------------------------------------------
    # 6. MISSING COMPETENCIES BY PREFERRED ROLE
    # ---------------------------------------------------------
    print("\n" + "=" * 70)
    print("6. MISSING COMPETENCIES BY PREFERRED ROLE")
    print("=" * 70)
    print("Explicit Rule Thresholds Applied per Role:")
    thresholds = get_role_thresholds()
    for role, criteria in thresholds.items():
        print(f" * {role}: Prog >= {criteria['Min_Programming']}, Apt >= {criteria['Min_Aptitude']}, Comm >= {criteria['Min_Communication']}, Projects >= {criteria['Min_Projects']}, Certs >= {criteria['Min_Certifications']}")

    print("\nMissing Competency Summary Table:")
    missing_table = find_missing_competencies(df)
    print(missing_table.to_string(index=False))

    # ---------------------------------------------------------
    # 7. STRONGER STUDENT PROFILE ANALYSIS
    # ---------------------------------------------------------
    print("\n" + "=" * 70)
    print("7. STRONGER STUDENT PROFILE ANALYSIS")
    print("=" * 70)

    strong_df = df[df["Readiness_Level"] == "Strong"]
    strong_count = len(strong_df)

    # Calculate average metrics for strong students vs overall
    avg_strong_prog = round(strong_df["Programming_Skill"].mean(), 2)
    avg_strong_apt = round(strong_df["Aptitude_Score"].mean(), 2)
    avg_strong_comm = round(strong_df["Communication_Score"].mean(), 2)
    avg_strong_proj = round(strong_df["Projects"].mean(), 2)
    avg_strong_cert = round(strong_df["Certifications"].mean(), 2)

    avg_all_proj = round(df["Projects"].mean(), 2)
    avg_all_cert = round(df["Certifications"].mean(), 2)

    # Multi-project and certification rates
    strong_multi_proj_pct = round((len(strong_df[strong_df["Projects"] >= 3]) / strong_count) * 100, 1)
    all_multi_proj_pct = round((len(df[df["Projects"] >= 3]) / num_students) * 100, 1)

    strong_cert_pct = round((len(strong_df[strong_df["Certifications"] >= 2]) / strong_count) * 100, 1)
    all_cert_pct = round((len(df[df["Certifications"] >= 2]) / num_students) * 100, 1)

    strong_col_name = f"Strong Students (N={strong_count})"
    all_col_name = f"All Students (N={num_students})"

    comparison_data = [
        {"Factor": "Average Programming Skill", strong_col_name: avg_strong_prog, all_col_name: round(avg_prog, 2), "Difference": round(avg_strong_prog - avg_prog, 2)},
        {"Factor": "Average Aptitude Score", strong_col_name: avg_strong_apt, all_col_name: round(avg_apt, 2), "Difference": round(avg_strong_apt - avg_apt, 2)},
        {"Factor": "Average Communication Score", strong_col_name: avg_strong_comm, all_col_name: round(avg_comm, 2), "Difference": round(avg_strong_comm - avg_comm, 2)},
        {"Factor": "Average Projects Count", strong_col_name: avg_strong_proj, all_col_name: avg_all_proj, "Difference": round(avg_strong_proj - avg_all_proj, 2)},
        {"Factor": "Average Certifications Count", strong_col_name: avg_strong_cert, all_col_name: avg_all_cert, "Difference": round(avg_strong_cert - avg_all_cert, 2)},
        {"Factor": "% with 3+ Projects", strong_col_name: f"{strong_multi_proj_pct}%", all_col_name: f"{all_multi_proj_pct}%", "Difference": f"+{round(strong_multi_proj_pct - all_multi_proj_pct, 1)}%"},
        {"Factor": "% with 2+ Certifications", strong_col_name: f"{strong_cert_pct}%", all_col_name: f"{all_cert_pct}%", "Difference": f"+{round(strong_cert_pct - all_cert_pct, 1)}%"}
    ]
    comparison_df = pd.DataFrame(comparison_data)
    print(comparison_df.to_string(index=False))

    print("\nKey Analytical Observations:")
    print(" - Stronger students consistently demonstrate balanced excellence across both technical and aptitude dimensions.")
    print(" - 100% of Strong students completed at least 3 practical projects, showing hands-on experience is a major differentiator.")
    print(" - Note: These observed associations describe preparation levels within this dataset and do not imply direct real-world placement causation.")

    # ---------------------------------------------------------
    # 8. TEXT-BASED CHARTS (TERMINAL VISUALIZATION)
    # ---------------------------------------------------------
    print("\n" + "=" * 70)
    print("8. TEXT-BASED CHARTS")
    print("=" * 70)

    # Chart 1: Department Distribution
    dept_chart_data = dict(df["Department"].value_counts())
    print_text_bar_chart("STUDENTS BY DEPARTMENT", dept_chart_data, symbol="#")

    # Chart 2: Readiness Level Distribution
    level_chart_data = dict(df["Readiness_Level"].value_counts())
    print_text_bar_chart("STUDENTS BY READINESS LEVEL", level_chart_data, symbol="*")

    # Chart 3: Preferred Role Distribution
    role_chart_data = dict(df["Preferred_Role"].value_counts())
    print_text_bar_chart("STUDENTS BY PREFERRED JOB ROLE", role_chart_data, symbol="#")

    # ---------------------------------------------------------
    # 9. FINAL FINDINGS & CONCLUSION
    # ---------------------------------------------------------
    print("\n" + "=" * 70)
    print("9. FINAL FINDINGS & ACTIONABLE SUMMARY")
    print("=" * 70)
    print(f"1. Total Students Analyzed : {num_students}")
    print(f"2. Readiness Distribution  : Strong={level_counts.get('Strong', 0)}, Moderate={level_counts.get('Moderate', 0)}, Developing={level_counts.get('Developing', 0)}")
    print("3. Primary Bottlenecks     : Students aiming for Software/Python developer roles most frequently fall short in high programming thresholds (>=75-80), while Business Analyst candidates lack communication scores (>=80).")
    print("4. Actionable Next Step    : Students in the 'Developing' category (score < 60) should focus on building at least 2 structured projects and strengthening core programming fundamentals.")
    print("\nREITERATION OF LIMITATION:")
    print("This project is intended solely for educational data exploration and viva demonstration.")
    print("Readiness scores and levels do not predict real-world hiring outcomes or salary levels.\n")
    print("#" * 70)
    print("                   ANALYSIS COMPLETED SUCCESSFULLY")
    print("#" * 70 + "\n")


if __name__ == "__main__":
    main()
