# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]\
# example_list = [-1,3,5,-5]
# def biggie_size(arr):
#     for i in range(0, len(example_list)):
#         if example_list[i] > 0:
#             example_list[i] = "big"
#     return example_list
# print(biggie_size(example_list))

#Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. 
# (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
example_list = [-1,5,2,3]
def count_positives(arr):
    empty_list = []
    for i in range(0, len(example_list)):
        if i > 0:
            empty_list.append(i)
    print(empty_list)
    if i > 0:
            len(example_list)-1 = len(empty_list)
    return example_list
print(count_positives(example_list))

