#Problem 1: There are n users in a queue waiting to stream their favorite movies, where the 0th user is at the front of the queue and the (n - 1)th user is at the back of the queue.
#You are given a 0-indexed integer array movies of length n where the number of movies that the ith user would like to stream is movies[i].

#Each user takes exactly 1 second to stream a movie.
#A user can only stream 1 movie at a time and has to go back to the end of the queue (which happens instantaneously) in order to stream more movies. 
#If a user does not have any movies left to stream, they will leave the queue.
#Return the time taken for the user at position k (0-indexed) to finish streaming all their movies.

#ok i think i kind of get it, so we basically subtract 1 from each movie (index) until the k index reaches 0

def time_required_to_stream(movies,k):
    #we will keep track of the number ofi terations it takes for the k idex to reach 0, then return it 
    time_counter=0

    while movies[k]>0:
        for i in range(len(movies)):
            if movies[i]>0:
                movies[i]-=1
                time_counter+=1
            if movies[k]==0:
                break
    return time_counter

#Problem 2: You are given a list watchlist representing a list of shows sorted by popularity for a particular user. 
# The user wants to discover new shows they haven't heard of before by reversing the list to show the least popular shows first.
#Using the two-pointer approach, implement a function reverse_watchlist() that reverses the order of the watchlist in-place. 
# This means that the first show in the given list should become the last, 
# the second show should become the second to last, and so on. Return the reversed list.
#Do not use list slicing (e.g., watchlist[::-1]) to achieve this.

def reverse_watchlist(watchlist):
    #ok so we need to reverse the watchlist in place so we do need two pointers 

    left=0
    right=len(watchlist)-1

    while left<right:
        #we start swapping from the left and right pointers 
        watchlist[left],watchlist[right]=watchlist[right],watchlist[left]
        #we move the left pointer to the right and the right pointer to the left
        left+=1
        right-=1    
    return watchlist


#Problem 3: You are given a string schedule representing the lineup of shows on a streaming platform, 
# where each character in the string represents a different show. 
# A duplicate removal consists of choosing two adjacent and equal shows and removing them from the schedule.
# We repeatedly make duplicate removals on schedule until no further removals can be made.
# Return the final schedule after all such duplicate removals have been made. The answer is guaranteed to be unique.

def remove_duplicate_shows(schedule):
    # Adjacent means theyre next to each other so if the next character is the same as the current then we can pop it 

    stack=[]

    for i in schedule:
        if stack and stack[-1]==i:
            stack.pop()
        else:
            stack.append(i)
    return ''.join(stack)



#Problem 4: You manage a collection of view counts for different shows on a streaming platform. 
# You are given an array view_counts of n integers, where n is even.

#You repeat the following procedure n / 2 times:
'''
Remove the show with the smallest view count, min_view_count, and the show with the largest view count, max_view_count, from view_counts.
Add (min_view_count + max_view_count) / 2 to the list of average view counts average_views.
Return the minimum element in average_views.

'''

