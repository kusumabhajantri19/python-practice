# import time
# print(time.time())
# print(time.localtime(time.time()))
# print(time.asctime(time.localtime(time.time())))
#
# import calendar
# # print(calendar.month(2025,9))
# # print(calendar.month(2004,6,))
# # print(calendar.calendar(2025))
# print(calendar.calendar(2025))
# print(calendar.calendar(2025)[1:5])
#
#
# import calendar
#
# year = 2025
#
# # Print months 1 to 6 (January to June)
# for month in range(1, 7):
#     print(calendar.month(year, month))
#
#
# import datetime
#
# # Take user input
# year = int(input("Enter year: "))
# month = int(input("Enter month: "))
# day = int(input("Enter day: "))
#
# # Create a date object
# a = datetime.date(year, month, day)
#
# # Print the day name
# print(f"The day is: {a:%A}")




my_tuple1 = [1,2,3,"nidhi","hi"]
my_tuple1[0] = "ambika"
print(my_tuple1)
print(my_tuple1[1:3])
print(my_tuple1)
my_tuple2 = [7,9,6,89,4]
total_tuple = my_tuple1 + my_tuple2
print(total_tuple)

set1 = {"mango", "orange", "apple"}
set2 = {"nango", "banana", "grapes"}
union = set1 - set2
print(union)
set1.add("dragon")
print(set1)
set1.discard("orange")
print(set1)
# items = ["bru","coffee",1,2,'c']
items = ["hi",3,5,5,6,4]
print(type(items))
print(items)
items = tuple(items)
# print(items)
print(type(items))
print(items)
temp_list = list(items)
temp_list[2] = "hello"
print(temp_list)
items = set(items)
print(type(items))
items.add("hello")
print(items)








