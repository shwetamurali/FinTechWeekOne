def decode(code):
    finalSentence=""
    for c in code:
        if( (ord(c)<97 and ord(c)>90) or (ord(c)<65) or (ord(c)>125) ):
             finalSentence+= c
        elif(c=='A' or c=='B' or c=='C' or c=='a' or c=='b' or c=='c'):
            finalSentence+=chr(ord(c) + 23)
        else:
            finalSentence+=chr(ord(c) - 3)
    return finalSentence
    
def encode(sentence):
    finalSentence=""
    for c in sentence:
        if( (ord(c)<97 and ord(c)>90) or (ord(c)<65) or (ord(c)>125) ):
            finalSentence+= c
        elif(c=='Z' or c=='X' or c=='Y' or c=='z' or c=='x' or c=='y'):
            finalSentence+=chr(ord(c) - 23)
        else:
            finalSentence+=chr(ord(c) + 3) 
    return finalSentence         
print(decode("URFN SDSHU VFLVVRUV PDNHV PH VDG"))
print(encode("ROCK PAPER SCISSORS MAKES ME SAD"))