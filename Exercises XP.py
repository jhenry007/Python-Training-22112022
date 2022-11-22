#Exercise 1 : Set
#Create a set called my_fav_numbers with all your favorites numbers.
my_fav_numbers = {1, 2, 3, 4, 5, 6, 7, 8}
print(my_fav_numbers)
#Add two new numbers to the set.
my_fav_numbers.update([12, 15])
print(my_fav_numbers)
#Remove the last number.
my_fav_numbers.discard(15)
print(my_fav_numbers)

#Create a set called friend_fav_numbers with your friend’s favorites numbers.
friend_fav_numbers = {10, 12, 13, 14, 15, 16, 17, 18}

#Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.
my_fav_numbers.update(friend_fav_numbers)
print(my_fav_numbers)

#---------------------------------------------------------------------------------------------
#Exercise 2: Tuple
#Given a tuple which value is integers, is it possible to add more integers to the tuple?
# --> No, tuple are not mutable

#---------------------------------------------------------------------------------------------
#Exercise 3: List
#Remove “Banana” from the list.
basket = ["Banana", "Apples", "Oranges", "Blueberries"];
basket.pop(0)
print(basket)

#Remove “Blueberries” from the list.
basket = ["Banana", "Apples", "Oranges", "Blueberries"];
basket.pop(-1)
print(basket)

#Add “Kiwi” to the end of the list.
basket.append("Kiwi")
print(basket)

#Add “Apples” to the beginning of the list.
basket.insert(0,"apples")
print(basket)

#Count how many apples are in the basket.
len(basket)
print(len(basket[0]))

#Empty the basket.
basket.clear()

#Print(basket)
print(basket)

#---------------------------------------------------------------------------------------------
#Exercise 4: Floats
#Recap – What is a float? What is the difference between an integer and a float?
# A float is a number with a decimal value, an integer is a number without decimal

#Can you think of another way to generate a sequence of floats?
# By using a comprehensive list

#Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).
x = [i/2 for i in range(3, 11)]
print(x)

#Exercise 5: For Loop
#Use a for loop to print all numbers from 1 to 20, inclusive.
#Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.

numbers = range(1, 21)
for number in numbers:
  print(number)

numbers = range(1, 21)
for number in numbers:
	if number % 2 ==0:
		print(number)

#Exercise 6 : While Loop
#Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.
myname = input("Please insert you name !")
while myname != "Jeremie":
	myname = input("Please insert you name !")

print("Nice Name Jeremie !")

#Exercise 7: Favorite fruits
#Ask the user to input their favorite fruit(s) (one or several fruits).
#Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg.
# "apple mango cherry".
#Store the favorite fruit(s) in a list (convert the string of words into a list of words).
#Now that we have a list of fruits, ask the user to input a name of any fruit.
#If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
#If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.

fav_fruit = input("Hello you ! Please insert your favourite fruit(s) - seperated by a space if you would like to input several fruits : ")
list_fav_fruit = fav_fruit.split()
print(list_fav_fruit)

fav_fruit2 = input("Please select your favourite fruit")
list_fav_fruit2 = fav_fruit2.split()
if any(item in list_fav_fruit2 for item in list_fav_fruit):
    # 👇️ this runs
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print('You chose a new fruit. I hope you enjoy')

#Exercise 8: Who ordered a pizza ?
#Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’
# stop asking for toppings.
#As they enter each topping, print a message saying you’ll add that topping to their pizza.
#Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).

my_list = []
toppings = ""
fav_pizza = str(input("Please insert your pizza toppings here ! "))
list_fav_pizza = fav_pizza.split()
print(list_fav_pizza)
while toppings != "Quit":
	toppings = input("We’ll add this topping to your pizza. Another topping to add or you'll write Quit to close this window ?")
	all_toppings = my_list.append(toppings)
print("Thank you for your order ! We will get back to your shortly")
print(all_toppings)

# TO COMPLETE


