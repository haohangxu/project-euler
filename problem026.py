#!/usr/bin/env python

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Project Euler
# Problem 26
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

###########################################
###               IMPORTS               ###
###########################################

###########################################
###               GLOBALS               ###
###########################################
    
###########################################
###            FUNCTION DEFS            ###
###########################################

#=============================================================================#
# Finds the length of reciprocal cycle for a number n
# We keep track of remainders--once we hit the same remainder, we have 
# finished our cycle.
def find_cycle_len(n):
    # initialize tracker
    tracker = [-1] * n
    
    # initialize remainder (starts at 1)
    r = 1

    # by pidgeonhole, we need at most n iterations to find a cycle
    for i in range(n):
        # if remainder is 0, cycle is 0 since decimal terminates
        if r == 0: 
            return 0
        
        # check if remainder has already been reached 
        if tracker[r] >= 0: 
            return i - tracker[r]

        # otherwise, mark the remainder as reached
        tracker[r] = i
        
        # calculate new remainder
        while (r < n): 
            r *= 10

        r = r % n

    return -1
    
###########################################
###          MAIN FUNCTION              ###
###########################################

max_cycle_len = 0
max_cycle_denom = 1

for i in range(2, 1000):
    i_cycle_len = find_cycle_len(i)
    print('%d: %d' % (i, i_cycle_len))
    if i_cycle_len > max_cycle_len: 
        max_cycle_len = i_cycle_len
        max_cycle_denom = i

print('Longest cycle is 1/%d with length %d' % (max_cycle_denom, max_cycle_len))
