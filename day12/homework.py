#N1
# Write a function which converts the input string to uppercase.
def make_upper_case(s):
    return s.upper()

print(make_upper_case("giorgi bibilashvili"))

#2
# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!

def are_you_playing_banjo(name):
    if name[0]=="r":
        return name+" plays banjo"
    elif name[0]=="R":
        return name+" plays banjo"
    else:
        return name+" does not play banjo"
    
print(are_you_playing_banjo("rico"))

#3
#Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

def invert(lst):
    invert_num=[]
    for element in lst:
        invert_num.append(element * -1)
    return invert_num

#N4
# #Can you find the needle in the haystack?

# Write a function findNeedle() that takes an array full of junk but containing one "needle"

# After your function finds the needle it should return a message (as a string) that says:

# "found the needle at position " plus the index it found the needle, so:

def find_needle(haystack):
    for element in haystack:
        if element=="needle":
            return "found the needle at position " + str(haystack.index("needle"))
        
print(find_needle(["junk","needle"]))


#N5
#Write a function that takes an array of numbers and returns the sum of the numbers. The numbers can be negative or non-integer. If the array does not contain any numbers then you should return 0.

def sum_array(a):
    list(a)
    empty_sum=0
    for i in a:
        empty_sum+=i
    return empty_sum
        
