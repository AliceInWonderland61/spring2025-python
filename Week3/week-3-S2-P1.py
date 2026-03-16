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
    
