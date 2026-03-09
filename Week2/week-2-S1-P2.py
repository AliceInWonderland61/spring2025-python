#Given two lists of length n, crew and position, map the space station crew to their position on board the international space station.
#Each crew member crew[i] has job position[i] on board, where 0 <= i < n and len(crew) == len(position).
#Hint: Introduction to dictionaries

def space_crew(crew, position):
    combined={}

    for i in range(len(crew)):
        if crew[i] not in combined:
            combined[crew[i]] = position[i]
    return combined

#Problem 2: Given a dictionary planets that maps planet names to a dictionary containing the planet's number of moons and orbital period, 
# write a function planet_lookup() that accepts a string planet_name and returns a string in the form Planet <planet_name> has an orbital period of <orbital period> Earth days 
# and has <number of moons> moons. If planet_name is not a key in planets, return "Sorry, I have no data on that planet.".

def planet_lookup(planet_name):
    #i'm assuming I have to declare the dictionary beforehand 
    planetary_info = {
    "Mercury": {
        "Moons": 0,
        "Orbital Period": 88
    },
    "Earth": {
        "Moons": 1,
        "Orbital Period": 365.25
    },
    "Mars": {
        "Moons": 2,
        "Orbital Period": 687
    },
    "Jupiter": {
        "Moons": 79,
        "Orbital Period": 10592
    }
}
    if planet_name in planetary_info:
        orbital_period=planetary_info[planet_name]["Orbital Period"]
        moons=planetary_info[planet_name]["Moons"]
        return f"Planet {planet_name} has an orbital period of {orbital_period} Earth days and has {moons} moons."
    else:        
        return "Sorry, I have no data on that planet."


#Problem 3:As part of your job as an astronaut, you need to perform routine safety checks. 
# You are given a dictionary oxygen_levels which maps room names to current oxygen levels and two integers min_val and max_val specifying the acceptable range of oxygen levels. 
# Return a list of room names whose values are outside the range defined by min_val and max_val (inclusive).

def check_oxygen_levels(oxygen_levels, min_val, max_val):
    #unacceptable rooms list
    failed=[]
    #loop through the oxygen levels dictionry 
    for i in oxygen_levels:
        if oxygen_levels[i] < min_val or oxygen_levels[i] > max_val:
            failed.append(i)
    return failed

#Problem 4: Write a function data_difference() that accepts two dictionaries experiment1 and experiment2 
# and returns a new dictionary that contains only key-value pairs found exclusively in experiment1 but not in experiment2.

def data_difference(experiment1, experiment2):
    #new dictionary to hold pairs found in experiment1 but not in experiment2
    exclusive={}

    #loop through experiment1 and check if key is not in experiment2
    for i in experiment1:
        if i not in experiment2:
            exclusive[i]=experiment1[i]
        #so the example shows that there is a key with the same name in both dictionaries but their values are different 
        #that also counts as being exclusive so I added an additional condition to check for that 
        elif i in experiment2 and experiment1[i] != experiment2[i]:
            exclusive[i]=experiment1[i]
    return exclusive 


#Problem 5: NASA has asked the public to vote on a new name for one of the nodes in the International Space Station. 
# Given a list of strings votes where each string in the list is a voter's suggested new name, 
# implement a function get_winner() that returns the suggestion with the most number of votes.
#If there is a tie, return either option.

def get_winner(votes):
    #so we create a dictionary that keeps track of the strings we come across and the value will be how many times we come across that string 

    vote_count={}

    for i in votes:
        if i not in vote_count:
            vote_count[i]=1
        else:
            vote_count[i]+=1
    # now we fiind the max value in the vote_count dictionary and return that key

    return max(vote_count, key=vote_count.get)

#Problem 6: Ground control has sent a transmission containing important information. 
# A complete transmission is one where every letter of the English alphabet appears at least once.
#Given a string transmission containing only lowercase English letters, return true if the transmission is complete, or false otherwise.

def check_if_complete_transmission(transmission):
    #i guess we create the alphabet as a string we can use as reference 

    alphabet="abcdefghijklmnopqrstuvwxyz"

    i=0

    while i<len(alphabet):
        if alphabet[i] in transmission:
            alphabet=alphabet.replace(alphabet[i], '')
            i+=1
        else:
            return False
    
    return True
    

#Problem 7: Ground control is analyzing signal patterns received from different probes. 
# You are given a 0-indexed array signals consisting of distinct strings.
#The string signals[i] can be paired with the string signals[j] if the string signals[i] is equal to the reversed string of signals[j]. 0 <= i < j < len(signals). 
# Return the maximum number of pairs that can be formed from the array signals.
#Note that each string can belong in at most one pair.

