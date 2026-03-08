#Problem1
#Given two lists of strings artists and set_times of length n, write a function lineup() that maps each artist to their set time.
#An artist artists[i] has set time set_times[i]. Assume i <= 0 < n and len(artists) == len(set_times).

def lineup(artists, set_times):
    dic={} #have a dictionary to store the artists and ther times

    for i in range(len(artists)):
        #as its's traversing the artist list, it will add the artis and then add the set time of the set_time list 
        dic[artists[i]]=set_times[i] 
    return dic



#Problem 2
#You are designing an app for your festival to help attendees have the best experience possible! 
# As part of the application, users will be able to easily search their favorite artist and find out the day, time, and stage the artist is playing at. 
# Write a function get_artist_info() that accepts a string artist and a dictionary festival_schedule mapping artist's names to dictionaries containing 
# the day, time, and stage they are playing on. Return the dictionary containing the information about the given artist.

#If the artist searched for does not exist in festival_schedule, return the dictionary {"message": "Artist not found"}.

def get_artist_info(artist, festival_schedule):
    #loop through artist and find it then return the schedule 

    for i in festival_schedule:
        if i==artist:
            return festival_schedule[i]
        else:
            return {"message": "Artist not found"}

            

#Problem 3
#A dictionary ticket_sales is used to map ticket type to number of tickets sold. 
#Return the total number of tickets of all types sold.

def total_sales(ticket_sales):
    sum=0
    for i in ticket_sales.values():
        sum+=i
    return sum 

#Problem 4
#Demand for your festival has exceeded expectations, so you're expanding the festival to span two different venues. 
# Some artists will perform both venues, while others will perform at just one. To ensure that there are no scheduling conflicts, 
# implement a function identify_conflicts() that accepts two dictionaries venue1_schedule and venue2_schedule each mapping the artists playing at the venue to their set times. 
# Return a dictionary containing the key-value pairs that are the same in each schedule.

def identify_conflicts(venue1_schedule, venue2_schedule):
    conflict={}

    for key, value in venue1_schedule.items():
        #if the current key is found in venue2 we check that their value is the same as in venue1,
        #if it is, add it to our conflict dictionary 
        if key in venue2_schedule and venue2_schedule[key]==value:
            conflict[key]=value
    return conflict 



#Problem 5
# As part of the festival, attendees cast votes for their favorite set. 
# Given a dictionary votes that maps attendees id numbers to the artist they voted for, 
# return the artist that had the highest number of votes. 
# If there is a tie, return any artist with the top number of votes.

def best_set(votes):
    dict={}

    for i in votes.values():
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    #find the max value in dict and getting the key from that dictionary 
    return max(dict, key=dict.get)
        

#Problem 6: You are given an array audiences consisting of positive integers representing the audience size for different performances at a music festival.
#Return the combined size of every audience that had the maxmium size.
#The audience size of a performance is the number of people who attended that performance.

def max_audience_performances(audiences):
    #get the max number first 
    aud=max(audiences)

    sum=0
    #check to see how many times that max number appears in the last 
    for i in audiences:
        #if we find the max number again then add it to the sum 
        if i==aud:
            sum+=i
    return sum

#Problem 7: If you used a dictionary as part of your solution to max_audience_performances() in the previous problem,
# try reimplementing the function without using a dictionary. If you implemented max_audience_performances() without using a dictionary, 
# try solving the problem with a dictionary.

#Once you've come up with your second solution, compare the two. Is one solution better than the other? Why or why not?

def max_audience_performances_dict(audiences):
    dict={}
    
    #add audiences into a dictionary 
    for i in audiences:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    #find the largest audience size, then multiply by how many times it appeared
    max_key = max(dict)
    #print("this is the current max key:", max_key) 
    return max_key * dict[max_key]
    
#Problem 8: Given an array of integers popularity_scores representing the popularity scores of songs in a music festival playlist, 
# return the number of popular song pairs.
# A pair (i, j) is called popular if the songs have the same popularity score and i < j.
# Hint: number of pairs = (n x n-1)/2

