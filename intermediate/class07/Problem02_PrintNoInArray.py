def printNumberNoInArray(arr):
    if arr is None or len(arr) == 0:
        return
    for value in arr:
        modify(value, arr)
    res=[i+1 for i,v in enumerate(arr) if v!=i+1]
    return res



def modify(value, arr):
    while arr[value - 1] != value:
        tmp = arr[value - 1]
        arr[value - 1] = value
        value = tmp


arr = [1, 3, 4, 5, 7, 2, 3, 4]
result = printNumberNoInArray(arr)
print(result)
