numbers = [10,37,45,12,56,80,96,101]

print("Original list:", numbers)
num = int(input("Enter a number to search: "))
for i in numbers:
    if i == num:
        print(num, "is in the list.")
        break
    else:
        print(num, "is not in the list.")
        break

print("Original list:", numbers)
new_number = int(input("Enter a number to update: "))
pos = int(input("Enter the position of new_number: "))
numbers[pos] = new_number
print("Updated list:", numbers)


filtered = []
num = int(input("Enter a number: "))
for i in numbers:
    if i > num:
        filtered.append(i)
print("Filtered list:", filtered)


numbers = ['70','45','20','25','80','85','40']
print("Original list:", numbers)
numbers.append("30")
numbers.sort()
print("Updated list:", numbers)


