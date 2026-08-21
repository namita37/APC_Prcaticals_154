cities = {"Pune": 7000000, "Mumbai": 20000000, "Delhi": 19000000, "Nashik": 2000000}

city = input("Enter city to remove: ")

if city in cities:
    del cities[city]
    print(cities)
else:
    print("City not found.")
