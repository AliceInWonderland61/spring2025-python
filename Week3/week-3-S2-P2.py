#Problem1: You are managing the budget for a global expedition, where the cost of supplies is represented by an integer array costs, 
# where costs[i] is the cost of the ith supply item.
#There is a special discount available during the expedition. 
# If you purchase the ith item, you will receive a discount equivalent to costs[j], 
# where j is the minimum index such that j > i and costs[j] <= costs[i]. 
# If no such j exists, you will not receive any discount.
#Return an integer array final_costs where final_costs[i] is the final cost you will pay for the ith supply item, 
# considering the special discount.

def final_supply_costs(costs):
    #ok so basically, for each number look right 
    #find the first smaller number or equl number 
    #then subtract it from that number 
    new_costs=[]
    
    for i in range(len(costs)):
        discount=0
        for j in range(i+1, len(costs)):
            if costs[j]<=costs[i]:
                discount=costs[j]
                break
        new_costs.append(costs[i]-discount)
    return new_costs


#Problem 2: During your global expedition, you encounter a series of landmarks, 
# each represented by a string in the array landmarks. 
# Your task is to find and return the first symmetrical landmark name. 
# If there is no such name, return an empty string "".
#A landmark name is considered symmetrical if it reads the same forward and backward.

def first_symmetrical_landmark(landmarks):
    #this might be a tad bit tricky but for now i'll have left and right as my pointers 
    #so we'll need two loops one for the entire landmarks array and the other so that for each word we come across, we loop through each character 

    for i in range(len(landmarks)):
        left=0
        right=len(landmarks[i])-1
        word=landmarks[i]
        is_symmetrical=True

        while left<right:
            if word[left]!=word[right]:
                is_symmetrical=False
                break
            left+=1
            right-=1
        if is_symmetrical:
            return word
    return ""


#Problem 3: During your global expedition, you are mapping out the terrain elevations, where the elevation of each point is represented by an integer. 
# You are given a string terrain of length n, where:
'''
terrain[i] == 'I' indicates that the elevation at the ith point is lower than the elevation at the i+1th point (elevation[i] < elevation[i + 1]).
terrain[i] == 'D' indicates that the elevation at the ith point is higher than the elevation at the i+1th point (elevation[i] > elevation[i + 1]).
Your task is to reconstruct the elevation sequence and return it as a list of integers. 
If there are multiple valid sequences, return any of them.

Hint: Try using two variables: one to track the smallest available number and one for the largest. 
As you process each character in the string, assign the smallest number when the next elevation should increase ('I'), and assign the largest number when the next elevation should decrease ('D').

'''
def terrain_elevation_match(terrain):
    #kinda confusing but we're using numbers 0 to n where n is the lenght of the terrain 
    n=len(terrain)
    smallest=0
    largest=n
    new_terrain=[]
    for i in range(n):
        if terrain[i]=='I':
            new_terrain.append(smallest)
            smallest+=1
        else:
            new_terrain.append(largest)
            largest-=1
    new_terrain.append(smallest) #we can append either smallest or largest since they will be the same at this point 
    return new_terrain

#Problem 4: You are recording journal entries during a global expedition, where each entry is represented by a 0-indexed integer array, logs. 
# The concatenation of two journal entries means combining their numerals into one.
#For example, concatenating the numbers 15 and 49 results in 1549.
#Your task is to calculate the total concatenation value of all the journal entries, which starts at 0. 
# To do this, perform the following steps until no entries remain:


'''
1. If there are at least two entries in the logs, concatenate the first and last entries, add the result to the current concatenation value, and then remove these two entries.
2. If there is only one entry left, add its value to the concatenation value and remove it from the array.
3. Repeat until the array logs is empty
4. Return the final concatenation value after all entries have been processed.
'''

