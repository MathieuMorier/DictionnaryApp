import json
from difflib import get_close_matches

data = json.load(open(r"C:\Users\Mathi\PythonMegaCourse\Apps\App1_EnglishDictionnary\data.json"))

def tranlate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        yes_no = input("Did you mean %s instead? Enter Y if yes and N if no:  " % get_close_matches(word, data.keys())[0])
        if yes_no == 'Y':
            return data[get_close_matches(word, data.keys())[0]]
        elif yes_no == 'N':
            return "The word doesn't exist"
        else:
            return "We didn't understand your entry"
    else:
        return "The word doesn't exist"

word = input("Enter a word: ")

output = tranlate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
     print(output)