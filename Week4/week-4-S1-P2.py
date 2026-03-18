#Problem 1: You need to filter out memes that are too long from your dataset. 
# Memes that exceed a certain length are less likely to go viral.
#Write the filter_meme_lengths() function, which filters out memes whose lengths exceed a given limit. 
# The function should return a list of meme texts that are within the acceptable length.
#Evaluate the time and space complexity of your solution. 
# Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def filter_meme_lengths(memes, max_length):
    #i think we need to count spaces as well 
    output_memes=[]

    for i in memes:
        if len(i)<=max_length:
            output_memes.append(i)
    return output_memes

memes = ["This is hilarious!", "A very long meme that goes on and on and on...", "Short and sweet", "Too long! Way too long!"]
memes_2 = ["Just right", "This one's too long though, sadly", "Perfect length", "A bit too wordy for a meme"]
memes_3 = ["Short", "Tiny meme", "Small but impactful", "Extremely lengthy meme that no one will read"]


#Problem 2: You want to identify the top meme creators based on the number of memes they have created.
#Write the count_meme_creators() function, which takes a list of meme dictionaries and returns the creators' names and the number of memes they have created.
#Evaluate the time and space complexity of your solution. 
# Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def count_meme_creators(memes):
    new_dictionary={}
    for i in memes:
        creator=i['creator']
        if creator in new_dictionary:
            new_dictionary[creator]+=1
        else:
            new_dictionary[creator]=1
    return new_dictionary


#Problem 3: You're tasked with identifying trending memes. 
# A meme is considered "trending" if it appears in the dataset multiple times.
#Write the find_trending_memes() function, which takes a list of meme texts and returns a list of trending memes, 
# where a trending meme is defined as a meme that appears more than once in the list.
# Evaluate the time and space complexity of your solution. 
# Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def find_trending_memes(memes):
    trending=[]
    dictionary={}

    for i in memes:
        if i in dictionary:
            dictionary[i]+=1
        else:
            dictionary[i]=1

    for i in dictionary:
        if dictionary[i]>1:
            trending.append(i)

    return trending


#Problem 4: You want to see how memes would trend if they were posted in reverse order.
#Write the reverse_memes() function, which takes a list of memes (representing the order they were posted) and returns a new list with the memes in reverse order.
#Evaluate the time and space complexity of your solution. 
# Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def reverse_memes(memes):
    #so we could create a new list and travel backwards 
    reversed_memes=[]
    counter=len(memes)-1
    while counter>=0:
        reversed_memes.append(memes[counter])
        counter-=1
    return reversed_memes


#Problem 5: You've been given partially completed code to identify pairs of memes that frequently appear together in posts. 
# However, before you can complete the implementation, you need to ensure the plan is correct and then review the provided code to identify and fix any potential issues.

'''
Your task is to:

Plan:

Write a detailed plan (pseudocode or step-by-step instructions) on how you would approach solving this problem. Consider how you would:

Iterate through each post.

Generate pairs of memes.

Count the frequency of each pair.

Identify pairs that appear more than once.

Ensure the final result is accurate and efficient.

Review:

Examine the provided code and answer the following questions:

Are there any logical errors in the code? If so, what are they, and how would you fix them?

Are there any inefficiencies in the code that could be improved? If so, how would you optimize it?

Does the code correctly handle edge cases, such as an empty list of posts or posts with only one meme?

'''

def find_trending_meme_pairs(meme_posts):
    pair_count = {}

    for post in meme_posts:
        # Sort or set-ify to handle duplicates/ordering consistently
        post = list(set(post)) 
        n = len(post)
        
        for i in range(n):
            for j in range(i + 1, n): # Start at i+1 to avoid double-counting
                # Sort alphabetically to ensure (A, B) is same as (B, A)
                pair = tuple(sorted([post[i], post[j]]))
                
                pair_count[pair] = pair_count.get(pair, 0) + 1

    # List comprehension for efficiency
    return [pair for pair, count in pair_count.items() if count >= 2]



