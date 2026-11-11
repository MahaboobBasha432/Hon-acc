import pandas as pd
import matplotlib.pyplot as plt


employees=pd.read_csv(r"employees.csv")
departments=pd.read_csv(r"departments.csv")

employees=employees.drop_duplicates()

employees=employees.sort_values(by="Salary", ascending=False)

merged=pd.merge(employees, departments, on="DeptID", how="left")

print(merged)

dept_count= merged["Department"].value_counts()

# dept_count=merged.groupby("Department")
# ["EmpID"].count()
# print(merged.columns.tolist())

print("Department-wise Employees count:")
print(dept_count)


dept_count.plot(kind="pie", autopct="%1.1f%%")
plt.title("Department-wise Employees Distribution")
plt.ylabel("")
plt.savefig("department_pie_chart.png")
plt.close()

plt.figure(figsize=(9, 5))
plt.bar(merged["Name"], merged["Salary"])
plt.xlabel("Employee Salary")
plt.ylabel("Salary")
plt.title("Employee Salary")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("employee_salary_bar_chart.png")
plt.close()

merged.to_excel("merged_employees.xlsx", index=False)

print("\nEmployees sorted by salary:")
print(merged[["EmpId", "Name", "Department", "Salary"]])

print("\nAll files saved sucessfully.")
