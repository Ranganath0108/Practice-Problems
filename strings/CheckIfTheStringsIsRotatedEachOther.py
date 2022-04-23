"""A Program to check if strings are rotations of each other or not
Difficulty Level : Easy
Last Updated : 21 Apr, 2022
Given a string s1 and a string s2, write a snippet to say whether s2 is a rotation of s1? 
(eg given s1 = ABCD and s2 = CDAB, return true, given s1 = ABCD, and s2 = ACBD , return false)"""


def Is_rotated(s1, s2):
    s1 = s1+s1
    if(len(s1) != len(s2)):
        return False
    if(s2 in s1):
        return True
    return False


print(Is_rotated("ABCD", "CDAB"))
print(Is_rotated("ABCD", "ACBD"))
