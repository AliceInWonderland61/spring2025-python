#Problem 1: You're planning an epic trip and have a dictionary of destinations mapped to their respective rating scores. 
# Your goal is to visit only the best-rated destinations. Write a function that takes in a dictionary destinations and a rating_threshold as parameters. 
# The function should iterate through the dictionary and remove all destinations that have a rating strictly below the rating_threshold. Return the updated dictionary.

def remove_low_rated_destinations(destinations, rating_threshold):
    # Collect keys first so we can safely remove from the dictionary.
    #i thought we'd remove as we go but that would cause issues when traversing the dictionary 
    keys_to_remove = []
    for destination, rating in destinations.items():
        #add it to a list if it's less than the threshold so we know what items to remove later on 
        if rating < rating_threshold:
            keys_to_remove.append(destination)
    #now that we have the list of keys we need to remove, we loop through those, find them in the dictionary and removr them 
    for destination in keys_to_remove:
        destinations.pop(destination)

    return destinations

#Problem 2: As a seasoned traveler, you've collected a variety of souvenirs from different destinations. 
# You have an array of string souvenirs, where each string represents a type of souvenir. 
# You want to know if the number of occurrences of each type of souvenir in your collection is unique.
#Write a function that takes in an array souvenirs and returns True if the number of occurrences of each value in the array is unique, or False otherwise.

def unique_souvenir_counts(souvenirs):

    #so my idea is to create a dictionary for those items and if we come cross a souvenur again, then we automatically return false 
    #after the loop ends, we return true 
    #i keep reading things wrong, so we want to make sure that the value per key is not the same for other keys 

    souvenir_counts={}
    for i in souvenirs:
        if i in souvenir_counts:
            souvenir_counts[i] += 1
        else:
            souvenir_counts[i] = 1

    #so i'm trying to see how to do this, i might have to do another for loop 
    #for each key, search through the other values of the dictionary to see if we have a siilar value

    for i in souvenir_counts:
        for j in souvenir_counts:
            #we want to make sure that the values are not the same 
            # we don't want to compare the same key to itself so we add a condition that if i and j are the same key we skip
            #if i and j are different keys BUT the values are the same, then that means we have to return False because the 
            #occurences are the same for two different keys
            if i!=j and souvenir_counts[i] == souvenir_counts[j]:
                return False
    return True
        

# Problem 3: You make friends with a local at your latest destination, and they give you a coded message with the name of a secret beach most tourists don't know about! 
# You are given the strings key and message which represent a cipher key and a secret message, respectively. 
# The steps to decode the message are as follows:
'''
Use the first appearance of all 26 lowercase English letters in key as the order of the substitution table.
Align the substitution table with the regular English alphabet.
Each letter in message is then substituted using the table.
Spaces ' ' are transformed to themselves.

'''
#For example, given key = "travel the world" (an actual key would have at least one instance of each letter in the alphabet), 
# we have the partial substitution table of ('t' -> 'a', 'r' -> 'b', 'a' -> 'c', 'v' -> 'd', 'e' -> 'e', 'l' -> 'f', 'h' -> 'g', 'w' -> 'h', 'o' -> 'i', 'd' -> 'j')
#Write a function decode_message() that accepts the strings key and message and returns a string representing the decoded message.

def decode_message(key, message):
    #ok so key is the alphabet order 
    #so I need to create a dictionary that goes through an alphabet variable and the value is the key variables (I think)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    dictionary={}

    for i in key:
        #if that letter is not saved in the dictionary and it's not a space, then we add it to the dictionary 
        if i not in dictionary and i != ' ':
            #the value of that key (letter) is the next letter of the alphabet 
            dictionary[i] = alphabet[len(dictionary)]
    
    #now that we have it all mapped out we start decoding the message
    decoded_message = ""

    for i in message:
        #add the spaces cause it's part of the message
        if i == ' ':
            decoded_message += ' '
        else:
            #we want to add the value of the key (letter) to the decoded message 
            decoded_message += dictionary[i]

    return decoded_message


#Problem 4: In a list of travel packages, we define a harmonious travel sequence as a sequence where the difference between the maximum and minimum ratings is exactly 1.
#Given an integer array ratings, return the length of the longest harmonious travel sequence among all its possible subsequences.
#A subsequence of an array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.
#You are provided with a partially implemented solution that contains bugs. Your task is to identify and fix the bugs to ensure the solution works correctly.

