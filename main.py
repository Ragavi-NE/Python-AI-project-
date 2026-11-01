"""Student Performance Analytics System - main program."""

import pandas as pd
import functions as fn

pd.set_option("display.width", 200)
pd.set_option("display.max_columns", 20)


def heading(text):
    print("\n" + "=" * 70)
    print(text.upper())
    print("=" * 70)


def main():
    # Step 2 - read the data
    df = fn.load_data("students.csv")
    heading("1. Dataset Overview")
    print(f"Records : {df.shape[0]}")
    print(f"Columns : {', '.join(df.columns)}")
    print(f"Missing values: {int(df.isnull().sum().sum())}\n")
    print(df.head())

    # Step 3 - process the data
    df = fn.calculate_total_and_average(df)
    df = fn.add_grades(df)
    df = fn.add_pass_fail(df)
    df = fn.add_attendance_flag(df)

    heading("2. Student Report (Total, Average, Grade, Result)")
    print(df[["Student_ID", "Name", "Department", "Total", "Average",
              "Grade", "Result", "Attendance_Status"]].to_string(index=False))

    # Step 4 - analysis
    s = fn.class_summary(df)
    heading("3. Class Summary")
    print(f"Total students      : {s['total_students']}")
    print(f"Passed / Failed     : {s['passed']} / {s['failed']}  ({s['pass_percentage']}% pass)")
    print(f"Overall class average: {s['class_average']}")
    print(f"Highest average     : {s['highest_name']} ({s['highest_avg']})")
    print(f"Lowest average      : {s['lowest_name']} ({s['lowest_avg']})")
    print(f"Average attendance  : {s['avg_attendance']}%")
    print(f"Attendance shortage : {s['attend
