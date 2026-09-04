filename = input("Enter attendance file name: ")

with open(filename, "r") as file:
    for line in file:
        roll, name, present, total = line.strip().split(",")
        percentage = int(present) / int(total) * 100
        print(name, ":", percentage, "%")
        if percentage < 75:
            print("  Below 75%")
