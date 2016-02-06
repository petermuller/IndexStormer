#!/usr/bin/env python
"""
IndexStormer.py

A really REALLY naive version of DirBuster
Made for the Week 2 SPARSA Challenge

Peter Muller
"""
import requests

import ISConfig

__author__ = 'Peter Muller'

def main():
    """
    Main program driver; AKA break the things
    :return:
    """
    isc = ISConfig.ISConfig()
    r = requests.get(isc.url, headers=isc.headers)
    print(r.status_code)


if __name__ == "__main__":
    #If file is run as a program, run the main function
    main()