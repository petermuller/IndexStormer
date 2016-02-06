"""
ISConfig.py

Holds configuration settings for the program

Peter Muller
"""
__author__ = 'Peter Muller'

class ISConfig:
    """
    Class for holding configuration items
    """

    def __init__(self,
                 url="http://ctf.arch-cloud.com/",
                 delay=0):
        """

        :param url: The address to attack
        :param delay: The delay in ms to wait between requests
        :return:
        """
        self.url = url
        self.delay = delay

    def __str__(self):
        """
        Returns a readable version of the configuration
        :return: Stringified version of the configuration
        """
        return "URL=" + self.url + "\nDelay=" + str(self.delay)