def num_popular_pairs(popularity_scores):
    #ok so what we need to do is create a dictionary to count how many times each popularity score appears 
    #then we use the formula (n x n-1)/2 to calculate how many pairs we can make with that popularity score

    #example:
    '''
[5,2,5,5,2]

5 appears 3 times so 
3 x 2 /2=3
2 appears 2 times so 

2 x 1 /2=1 

now we add them up 
3+1=4 so the total popular pairs is 4



    '''
    dict={}
    for i in popularity_scores:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    
    pop_scores=0
    #go through the dictionary and for each value we do the calculation 
    for key, value in dict.items():
        pop_scores+=(value*(value-1))//2
    
    return pop_scores

#Problem 9: You are given two lists of strings s and t representing the stage arrangements of performers in two different performances at a music festival, 
# such that every performer occurs at most once in s and t, and t is a permutation of s.
#The stage arrangement difference between s and t is defined as the sum of the absolute difference between the index of the occurrence of 
# each performer in s and the index of the occurrence of the same performer in t.
#Return the stage arrangement difference between s and t.
#A permutation is a rearrangement of a sequence. For example, [3, 1, 2] and [2, 1 , 3] are both permutations of the list [1, 2, 3].
#Hint: Absolute value function

def find_stage_arrangement_difference(s,t):
    '''

    so we get the index from the first list and check where that same performer is in the second list 
    then we get the subtract their indexes and get the absolute value 
    then we tally up all those differences and return that as the final answer

    ex:
    ["bob", "alice", "charlie"]
    ["alice", "bob", "charlie"]

    abs(0-2)=2 -> this is for bob 
    abs(1-0)=1 -> this is for alice
    abs(2-2)=0 -> this is for charlie

    total difference = 2+1+0=3
    
    '''

    difference=0

    for i in range(len(s)):
        #first check if that artist is inside the second list 
        if s[i] in t:
            #if they are then go ahead and subtract the current index and the index where we found said artist 
            abs_diff=abs(i-t.index(s[i]))
            difference+=abs_diff
    return difference



#Problem 10: You're given strings vip_passes representing the types of guests that have VIP passes, and guests representing the guests you have at the music festival. 
# Each character in guests is a type of guest you have. 
# You want to know how many of the guests you have are also VIP pass holders.
#Letters are case sensitive, so "a" is considered a different type of guest from "A".
#Here is the pseudocode for the problem. Implement this in Python and explain your implementation step-by-step.

'''
1. Create an empty set called vip_set.
2. For each character in vip_passes, add it to vip_set.
3. Initialize a counter variable to 0.
4. For each character in guests:
   * If the character is in vip_set, increment the count by 1.
5. Return the count.

'''

def num_VIP_guests(vip_passes, guests):
    #empty set called vip_set
    vip_set=set()
    counter=0
    #for each character in vip_passes, add it to vip_set
    for i in vip_passes:
        vip_set.add(i)
    
    #for each character in guests:
    for i in guests:
        #if the character is in vip_set, increment the count by 1
        if i in vip_set:
            counter+=1
    return counter


#Problem 11: Given a string pattern and a string schedule, return True if schedule follows the same pattern. 
# Return False otherwise.
#Here, "follow" means a full match, such that there is a one-to-one correspondence between a letter in pattern and a non-empty word in schedule.
#You are provided with a partially implemented and buggy version of the solution. Identify and fix the bugs in the code. 
# Then, perform a thorough code review and suggest improvements.

def schedule_pattern(pattern, schedule):
    
    genres = schedule.split()

    if len(genres) != len(pattern):
        return False

    char_to_genre = {}
    genre_to_char = {}

    for char, genre in zip(pattern, genres):
        if char in char_to_genre:
            if char_to_genre[char] != genre:
                return False
        else:
            char_to_genre[char] = genre

        if genre in genre_to_char:
            if genre_to_char[genre] != char:
                return False
        else:
            genre_to_char[genre] = char

    return True


#Problem 12: You are given an array of strings performer_names, and an array performance_times that consists of distinct positive integers representing the performance durations in minutes. 
# Both arrays are of length n.
#For each index i, performer_names[i] and performance_times[i] denote the name and performance duration of the ith performer.
#Return performer_names sorted in descending order by the performance durations.

def sort_performers(performer_names, performance_times):
#we cannot use a dicttionary because we have repeated values in performer names 
    combined=list(zip(performer_names, performance_times))
    sort_combined=sorted(combined, key=lambda x:x[1], reverse=True)
    #after sorting it now I need to return the first element of each tuple in the sorted list 
    return [x[0] for x in sort_combined]