def find_the_log_conc_val(logs):
    #ok so we get the first and last value and combine them (not add)
    #ex first value is 7 an the last value is 4 then it's 74

    #so we keep that value saved up and we remove those values from the logs array 
    #we could probably make a list that saves the concatenated values and then sum them up at the end 

    cat_values=[]

    while len(logs)>1:
        first=logs[0]
        last=logs[-1]

        #so we need to convert them to strings cause if we just 'combine' them it won't work cause they're numbers 
        #once they're combined then we convert them back to integers
    
        cat_values.append(int(str(first) + str(last)))
        logs.pop(0) #removing the first value
        logs.pop(-1) #removing the last value
    if len(logs)==1:
        cat_values.append(logs[0]) #if there's one value left we just add it to the cat_values list
    return sum(cat_values) #we return the sum of all the concatenated values

#Problem 5: During a global expedition, explorers must gather supplies from a limited stockpile, which includes two types of resources: type 0 (e.g., food rations) and type 1 (e.g., medical kits). 
# The explorers are lined up in a queue, each with a specific preference for one of the two types of resources.

#The number of supplies in the stockpile is equal to the number of explorers. 
# The supplies are stacked in a pile. At each step:
'''
If the explorer at the front of the queue prefers the resource on the top of the stack, they will take it and leave the queue.
Otherwise, they will leave the resource and go to the end of the queue.
This process continues until no explorer in the queue wants to take the top resource, leaving some explorers unable to gather the supplies they need.

You are given two integer arrays explorers and supplies, where supplies[i] is the type of the ith resource in the stack (
i = 0 is the top of the stack) and explorers[j] is the preference of the jth explorer in the initial queue (j = 0 is the front of the queue). 
Return the number of explorers that are unable to gather their preferred supplies.

'''

def count_explorers(explorers, supplies):


    counter=0
    while explorers and supplies:
        #if we are constantly shifting so we only focus on the first explorer and supply 
        if explorers[0]==supplies[0]:
            explorers.pop(0)
            supplies.pop(0)
            counter=0
        else:
            explorers.append(explorers.pop(0)) #if the explorer doesn't want the supply we move them to the end of the queue
            counter+=1
        if counter==len(explorers): #if we've gone through the entire queue and we still can't make them happyt then we break out of the loop
            break
    return len(explorers) #the remaining explorers in the queue that couldn't get the supplied they wanted 

#Problem 6: During your global expedition, you are analyzing a binary terrain string, terrain, where 0 represents a valley and 1 represents a hill. 
# You need to count the number of non-empty balanced subsections in the terrain. 
# A balanced subsection is defined as a contiguous segment of the terrain where an equal number of valleys (0s) and hills (1s) appear, and all the 0s and 1s are grouped consecutively.
# Your task is to return the total number of these balanced subsections. 
# Note that subsections that occur multiple times should be counted each time they appear.

def count_balanced_terrain_subsections(terrain):
    prev_group=0
    curr_group=1
    count=0

    for i in range(1, len(terrain)):
        if terrain[i]==terrain[i-1]: #if the current character is the same as the previous one we just increase the current group count
            curr_group+=1
        else: #if it's different then we have a new group so we set the previous group to be the current group and reset the current group to 1
            prev_group=curr_group
            curr_group=1
        
        if prev_group>=curr_group: #if the previous group is greater than or equal to the current group then we can form a balanced subsection
            count+=1
    return count

#Problem 7: During your global expedition, you are monitoring various transmissions, each consisting of some signals separated by a single space. 
# You are given a searchSignal and need to check if it occurs as a prefix to any signal in a transmission.
#Return the index of the signal in the transmission (1-indexed) where searchSignal is a prefix of this signal. 
# If searchSignal is a prefix of more than one signal, return the index of the first signal (minimum index). 
# If there is no such signal, return -1.
#A prefix of a string s is any leading contiguous substring of s.

def is_prefix_of_signal(transmission,searchSignal):
    #so this kind of falls back a bit to the palindrome case 
    # I can make an array of the signals by splitting the transmission string by spaces 
    signals=transmission.split(" ")

    #then we start looping through the signals to see if searchSignal is there 
    for i in range(len(signals)):
        if signals[i].startswith(searchSignal): #if the signal starts with the searchSignal then we return the index (1-indexed)
            return i+1 #we want the exact place not the index 
    return -1


        



