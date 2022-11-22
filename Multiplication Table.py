inputbox = str(input("Please select a number, we will provide you with its multiplcation table : "))
# or we can use list1.index(20)
for i in range(11):
   for j in range(11):
      print(i * j, end='\t')
   print()

one_to_ten = 0
while one_to_ten != 10:
	one_to_ten = (one_to_ten)+1
	print(one_to_ten)

list1 = [5, 10, 15, 20, 25, 50, 20]
list1.reverse()
print(list1)

if not 20 in list1:
   print("20 is not at the list, can't replace")
else:
   index = list1.index(20)
   list1[index] = 200
   list1.reverse()
print(list1)