def find_longest_harmonious_travel_sequence(ratings):
     # Initialize a dictionary to store the frequency of each rating
    frequency = {}

    # Count the occurrences of each rating
    for rating in ratings:
        frequency[rating] = frequency.get(rating, 0) + 1

    max_length = 0

    # Find the longest harmonious sequence
    for rating in frequency:
        if rating + 1 in frequency:
            max_length = max(max_length, 
                        frequency[rating] + frequency[rating + 1])  

    return max_length


# Problem 5: You are given a 2D integer array trips and two integers start_dest and end_dest. 
# Each trips[i] = [starti, endi] represents an inclusive travel interval between starti and endi.
# Return True if each destination in the inclusive route [start_dest, end_dest] is covered by at least one trip in trips. 
# Return False otherwise.
# A destination x is covered by a trip trips[i] = [starti, endi] if starti <= x <= endi.

def is_route_covered(trips, start_dest, end_dest):
    #so as long as the first [][] has the first number of the start destination and the last [][] has the second number of the end destination 
    #then we can return true, otherwise we return false

    start=False
    end=False
    if trips[0][0]==start_dest or trips[0][1]==start_dest:
        start=True
    else:
        start=False
    
    if trips[len(trips)-1][0]==end_dest or trips[len(trips)-1][1]==end_dest:
        end=True
    else:
        end=False   
    
    if start==True and end==True:
        return True
    else:
        return False

#Problem 6: Given a list of integers destinations, where each integer represents the popularity score of a destination, return the most popular even destination.
#If there is a tie, return the smallest one. If there is no such destination, return -1.

def most_popular_even_destination(destinations):
    if len(destinations)==0:
        return -1
    
    #ohhh ok so we find the number that is repeated the most AND it's an even number 
    #I think I might have to do like a dictionary 
    dictionary={}
    even_dictionary={}

    for i in destinations:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1
    
    for i in destinations:
        if i%2==0:
            even_dictionary[i] = dictionary[i]
    
    #now we have a dictionary of the even numbers and their counts, we want to find the most popular one
    most_popular=-1

    for i in even_dictionary:
        if even_dictionary[i] > most_popular:
            most_popular = i
        elif even_dictionary[i] == most_popular and i < most_popular:
            most_popular = i
    return most_popular

#Problem 7: You are given an itinerary 'itinerary' representing a list of trips between cities, where each city is represented by an integer. 
# We consider an itinerary valid if it is a permutation of an itinerary template base[n].
#The template base[n] is defined as [1, 2, ..., n - 1, n, n] (in other words, it is an itinerary of length n + 1 that visits cities 1 to n - 1 exactly once, 
# plus visits city n twice). For example, base[1] = [1, 1] and base[3] = [1, 2, 3, 3].
#Return True if the given itinerary is valid, otherwise return False.
#A permutation is an arrangement of a set of elements. For example [3, 2, 1] and [2, 3, 1] are both possible permutations of the set of numbers 1, 2, and 3.

def is_valid_itinerary(itinerary):
    # so if i understand correctly, the biggest number in the itineratry needs to appear twice 
    #created a dictionary to count how many times each city appears in the itinerary 
    dictionary={}
    for i in itinerary:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1   
    
    #created a counter to make sure that no cities appear more than twice
    #if the largest city appears more than twice, then we return false
    count=0
    for i in dictionary:
        # i should probably count how many cities have a count of 2 
        if dictionary[i]==2:
            count+=1

    # Check if the largest city appears exactly twice
    max_city = max(dictionary.keys())
    if dictionary[max_city] != 2:
        return False
    
    if count==1:
        return True
    else:
        return False 


#Problem 8: Given two lists of tourist attractions, tourist_list1 and tourist_list2, find the common attractions with the least total travel time.
#A common attraction is one that appears in both tourist_list1 and tourist_list2.
#A common attraction with the least total travel time is a common attraction such that 
# if it appeared at tourist_list1[i] and tourist_list2[j] then i + j should be the minimum value among all the other common attractions.
#Return all the common attractions with the least total travel time. Return the answer in any order.

def find_attractions(tourist_list1, tourist_list2):
    index_map = {}

    for i, attraction in enumerate(tourist_list1):
        index_map[attraction] = i

    min_time = float('inf')
    result = []

    for j, attraction in enumerate(tourist_list2):
        if attraction in index_map:
            total_time = index_map[attraction] + j

            if total_time < min_time:
                min_time = total_time
                result = [attraction]
            elif total_time == min_time:
                result.append(attraction)

    return result    



