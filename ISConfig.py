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
                 delay=0
                 ):
        """

        :param url: The address to attack
        :param delay: The delay in ms to wait between requests
        :return:
        """
        self.url = url
        self.delay = delay
        self.headers = {}
        self.headers["user-agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36"


    def __str__(self):
        """
        Returns a readable version of the configuration
        :return: Stringified version of the configuration
        """
        return "URL=" + self.url + "\nDelay=" + str(self.delay)