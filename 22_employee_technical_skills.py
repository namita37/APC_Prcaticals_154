employee1 = {"Python", "Java", "SQL", "HTML"}
employee2 = {"Python", "SQL", "CSS", "JavaScript"}

common = employee1 & employee2
unique_employee1 = employee1 - employee2
unique_employee2 = employee2 - employee1
all_skills = employee1 | employee2

print("Common skills:", common)
print("Skills unique to Employee 1:", unique_employee1)
print("Skills unique to Employee 2:", unique_employee2)
print("All available skills:", all_skills)
