morning = {"Pratik", "Amit", "Rahul", "Sneha"}
afternoon = {"Rahul", "Sneha", "Pooja", "Rohan"}

both = morning & afternoon
only_morning = morning - afternoon
only_afternoon = afternoon - morning
at_least_one = morning | afternoon

print("Both sessions:", both)
print("Only morning:", only_morning)
print("Only afternoon:", only_afternoon)
print("At least one session:", at_least_one)
