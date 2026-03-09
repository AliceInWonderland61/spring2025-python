# Imagine you are working on a wildlife conservation database. 
# Write a function named most_endangered() that returns the species with the highest conservation priority based on its population.
# The function should take in a list of dictionaries named species_list as a parameter. 
# Each dictionary represents data associated with a species, including its name, habitat, and wild population. 
# The function should return the name of the species with the lowest population.
# If there are multiple species with the lowest population, return the species with the lowest index.


def most_endangered(species_list):
    # I guess we loop througu species list and compare the population of each species 
    #i made a minimum population variable so we can keep track of the lowest population we have come across 
    min_population=species_list[0]["population"]
    
    #we also wanna keep track of the name of that population so we can return it
    min_name=species_list[0]["name"]

    for i in species_list:
        if i["population"]<min_population:
            min_population=i["population"]
            min_name=i["name"]
    return min_name

#Problem 3: In a wildlife research station, each letter of the alphabet represents a different observation point laid out in a single row. 
# Given a string station_layout of length 26 indicating the layout of these observation points (indexed from 0 to 25), you start your journey at the first observation point (index 0). 
# To make observations in a specific order represented by a string observations, you need to move from one point to another.
#The time taken to move from one observation point to another is the absolute difference between their indices, |i - j|.
#Write a function that returns the total time it takes to visit all the required observation points in the given order with one movement.


''' 
Basically have the alphabet represent an index per character 
abcdefghijklmnopqrstuvwxyz

if we have the string "abe"

a-> abs(0-0)=0
b->abs(0-1)=1 ---> so we're still at a which is index 0 and to get to b we move to index 1
e->abs(1-4)=3  -----> we were in at b which is index 1 and to get to e we move to index 4


Now we tally them up: 0+1+3=4 and that's what we return 
'''

def navigate_research_station(station_layout, observations):
    #we need a counter variable and a current varialbe 
    #counter to keep track of the total time 
    time=0
    #current to keep track of where we are and use it to calculate the time to go to the next observation point
    current=0


    for i in range(len(observations)):
        next_index = station_layout.index(observations[i])
        time += abs(current - next_index)
        current = next_index

        if observations[i] in station_layout:
            current=station_layout.index(observations[i])
            time+=abs(current-station_layout.index(observations[i]))
    return time 


#Problem 4:In your work with a wildlife conservation database, you have two lists: observed_species and priority_species. 
# The elements of priority_species are distinct, and all elements in priority_species are also in observed_species.
#Write a function prioritize_observations() that sorts the elements of observed_species such that the relative ordering of items in observed_species matches that of priority_species. 
# Species that do not appear in priority_species should be placed at the end of observed_species in ascending order.


def prioritize_observations(observed_species, priority_species):
    #so my idea is that we create a dictinary with the species as the key in the order of the priority species 
    #and save how many times they appear as the key 
    #then when we outut it we loop through the new dictinary and output the species however man times the value number is 

    order_dict={}
    for i in priority_species:
        if i in observed_species:
            order_dict[i]=observed_species.count(i)
    
    #we have added the priority species to the dictionary and used coutn to count how many times they appear in observedd_species 
    #now we loop and can add them to a list 

    output=[]
    for i in order_dict:
        for j in range(order_dict[i]):
            output.append(i)
    #so i need to add the species that were not in the priority lit 
    for i in observed_species:
        if i not in priority_species:
            output.append(i)
    return output


#Problem 5: You are given a 0-indexed integer array species_populations of even length, where each element represents the population of a particular species in a wildlife reserve.
'''
As long as species_populations is not empty, you must repetitively:

Find the species with the minimum population and remove it.
Find the species with the maximum population and remove it.
Calculate the average population of the two removed species.
The average of two numbers a and b is (a+b)/2.

For example, the average of 200 and 300 is (200+300)/2=250.

Return the number of distinct averages calculated using the above process.

Note that when there is a tie for a minimum or maximum population, any can be removed.


'''

def distinct_averages(species_populations):
# ok so we need to continuously look for min and max while editing the species population 
#for loop didn't quite work for this so now I'll be using a while loop and just keep going until the list is empty
    total_averages=set()
    #we'll traverse the length of the species_populations list and continuosly find the min and max
    while len(species_populations)>0:
        #continuosly find the min and max population 
        min_population=min(species_populations)
        max_population=max(species_populations)
        #get the average of these two 
        average=(min_population+max_population)/2
        #add the average to the set of the total averages
        total_averages.add(average)
        #remove the min and max population so we can search for the next two min and max 
        species_populations.remove(min_population)
        species_populations.remove(max_population)
    #after we have removed all of the species then we get the total length of the total averages of the set, we return it 
    return len(total_averages)

   

# Problem 6: As a conservationist, your research center has been raising multiple endangered species and is now ready to reintroduce them into their native habitats. 
# You are given two 0-indexed strings raised_species and target_species. 
# The string raised_species represents the list of species available to release into the wild at your center, 
# where each character represents a different species. The string target_speciesrepresents a specific sequence of species you want to form and release together.
# You can take some species from raised_species and rearrange them to form new sequences.
# Return the maximum number of copies of target_species that can be formed by taking species from raised_species and rearranging them.

