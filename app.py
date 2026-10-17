"""
Placement Readiness Explorer - Streamlit Web Application
=========================================================
A student data analysis application to explore placement readiness
using Python, NumPy, Pandas, and Streamlit.
"""

import os
import streamlit as st
import pandas as pd
import numpy as np

# Import core dataset and analysis functions from placement_readiness.py
from placement_readiness import (
    get_dataset,
    get_processed_dataset,
    get_role_thresholds,
    find_missing_competencies,
    calculate_readiness_score,
    assign_readiness_level,
    load_user_data,
    save_user_data,
    USER_DATA_FILE
)

# ------------------------------------------------------------------------------
# PAGE CONFIGURATION
# ------------------------------------------------------------------------------
st.set_page_config(
    page_title="Placement Readiness Explorer",
    layout="wide"
)

# User-facing column name mappings for readable tables
DISPLAY_COLUMNS_MAP = {
    "Student_ID": "Student ID",
    "Department": "Department",
    "Preferred_Role": "Preferred Role",
    "Programming_Skill": "Programming Skill",
    "Aptitude_Score": "Aptitude Score",
    "Communication_Score": "Communication Score",
    "Projects": "Projects",
    "Certifications": "Certifications",
    "Readiness_Score": "Readiness Score",
    "Readiness_Level": "Readiness Level",
    "Record_Source": "Record Source"
}


def get_display_table(dataframe, selected_cols=None):
    """
    Returns a copy of the dataframe with human-readable column names for display.
    """
    if selected_cols is None:
        selected_cols = [c for c in DISPLAY_COLUMNS_MAP.keys() if c in dataframe.columns]
    table = dataframe[selected_cols].copy()
    return table.rename(columns=DISPLAY_COLUMNS_MAP)


# ------------------------------------------------------------------------------
# DATA LOADING
# ------------------------------------------------------------------------------
df = get_processed_dataset()
total_students = len(df)
sample_count = len(df[df["Record_Source"] == "Sample"])
user_count = len(df[df["Record_Source"] == "User Added"])

# ------------------------------------------------------------------------------
# SIDEBAR NAVIGATION
# ------------------------------------------------------------------------------
st.sidebar.markdown("### Navigation")
page = st.sidebar.radio(
    "Go to",
    [
        "Overview",
        "Student Records",
        "Add Student",
        "Department Analysis",
        "Role Analysis",
        "Readiness Review",
        "Findings and Method"
    ],
    label_visibility="collapsed"
)

st.sidebar.divider()
st.sidebar.markdown(f"**Total Records:** {total_students}")
st.sidebar.caption(f"{sample_count} sample records\n\n{user_count} student-added records")

# ------------------------------------------------------------------------------
# HEADER
# ------------------------------------------------------------------------------
st.markdown("<h3 style='margin-bottom: 2px; color: #34495E;'>Placement Readiness Explorer</h3>", unsafe_allow_html=True)
st.caption("Explore student skills, compare departments and identify areas to improve.")
st.write("")

# ==============================================================================
# 1. OVERVIEW
# ==============================================================================
if page == "Overview":
    # Key summary metrics
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.metric("Total Students", total_students)
    with m2:
        avg_prog = round(float(df["Programming_Skill"].mean()), 1)
        st.metric("Avg. Programming", f"{avg_prog} / 100")
    with m3:
        avg_apt = round(float(df["Aptitude_Score"].mean()), 1)
        st.metric("Avg. Aptitude", f"{avg_apt} / 100")
    with m4:
        avg_comm = round(float(df["Communication_Score"].mean()), 1)
        st.metric("Avg. Communication", f"{avg_comm} / 100")

    st.caption(f"{sample_count} sample records and {user_count} student-added records currently in dataset.")
    st.write("")

    # Short preview table
    st.markdown("##### Recent Student Preview")
    preview_cols = ["Student_ID", "Department", "Preferred_Role", "Readiness_Score", "Readiness_Level"]
    st.dataframe(get_display_table(df.head(5), preview_cols), hide_index=True)

    st.caption("Showing the first 5 records. Switch to **Student Records** in the sidebar to view and filter the full dataset.")


