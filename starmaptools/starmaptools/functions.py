import re

#===========================
# *   urlify
#===========================

def urlify(string):
    return string.replace(' ', '+')

#===========================
# *   find_whole_word
#===========================

def find_whole_word(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search