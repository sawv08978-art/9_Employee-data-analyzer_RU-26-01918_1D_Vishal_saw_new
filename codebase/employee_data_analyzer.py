import pandas as pd
import matplotlib.pyplot as plt


def load_and_clean(filename):
    df = pd.read_csv(filename)
    before = len(df)
    df = df.drop_duplicates().reset_index(drop=True)
    duplicates = before - len(df)
    missing = int(df["Salary"].isna().sum())
    mean_salary = df["Salary"].mean()
    df["Salary"] = df["Salary"].fillna(mean_salary)
    return df, duplicates, missing, mean_salary


def summary(df, show_total=True):
    top = df.loc[df["Salary"].idxmax()]
    print(f"Employees: {len(df)} | Average salary: {df['Salary'].mean():.2f}")
    print(f"Highest paid: {top['Name']} ({top['Salary']:.0f})")
    if show_total:
        print(f"Total payroll: {df['Salary'].sum():.0f}")


print("Test Case 1: Normal Input")
df, d, m, ms = load_and_clean("test_case1.csv")
summary(df)

print("\nTest Case 2: Boundary / Minimum Input")
df, d, m, ms = load_and_clean("test_case2.csv")
summary(df, show_total=False)

print("\nTest Case 3: Invalid Input")
df, d, m, ms = load_and_clean("test_case3.csv")
print(f"Duplicates removed: {d}")
print(f"Missing Salary filled with mean: {ms:.2f}")
print(f"Cleaned rows: {len(df)}")

print("\nTest Case 4: Different Valid Scenario")
df, d, m, ms = load_and_clean("test_case1.csv")
dept = df.groupby("Department")["Salary"].agg(["count", "mean"])
dept = dept.sort_values("count", ascending=False)
for name, row in dept.iterrows():
    print(f"{name}: {int(row['count'])} employees | Avg salary: {row['mean']:.2f}")
above = df[df["Salary"] > 45000]
print("Above 45000: " + " | ".join(f"{r['Name']} ({r['Salary']:.0f})" for _, r in above.iterrows()))
print("Bar chart 'Department-wise Average Salary' displayed")
plt.bar(dept.index, dept["mean"], color="steelblue")
plt.title("Department-wise Average Salary")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.show()
