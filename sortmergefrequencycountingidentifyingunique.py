set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print("common elements:", set1.intersection(set2))
print("unique elements in set1:", set1.symmetric_difference(set2))


dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 2, 'c': 4, 'd': 5}
merged = dict1|dict2
print("dict 1:", dict1)
print("dict 2:", dict2)
print("merged dict:", merged)


leaders = {'computer science':'athira','mech':'lakshmi','electric':'rosh','civil':'shali','MBA':'athulya','MCA':'mithra'}
count_of_items = len(leaders)
print("count of leaders in CCE:", count_of_items)

fruits = {'apple':3,'orange':5,'grape':5,'watermelon':8}
print("original:",fruits)
sorted_dict = dict(sorted(fruits.items()))
print("sorted:",sorted_dict)


