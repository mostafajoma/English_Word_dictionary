# import libraries
import json
from difflib import get_close_matches
# load the data from json file
data = json.load(open('../data.json'))
# create a function 
def definition(word):
    word = word.lower()
    word = word.upper()
    # create conditionals
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys())) > 0:
        yn = input("Did you mean %s insted? Enter Y for yes and N for no." % get_close_matches(word, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "The word does not exist. Please double check it."
        else:
            return "We did not understand your entry."
    else:
        return "The word does not exist. Please double checkhi"

# ask the user for an input
word = input("Enter word: ")
# create coditionals for clean output
output = definition(word)
if type(output) == list:
    for item in output:
        print(item)

else:
    print(output)
