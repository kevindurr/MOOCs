#Write a function called random_marks. random_marks should
#take three parameters, all integers. It should return a
#string.
#
#The first parameter represents how many apostrophes should
#be in the string. The second parameter represents how many
#quotation marks should be in the string. The third
#parameter represents how many apostrophe-quotation mark
#pairs should be in the string.
#
#For example, random_marks(3, 2, 3) would return this
#string: #'''""'"'"'"
#
#Note that there are three apostrophes, then two quotation
#marks, then three '" pairs.
def random_marks(fir, sec, third):
    ret = ""
    ret += fir * "'"
    ret += sec * '"'
    ret += third * ''''"'''
    return ret

print(random_marks(3, 2, 3))

# 5/5