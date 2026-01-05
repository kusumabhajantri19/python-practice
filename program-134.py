

#Compare two strings lexicographically (like dictionary order).

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if s1 == s2:
    print("Both strings are equal")
elif s1 < s2:
    print("First string comes first (s1 < s2)")
else:
    print("Second string comes first (s1 > s2)")