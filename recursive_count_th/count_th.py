'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    
    if(len(word)<2):
        return 0

    if word[0:2] == 'th':
        count = 1
    else:
        count = 0

    if(len(word)>=2):
        j=count+count_th(word[1:])
        return j

print(count_th('abcthxth'))        