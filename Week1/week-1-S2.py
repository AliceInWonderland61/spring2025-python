#here we will type 


#problem 1:
#Write a function reverse_sentence() that takes in a string sentence and returns the sentence with the order of the words reversed. 
# The sentence will contain only alphabetic characters and spaces to separate the words. 
# If there is only one word in the sentence, the function should return the original string.

def reverse_sentence(sentence):
    #Base Case: If there is only one word, return the original string
    if not ' ' in sentence:
        return sentence 

    #split the sentence first 
    split=sentence.split()

    #reverse the list of the words
    #return split.reverse()
    reverse_words = split[::-1]
    #after you split you need to join them again 
    return ' '.join(reverse_words)

#Problem 2: In the extended universe of fictional bears, Goldilocks finds an enticing list of numbers in the Three Bears' house. 
# She doesn't want to take a number that's too high or too low - she wants a number that's juuust right. 
# Write a function goldilocks_approved() that takes in the list of distinct positive integers nums and 
# returns any number from the list that is neither the minimum nor the maximum value in the array, or -1 if there is no such number.

#Return the selected integer.

def goldilocks_approved(nums):

    #must be positive integers
    #need to sort the nums and return the middle number 
    if len(nums) < 3:
        return -1
    #sort the list 
    #nums.sort()

    #need to return the middle number 
    #middle=len(nums)//2

    #return nums[middle] 
    minimum = min(nums)
    maximum = max(nums)
    for num in nums:
        if num != minimum and num != maximum:
            return num


#problem 3: Pooh is eating all of his hunny jars in order of smallest to largest. 
# Given a list of integers hunny_jar_sizes, write a function delete_minimum_elements() that continuously removes the minimum element until the list is empty. 
# Return a new list of the elements of hunny_jar_sizes in the order in which they were removed.

def delete_minimum_elements(hunny_jar_sizes):
    new_list=[] #this is where the removed elements are going to be stored
    #loop through the hunny jar list 
    while len(hunny_jar_sizes)>0:
      
    #get the minimum element and save it to minimum
        minimum=min(hunny_jar_sizes)
        #we append that current minimum to the new list 
        new_list.append(minimum)
        #Then remove the current minimum from the original list so we can find the next smallest 
        hunny_jar_sizes.remove(minimum)
    return new_list


#Problem 4: Write a function sum_of_digits() that accepts an integer num and returns the sum of num's digits.

def sum_of_digits(num):
    #should we do a for loop that goes through each digit and adds it to a sum varaible ?
    sum=0
    #so I need to convert the number to a string so i can loop through each digit 
    for i in str(num):
        #convert i back into an integer and add it to the sum variable
        sum+=int(i)
    return sum


#Problem 5: Tigger has developed a new programming language Tiger with only four operations and one variable tigger.
'''
bouncy and flouncy both increment the value of the variable tigger by 1.
trouncy and pouncy both decrement the value of the variable tigger by 1.
Initially, the value of tigger is 1 because he's the only tigger around! Given a list of strings operations containing a list of operations, return the final value of tigger after performing all the operations.


'''

def final_value_after_operations(operations):
    tigger=1
    for i in operations:
        if i=="bouncy" or i=="flouncy":
            tigger+=1
        
        elif i=="trouncy" or i=="pouncy":
            tigger-=1
    return tigger

#Problem 6: Given an array of strings words and a string s, implement a function is_acronym() that 
# returns True if s is an acronym of words and returns False otherwise.
'''
The string s is considered an acronym of words if it can be formed by concatenating the first character of each string in words in order. 
For example, "pb" can be formed from ["pooh"", "bear"], but it can't be formed from ["bear", "pooh"].
'''
def is_acronym(words, s):
  #ok so I misunderstood, essentially the acronym is the frist letter of each word in the 'words' list 
    acronym=""
    for i in words:
      #to get the first character of each word in 'words'
      #i will change to the next available word in the list 
      acronym+=i[0]
    #if the acronym is the same as s then then we return true 
    if acronym==s:
      return True
    else:
      return False



#Problem 7: Write a function make_divisible_by_3() that accepts an integer array nums. 
# In one operation, you can add or subtract 1 from any element of nums. 
# Return the minimum number of operations to make all elements of nums divisible by 3.

def make_divisible_by_3(nums):
    #so i need to evaluate the number and see if it's divisible by 3
    if len(nums)==0:
        return 0
    operations=0
    for i in nums:
        if i%3==0:
            continue
        elif i%3==1:
            #i need to add 2 to the value 
            i+=2
            operations+=1
        elif i%3==2:
            #I need to add 1 to the value 
            i+=1
            operations+=1
    return operations

#Problem 8: Given two lists lst1 and lst2, write a function exclusive_elemts() 
#that returns a new list that contains the elements which are in lst1 but not in lst2 and the elements that are in lst2 but not in lst1.

def exclusive_elemts(lst1, lst2):
    #if it's in list1 but not in list2, then we add it to a new list
    new_lst=[]


    for i in lst1:
        if i not in lst2:
            new_lst.append(i)
    
    for j in lst2:
        if j not in lst1:
            new_lst.append(j)
    
    return new_lst

#Problem 9: Write a function merge_alternately() that accepts two strings word1 and word2. 
# Merge the strings by adding letters in alternating order, starting with word1. 
# If a string is longer than the other, append the additional letters onto the end of the merged string.
#Return the merged string.

def merge_alternately(word1, word2):
    #so i could probably split each letter in the word1 and word2 and then start alternatingly adding them to a new string 
    #so this takes each character in the word and puts it into the list 
    split1=list(word1)
    split2=list(word2)
    new_list=[]

    i=0
    #so we need to loop through the two lists and add the characters to the new list
    while i<len(split1) and i<len(split2):
        new_list.append(split1[i])
        new_list.append(split2[i])
        i+=1
    
    #so if one of the lists is longer than the other we need to append the remaining character 
    if len(split1)>len(split2):
        new_list+=split1[i:]
    else:
        new_list+=split2[i:]
    return "".join(new_list) #join all the characters together in a string

#Problem 10: Eeyore has collected two piles of sticks to rebuild his house and needs to choose pairs of sticks whose lengths are the right proportion. 
# Write a function good_pairs() that accepts two integer arrays pile1 and pile2 where each integer represents the length of a stick. 
# The function also accepts a positive integer k. 
# The function should return the number of good pairs.
#A pair (i, j) is called good if pile1[i] is divisible by pile2[j] * k. Assume 0 <= i <= len(pile1) - 1 and 0 <= j <= len(pile2) - 1

#so apparently we need to loop through the second list, get each value mulitply it by k and then 
#use it as the mod value for the the values in the first list 

def good_pairs(pile1, pile2, k):
    pairs=0 #current pairs is 0
    for i in pile1:
        #so we get the first element in pile1
        for j in pile2:
            #get the first elementin pile2 and multiply it by k
            #if that value is divisible by the current i then we have a good pair
            if i%(j*k)==0:
                #update the pair 
                pairs+=1

    return pairs


pile1 = [1, 3, 4]
pile2 = [1, 3, 4]
k = 1
print(good_pairs(pile1, pile2, k))

pile1 = [1, 2, 4, 12]
pile2 = [2, 4]
k = 3
print(good_pairs(pile1, pile2, k))