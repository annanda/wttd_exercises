#!/usr/bin/python2.4 -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic string exercises


# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
def verbing(s):
    if len(s) < 3:
        return s
    if s.endswith("ing"):
        sufixo = "ly"
    else:
        sufixo = "ing"

    return s + sufixo


    list_s = list(s)

    if s.endswith("ing"):
        list_s += ["l", "y"]
    else:
        list_s += ["i", "n", "g"]
    return "".join(list_s)


# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
    import re
    return re.sub(r'not\b(.(?!not))*?bad', "good", s)
    return re.sub(r'not(.*)bad', "good", s)

    word_not = "not"
    word_bad = "bad"
    not_index = s.find(word_not)
    bad_index = s.rfind(word_bad) + 3

    if not_index > bad_index:
        return s
    return s.replace(s[not_index:bad_index], "good")





# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
def front_back(a, b):
    def is_even(number):
        if number % 2 == 0:
            return True
        return False

    def divide_even_string(s):
        s_front = s[:len(s) // 2]
        s_back = s[len(s) // 2:]
        return s_front, s_back

    def divide_odd_string(s):
        s_front = s[:len(s) // 2 + 1]
        s_back = s[len(s) // 2 + 1:]
        return s_front, s_back

    if is_even(len(a)):
        a_front, a_back = divide_even_string(a)
    else:
        a_front, a_back = divide_odd_string(a)
    if is_even(len(b)):
        b_front, b_back = divide_even_string(b)
    else:
        b_front, b_back = divide_odd_string(b)

    return a_front + b_front + a_back + b_back
 

# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
    print('verbing')
    test(verbing('hail'), 'hailing')
    test(verbing('swiming'), 'swimingly')
    test(verbing('do'), 'do')

    print()
    print('not_bad')
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")
    test(not_bad("This is not not bad"), "This is not good")

    print()
    print('front_back')
    test(front_back('abcd', 'xy'), 'abxcdy')
    test(front_back('abcde', 'xyz'), 'abcxydez')
    test(front_back('Kitten', 'Donut'), 'KitDontenut')


if __name__ == '__main__':
    main()
