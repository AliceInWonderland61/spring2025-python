#just a comment

#Write a function welcome() that prints the string "Welcome to The Hundred Acre Wood!".
def welcome():
    print("Welcome to The Hundred Acre Wood!")

    
#Write a function greeting() that accepts a single parameter, a string name, and prints the string 
# Welcome to The Hundred Acre Wood <name>! My name is Christopher Robin."

def greeting(name):
    print(f'Welcome to The Hundred Acre Wood {name}! My name is Christopher Robin.')

#Write a function print_catchphrase() that accepts a string character as a parameter and 
# #prints the catchphrase of the given character as outlined in the table below.
def print_catchphrase(character):
    lowerCharacter = character.lower()
    
    if lowerCharacter =='pooh':
        print("Oh, bother!")
    elif lowerCharacter =='tigger':
        print("TTFN: Ta-ta for now!")
    elif lowerCharacter =='eeyore':
        print("Thanks for noticing me.")
    elif lowerCharacter =='christopher robin':
        print('Silly old bear.')
    else:
        print(f"Sorry! I don't know {character}'s catchphrase!")
    
    



#Implement a function get_item() that accepts a 0-indexed list items and a non-negative integer x and returns the element at index x in items. 
# If x is not a valid index of items, return None.




def get_item(items, x):
    length = len(items)
    if(length >= x ):
        my_item = items[x]
        return my_item
    return None



#question 5
#Winnie the Pooh wants to know how much honey he has. 
# Write a function sum_honey() that accepts a list of integers hunny_jars and returns the sum of all elements in the list. Do not use the built-in function sum().

def sum_honey(hunny_jars):
	# return sum(hunny_jars)
    size = len(hunny_jars)
    sum = 0
    while(size):
        sum += hunny_jars[size-1]
        size -= 1
    return sum


#question 6
#Help Winnie the Pooh double his honey! Write a function doubled() that accepts a list of integers hunny_jars as a parameter and multiplies each element in the list by two. Return the doubled list.
def doubled(hunny_jars):
	# return sum(hunny_jars)
    size = len(hunny_jars)
    sum = 0
    while(size):
        hunny_jars[size-1] *= 2
        size -= 1
    return hunny_jars



#question 7
#Winnie the Pooh and his friends are playing a game called Poohsticks where they drop sticks in a stream and race them. They time how long it takes each player's stick to float under Poohsticks Bridge to score each round.
#Write a function count_less_than() to help Pooh and his friends determine how many players should move on to the next round of Poohsticks. count_less_than() should accept a list of integers race_times and an integer threshold and return the number of race times less than threshold.


	

#Write a function print_todo_list() that accepts a list of strings named tasks. The function should then number and print each task on a new line using the format:

#Pooh's To Dos:
#1. Task 1
#2. Task 2
#...

#question 9
#Rabbit is very particular about his belongings and wants to own an even number of each thing he owns. 
# Write a function can_pair() that accepts a list of integers item_quantities. 
# Return True if each number in item_quantities is even. Return False otherwise.
def can_pair(item_quantities):
    divsor = 0
    while(divsor < len(item_quantities)):
        if(item_quantities[divsor]%2 == 0):
            divsor += 1
            continue
        else:
            return False
    return True  
   
    
item_quantities = [2, 4, 6, 8]
print(can_pair(item_quantities))

item_quantities = [1, 2, 3, 4]
print(can_pair(item_quantities))

item_quantities = []
print(can_pair(item_quantities))

#problem 10
#Piglet's has collected a big pile of his favorite food, haycorns, and wants to split them evenly amongst his friends. 
# Write a function split_haycorns() to help Piglet determine the number of ways he can split his haycorns into even groups. 
# split_haycorns() accepts a positive integer quantity as a parameter and returns a list of all divisors of quantity.
def split_haycorns(quantity):
    my_list = []
    divsor = 1
    while(divsor <= quantity):
        if(quantity%divsor == 0):
            my_list.append(divsor)
        divsor += 1
    return my_list  




#problem 11


# 12. 
#Pooh, Piglet, and Roo are looking for thistles to gift their friend Eeyore. 
# Write a function locate_thistles() that takes in a list of strings items and returns a list of the indices of any elements with value "thistle". 
# The indices in the resulting list should be ordered from least to greatest.


def locate_thistles(items):
    index = 0
    my_list = []
    substring = 'thistle'
    while(index < len(items)):
        if substring in items[index]:
            my_list.append(index)
        index += 1
    return my_list

