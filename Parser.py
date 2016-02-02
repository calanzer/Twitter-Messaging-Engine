"""
*Christian Lanzer*
*Parser.py*
This will take the string that is provided to it
It will split the string into a list of words
It will also separate words that start with an @ symbol into a differet "person" list

"""

mystring = "@Frank @it is very nice to meet you"
mylist = mystring.split(" ")
person = []
str1 = "@"
wordnumber = 1
print mylist
for word in mylist:
    print "This is word %d %s" % (wordnumber,  word)
    wordnumber += 1
    for letter in word:
        if letter == '@':
            person.append(word)
print person
print mylist






