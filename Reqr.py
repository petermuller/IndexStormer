"""
Reqr.py

Makes requests and records results
AKA
Kicks butt and takes names

Peter Muller
"""

from requests import head, ConnectionError
from ISConfig import ISConfig

__author__ = 'Peter Muller'

class Reqr:
    """
    Class for making requests to a site
    """

    def __init__(self,
                 url="http://ctf.arch-cloud.com/",
                 delay=0
                 ):
        """
        Constructor for Reqr
        Starts a dictionary of successes and
        a configuration object
        :param delay: Amount of time in seconds to wait between reqs
        :return:
        """
        self.hits = {}  # persistent memory for storing interesting data
        self.isc = ISConfig(url=url, delay=delay)

    def makeReq(self,comb):
        """
        Makes a request to the server in the configuration object
        :param comb: the random string to try
        :return:
        """
        try:
            # make a head request to save space
            resp = head(self.isc.url + str(comb), headers=self.isc.headers)
            if resp.status_code not in [400, 404, 502]:
                # if interesting response code, record it
                self.hits[comb] = resp.status_code
                print(comb + " " + str(self.hits[comb]))
        except ConnectionError as err:
            print(err)  # Error "handling"
