employees = [
    ["Niharika", "IT", 50000],
    ["Purva", "HR", 40000],
    ["Sanchita", "IT", 60000],
    ["Sanskruti", "Sales", 45000],
    ["Shreya", "HR", 50000]
]

highest = max(employees, key=lambda x: x[2])
average = sum(x[2] for x in employees) / len(employees)

print("Highest Salary:", highest[0], highest[2])
print("Average Salary:", average)

departments = {}

for name, dept, salary in employees:
    if dept not in departments:
        departments[dept] = []
    departments[dept].append(salary)

print("Department Wise Salary:")

for dept in departments:
    print(dept, sum(department))