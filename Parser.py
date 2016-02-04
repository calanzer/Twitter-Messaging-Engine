"""
*Christian Lanzer*
*Parser.py*
This will take the string that is provided to it
It will split the string into a list of words
It will also separate words that start with an @ symbol into a differet "person" list
It will separate words that start with a # symbol in a different "topic" list
"""

#Input to the engine, or our 'tweet' I simply declared it here but idealy it would be user input.
mystring = "@Frank @it #is very #nice to meet you"
#Takes our string and splits the words into a list
mylist = mystring.split(" ")
#Person list contains all words that start with '@'
person = []
#Topic list conatins all word that start with '#'
topic = []
#This is just an increment for our print function to tell us which word number we are on
wordnumber = 1

print mylist

#This function will go through the words in our sentence and print them out, it will also sort through
#the words that start with '@' or '#' and add them to the person or topic list.
for word in mylist:
    print "This is word %d %s" % (wordnumber,  word)
    wordnumber += 1
    for letter in word:
        if letter == '@':
            person.append(word)
        if letter == '#':
            topic.append(word)
print person
print topic
print mylist
print len(mystring)

import unittest

#Unit tests that check to make sure our lists contain the appropriate values. I used the assertListEqual
#function to compare lists. It will also check to make sure our tweet is under 140 chars.
class PrimesTestCase(unittest.TestCase):

    def test_pass(self):
        self.assertTrue(True)

    def test_list(self):
        testList = ['@Frank', '@it', '#is', 'very', '#nice', 'to', 'meet', 'you']
        self.assertListEqual(mylist, testList)

    def test_list_person(self):
        testPerson = ['@Frank', '@it']
        self.assertListEqual(person, testPerson)

    def test_list_topic(self):
        testTopic = ['#is', '#nice']
        self.assertListEqual(topic, testTopic)

    def test_size(self):
        self.assertTrue(len(mystring) < 140)


if __name__ == '__main__':
    unittest.main()






