#task 2
# Input list initialized to empty list
list1 = []
n = int(input("Enter number of elements : "))
# iterating till the range and taking input
for i in range(0, n):
    ele = int(input())
    # adding the element
    list1.append(ele)  

# Initialize an empty list to store positive numbers
list2 = []

# Iterate through list1 and add positive numbers to list2
for num in list1:
    if num > 0:
        list2.append(num)

# Print the positive numbers in list2
print("List2:", list2)
