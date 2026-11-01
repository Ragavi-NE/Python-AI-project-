"""Reusable functions for the Student Performance Analytics System."""

import numpy as np
import pandas as pd

SUBJECTS = ["Maths", "Physics", "Chemistry", "English", "Computer_Science"]
PASS_MARK = 40          # minimum marks needed in EVERY subject to pass
MIN_ATTENDANCE = 75     # attendance (%) below this is flagged as a shortage


def load_data(path):
    """Read the student CSV file into a Pandas DataFrame."""
    return pd.read_csv(path)


def calculate_total_and_average(df):
    """Add Total and Average columns using NumPy on the subject marks."""
    marks = df[SUBJECTS].to_numpy()
    df["Total"] = np.sum(marks, axis=1)
    df["Average"] = np.round(np.mean(marks, axis=1), 2)
    return df


def assign_grade(average):
    """Grading rule based on a student's average marks."""
    if average >= 90:
        return "O"
    elif average >= 80:
        return "A+"
    elif average >= 70:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= PASS_MARK:
        return "D"
    return "F"


def add_grades(df):
    """Loop through every student and assign a grade."""
    grades = []
    for avg in df["Average"]:
        grades.append(assign_grade(avg))
    df["Grade"] = grades
    return df


def add_pass_fail(df):
    """A student passes only if every subject is at least PASS_MARK."""
    results = []
    for _, row in df.iterrows():
        if (row[SUBJECTS] >= PASS_MARK).all():
            results.appe
