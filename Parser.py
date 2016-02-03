"""
*Christian Lanzer*
*Parser.py*
This will take the string that is provided to it
It will split the string into a list of words
It will also separate words that start with an @ symbol into a differet "person" list
It will separate words that start with a # symbol in a different "topic" list
"""


mystring = "@Frank @it #is very #nice to meet you"
mylist = mystring.split(" ")
person = []
topic = []
str1 = "@"
wordnumber = 1
print mylist
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

import unittest

class PrimesTestCase(unittest.TestCase):

    def test_pass(self):
        self.assertTrue(True)

    def test_list(self):
        testTopic = ['#is', '#nice']
        self.assertListEqual(topic, testTopic)

if __name__ == '__main__':
    unittest.main()






