#Problem 1: You're curating a large collection of NFTs for a digital art gallery, and your first task is to extract the names of these NFTs from a given list of dictionaries. 
# Each dictionary in the list represents an NFT, and contains information such as the name, creator, and current value.
#Write the extract_nft_names() function, which takes in this list and returns a list of all NFT names.

#Evaluate the time and space complexity of your solution. 
# Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def extract_nft_names(nft_collection):
    #so we're just gunna make an array of names 
    nft_names=[]

    for i in nft_collection:
        nft_names.append(i['name'])

    return nft_names


#Problem 2: You're responsible for ensuring the quality of the NFT collection before it is displayed in the virtual gallery. 
# One of your tasks is to review and debug the code that extracts the names of NFTs from the collection. 
# A junior developer wrote the initial version of this function, but it contains some bugs that prevent it from working correctly.

'''
Task:

Review the provided code and identify the bug(s).

Explain what the bug is and how it affects the output.

Refactor the code to fix the bug(s) and provide the correct implementation.

'''

def extract_nft_names(nft_collection):
    nft_names = []
    for nft in nft_collection:
        #nft_names += nft["name"] -> this doesn't work we need to .append it
        nft_names.append(nft["name"])
    return nft_names



#Problem 3: You have been tasked with identifying the most popular NFT creators in your collection. 
# A creator is considered "popular" if they have created more than one NFT in the collection.
#Write the identify_popular_creators() function, which takes a list of NFTs and returns a list of the names of popular creators.
#Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.


def identify_popular_creators(nft_collection):
    #i could create another dictionary and count the number of times each creator appears 
    creator_count = {}
    popular_creators = []

    for i in nft_collection: #this is O(n) cause it's a for loop that goes n times 
        creator=i['creator'] # we get the creator of the current i 
        if creator in creator_count:
            creator_count[creator] += 1 #if the creator is already in the dictionary we add 1 to their count
        else:
            creator_count[creator] = 1 #if the creator is not in the dictionary we add them with a count of 1
    

    #now we look at the counts we got for the creator and if it's greater than 1 we add it to the populr crators list 
    for i in creator_count: #this is also O(n) cause it's a for loop that goes n times 
        if creator_count[i] > 1:
            popular_creators.append(i)
    return popular_creators

#overall time complexity is O(n) + O(n) = O(2n) which simplifies to O(n) because we drop the constant.



#Problem 4: You want to provide an overview of the NFT collection to potential buyers. 
# One key statistic is the average value of the NFTs in the collection. 
# However, if the collection is empty, the average value should be reported as 0.
#Write the average_nft_value function, which calculates and returns the average value of the NFTs in the collection.
#Evaluate the time and space complexity of your solution. 
# Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def average_nft_value(nft_collection):
    #so basically get all the values, add them up and divide them by the number of nfts we have 

    sum_values=0
    for i in nft_collection:
        sum_values+=float(i['value'])
    
    if len(nft_collection)==0:
        return 0
    else:
        return sum_values/len(nft_collection)


#Problem 5: Some NFTs are grouped into collections, and each collection might contain multiple NFTs. 
# Additionally, each NFT can have a list of tags describing its style or theme (e.g., "abstract", "landscape", "modern"). 
# You need to search through these nested collections to find all NFTs that contain a specific tag.
#Write the search_nft_by_tag() function, which takes in a nested list of NFT collections and a tag to search for. 
# The function should return a list of NFT names that have the specified tag.
#Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def search_nft_by_tag(nft_collections, tag):
    #so we make a list of nft names with that tag

    nft_names=[]
    for i in nft_collections:
        #yah we might need a double for loop causw there's multiple tags 
        for j in i:
            if tag in j['tags']:
                nft_names.append(j['name'])
    return nft_names
#it'll be O(n^2) because we have a double for loop 


#Problem 6: NFTs are processed in a queue that follows First-In, First-Out (FIFO). 
# Given a list of NFT names in their initial queue order, return the order in which they are processed.
#Write the process_nft_queue() function, which takes a list of NFTs. 
# The function should return a list of NFT names in the order they were processed.
#Evaluate the time and space complexity of your solution. 
# Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def process_nft_queue(nft_queue):
    #it's basically the same as the other one where we just make a list and return those 
    names=[]

    for i in nft_queue:
        names.append(i['name'])
    return names
#the time complexity is O(n) because we have a single for loop 


#Problem 7: You want to ensure that NFTs are added in a balanced way. For example, every "add" action must be properly closed by a corresponding "remove" action.
#Write the validate_nft_actions() function, which takes a list of actions (either "add" or "remove") and returns True if the actions are balanced, and False otherwise.
#A sequence of actions is considered balanced if every "add" has a corresponding "remove" and no "remove" occurs before an "add".
#Evaluate the time and space complexity of your solution. 
# Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def validate_nft_actions(actions):
    #we do need a counter to keep track of the number of adds and removes so we know they're balanced 
    add_count=0
    remove_count=0

    for i in actions:
        if i=='add':
            add_count+=1
        elif i=='remove':
            remove_count+=1
            if remove_count>add_count: #if we have more removes than adds at any point then it's not balanced 
                return False
    return add_count==remove_count #at the end we check if the number of adds and removes are equal for it to be balanced
#the time complexity is O(n) because we have a single for loop that goes through the


#Problem 8: Buyers often look for NFTs that are closest in value to their budget. 
# Given a sorted list of NFT values and a budget, you need to find the two NFT values that are closest to the given budget: 
# one that is just below or equal to the budget and one that is just above or equal to the budget. 
# If an exact match exists, it should be included as one of the values.
#Write the find_closest_nft_values() function, which takes a sorted list of NFT values and a budget, and returns the pair of the two closest NFT values.
#Evaluate the time and space complexity of your solution. 
# Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def find_closest_nft_values(nft_values, budget):
    #i guess I could just sort them and then search for the index that is bigger thatn the budget and index-1 would be the one just below the budget
    low=0
    high=0
    nft_values.sort() #the time compleity for this is O(n log n) due to the sort function 
    for i in range(len(nft_values)):
        if nft_values[i]>=budget:
            high=i
            low=i-1
            break
    if low<0: #if the budget is less than the lowest value in the list
        return (None, nft_values[0])
    elif high>=len(nft_values): #if the budget is greater than the highest value    
        return (nft_values[-1], None)
    else:
        return (nft_values[low], nft_values[high])



