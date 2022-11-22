#Code to update all occurences
list1 = [5, 10, 15, 20, 25, 50, 20]
checking_20 = 20
# or we can use list1.index(20)
if checking_20 in list1:
    print(f'{checking_20} is present in the list')

    for i in range(len(list1)):
        if list1[i] == 20:
            list1[i] == 200
else:
    print(f'{checking_20} is not present in the list')

print(list1)

#Code to update only 1 occurence
list1 = [5, 10, 15, 20, 25, 50, 20]
if not 20 in list1:
   print("20 is not at the list, can't replace")
else:
   index = list1.index(20)
   list1[index] = 200
print(list1)

my_tuple = (10, 20, 30, 40)
a, b, c, d = my_tuple
print(a, b, c, d)
