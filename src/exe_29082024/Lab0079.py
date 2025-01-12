# List
# List - Collection of items (duplicates allowed)
my_list = [1, 2, 3]

print(my_list)
print(len(my_list))  # len always start from 1

print(my_list[0])
print(my_list[2])

my_list[0] = "Mayank"
print(my_list)

# indexing

print("element at the index 0 is: ", my_list[0])
print("element at the index 1 is: ", my_list[1])
print("element at the index 2 is: ", my_list[2])

for element in my_list:
    print(element)

print("--------------------")

my_list.append(4)  # append - add the item at the end of the list
my_list.append(5)  # append - add the item at the end of the list
my_list.append(6)
my_list.extend([7, 8, 9, "Rajput"])  # extend - to add multiple elements to list

my_list.insert(1, "LEO")  # Insert - it will add at the specific index and shift previous one
my_list.remove("LEO")

print(my_list)
