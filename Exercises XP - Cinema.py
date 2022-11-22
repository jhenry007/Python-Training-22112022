#---------------------------------------------------------------------------------------------
#Exercise 9: Cinemax
# #A movie theater charges different ticket prices depending on a person’s age.
#         # if a person is under the age of 3, the ticket is free.
#         if they are between 3 and 12, the ticket is $10.
#         if they are over the age of 12, the ticket is $15.
#     Ask a family the age of each person who wants a ticket.
#     Store the total cost of all the family’s tickets and print it out.

list_cinema = []
#age_cinema = int(input("Please insert the age of each person : "))
age_cinema = ""
while age_cinema != 0:
	age_cinema = int(input("Please select a person's age. Please input 0 if no more family member'age to input"))
	if int(age_cinema) < 3:
		age_cinema = 0
		list_cinema.append(age_cinema)
	elif 3 <= age_cinema < 12:
		age_cinema = 10
		list_cinema.append(age_cinema)
	elif age_cinema >= 12:
		age_cinema = 15
		list_cinema.append(age_cinema)

print(list_cinema)
print("Total cinema cost is $", sum(list_cinema))

# A group of teenagers are coming to your movie theater and want to watch a movie that is restricted
# for people between the ages of 16 and 21.
# Given a list of names, write a program that asks teenager for their age,
# if they are not permitted to watch the movie, remove them from the list.
# At the end, print the final list.

names_not_restricted = ["James", "David", "Berty", "Kurtis"]
checking_name = input("Please input your name here : ")
for name in names_not_restricted:
	if name == checking_name:
		names_not_restricted.remove(checking_name)
		#print(checking_name)
print(names_not_restricted)

#///////////////////////2nd way :

names_not_restricted1 = ["James", "David", "Berty", "Kurtis"]
checking_age1 = int(input("Please input your age here : "))
checking_name1 = str(input("Please input your name here : "))
for name1 in names_not_restricted1:
	if name1 == checking_name1:
		if 16 <= checking_age1 < 21:
			names_not_restricted1.remove(checking_name1)
		#print(checking_name)
print(names_not_restricted1)