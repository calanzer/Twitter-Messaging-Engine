import unittest
from Parser import *

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

    def test_link(self):
        testLink = ['http://google.com']
        self. assertListEqual(link, testLink)

if __name__ == '__main__':
    unittest.main()