# ==============================================================================
# 2. STUDENT RECORDS
# ==============================================================================
elif page == "Student Records":
    st.markdown("##### Student Records")
    st.caption("Browse, filter, and inspect student records across the dataset.")

    # Filter controls in columns
    f1, f2, f3, f4 = st.columns(4)

    dept_options = ["All"] + sorted(list(df["Department"].unique()))
    role_options = ["All"] + sorted(list(df["Preferred_Role"].unique()))
    level_options = ["All", "Strong", "Moderate", "Developing"]
    source_options = ["All", "Sample", "User Added"]

    with f1:
        sel_dept = st.selectbox("Department", dept_options)
    with f2:
        sel_role = st.selectbox("Preferred Role", role_options)
    with f3:
        sel_level = st.selectbox("Readiness Level", level_options)
    with f4:
        sel_source = st.selectbox("Record Source", source_options)

    # Filter the DataFrame
    filtered_df = df.copy()
    if sel_dept != "All":
        filtered_df = filtered_df[filtered_df["Department"] == sel_dept]
    if sel_role != "All":
        filtered_df = filtered_df[filtered_df["Preferred_Role"] == sel_role]
    if sel_level != "All":
        filtered_df = filtered_df[filtered_df["Readiness_Level"] == sel_level]
    if sel_source != "All":
        filtered_df = filtered_df[filtered_df["Record_Source"] == sel_source]

    if filtered_df.empty:
        st.info("No student records match the selected filter combination.")
    else:
        st.write(f"Showing **{len(filtered_df)}** of **{total_students}** records:")
        st.dataframe(get_display_table(filtered_df), hide_index=True)

    st.write("")

    # Simple Record Management Subsection
    with st.expander("Manage Added Records", expanded=False):
        user_df = load_user_data(USER_DATA_FILE)
        if user_df.empty:
            st.info("No student-added records in storage. Sample records (STU001–STU040) are protected and cannot be deleted.")
        else:
            st.markdown(f"**Saved Student-Added Records ({len(user_df)})**")
            st.dataframe(get_display_table(user_df), hide_index=True)

            del_id = st.selectbox("Select Student ID to remove", sorted(user_df["Student_ID"].tolist()))
            if st.button("Delete Record", type="secondary"):
                updated_user_df = user_df[user_df["Student_ID"] != del_id]
                save_user_data(updated_user_df, USER_DATA_FILE)
                st.success(f"Student record '{del_id}' removed from storage.")
                st.rerun()


# ==============================================================================
# 3. ADD STUDENT
# ==============================================================================
elif page == "Add Student":
    st.markdown("##### Add a Student Record")
    st.caption("Enter details for a new student. Validated entries are saved to student_data.csv and included in all analysis.")

    with st.form("add_student_form", clear_on_submit=False):
        # 1. Student Information
        st.markdown("**Student Information**")
        c1, c2, c3 = st.columns(3)
        with c1:
            input_id = st.text_input("Student ID", placeholder="e.g. STU101")
        with c2:
            input_dept = st.selectbox("Department", ["Computer Science", "Data Science", "Information Technology"])
        with c3:
            input_role = st.selectbox("Preferred Role", ["Software Developer", "Data Analyst", "Python Developer", "Business Analyst"])

        # 2. Assessment Scores
        st.markdown("**Assessment Scores (0 to 100)**")
        s1, s2, s3 = st.columns(3)
        with s1:
            input_prog = st.number_input("Programming Skill", min_value=0, max_value=100, value=75, step=1)
        with s2:
            input_apt = st.number_input("Aptitude Score", min_value=0, max_value=100, value=75, step=1)
        with s3:
            input_comm = st.number_input("Communication Score", min_value=0, max_value=100, value=75, step=1)

        # 3. Experience and Certifications
        st.markdown("**Experience**")
        e1, e2 = st.columns(2)
        with e1:
            input_proj = st.number_input("Number of Projects", min_value=0, max_value=25, value=2, step=1)
        with e2:
            input_cert = st.number_input("Number of Certifications", min_value=0, max_value=25, value=1, step=1)

        st.write("")
        submit = st.form_submit_button("Add Student")

    if submit:
        clean_id = input_id.strip()

        # Input validation
        if not clean_id:
            st.warning("Please provide a Student ID.")
        elif clean_id.upper() in df["Student_ID"].str.upper().values:
            st.error(f"Student ID '{clean_id}' already exists. Please choose a unique identifier.")
        elif not (0 <= input_prog <= 100 and 0 <= input_apt <= 100 and 0 <= input_comm <= 100):
            st.error("All scores must be between 0 and 100.")
        elif input_proj < 0 or input_cert < 0:
            st.error("Project and certification counts cannot be negative.")
        else:
            new_record = {
                "Student_ID": clean_id,
                "Department": input_dept,
                "Programming_Skill": int(input_prog),
                "Aptitude_Score": int(input_apt),
                "Communication_Score": int(input_comm),
                "Projects": int(input_proj),
                "Certifications": int(input_cert),
                "Preferred_Role": input_role,
                "Record_Source": "User Added"
            }

            user_df = load_user_data(USER_DATA_FILE)
            user_df = pd.concat([user_df, pd.DataFrame([new_record])], ignore_index=True)
            save_user_data(user_df, USER_DATA_FILE)

            score = calculate_readiness_score(input_prog, input_apt, input_comm, input_proj, input_cert)
            level = assign_readiness_level(score)

            st.success(f"Student '{clean_id}' added successfully. Calculated Readiness Score: {score}/100 ({level}).")
            st.rerun()


