
print('@ stand near capital vowel')
print('* stand near small vowel')
def Translate(phrase):
    Translation=""
    for letter in phrase:
        if letter.lower() in "auioe":
            if letter.isupper():
                Translation =Translation + letter + '@'
            else:
                Translation =Translation + letter + '*'
             
        else:
            Translation =Translation + letter
    return Translation
print(Translate(raw_input('enter a phrase:')))   
