#Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

# The output should be two capital letters with a dot separating them.

def abbrev_name(name):
    word=name.split()
    initial=word[0][0].upper() + "."+ word[1][0].upper()
    return initial
    
    
    

print(abbrev_name("giorgi bibilashvili"))

