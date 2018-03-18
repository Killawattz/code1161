"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

#Is a vairable for a list of those words
some_words = ['what', 'does', 'this', 'line', 'do', '?']

# For the function word in the list some_words, it prints a random value from some_words 
for word in some_words:
    print(word)#loop prints each word in the list until all words have been printed

# For the function x in the list some_words, it prints the value of x in some_words
for x in some_words:
    print(x)#does the exact same function

print(some_words)

#If the length of the variable in some_words is greater than 3, than it will print 'some_words contains more than 3 words
if len(some_words) > 3:
    print('some_words contains more than 3 words')#checks the list and prints the string

def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """

    #The following line prints a named tuple of the platforms system, node, release, version, machine and processor
    print(platform.uname())#Results as expected

usefulFunction()
 