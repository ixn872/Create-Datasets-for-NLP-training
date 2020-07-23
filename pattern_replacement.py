import re
#I want user input prompt... etc and to join phrases at the end
phrase=("lorem","ipsum","dolor", "fright", "nec","pellentesque","eu",
         "pretium","quis","sem","nulla","consequat","massa","quis",)

def replace_right(phrase):
    phrase=list(phrase)
    for i in range(len(phrase)):
        if re.search(r"right",phrase[i]):
           phrase[i]=re.sub(r"right","left",phrase[i])
    return phrase
replace_right(phrase)
