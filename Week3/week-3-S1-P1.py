# You are managing a social media platform and need to ensure that posts are properly formatted. 
# Each post must have balanced and correctly nested tags, such as () for mentions, [] for hashtags, and {} for links. 
# You are given a string representing a post's content, and your task is to determine if the tags in the post are correctly formatted.
# A post is considered valid if:
# Every opening tag has a corresponding closing tag of the same type.
# Tags are closed in the correct order.

def is_valid_post_format(posts):
    stack=[]
    dictionary={')':'(',
                ']':'[',
                '}':'{'}

    
    for i in posts:
        if i == '(' or i == '[' or i == '{':
            stack.append(i)
        
        elif i == ')' or i == ']' or i == '}':
            if dictionary[i]==stack[-1]:
                stack.pop()
            else:
                return False
    if len(stack)!=0:
        return False
    return True
    
# Problem 2: On your platform, comments on posts are displayed in the order they are received. 
# However, for a special feature, you need to reverse the order of comments before displaying them. 
# Given a queue of comments represented as a list of strings, reverse the order using a stack.

def reverse_comments_queue(comments):
    #createa a stack to start the reversal process
    stack=[]
    for i in comments:
        stack.append(i)
    #create a stack with the reversed comments 
    reversed_comments=[]
    #we pop the comments from the stack and transfer then over to reversed_comments
    while len(stack)!=0:
        reversed_comments.append(stack.pop())
    
    return reversed_comments


#Problem 3: As part of a new feature on your social media platform, you want to highlight post titles that are symmetrical, 
# meaning they read the same forwards and backwards when ignoring spaces, punctuation, and case. 
# Given a post title as a string, use a new algorithmic technique the two-pointer method to determine if the title is symmetrical.

def is_symmetrical_title(title):

    #declare two strings 

    string1=""
    for i in title:
        if i!= ' ':
            string1+=i.lower()
            
    
    string2=string1[::-1]

    back=len(string1)-1

    print(string1)
    print(string2)

    #loop through string1
    for i in range(len(string1)):
        if string1[i]!=string2[i]:
            return False
        
    return True 

#Problem 4: You track your daily engagement rates as a list of integers, sorted in non-decreasing order. 
# To analyze the impact of certain strategies, you decide to square each engagement rate and then 
# sort the results in non-decreasing order.

#Given an integer array engagements sorted in non-decreasing order, 
# return an array of the squares of each number sorted in non-decreasing order.


#ok looks like we have our function engagement_boost and it takes a list of engagements as input 
def engagement_boost(engagements):
    #it seeems it's creating a list to store the squared engagements 
    squared_engagements = []
    #travering engagements 
    for i in range(len(engagements)):
        #we create a variable to stroe the squared engagment, it's taking the current i it finds and multiplying it by itself to get the square
        squared_engagement = engagements[i] * engagements[i]
        #then it just aooends it to the squared_engagements list we made 
        #i think it's also saving the index where we find that specific i
        squared_engagements.append((squared_engagement, i))
    #now it reverses the squared_engagements list, so the highest squared engagement will be at the beginning of the list and the lowest will be at the end
    squared_engagements.sort(reverse=True)
    #for some reason it's getting the length of engagements and creating a list of 0s with that same lenght 
    #i'm assuming they're just placeholders 
    result = [0] * len(engagements)
    #created a variable called position and it's set to the last index of the engagements list
    position = len(engagements) - 1
    
    #So we'ree looping through swuared engagements and useing two variables, square and original_index
    for square, original_index in squared_engagements:
        #i think they're just doing a reverse without the actual .reverse() function 
        result[position] = square
        #then -1 cause we're travering backwareds 
        position -= 1
    
    return result


#Problem 5: You want to make sure your posts are clean and professional. Given a string post of lowercase and uppercase English letters, 
# you want to remove any pairs of adjacent characters where one is the lowercase version of a letter and the other is the uppercase version of the same letter. 
# Keep removing such pairs until the post is clean.

#A clean post does not have two adjacent characters post[i] and post[i + 1] where:
'''
post[i] is a lowercase letter and post[i + 1] is the same letter in uppercase or vice-versa.
Return the clean post.

Note that an empty string is also considered clean.

'''

def clean_post(post):
    stack=[]
    #let's account for empyt string which is also considered clean 
    if len(post)==0:
        return ""
    
    for i in post:
        if len(stack)==0:
            stack.append(i)
        else:
            if stack[-1].lower()==i.lower() and stack[-1].isupper()!=i.isupper():
                stack.pop()
            else:
                stack.append(i)

    return "".join(stack)
    
#Problem 6: You want to add a creative twist to your posts by reversing the order of characters in each word within your post 
# while still preserving whitespace and the initial word order. 
# Given a string post, use a queue to reverse the order of characters in each word within the sentence.

def edit_post(post):
    #so i could probably split each post and do a .reverse for each index (word)
    words=post.split()

    for i in range(len(words)):
        words[i]=words[i][::-1]
    return " ".join(words)

#Problem 7: You often draft your posts and edit them before publishing. 
# Given two draft strings draft1 and draft2, return true if they are equal when both are typed into empty text editors. 
# '#' means a backspace character.
#Note that after backspacing an empty text, the text will remain empty.

def post_compare(draft1, draft2):
    stack1=[]
    stack2=[]

    for i in draft1:
        if i=='#':
            if len(stack1)!=0:
                stack1.pop()
        else:
            stack1.append(i)
    
    for i in draft2:
        if i=='#':
            if len(stack2)!=0:
                stack2.pop()
        else:
            stack2.append(i)
    
    return stack1==stack2





    



             


