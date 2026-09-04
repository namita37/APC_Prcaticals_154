def binary_search_recursive(arr, target, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    if target < arr[mid]:
        return binary_search_recursive(arr, target, low, mid - 1)
    return binary_search_recursive(arr, target, mid + 1, high)


print(binary_search_recursive([10, 20, 30, 40, 50], 40))
