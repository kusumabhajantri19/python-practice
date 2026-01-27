
#sum of array using recurssion

def sum_array(arr, n):
    if n == 0:          
        return 0
    return arr[n-1] + sum_array(arr, n-1)


arr = [2, 4, 6, 8]
n = len(arr)
print(sum_array(arr, n))