def minimum_average_view_count(view_counts):
    #kinda confusing but imma just follow it step by step
    #so i need to repeat the procedure n/2 times so i'll use a for loop
    average_views=[]
    for i in range(len(view_counts)//2):

        #1 remove the show with the smalles view count min_view_count
        min_view_count=min(view_counts)
        view_counts.remove(min_view_count)
       

        #2 remove the show with the largest view count max_view_count
        max_view_count=max(view_counts)
        view_counts.remove(max_view_count)
        


        #3 Add min_view_count + max_view_count / 2 to the list of average view counts average_views
        
        average_views.append((min_view_count+max_view_count)/2)

    #4 return the minimum element in average_views
    return min(average_views)

#Problem 5: You have a watchlist consisting only of uppercase English letters representing movies. 
# Each movie is represented by a unique letter.
#You can apply some operations to this watchlist where, in one operation, you can remove any occurrence of one of the movie pairs "AB" or "CD" 
# from the watchlist.
#Return the minimum possible length of the modified watchlist that you can obtain.
#Note that the watchlist concatenates after removing the movie pair and could produce new "AB" or "CD" pairs.

def min_remaining_watchlist(watchlist):

#so it looks like we need to remove the pairs "AB" and "CD" from the watchlist until we're done so if I use a stack I can safely look for them 
    stack=[]

    for i in watchlist:
        if stack and ((stack[-1]=='A' and i=='B') or (stack[-1]=='C' and i=='D')):
            stack.pop()
        else:
            stack.append(i)


    return len(stack)


#Problem 6: You are given a 0-indexed array ratings of size n consisting of non-negative integers. 
# Each integer represents the rating of a show in a streaming service.
#You need to apply n - 1 operations to this array where, in the ith operation (0-indexed), you will apply the following on the ith element of ratings:
#If ratings[i] == ratings[i + 1], then multiply ratings[i] by 2 and set ratings[i + 1] to 0. 
# Otherwise, you skip this operation.
#After performing all the operations, shift all the 0's to the end of the array.
#For example, the array [1,0,2,0,0,1] after shifting all its 0's to the end, is [1,2,1,0,0,0].
#Return the resulting array of ratings.

def apply_rating_operations(ratings):
    #i think we have to modify the array instead of creating a new one 
    counter=0
    new_ratings=[]
    for i in range(len(ratings)-1):
        #so for the i+1 element, i think we'd need to skip it or do some sort of evlauation to check if its 0 or not

        if ratings[i]==ratings[i+1]and len(ratings)>i+1:
            ratings[i]*=2
            
            ratings[i+1]=0
            
    
    #so now we need to shift the 0s to the end of the array 
    #we could keep a counter of how many 0s there are and then append that many 0s to the end of the array after wer remove them 
    #first we remove the 0s from the array 
    for i in ratings:
        if i!=0:
            new_ratings.append(i)
    
    for i in range(len(ratings)-len(new_ratings)):
        new_ratings.append(0)
    return new_ratings

#Problem 7: You are managing a watchlist for a streaming service, represented by a string watchlist consisting of lowercase English letters, 
# where each letter represents a different show.
# You are allowed to perform operations on this watchlist. 
# In one operation, you can replace a show in watchlist with another show (i.e., another lowercase English letter).

#Your task is to make the watchlist a palindrome with the minimum number of operations possible. 
#If there are multiple palindromes that can be made using the minimum number of operations, make the lexicographically smallest one.

#A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, 
# string a has a letter that appears earlier in the alphabet than the corresponding letter in b.
#Return the resulting watchlist string.
#Implement the following pseudocode:
'''
1. Convert the watchlist string to a list.
2. Initialize two pointers:
   * Left Pointer: Start at the beginning of the list (index 0).
   * Right Pointer: Start at the end of the list (last index).
3. While the left pointer is less than the right pointer:
   a. Compare the characters at the left and right pointers.
   b. If the characters are different:
      * Replace the character that is alphabetically later (greater) with the one that is earlier (smaller) to make the string lexicographically smaller.
   c. Move the left pointer one step to the right.
   d. Move the right pointer one step to the left.
4. Convert the list back to a string.
5. Return the resulting string.
'''

def make_smallest_watchlist(watchlist):
    #alriiggghhtty let's start following instructions 

    #convert the watchlist string to a list
    watchlist=list(watchlist)

    #initialize two pointers: left and right 
    left=0
    right=len(watchlist)-1

    #while the left pointer is less thatn the right pointer 
    while (left<right):
        #compare the charactesrs at the left and right pointeres
        if watchlist[left]!=watchlist[right]:
            #replace the character that is alphabetically later with the onte that is ealier (so i'm assuming the right one replaces the left one)
            if watchlist[left]>watchlist[right]:
                watchlist[left]=watchlist[right]
            else:
                watchlist[right]=watchlist[left]
        #move the left pointer one step to the right and the right pointer one tep to the left 
        left+=1
        right-=1

        #Conver the list back to a string 
    watchlist=''.join(watchlist)
    return watchlist

print(make_smallest_watchlist("egcfe")) 
print(make_smallest_watchlist("abcd")) 
print(make_smallest_watchlist("seven")) 
