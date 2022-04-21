"""10. Minimum no. of jumps to reach an end of an array



Given an array of N integers arr[] where each element represents the max number of steps that can be made forward from that element. Find the minimum number of jumps to reach the end of the array (starting from the first element). If an element is 0, then you cannot move through that element.
Note: Return -1 if you can't reach the end of the array."""


def minJumps(arr):
    max_index = 0
    halt = 0
    jump = 0
    if(len(arr) == 1):
        return 1
    if(arr[0] == 0):
        return 1
    for i in range(len(arr)):
        max_index = max(max_index, i+arr[i])

        if(max_index >= len(arr)-1):
            jump += 1
            return jump
        if(halt == i):
            halt = max_index
            jump += 1
    if(halt >= len(arr)-1):
        return jump
    else:
        return -1


print(minJumps([1, 4, 3, 2, 6, 7]))