#Problem 6: You're tasked with analyzing the order in which memes gain popularity. 
# Memes are posted in a sequence, and their popularity grows as they are reposted.

#Write the simulate_meme_reposts() function, which takes a list of memes (representing their initial posting order) and simulate their reposting by processing each meme in the queue. 
# Each meme can be reposted multiple times, and for each repost, it should be added back to the queue. 
# The function should return the final order in which all reposts are processed.
#Evaluate the time and space complexity of your solution. 
# Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def simulate_meme_reposts(memes, reposts):
    #so we have memes and reposts
    #could we just make a new list 
    #actually when we traverse, we just look at the reposts and add those to the end of the list and the loop won't end until 
    #all reposts are 0
    from collections import deque
    queue = deque()

    for i in range(len(memes)):
        queue.append((memes[i], reposts[i]))

    final_order = []

    while queue:
        meme, count = queue.popleft()
        final_order.append(meme)

        if count > 1:
            queue.append((meme, count - 1))

    return final_order


  
#Problem 7: You're interested in identifying groups of memes that, when combined, have a total popularity score closest to a target value. 
# Each meme has an associated popularity score, and you want to find the two memes whose combined popularity score is closest to the target value. 
# The list of memes is already sorted by their popularity scores.

#Write the find_closest_meme_pair() function, which takes a sorted list of memes (each with a name and a popularity score) and a target popularity score. 
# The function should return the names of the two memes whose combined popularity score is closest to the target.

#Evaluate the time and space complexity of your solution. 
# Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def find_closest_meme_pair(memes, target):
    left = 0
    right = len(memes) - 1

    closest_pair = None
    closest_diff = float("inf")

    while left < right:
        left_name, left_popularity = memes[left]
        right_name, right_popularity = memes[right]

        current_sum = left_popularity + right_popularity
        current_diff = abs(target - current_sum)

        if current_diff < closest_diff:
            closest_diff = current_diff
            closest_pair = (left_name, right_name)

        if current_sum < target:
            left += 1
        elif current_sum > target:
            right -= 1
        else:
            return (left_name, right_name)

    return closest_pair

#Problem 8: You need to analyze the trends of various memes over time. 
# You have a dataset where each meme has a name, a list of daily popularity scores (number of reposts each day), and other metadata.

#Write the find_trending_meme() function, which takes in a list of memes (each with a name and a list of daily repost counts) 
# and a time range (represented by a start and end day, inclusive). 
# The function should return the name of the meme with the highest average reposts over the specified period. 
# If there is a tie, return the meme that appears first in the list.

#Evaluate the time and space complexity of your solution. 
# Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def find_trending_meme(memes, start_day, end_day):
    #ok so the range is the start and end day 
    #we get the averages and we return the one with the highest average
    trending_meme = None
    highest_average = float("-inf")

    for i in memes:
        name = i['name']
        reposts = i['reposts']
        average_reposts = sum(reposts[start_day:end_day + 1]) / (end_day - start_day + 1)

        if average_reposts > highest_average:
            highest_average = average_reposts
            trending_meme = name
    return trending_meme

memes = [
    {"name": "Distracted boyfriend", "reposts": [5, 3, 2, 7, 6]},
    {"name": "Dogecoin to the moon!", "reposts": [2, 4, 6, 8, 10]},
    {"name": "One does not simply walk into Mordor", "reposts": [3, 3, 5, 4, 2]}
]

memes_2 = [
    {"name": "Surprised Pikachu", "reposts": [2, 1, 4, 5, 3]},
    {"name": "This is fine", "reposts": [3, 5, 2, 6, 4]},
    {"name": "Expanding brain", "reposts": [4, 2, 1, 4, 2]}
]

memes_3 = [
    {"name": "Y U No?", "reposts": [1, 2, 1, 2, 1]},
    {"name": "Philosoraptor", "reposts": [3, 1, 3, 1, 3]}
]
print(find_trending_meme(memes, 1, 3))
print(find_trending_meme(memes_2, 0, 2))
print(find_trending_meme(memes_3, 2, 4))