#Problem 1: Write a function batman() that prints the string "I am vengeance. I am the night. I am Batman!".
def batman():
    print("I am vengeance. I am the night. I am Batman!")

#Problem 2: Write a function madlib() that accepts one parameter, a string verb. 
# The function should print the sentence: "I have one power. I never <verb>. - Batman".

def madlib(verb):
    print("I have one power. I never",verb,"- Batman")

#Problem 3: Write a function trilogy() that accepts an integer year and prints the title of the Batman trilogy movie released that year as outlined below.
'''
Year	Movie Title
2005	"Batman Begins"
2008	"The Dark Knight"
2012	"The Dark Knight Rises"
'''
#If the given year does not match one of the years in the table above, print "Christopher Nolan did not release a Batman movie in <year>."

def trilogy(year):
    if year==2005:
        print("Batman Begins")
    elif year==2008:
        print("The Dark Knight")
    elif year==2012:
        print("The Dark Knight Rises")
    else:
        print("Christopher Nolan did not release a Batman movie in",year)


#Problem 4: Implement a function get_last() that accepts a list of items items and returns the last item in the list. 
# If the list is empty, return None.

def get_last(items):
    #get list of items and return the last item
    #if no item return none
    if len(items)==0:
        return None
    else:
        #so i can get the length of the item and do a -1 since we do start from 0
        return items[len(items)-1]
    
#Problem 5: Write a function concatenate() that takes in a list of strings words and returns a string concatenated that concatenates all elements in words.
def concatenate(words):
    new_list=""
    for i in words:
        new_list+=i
    return new_list


#Problem 6: Write a function squared() that accepts a list of integers numbers as a parameter and squares each item in the list. 
# Return the squared list.

def squared(numbers):
    squared_list=[]
    for i in numbers:
        squared_list.append(i*i)
    return squared_list



#Problem 7: Write a function nanana_batman() that accepts an integer x and prints the string "nanana batman!" where "na" is repeated x times. 
# Do not use the * operator.

def nanana_batman(x):
    string=""
    for i in range(x):
        
        string+="na"
    string+=" batman!"
    print(string)


#Problem 8: Write a function find_villain() that accepts a list crowd and a value villain as parameters and returns a list of all indices where the villain is found hiding in the crowd.
def find_villain(crowd, villain):
    villain_indices=[]
    for i in range(len(crowd)):
        if crowd[i]==villain:
            villain_indices.append(i)
    return villain_indices

#Problem 9: Write a function get_odds() that takes in a list of integers nums and returns a new list containing all the odd numbers in nums.
def get_odds(nums):
    odd=[]
    for i in nums:
        if i%2!=0:
            odd.append(i)
    return odd


#Problem 10: Write a function up_and_down() that accepts a list of integers lst as a parameter. 
#The function should return the number of odd numbers minus the number of even numbers in the list.

def up_and_down(lst):
    counter_odd=0
    counter_even=0
    for i in lst:
        if i%2==0:
            counter_even+=1
        else:
            counter_odd+=1
    return counter_odd-counter_even

#Problem 11: Write a function running_sum() that accepts a list of integers superhero_stats representing the number of crimes Batman has stopped each month in Gotham City. 
# The function should modify the list to return the running sum such that superhero_stats[i] = sum(superhero_stats[0]...superhero_stats[i]). 
# You must modify the list in place; you may not create any new lists as part of your solution.

def running_sum(superhero_stats):
    #so I'll automatically add the first value to sum so we can go over the next value 

    sum=superhero_stats[0]
    print('current sum:', sum)
    #i wanna start with the second value since we already added the first value to sum 
    #apparently even though you declared the i value to be 1, when you do a for loop it will overide it and start from 0
    i=1

    #need to update for loop to include the i value so it starts from 1 and not 0
    for i in range(1,len(superhero_stats)):
        #add that value to sum 
        sum+=superhero_stats[i]
        #print('sum:', sum)
        #then update that same index with that new sum 
        superhero_stats[i]=sum
        #print('curesuperhero_stats[i]:', superhero_stats[i])
    return superhero_stats


#Problem 12: Write a function shuffle() that accepts a list cards of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn]. 
#Return the list in the form [x1,y1,x2,y2,...,xn,yn].

def shuffle(cards):
    #ok so I need to divide the list into two parts then alternate between the two parts to create a new list 
    shuffled_list=[]

    median=len(cards)//2 #// is a floor division so it'll round to the nearest whole number
  
    lst1=[]
    lst2=[]
#created two lists so I can alternate between the two lists
    for i in range(median):
        lst1.append(cards[i])
    for j in range(median,len(cards)):
        lst2.append(cards[j])
    
    #ok so now that i have two lists with the first half and the second half it's time to alternate

    for k in range(median):
        shuffled_list.append(lst1[k])
        shuffled_list.append(lst2[k])

    return shuffled_list



