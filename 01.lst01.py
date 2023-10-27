#(a) Print out the total number of items in the list.
"""
lst=[]
    # number of items as input
n = int(input("Enter number of items : "))
for i in range(0, n):
    ele = int(input())
    # adding the items
    lst.append(ele)  
 
print(lst)220.
output:
Enter number of items : 5
1
2
3
4
5
[1, 2, 3, 4, 5]

#(b) Print out the fourth item (index 3) in the list.
lst=[1,2,3,4,5]
print(lst.index(4))  

output:
Enter number of items : 5
1
2
3
4
5
[1, 2, 3, 4, 5]
3

#(c) Print out the last three items in the list.
lst=[1,2,3,4,5]


last_three_items = lst[-3:]

for item in last_three_items:
    print(item)
output:
1
2
3
4
5
[1, 2, 3, 4, 5]
3
3
4
5

#(d) Print out all the items in the list except the first two.
lst= [1, 2, 3, 4, 5]
items_except_first_two = lst[2:]

for item in items_except_first_two:
    print(item)

output:
3
4
5


#(e) Print out the list in reverse order.
lst=[1,2,3,4,5]

print("The original list   is : " + str(lst))
 
for i in range(0, len(lst)):
 
    if i == (len(lst)-1):
        print("The last element of list using loop : "
              + str(lst[i]))
 
lst.reverse()
print("The last element of list using reverse : "
      + str(lst[0]))
output:
Enter number of items : 5
1
2
3
4
5
[1, 2, 3, 4, 5]
3
The original list is : [1, 2, 3, 4, 5]
The last element of list using loop : 5
The last element of list using reverse : 5

#(f) Print out the largest and smallest values in the list.
lst = [1,2,3,4,5]

largest_value = max(lst )
smallest_value = min(lst )

print("Largest value:", largest_value)
print("Smallest value:", smallest_value)

output:
Largest value: 5
Smallest value: 1

#(g) Print out the sum of all the values in the list.
lst = [1,2,3,4,5]

# Use the sum() function to calculate the sum
total = sum(lst)

# Print the sum
print("Sum of all values:", total)
output:
Sum of all values: 15

#(h) If the list contains a zero, print out the index of the first zero in the list, and otherwise print outa message saying there are no zeroes.
lst = [1,2,3,4,5]

zero_index = None


for index, value in enumerate(lst):
    if value == 0:
        zero_index = index
        break  


if zero_index is not None:
    print("Index of the first zero:", zero_index)
else:
    print("There are no zeroes in the list.")

output:
There are no zeroes in the list.

#(i) Sort the list and print out the list after sorting.

# Sample list
lst = [5,4,2,3,1]

# Sort the list using the sorted() function
sorted_lst = sorted(lst)

# Print the sorted list
print("Sorted lst:", sorted_lst)
output:
Sorted lst: [1, 2, 3, 4, 5]

#(j) Delete the first item from the (now sorted) list and print out the new list.
lst = [5,4,2,3,1]

# Sort the list in ascending order
lst.sort()

# Delete the first item by slicing the list
new_lst = lst[1:]

# Print the new list
print("New list after deleting the first item:", new_lst)
output:
New list after deleting the first item: [2, 3, 4, 5]
 
#(k) Change the second-to-last item in the list to 9876 and print out the new list.
# Sample list
lst = [1,2,3,4,5]

# Change the second-to-last item to 9876
lst[-2] = 9876

# Print the new list
print("New list after changing the second-to-last item:", lst)
output:
New list after changing the second-to-last item: [1, 2, 3, 9876, 5]

#(l) Append the value -500 to the end of the list and print out the new list.
lst = [1,2,3,4,5]

# Append -500 to the end of the list
lst.append(-500)

# Print the new list
print("New list after appending -500:", lst)
output:
New list after appending -500: [1, 2, 3, 4, 5, -500]
"""
