

import sys
# l = [x*x for x in range(1,10001)]
l = [x*x for x in range(1,5)]
print(type (l))
print(sys.getsizeof(l))
for i in  l:
    print(i)
# print(sys.getsizeof(l))

# gl = ( x*x for x in range(1,10001))
gl = ( x*x for x in range(1,5))
print(type(gl))
print(sys.getsizeof(gl))
for i in gl:
    # print(type(gl))
# print(sys.getsizeof(gl))
    print(i)