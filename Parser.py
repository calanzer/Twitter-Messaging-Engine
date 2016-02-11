"""
*Christian Lanzer*
*Parser.py*
This will take the string that is provided to it
It will split the string into a list of words
It will also separate words that start with an @ symbol into a differet "person" list
It will separate words that start with a # symbol in a different "topic" list
"""
import re
from Tweet import regex, link, person, topic, mylist, mystring

#This function will go through the words in our sentence and print them out, it will also sort through
#the words that start with '@' or '#' and add them to the person or topic list.
def text_parser(mylist):
    wordnumber = 1
    for word in mylist:
        print "This is word %d %s" % (wordnumber,  word)
        wordnumber += 1
        if re.findall(regex, word):
            link.append(word)
        for letter in word:
            if letter == '@':
                person.append(word)
            if letter == '#':
                topic.append(word)
text_parser(mylist)
print person
print topic
print mylist
print link
print len(mystring)







