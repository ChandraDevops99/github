def find_sum(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + find_sum(lst[1:])

my_list = [10, 20, 30, 40, 50]
total_sum = find_sum(my_list)
print("Sum of elements (using recursion):", total_sum)
 