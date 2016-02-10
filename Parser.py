"""
*Christian Lanzer*
*Parser.py*
This will take the string that is provided to it
It will split the string into a list of words
It will also separate words that start with an @ symbol into a differet "person" list
It will separate words that start with a # symbol in a different "topic" list
"""
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
url = []
wordnumber = 1
#Got the regex compiler to test for URLs from http://stackoverflow.com/questions/23459812/using-re-compile-and-re-sub
#What the regex compiler does though is basically confirm the the 'word' is a http:// or a https://
regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

#This function will go through the words in our sentence and print them out, it will also sort through
#the words that start with '@' or '#' and add them to the person or topic list.
for word in mylist:
    print "This is word %d %s" % (wordnumber,  word)
    wordnumber += 1
    if re.findall(regex, word):
        url.append(word)
    for letter in word:
        if letter == '@':
            person.append(word)
        if letter == '#':
            topic.append(word)
print person
print topic
print mylist
print url
print len(mystring)

import unittest

#Unit tests that check to make sure our lists contain the appropriate values. I used the assertListEqual
#function to compare lists. It will also check to make sure our tweet is under 140 chars.
class PrimesTestCase(unittest.TestCase):

    def test_pass(self):
        self.assertTrue(True)

    def test_list(self):
        testList = ['@Frank', '@it', '#is', 'very', '#nice', 'to', 'meet', 'you','check', 'out', 'http://google.com', 'dont', 'check','out', 'google.com']
        self.assertListEqual(mylist, testList)

    def test_list_person(self):
        testPerson = ['@Frank', '@it']
        self.assertListEqual(person, testPerson)

    def test_list_topic(self):
        testTopic = ['#is', '#nice']
        self.assertListEqual(topic, testTopic)

    def test_size(self):
        self.assertTrue(len(mystring) < 200)

    def test_url(self):
        testURL = ['http://google.com']
        self. assertListEqual(url, testURL)


if __name__ == '__main__':
    unittest.main()






