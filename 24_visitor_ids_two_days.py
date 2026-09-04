day1 = {101, 102, 103, 104, 105}
day2 = {103, 104, 105, 106, 107}

unique_visitors = day1 | day2
returning_visitors = day1 & day2
only_first_day = day1 - day2
only_second_day = day2 - day1

print("Unique visitors:", unique_visitors)
print("Returning visitors:", returning_visitors)
print("Visitors only on first day:", only_first_day)
print("Visitors only on second day:", only_second_day)
