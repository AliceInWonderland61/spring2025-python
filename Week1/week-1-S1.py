#Problem 1: Write a function welcome() that prints the string "Welcome to The Hundred Acre Wood!".
def welcome():
    print("Welcome to The Hundred Acre Wood!")

    
#Problem 2: Write a function greeting() that accepts a single parameter, a string name, and prints the string 
# Welcome to The Hundred Acre Wood <name>! My name is Christopher Robin."

def greeting(name):
    print(f'Welcome to The Hundred Acre Wood {name}! My name is Christopher Robin.')

#Problem 3:Write a function print_catchphrase() that accepts a string character as a parameter and 
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
    
    

#Problem 4: Implement a function get_item() that accepts a 0-indexed list items and a non-negative integer x and returns the element at index x in items. 
# If x is not a valid index of items, return None.

def get_item(items, x):
    length = len(items)
    if(length >= x ):
        my_item = items[x]
        return my_item
    return None



#Problem 5: Winnie the Pooh wants to know how much honey he has. 
# Write a function sum_honey() that accepts a list of integers hunny_jars and returns the sum of all elements in the list. 
# Do not use the built-in function sum().

def sum_honey(hunny_jars):
	# return sum(hunny_jars)
    size = len(hunny_jars)
    sum = 0
    while(size):
        sum += hunny_jars[size-1]
        size -= 1
    return sum



#Problem 6: Help Winnie the Pooh double his honey! 
# Write a function doubled() that accepts a list of integers hunny_jars as a parameter and multiplies each element in the list by two. 
# Return the doubled list.
def doubled(hunny_jars):
	# return sum(hunny_jars)
    size = len(hunny_jars)
    sum = 0
    while(size):
        hunny_jars[size-1] *= 2
        size -= 1
    return hunny_jars


#Problem 7: Winnie the Pooh and his friends are playing a game called Poohsticks where they drop sticks in a stream and race them. 
#They time how long it takes each player's stick to float under Poohsticks Bridge to score each round.
#Write a function count_less_than() to help Pooh and his friends determine how many players should move on to the next round of Poohsticks. 
# count_less_than() should accept a list of integers race_times and an integer threshold and return the number of race times less than threshold.

def count_less_than(race_times, threshold):
    count=0

    for i in race_times:
        if i< threshold:
            count+=1
    return count



#Problem 8: Write a function print_todo_list() that accepts a list of strings named tasks. 
# The function should then number and print each task on a new line using the format:

#Pooh's To Dos:
#1. Task 1
#2. Task 2
#...

def print_todo_list(tasks):
    counter=1
    for i in tasks:
        #apparently if you do print(counter,". ", i) it will add a space after the dot, so I need to use an f string to avoid that 
        print(f"{counter}. {i}")
        counter+=1


#Problme 9: Rabbit is very particular about his belongings and wants to own an even number of each thing he owns. 
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
   



#Problem 10: Piglet's has collected a big pile of his favorite food, haycorns, and wants to split them evenly amongst his friends. 
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




#Problem 11: Signs in the Hundred Acre Wood have been losing letters as Tigger bounces around stealing any letters he needs to spell out his name. 
# Write a function tiggerfy() that accepts a string s, and returns a new string with the letters t, i, g, e, and r removed from it.

def tiggerfy(s):
    new_string=""

    for i in s:
        #if the current letter is inside tigger, then we will remove it from the string 
       #noticed it had an issue with upper case letters so I did both versions of the name 
        if i not in 'tiger' and i not in 'TIGER':
            new_string+=i
            
    return new_string


# Problem 12: Pooh, Piglet, and Roo are looking for thistles to gift their friend Eeyore. 
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

