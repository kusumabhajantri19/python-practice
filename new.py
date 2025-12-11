# Messege =" how are you>> "
# print(Messege.upper())
# print(Messege.lower())
# print(Messege.replace(" ","_"))
# print(Messege.strip())
#
# Messege = "Hello woerld!"
# print(len(Messege))

# number1=int(input("Enter number: "))
# number2=int(input("Enter number: "))
# if number1>10 and number2>10:
#  print("both numbers are large")

# number1 = int(input("Enter number: "))
# number2 = int(input("Enter number: "))
# if number1 > 10 or number2 < 5:
#     print(" number1 is large")
# else:
#     print("number2 is lesser")

# age =int(input("Enter age:"))
# if age >= 18 and age < 50:
#  print("You are adult")
# else:
#  print("You are older")

# my_list = ['a','b','c','d','e']
# my_string = "python"
#
# print('c' in my_list)
# print("python" not in my_string)
#
# a=10
# b=20
# print(a&b)

list = [1,6,8,4,2,9]
mid = len(list)//2
left = list[:mid]
right = list[mid:]
left = sorted(left)
right = sorted(right)
i=j=0
sorted_list = []
while i < len(left) and j < len(right):
  if left[i] < right[j]:
      sorted_list.append(left[i])
      i +=1
  else:
      sorted_list.append(right[j])
      j +=1
sorted_list.extend(left[i:])
sorted_list.extend(right[j:])
print("Previous list:",list)
print("Sorted list:", sorted_list)






