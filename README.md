# IndexStormer
SPARSA Challenge #2: Create a program similar to DirBuster to find hidden directories and files.

## Requirements

This script requires the following packages, which may or may not be included with your Python:
- python 2.7.x
- requests
- brute

If you don't have them, try using
```console
pip install requests
```
or
```console
pip install brute
```
to install them.

## Configuration

Some preset values are available in Reqr.py, but to use this in different settings, or with a different server, you
can pass arguments into the Reqr constructor to change the URL or delay time between new request threads. Use the
'url' and 'delay' args in Reqr to set these.

By default the script will ramp from 1 character to the number of characters in the length parameter specified in the
brute call. To instead do one set of characters at a time, change ramp to False and length to your desired string length.

## Running

This script can be run by simply running
```console
python IndexStormer.py
```
