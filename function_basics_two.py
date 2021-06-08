# def countdown():
#     for num in range (5,-1,-1):
#         print(num)
# countdown()

# def printAndReturn(arr):
#     print(arr[0]) 
#     return arr[1]
# print(printAndReturn([1,2,3]))

# def firstPlusLength(arr):
#     sum = arr[0] + len(arr)
#     return sum
# print(firstPlusLength([1,2,3,4,5]))

# test_list1 = [5,2,3,2,1,4]
# test_list2 = [1,2,1,2,1,3]
# def valuesGreaterThanSecond(arr):
#     new_list = []
#     for i in arr:
#         if i > arr[1]:
#             new_list.append(i)
            # after the for loop finishes then do the if and else check!
#     if len(new_list) < 2: 
#         return False
#     else:
#         print (len(new_list))
#         return new_list
# print(valuesGreaterThanSecond(test_list1))
# print(valuesGreaterThanSecond(test_list2))
size = 6
value = 2
def thisLengthThatValue(size,value):
    new_list = []
    for i in range(size):
        new_list.append(value)
    return new_list
print(thisLengthThatValue(size,value))
