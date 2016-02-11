import re

#Input to the engine, or our 'tweet' I simply declared it here but idealy it would be user input.
mystring = "@Frank @it #is very #nice to meet you check out http://google.com dont check out google.com"
#Takes our string and splits the words into a list
mylist = mystring.split(" ")
#Person list contains all words that start with '@'
person = []
#Topic list conatins all word that start with '#'
topic = []
#This is just an increment for our print function to tell us which word number we are on
link = []
#Got the regex compiler to test for URLs from http://stackoverflow.com/questions/23459812/using-re-compile-and-re-sub
#What the regex compiler does though is basically confirm the the 'word' is a http:// or a https://
regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)