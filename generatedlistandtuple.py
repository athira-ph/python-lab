initial_list = input("enter sequence of numbers:")
converted_list = initial_list.split(",")
number_list = []
for i in converted_list:
    cleaned = i.strip()
    number_list.append(cleaned)
number_tuple = tuple(number_list)
print("List:", number_list)
print("Tuple:", number_tuple)
total = len(number_list)
print("Total number of elements:", total)
print("First element:", number_list[0])
print("Last element:", number_list[-1])
print("reversed list:", number_list[::-1])


