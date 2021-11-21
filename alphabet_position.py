import string

from string import ascii_lowercase


LETTERS = {letter: str(index) for index, letter in enumerate(ascii_lowercase, start=1)} 

#print(LETTERS)


def alphabet_position(text):
    arr = []
    
    for n in range(len(text)):
        try:
            #print(text[n].lower())
            l = text[n].lower()
            
            pos = LETTERS[l]
            #print(LETTERS[n])
            #pos = LETTERS[n]
            arr.append(int(pos))
        except:
            pass
    #print(*arr,sep=',')
    #return (str(arr))
    #return (*arr,sep=',')
    return (str(arr)[1:-1].replace(',',''))

alphabet_position("The sunset sets at twelve o' clock.")
