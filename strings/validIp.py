"""Program to generate all possible valid IP addresses from given  string.

Given a string containing only digits, restore it by returning all possible valid IP address combinations.
A valid IP address must be in the form of A.B.C.D, where A, B, C, and D are numbers from 0-255. 
The numbers cannot be 0 prefixed unless they are 0.





"""

def is_valid(ip):
    ip = ip.split(".")

    for i in ip:
        if (len(i) > 3 or int(i) < 0 or
                int(i) > 255):
            return False
        if len(i) > 1 and int(i) == 0:
            return False
        if (len(i) > 1 and int(i) != 0 and
                i[0] == '0'):
            return False

    return True


def convert(s):

    sz = len(s)

    if sz > 12:
        return []
    snew = s
    l = []
    for i in range(1, sz - 2):
        for j in range(i + 1, sz - 1):
            for k in range(j + 1, sz):
                snew = snew[:k] + "." + snew[k:]
                snew = snew[:j] + "." + snew[j:]
                snew = snew[:i] + "." + snew[i:]

                if(is_valid(snew)):
                    l.append(snew)

                snew = s

    return l


A = "25525511135"
print(convert(A))
