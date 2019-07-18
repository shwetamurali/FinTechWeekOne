name = input("What is your name? ")
print("Hi, "+name)
favoriteTVShow=input("What is your favorite TV show? ")
favoriteTVShow=favoriteTVShow.lower()
def tvTaste(paramName,show):
    if(show=="the office" or show=="grey's anatomy"):
        print("You have good taste, "+paramName)
        return True
    elif(show=="jersey shore" or "dance moms") :
         print("You have awful taste, "+paramName)
         return False
    else:
        print("You have bad taste, "+paramName)
        return False
output=tvTaste(name, favoriteTVShow)
#print(output)