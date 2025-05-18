#Sort the elements in list without using built in function(like sort())
def bubble_sort(listex):
    n = len(listex)
    for i in range(n):
        # Flag to optimize by stopping early if no swaps occur
        swapped = False
        for j in range(n - i - 1):
            if listex[j] > listex[j + 1]:
                # Swap elements
               listex[j], listex[j + 1] = listex[j + 1], listex[j]
            swapped = True
        # If no swaps occurred in this pass, the array is already sorted
        if not swapped:
            break
    return listex

# Example usage
listex = [1,2,5,10,15,78,9,7,3] 
sorted_array = bubble_sort(listex)
print("Sorted array:", sorted_array)