# ==============================================================================
# 4. DEPARTMENT ANALYSIS
# ==============================================================================
elif page == "Department Analysis":
    st.markdown("##### Department Analysis")
    st.caption("Comparison of student enrollment and average scores across academic departments.")

    dept_stats = df.groupby("Department").agg({
        "Student_ID": "count",
        "Programming_Skill": "mean",
        "Aptitude_Score": "mean",
        "Communication_Score": "mean",
        "Projects": "mean",
        "Certifications": "mean"
    }).round(1).reset_index()

    dept_stats_display = dept_stats.rename(columns={
        "Department": "Department",
        "Student_ID": "Student Count",
        "Programming_Skill": "Avg. Programming",
        "Aptitude_Score": "Avg. Aptitude",
        "Communication_Score": "Avg. Communication",
        "Projects": "Avg. Projects",
        "Certifications": "Avg. Certifications"
    })

    st.dataframe(dept_stats_display, hide_index=True)

    st.write("")
    st.markdown("**Average Scores by Department**")
    chart_data = dept_stats.set_index("Department")[["Programming_Skill", "Aptitude_Score", "Communication_Score"]]
    chart_data = chart_data.rename(columns={
        "Programming_Skill": "Programming",
        "Aptitude_Score": "Aptitude",
        "Communication_Score": "Communication"
    })
    st.bar_chart(chart_data)


# ==============================================================================
# 5. ROLE ANALYSIS
# ==============================================================================
elif page == "Role Analysis":
    st.markdown("##### Role Analysis")
    st.caption("Student interest across preferred career roles and benchmark skill requirements.")

    r1, r2 = st.columns([1, 1])

    with r1:
        st.markdown("**Students per Role**")
        role_counts = df["Preferred_Role"].value_counts().reset_index()
        role_counts.columns = ["Preferred Role", "Student Count"]
        st.dataframe(role_counts, hide_index=True)

    with r2:
        st.markdown("**Entry-Level Role Benchmarks**")
        thresholds = get_role_thresholds()
        bench_records = []
        for role, criteria in thresholds.items():
            bench_records.append({
                "Role": role,
                "Min Programming": criteria["Min_Programming"],
                "Min Aptitude": criteria["Min_Aptitude"],
                "Min Comm.": criteria["Min_Communication"],
                "Min Projects": criteria["Min_Projects"],
                "Min Certs": criteria["Min_Certifications"]
            })
        st.dataframe(pd.DataFrame(bench_records), hide_index=True)

    st.write("")
    st.markdown("**Common Missing Competencies by Role**")
    st.caption("Number of students targeting each role whose current scores or experience fall below the benchmark:")
    missing_df = find_missing_competencies(df)
    st.dataframe(missing_df, hide_index=True)