def max_species_copies(raised_species, target_species):
    #so my idea of this is to create a dictionary in the order of the target species and count how many times each species appears 
    #we then return the lowest number because technically that as many copies we can make with the designated species 

    #for example if we have aabbcccc and we want to make abc the number would have to be 2 because we can only use 2 a's and 2 b's even though we have 4 c's

    #create your dictionary 
    species_count={}
    #loop through the target species because that's the order we want to save the species in the dictionary 
    for i in target_species:
        #if that species is inside the overall species list in raised_species, 
        if i in raised_species:
            #add it to the dictioanry and save the number of occurences we find that species in the overall species list 
            species_count[i]=raised_species.count(i)
    
    #we return the lowest number in the dictionary 
    return min(species_count.values())


#Problem 7: You are given a string ecosystem_data that consists of digits and lowercase English letters. 
# The digits represent the observed counts of various species in a protected ecosystem.
#You will replace every non-digit character with a space. 
# For example, "f123de34g8hi34" will become " 123 34 8 34". 
# Notice that you are left with some species counts that are separated by at least one space: "123", "34", "8", and "34".
#Return the number of unique species counts after performing the replacement operations on ecosystem_data.
#Two species counts are considered different if their decimal representations without any leading zeros are different.

'''
ok so lets say we have the string "f123de34g8hi34"

we do a loop that compares each character to see if it's a digit or not, if it's not a digit, then we replace it with a space 
the new string should be 
" 123 34 8 34"

Now we need to return the number of unique 'species' in this case we have 123, 34, 8, and 34 but since 34 is repeated twice we don't count it twice 
So the number of unique 'species' should be 3 because we have 123, 34, and 8
'''

def count_unique_species(ecosystem_data):\
    #create a new list to save the new modified string
    new_list=[]
    current_number=""
    #traverse the ecosystem data
    for i in ecosystem_data:
        #so a bug arose and essentially what it was doing was treatig each number as a different species and making it's own index 
        #but what I want is for the numbers that are consecutive to be added to the same index 
        #so as long as we incur a digit, we add it to the current number variable, if we see a non digit, that's our queue to append that current number 
        #to a list and then reset the variable so it can receive the next consecutive numbers (if they are consecutive, sometimes it's just one number)
        if i.isdigit():
            current_number+=i
        #if it's not a digit, then we append a space instead 
        else:
            if current_number!="":
                #so we're supposed to remove the leading 0s and according to the documentation, if we convert it to an integer, those 0s are removed 
                new_list.append(int(current_number))
                current_number=""
    #if there are remianing numbers in current number then we just append them 
    if current_number!="":
        new_list.append(int(current_number))

    
    #contemplated on using a dictionary to save all the unique species as keys since dictionaries don't repeat keys, but after further investigation 
    #I found out that sets also don't repeat values and they are probably easier to implement do we'll go down that route 

    #also missed one of the instructions where it says tghat if there are leading 0s then we don't include that as unique species so I need to check the list
    #i could either modify the list or modify the set, but i'm not too sure yet lemme check 

    non_repeated=set(new_list)
    return len(non_repeated)


# Problem 8: In an effort to understand species diversity in different habitats, researchers are analyzing species pairs observed in various regions. 
# Each pair is represented by a list [a, b] where a and b represent two species observed together.
# A species pair [a, b] is considered equivalent to another pair [c, d] if and only if either (a == c and b == d) or (a == d and b == c). 
# This means that the order of species in a pair does not matter.
#Your task is to determine the number of equivalent species pairs in the list of observed species pairs.

def num_equiv_species_pairs(species_pairs):
    #i think we did something similar to this ? or maybe not idk 
    # we need to traverse each 
    #we could probably assign each pair to like a variable and then compare 
    #like a is [0][0] b is [0][1] and then we compare it to the next pair and see if they are equivalent
    #might not be the best run time but it should work 

#create a varable counter to keep track of how many pairs we encoutnter
    counter=0
#so we traverse the list of species paris 
    for i in range(len(species_pairs)):
        #because in the list they're saved like [[1,2], [3,4],[4,3]] etc
        #[i] is going to the the first pair we encounter, in this case it would be referring to [1,2] 
        #[0] is referring to the first element in that pair which is 1
        #[1] is referring to the second element in that pair which is 2 

        #the only one tat changes is i because we progress to the next pair 
        a=species_pairs[i][0]
        b=species_pairs[i][1]
        for j in range(i+1,len(species_pairs)):
            #now we look at the next pair 
            #again j signifies the pair we're looking at 
            #[0] or [1] referrs to the position of the pair 
            c=species_pairs[j][0]
            d=species_pairs[j][1]

            #we check if any of these equal each other 
            #keep in mind we're comparing the current pair to the next pair, we will remian in the first pair until we finish going through all 
            #the pairs inside species_pair
            if (a==c and b==d) or (a==d and b==c):
                counter+=1
    return counter 
