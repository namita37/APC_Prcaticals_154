user1 = {"Amit", "Rahul", "Sneha", "Pooja", "Rohan"}
user2 = {"Rahul", "Sneha", "Kiran", "Neha", "Rohan"}

mutual = user1 & user2
unique_user1 = user1 - user2
unique_user2 = user2 - user1
total_unique = user1 | user2

print("Mutual friends:", mutual)
print("Friends unique to User 1:", unique_user1)
print("Friends unique to User 2:", unique_user2)
print("Total unique friends:", total_unique)