def max_number_of_string_pairs(signals):
    #ok so we need a variable to keep track of the number of pairs we can make
    pairs_num=0

    #it's kinda ugly time wise but we could use a nested for loop to compare each string with every other string and check if they are reverses of each other

    for i in range(len(signals)):
        for j in range(i+1, len(signals)):
        #once again I read it wrong; scratch previous solutioin we're looking for reverses 
            if signals[i][0]==signals[j][1] and signals[i][1]==signals[j][0]:
                pairs_num+=1
    
                
    return pairs_num

#Problem 8: You are given two 0-indexed integer arrays signals1 and signals2, representing signal data from two different probes. 
# Return a list answer of size 2 where:
'''
answer[0] is a list of all distinct integers in signals1 which are not present in signals2.
answer[1] is a list of all distinct integers in signals2 which are not present in signals1.
Note that the integers in the lists may be returned in any order.

Below is the pseudocode for the problem. Implement this in Python and explain your implementation step-by-step.

1. Convert signals1 and signals2 to sets.
2. Find the difference between set1 and set2 and store it in diff1.
3. Find the difference between set2 and set1 and store it in diff2.
4. Return the list [diff1, diff2].
    
'''

def find_difference(signals1, signals2):
    #first convert signals1 and signals2 to sets
    set1=set(signals1)
    set2=set(signals2)

    #seoncd we find the difference between set1 and set2 but before this we need diff1 and diff2 to be created
    diff_1=set()
    diff_2=set()

    for i in set1:
        if i not in set2:
            diff_1.add(i)

    for i in set2:
        if i not in set1:
            diff_2.add(i)

    return [list(diff_1), list(diff_2)]


#Problem 9: Two space probes have collected signals represented by integer arrays signals1 and signals2 of sizes n and m, respectively. 
# Calculate the following values:
'''
answer1: the number of indices i such that signals1[i] exists in signals2.
answer2: the number of indices j such that signals2[j] exists in signals1.
Return [answer1, answer2].
'''

def find_common_signals(signals1, signals2):
    #i guess we need two variables to keep track of the xommon number of sequences 
    common1=0
    common2=0

    for i in signals1:
        if i in signals2:
            common1+=1
    
    for j in signals2:
        if j in signals1:
            common2+=1
    return [common1, common2]

#Problem 10: If you implemented find_common_signals() in the previous problem using dictionaries, 
# try implementing find_common_signals() again using sets instead of dictionaries. 
# If you implemented find_common_signals() using sets, use dictionaries this time.

#Once you've come up with your second solution, compare the two. Is one solution better than the other? How so? Why or why not?

def find_common_signals_dict(signals1, signals2):
    #now we use dictionaries 

    repeated1={}
    repeated2={}

    for i in signals1:
        if i in signals2:
            if i not in repeated1:
                repeated1[i]=1
            else:
                repeated1[i]+=1
    
    for i in signals2:
        if i in signals1:
            if i not in repeated2:
                repeated2[i]=1
            else:
                repeated2[i]+=1
    
    return [sum(repeated1.values()), sum(repeated2.values())]
    


#Problem 11: Ground control needs to analyze the frequency of signal data received from different probes. 
# Given an array of integers signals, sort the array in increasing order based on the frequency of the values. 
# If multiple values have the same frequency, sort them in decreasing order. Return the sorted array.
#Below is a buggy or incomplete version of the solution. Identify and fix the bugs in the code. 
# Then, perform a code review and suggest improvements.

def frequency_sort(signals):
    freq = {}
    for signal in signals:
        if signal in freq:
            freq[signal] += 1
        else:
            freq[signal] = 1
    #changed x to -x so that it's ascending according to the frequency but descending according to the value of the signal
    sorted_signals = sorted(signals, key=lambda x: (freq[x], -x))

    return sorted_signals

#Problem 12: You are given an array paths, where paths[i] = [hubA, hubB] means there exists a direct communication path going from hubA to hubB. 
# Return the final communication hub, that is, the hub without any outgoing path to another hub.
#It is guaranteed that the paths form a line without any loops, therefore, there will be exactly one final communication hub.

def find_final_hub(paths):
    #so we need to compare the second element of the first [] to the first element of the second[] and so forth 

    final_comm_hub=paths[0][0]

    if len(paths)==1:
        return paths[0][1]
    
    for i in range(len(paths)):
        for j in range(i+1, len(paths)):
            
            if paths[i][1]==paths[j][0]:
                final_comm_hub=paths[j][1]
    return final_comm_hub


            