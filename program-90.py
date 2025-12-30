
#Maximum array using recurssion

def max_array(arr, n):
    if n == 1:          
        return arr[0]
    return max(arr[n-1], max_array(arr, n-1))

arr = [2, 9, 6, 8]
n = len(arr)
print(max_array(arr, n))