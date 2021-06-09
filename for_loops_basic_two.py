# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]\
# example_list = [-1,3,5,-5]
def biggie_size(arr):
    for i in range(0, len(example_list)):
        if example_list[i] > 0:
            example_list[i] = "big"
    return example_list
print(biggie_size(example_list))

#Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. 
# (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
def count_positives(example_list):
    positive_value = 0
    for i in example_list:
        if i > 0:
            positive_value += 1
    example_list.pop()
    example_list.append(positive_value)
    return example_list
print(count_positives([-1,1,1,1]))

# Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
# Example: sum_total([1,2,3,4]) should return 10
def sum_total(example_list):
    sum = 0
    for list_item in example_list:
        sum += list_item
    return sum
print(sum_total([1,2,3,4]))

#Create a function that takes a list and returns the average of all the values.
#Example: average([1,2,3,4]) should return 2.5
# equation average equals sum divided by length of list.
def average(example_list):
    sum = 0
    for list_item in example_list:
        sum += list_item
    average = sum / len(example_list)
    return average
print(average([1,2,3,4]))

#Length - Create a function that takes a list and returns the length of the list.
#Example: length([37,2,1,-9]) should return 4
def length(example_list):
    for list_item in example_list:
        length = len(example_list)
    return length
print(length([37,2,1,-9]))

#Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
#Example: minimum([37,2,1,-9]) should return -9
def minimum(example_list):
    if len(example_list) == 0:
        return False
    return min(example_list)
print(minimum([37,2,1,-9]))

#Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
#Example: maximum([37,2,1,-9]) should return 37
def maximum(example_list):
    if len(example_list) == 0:
        return False
    return max(example_list)
print(maximum([37,2,1,-9]))

#Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
#Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
def ultimate_analysis(example_list):
    sumTotal = 0
    average = 0
    minimum = 0
    maximum = 0
    length = 0
    for list_item in example_list:
        sumTotal += list_item
    average = sumTotal / len(example_list)
    minimum = min(example_list)
    maximum = max(example_list)
    length = len(example_list)
    total = {'sumTotal': sumTotal, 'average': average, 'minimum': minimum, 'maximum': maximum, 'length': length}
    return total
print(ultimate_analysis([37,2,1,-9]))

#Reverse List - Create a function that takes a list and return that list with values reversed. 
#Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]
def reverse_list(example_list):
    example_list.reverse()
    return example_list
print(reverse_list([37,2,1,-9]))
