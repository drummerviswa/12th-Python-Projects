import string


def revstr(string):
    rstr = ""
    for ch in string:
        rstr = ch+rstr
    return rstr
string = input("Enter a string: ")
print("The reverse of the string is: ", revstr(string))