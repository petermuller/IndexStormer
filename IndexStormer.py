#!/usr/bin/env python
"""
IndexStormer.py

A really REALLY naive version of DirBuster
Made for the Week 2 SPARSA Challenge

Peter Muller
"""

from time import sleep
from thread import start_new_thread

from brute import brute

from Reqr import Reqr

__author__ = 'Peter Muller'

def main():
    """
    Main program driver; AKA break the things
    :return:
    """
    reqr = Reqr(0.01) #Make requests with a 0.01 second delay
    try:
        for comb in brute(length=8, ramp=True, letters=True, symbols=False, spaces=False):
            start_new_thread(reqr.makeReq,(comb,)) #Spawn new thread for each request
            sleep(reqr.isc.delay) #Rate limiting
        print(reqr.hits) #if this ever finishes, print the dictionary
    except:
        #Should only happen on keyboard interrupts or failures
        print(reqr.hits) #emergency dictionary dump

if __name__ == "__main__":
    #If file is run as a program, run the main function
    main()