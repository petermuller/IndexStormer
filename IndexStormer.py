#!/usr/bin/env python
"""
IndexStormer.py

A really REALLY naive version of DirBuster
Made for the Week 2 SPARSA Challenge

Peter Muller
"""

import requests
from time import sleep

from brute import brute

import ISConfig

__author__ = 'Peter Muller'

def main():
    """
    Main program driver; AKA break the things
    :return:
    """

    # Parameters determining where to send requests
    isc = ISConfig.ISConfig()
    # Make a dictionary of things that are interesting
    hits = {}

    for comb in brute(length=10):
        r = requests.get(isc.url + comb, headers=isc.headers)
        if not (r.status_code == 404 or r.status_code == 502):
            #only record combination string and response code for space
            hits[comb] = r.status_code
            print(comb + ": " + str(r.status_code))
        sleep(isc.delay)
    print(hits)



if __name__ == "__main__":
    #If file is run as a program, run the main function
    main()