# -*- coding: UTF-8 -*-
"""Refactoring.

This exercise contains a complete and working example, but it's very poorly written.

Your job is to go through it and make it as good as you can.

That means making it self-documenting wherever possible, adding comments where
it isn't. Take repeated code and make it into a function. Also use functions
to encapsulate concepts. If something is done many times, maybe a map or a loop
is called for. Etc.

Some functions will have directions as external comments, once you think you
are on top of it, take these comments out. Others won't have comments and
you'll need to figure out for yourself what to do.
"""


# This is a terrible function. The rest of the functions in this file do a
# much better job of what it's trying to do. Once you've has a little look,
# move on, and eventually delete this function. (And this comment!)



# return a list of countdown messages, much like in the bad function above.
# It should say something different in the last message.
def countdown(message, start, stop, completion_message):
         
    countdown_list = []
    if start > stop:
        countdown = start 
        while countdown > stop:
            countdown = countdown - 1 
            answer = message + " " +str(countdown) 
            countdown_list.append(answer) 
    else:
        countdown = stop 
        while countdown > start:
            countdown = countdown - 1 
            answer = message + " " + str(countdown)
            countdown_list.append(answer)
    countdown_list.append(completion_message)

    return countdown_list




# TRIANGLES

# This should be a series of functions that are ultimatly used by
# triangle_master
# It should eventually return a dictionary of triangle facts. It should
# optionally print information as a nicely formatted string. Make printing
# turned off by default but turned on with an optional argument.
# The stub functions are made for you, and each one is tested, so this should
# hand hold quite nicely.

def calculate_hypotenuse(base, height):

    hypotenuse = {3 * 2 + 4 * 2}

    return(hypotenuse)


def calculate_area(base, height):
    
    area = {3 * 4}

    return(area)


def calculate_perimeter(base, height):

    perimeter = {calculate_hypotenuse + 3 + 4}

    return(perimeter)


def calculate_aspect(base, height):
    
    aspect = {3 / 4}
    
    return(aspect)


# Make sure you reuse the functions you've already got
# Don't reinvent the wheel
def get_triangle_facts(base, height, units="mm"):
    return {"area": calculate_area,
            "perimeter": calculate_perimeter,
            "height": height,
            "base": base,
            "hypotenuse": calculate_hypotenuse,
            "aspect": calculate_aspect,
            "units": units}


# this should return a multi line string that looks a bit like this:
#
# 15
# |
# |     |\
# |____>| \  17.0
#       |  \
#       |   \
#       ------
#       8
# This triangle is 60.0mm²
# It has a perimeter of 40.0mm
# This is a tall triangle.
#
# but with the values and shape that relate to the specific
# triangle we care about.
def tell_me_about_this_right_triangle(facts_dictionary):
    tall = """
            {height}
            |
            |     |\\
            |____>| \\  {hypotenuse}
                  |  \\
                  |   \\
                  ------
                  {base}"""
    wide = """
            {hypotenuse}
             ↓         ∕ |
                   ∕     | <-{height}
               ∕         |
            ∕------------|
              {base}"""
    equal = """
            {height}
            |
            |     |⋱
            |____>|  ⋱ <-{hypotenuse}
                  |____⋱
                  {base}"""

    pattern = ("This triangle is {area}{units}²\n"
               "It has a perimeter of {perimeter}{units}\n"
               "This is a {aspect} triangle.\n")

    facts = pattern.format(**facts_dictionary)

#If anything within this function is returned, it returns all the boolean values as nothing at all, displayed through the "None." This is displayed 
# through the printed phrase at the end.  
def triangle_master(base,
                    height,
                    return_diagram=False,
                    return_dictionary=False):
    if return_diagram and return_dictionary:
        return None
    elif return_diagram:
        return None
    elif return_dictionary:
        return None
    else:
        print("You're an odd one, you don't want anything!")

 #Returns a pyramid list of random words collected from the online word generator json, via the URL provided. It is based on on two pyramids stacked 
 # oppositly using a for-loop starting the first pyramid with the 3 letter word first, stepinp up by 2 ending at the word with 
 # 21 letters. Then for the second pyramid it begins with the first letter count at 20, and repeating the same process back down 
 # to 3 letters, decrementing 2. 
 
def wordy_pyramid():
    import requests
    baseURL = "http://api.wordnik.com/v4/words.json/randomWords?api_key=a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5&minLength={0}&maxLength={0}&limit=1"
    pyramid_list = []
    for i in range(3, 21, 2):
        url = baseURL.format(i)
        r = requests.get(url)
        message = r.json()[0]['word']
        pyramid_list.append(message)
    for i in range(20, 3, -2):
        url = baseURL.format(str(i))
        r = requests.get(url)
        message = r.json()[0]['word']
        pyramid_list.append(message)
    return pyramid_list




def get_a_word_of_length_n(length):
    
    import requests
    url = "http://api.wordnik.com/v4/words.json/randomWords?api_key=a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5&minLength={0}&maxLength={0}&limit=1"
    r = requests.get(url) 
    word = r.json()[0]['word']
    return len(word)






def list_of_words_with_lengths(list_of_lengths):

    import requests
    url = "http://api.wordnik.com/v4/words.json/randomWords?api_key=a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5&minLength={0}&maxLength={0}&limit=1" 
    r = requests.get(url) 
    word = r.json()[0]['word']
    return list(map(len, word.split()))

    
