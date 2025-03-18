import datetime

curr_time = datetime.datetime.now()
print(curr_time)

print(curr_time.day)
print(curr_time.year)
print(curr_time.strftime("%a"))
print(curr_time.strftime("%A"))

new_date = datetime.datetime(2020, 12, 11, 5, 10, 10)

print(new_date)