#!/usr/bin/python

# Pancakes : 2 sides, one happy side and a blank side 
# Stack of pancakes to serve -> X-Ray vision to know if it has the happy side or the blank side up
# Customer will be happy if they are served with the happy sides in the top 

# Way to flip the sides 
# Having a stack of N pancakes : 1, 2, ... N 
# First : choose the i TOP pancakes to flip
# Stack to split : 1, 2, ... i 
# Flip them : i, i-1, ... 1
# Put them on the top of the other ones
# Current stack :
# i, i-1, ... 1, i+1, i+2, ... N 

# Assuming that the happy face is represented as a + and the blank as a -
# If we have the following stack : --+-
# Take the first 3 and flip them 
# Current stack : -++-



# In this code, we will use 0 as happy face (+)
# and 1 as blank face (-)
# So the goal of this code will be to have a list fully filled by 0


def reverse_pancake(p):
    return (p+1) %2    

def flip (pancakes, index):
    # WARNING : the index start from 1 to len
    top = pancakes[:index]
    bottom = pancakes [index:]
    for i in range(index) :
        top[i] = reverse_pancake(pancakes[index-i-1])
    return top + bottom

def find_optimize_index (pancakes):
    # look for the longest straight which will be created by the flip operation

    # Look for the longest straight of 0 or 1 (named it p)
    # in pancakes and the second longest straight of !p from the beginning, 
    # if we got a longest straight then we keep this index 

    # Begin by finding the longest straight from the beginning
    i = 0
    p = pancakes[i]
    i = i + 1
    while i < len(pancakes) and pancakes[i] == p :
        i = i+1

    q = reverse_pancake(p)

    # Find the longest straight of q after i
    # the index of the beginning of this straight is l

    l = i
    longest = i

    # Loop to reach the end of pancakes list
    j = i
    len_ = len(pancakes)
    while j < len_:
        if pancakes[j] == q :
            current_straight = 0    
            while j < len_ and pancakes[j] == q :
                current_straight = current_straight +1
                j = j+1
            if current_straight > longest:
                longest = current_straight
                l = j - longest
        j = j+1

    return l

def happy(pancakes):
    return [0 for i in range(len(pancakes))]



test_data = [
    [0,1,1,0,1,0,1,1,1,0,0],
    [0,1],
    [0,1,0],
    [1],
    [1,1,0,1]
]

if __name__ == "__main__":
    for pancakes in test_data:
        print pancakes
        while pancakes != happy(pancakes) :
            opt = find_optimize_index(pancakes)
            print opt
            flip(pancakes, opt)

            # It doesn't seems that there is a case where a spliting cannot be found
            # if pancakes_ == pancakes :
            #     print ("Cannot find split list for current pancakes")
            #     break
            # else:
            #     print (opt)
            #     pancakes = pancakes_
