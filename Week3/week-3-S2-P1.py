#At a cultural festival, multiple performances are scheduled on a single stage. However, due to last-minute changes, some performances need to be rescheduled or canceled. The festival organizers use a stack to manage these changes efficiently.

#You are given a list changes of strings where each string represents a change action. The actions can be:
'''
"Schedule X": Schedule a performance with ID X on the stage.
"Cancel": Cancel the most recently scheduled performance that hasn't been canceled yet.
"Reschedule": Reschedule the most recently canceled performance to be the next on stage.
Return a list of performance IDs that remain scheduled on the stage after all changes have been applied.


'''

def manage_stage_changes(changes):

    #have two stacks
    #one for the incoming schedules
    #cancelled schedules (another stack)

    scheduled_stack=[]
    cancelled_stack=[]

    for i in changes:
        if "Schedule" in i:
            s=i.split()[1]
            
            scheduled_stack.append(s)
            

        elif "Cancel" in i:
            if len(scheduled_stack)!=0:
                cancelled_stack.append(scheduled_stack.pop())
            

        elif "Reschedule" in i:
            if len(cancelled_stack)!=0:
                scheduled_stack.append(cancelled_stack.pop())
            
    return scheduled_stack 

# Problem 2: You are organizing a festival and want to manage the queue of requests to perform. 
# Each request has a priority. Use a queue to process the performance requests in the order they arrive but ensure 
# that requests with higher priorities are processed before those with lower priorities. 
# Return the order in which performances are processed.

def process_performance_requests(requests):

    #sort based on the first idex of the tuple with is [0]

    sorted_priority=sorted(requests, key=lambda x:x[0], reverse=True)

    performance=[]

    for i in sorted_priority:
        performance.append(i[1])
    
    return performance 


#Problem 3: At the festival, there are various booths where visitors can collect points. 
# Each booth has a specific number of points available. 
# Use a stack to simulate the process of collecting points and return the total points collected after visiting all booths.

def collect_festival_points(points):

    #create a stack to store the total points
    total_stack=[]

    #reading in the points 
    for i in points:
        #append the first number 
        if len(total_stack)==0:
            total_stack.append(i)
        else:
            #add the next numbers from the stack 
            total_stack[-1]+=i
    
    return total_stack

#Problem 4: At the cultural festival, you are managing a treasure hunt where participants need to visit booths in a specific order. 
# The order in which they should visit the booths is defined by a series of clues. 
# However, some clues lead to dead ends, and participants must backtrack to previous booths to continue their journey.
#You are given a list of clues, where each clue is either a booth number (an integer) to visit or the word "back" indicating that the participant should backtrack to the previous booth.
#Write a function to simulate the participant's journey and return the final sequence of booths visited, in the order they were visited.

def booth_navigation(clues):
    #make a stack to store only the booths we need to vist
    tracker=[]

    for i in clues:
        if i=="back":
            if len(tracker)!=0:
                tracker.pop()
        else:
            tracker.append(i)
    return tracker 


#Problem 5: You are organizing a cultural festival and have two performance schedules, 
# schedule1 and schedule2, each represented by a string where each character corresponds to a performance slot. 
# Merge the schedules by adding performances in alternating order, starting with schedule1. 
# If one schedule is longer than the other, append the additional performances onto the end of the merged schedule.
#Return the merged performance schedule.

def merge_schedules(schedule1, schedule2):

    #so we're merging in an alternating order 
    # i remember reading about zip in python 
    zipped=zip(schedule1,schedule2)
    merged=""
    for i in zipped:
        #so in zipped it makes them [0][1] in an array [
        # 0]is the first element in schedule1 and [1]is the first element in scheudle2
        #since we want them to be strings we'll just add them as strings 
        merged+=i[0]+i[1]

    # Append any remaining performances from the longer schedule
    #if sschedule 1 is longer then take the length of schedule 2 as a starting point from wheree we need to start adding 
    if len(schedule1) > len(schedule2):
        merged += schedule1[len(schedule2):]
        #same here if the second one is bigger then take the length of schedule1 and use that index as the starting point 
    elif len(schedule2) > len(schedule1):
        merged += schedule2[len(schedule1):]

    return merged

#Problem 6: At a cultural festival, you have a schedule of events where each event has a unique popularity score. 
# The schedule is represented by two distinct 0-indexed integer arrays schedule1 and schedule2, 
# where schedule1 is a subset of schedule2.
#For each event in schedule1, find its position in schedule2 and determine the next event in schedule2 with a higher popularity score. 
# If there is no such event, then the answer for that event is -1.
#Return an array ans of length schedule1.length such that ans[i] is the next greater event's popularity score as described above.
def next_greater_event(schedule1, schedule2):
    #ok so we look at the first number in schedule 1, locate it on schedule 2 then look to the right of that number 
    #if that number is bigger than the currernt number then we add it to the answer arrray, if not we keep looking until we find a bigger numbert 
    #if there is no bigger number and we rached the end of the array then we just do -1

    combination=[]

    for i in schedule1:
        #get the index for that number and find it in schedule 2
        if i in schedule2:
            index=schedule2.index(i)
        found=False
        for j in range(index+1,len(schedule2)):
            if schedule2[j]>i:
                combination.append(schedule2[j])
                found=True
                break
        if not found:
            combination.append(-1)
    return combination 

#Problem 7: You are organizing a cultural festival and have a list of performances represented by an integer array performances. 
# Each performance is classified as either an even type (e.g., dance, music) or an odd type (e.g., drama, poetry).
#Your task is to rearrange the performances so that all the even-type performances appear at the beginning of the array, 
# followed by all the odd-type performances.
#Return any array that satisfies this condition.


def sort_performances_by_type(performances):
    #so we can just make two arrays and then merge them 

    even=[]
    odd=[]

    for i in performances:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    merged=even+odd
    return merged


    