# ==============================================================================
# 6. READINESS REVIEW
# ==============================================================================
elif page == "Readiness Review":
    st.markdown("##### Placement Readiness Review")
    st.caption("Evaluation of student preparation based on the weighted scoring formula.")

    # Category breakdown row
    level_counts = df["Readiness_Level"].value_counts()
    c1, c2, c3 = st.columns(3)
    with c1:
        strong_cnt = level_counts.get("Strong", 0)
        st.metric("Strong (>= 75)", f"{strong_cnt} students", f"{round(strong_cnt / total_students * 100, 1)}%")
    with c2:
        mod_cnt = level_counts.get("Moderate", 0)
        st.metric("Moderate (60 - 74.9)", f"{mod_cnt} students", f"{round(mod_cnt / total_students * 100, 1)}%")
    with c3:
        dev_cnt = level_counts.get("Developing", 0)
        st.metric("Developing (< 60)", f"{dev_cnt} students", f"{round(dev_cnt / total_students * 100, 1)}%")

    st.write("")
    st.markdown("**Readiness Category Distribution**")
    chart_levels = pd.Series({
        "Strong": level_counts.get("Strong", 0),
        "Moderate": level_counts.get("Moderate", 0),
        "Developing": level_counts.get("Developing", 0)
    })
    st.bar_chart(chart_levels)

    st.write("")
    st.markdown("**Students Ranked by Readiness Score**")
    sorted_df = df.sort_values(by="Readiness_Score", ascending=False)
    rank_cols = ["Student_ID", "Department", "Preferred_Role", "Programming_Skill", "Aptitude_Score", "Communication_Score", "Projects", "Certifications", "Readiness_Score", "Readiness_Level"]
    st.dataframe(get_display_table(sorted_df, rank_cols), hide_index=True)

    with st.expander("Scoring Formula & Rationale", expanded=False):
        st.markdown("""
        **Scoring Weights (Total: 100 Points):**
        - **Programming Skill (30%):** Score $\\times 0.30$ (Max 30 pts)
        - **Aptitude Score (25%):** Score $\\times 0.25$ (Max 25 pts)
        - **Communication Score (20%):** Score $\\times 0.20$ (Max 20 pts)
        - **Project Experience (15%):** 3 points per project, capped at 15 pts (5 projects)
        - **Certifications (10%):** 2.5 points per certification, capped at 10 pts (4 certs)

        **Classification Tiers:**
        - **Strong:** Score $\\ge 75.0$
        - **Moderate:** $60.0 \\le \\text{Score} < 75.0$
        - **Developing:** Score $< 60.0$
        """)


# ==============================================================================
# 7. FINDINGS AND METHOD
# ==============================================================================
elif page == "Findings and Method":
    st.markdown("##### Findings and Methodology")

    # Dynamic observations calculated from actual data
    top_dept = df.groupby("Department")["Programming_Skill"].mean().idxmax()
    top_dept_score = round(df.groupby("Department")["Programming_Skill"].mean().max(), 1)
    common_role = df["Preferred_Role"].value_counts().idxmax()
    common_role_cnt = df["Preferred_Role"].value_counts().max()

    strong_df = df[df["Readiness_Level"] == "Strong"]
    strong_pct = round((len(strong_df) / total_students) * 100, 1)

    st.markdown("**Key Observations from Current Data:**")
    st.markdown(f"""
    1. **Department Strengths:** **{top_dept}** holds the highest average programming score ({top_dept_score} / 100).
    2. **Role Interest:** **{common_role}** is the most popular role choice with {common_role_cnt} interested students.
    3. **Strong Profiles:** {len(strong_df)} students ({strong_pct}%) meet the Strong readiness threshold. In this group, average project completion is {round(strong_df['Projects'].mean(), 1)} projects compared to {round(df['Projects'].mean(), 1)} across the full batch.
    4. **Common Gaps:** Technical role candidates (Software and Python Developers) most frequently fall short in advanced programming cutoffs, while Business Analyst candidates primarily need stronger communication ratings.
    """)

    st.divider()

    st.markdown("**Methodology & Technical Approach:**")
    st.markdown("""
    - **Language and Libraries:** Built entirely in Python using NumPy for array statistics, Pandas for structured data manipulation, and Streamlit for the user interface.
    - **Data Persistence:** User-added records are stored in `student_data.csv` using standard UTF-8 encoding.
    - **Explainability:** Readiness scores use clear, predetermined weights rather than complex or opaque machine learning models, making every score easily explainable.
    """)

    st.write("")
    st.warning("This application uses synthetic student data and manually defined readiness rules for educational analysis. The readiness categories are not predictions of actual placement outcomes.")
