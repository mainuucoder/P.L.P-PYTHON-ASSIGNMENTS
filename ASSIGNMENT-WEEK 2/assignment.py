#Q1. empty list called my_list
my_list = []


#Q2. appending values to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)


#Q3. inserting a value at a specific index
my_list.insert(1, 15)        # Insert 15 at index 1 (second position)


#Q4. extending my_list with multiple values
my_list.extend([50, 60, 70])


#Q5. removing a specific value from my_list
my_list.pop()  # Removes and returns the last element (70)


#Q6. sorting my_list in ascending order
my_list.sort()  # Sorts the list in ascending order (modifies the original list)

#Q7. Finding and printing the index of the value 30 in my_list.
index_of_30 = my_list.index(30)
print(index_of_30)  # Output: 3