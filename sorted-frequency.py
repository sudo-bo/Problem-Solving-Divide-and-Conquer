# Given a sorted array and a number, 
# write a function called sortedFrequency 
# that counts the occurrences of the number in the array

def findOccurrence(arr, target, findFirstOrLast):
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        elif arr[mid] == target:
            result = mid
            if findFirstOrLast == "First":
                # Continue searching towards the left (lower indices)
                right = mid - 1
            elif findFirstOrLast == "Last":
                # Continue searching towards the right (higher indices)
                left = mid + 1
    return result

def sortedFrequency(arr, target):
    first = findOccurrence(arr, target, "First")
    if first == -1:
        return 0  # Target not found
    last = findOccurrence(arr, target, "Last")
    return last - first + 1

