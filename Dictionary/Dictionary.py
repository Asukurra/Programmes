# import json

# data = json.load(open("data.json"))

# def key():
#     answer = input('word plz\n')
#     for word in data.items():
#         if word.keys() == answer:
#             return word.values()
#         else:
#             print('no word found')

# key()

#my stupid attempt above on looping through everything until you find one that matches >.< 



# the word matcher is from a standard lib called difflib - can import difflib or from fifflib import SequenceMatcher 
#then can run SequenceMatcher(none, 'rainn', 'rain') - the first argument is to clear spaces or _ etc or misc junk from the string
# to get a % value of match you need .ratio() at the end - SequenceMatcher(none, 'rainn', 'rain').ratio()


# from difflib import get_close_matches is the metod that will return the top 3 closest matches, the arguments are
#  (str,list type object, n=3, ratio=0.6) string being the word passed, data.keys() being the list type object, n is the max number of returns 
# and ratio will only show anything above a ratio of >=0.6
# can use index to get only the top match etc     get_close_matches('rainn,data.keys())[0] will only return the highest result for the str rainn


import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data: 
        return data[word.title()]   
    elif word.upper() in data: 
        return data[word.upper()]     
    elif len(get_close_matches(word,data.keys())) > 0:
        suggested = get_close_matches(word,data.keys())
        print('Did you mean %s instead?\nPlease press Y for yes or anything else to try again\n' %suggested[0])
        answer = input('Y/N?   ')
        if answer.lower() == 'y':
            return translate(suggested[0])  
        else:
            print('no close matching word, please check spelling and try again!')
            word = input('Enter word: ') 
            return (translate(word))
    else:
        return 'That word dosnt exist, please try again'


word = input('Enter word: ')

output = (translate(word))    

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
