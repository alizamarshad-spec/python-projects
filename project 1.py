import pandas as pd
import csv
data = [
    ["Student_Name", "Math_Score", "Science_Score"],
    ["Ali", 78, 85],
    ["Sara", "", 40],
    ["Ahmed", 60, ""],
    ["Hina", 30, 45],
    ["Usman", 90, 88]
]

with open("raw_grades.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("raw_grades.csv created")

class Student:
    def __init__(self, name, math, science):
        self.name = name
        self.math = math
        self.science = science
        self.status = ""

    def check_status(self):
        avg = (self.math + self.science) / 2
        if avg >= 50:
            self.status = "Pass"
        else:
            self.status = "Fail"
        return avg

df = pd.read_csv("raw_grades.csv")
df = df.fillna(0)

results = []

for i, row in df.iterrows():
    s = Student(row["Student_Name"], row["Math_Score"], row["Science_Score"])
    avg = s.check_status()

    results.append([s.name, s.math, s.science, avg, s.status])

final_df = pd.DataFrame(results, columns=["Name", "Math", "Science", "Average", "Status"])
final_df["School_Year"] = "2023-2024"

final_df.to_csv("final_grades.csv", index=False)

print(final_df)