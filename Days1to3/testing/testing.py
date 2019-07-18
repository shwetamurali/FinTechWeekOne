# print("Hello World")
# print("What's up?")
# #Datatypes
# #anything between quotes is a string
# print("There is no mistake here.")
# #integers/numbers
# print(7)
# print(7 + 9)
# print(7+9)
# print(4-8) #-4
# print(3*3) #9
# print(25/5) #5
# print(25/6) #4.something
# print(4**2) #16
# print(23%4) #3
# #functions and methods
# name = "John Jacob Jingleheimer Schmidt"
# print(name)
# print("Hello" + str(4))
# print(int("4"))

# #Inputs
# firstName="Shweta"
# lastName=input("What is your last name?\n")
# print("Hello, " + firstName + " "+ lastName.lower().capitalize()+"! Nice to meet you!")
# print("Your initials are "+firstName[:1]+lastName[:1])
# age=int(input("How old are you? "))
# newAge = str(age+3)
# print("You will be "+newAge+" years old in 2022.")
# if(age>=21):
#     print("Congrats! You are old enough to drink- go grab a bottle of tequila!")
# else:
#     print("Shucks! Looks like you have to stick to soda for now. You cannot drink yet. ")











# #Control Flow
# number = input("What's your favorite number?\n")
# try:
#     newNum = int(number)
#     if(newNum%2==0):
#         print("Your number is even")
#     else:
#         print("Your number is odd")
# except:
#     print("Please enter a number.")
    




# favAnimal = "Ostriches"
# print(favAnimal[4])
# print("The first letter is " + favAnimal[0])
# print("The second letter is " + favAnimal[1])
# print("The third letter is " + favAnimal[2])

# for i in range(0,len(favAnimal)):
#     print("The " + str(i) + "th letter is " + favAnimal[i])
    

# #Survey
# continent=input("Which continent would you like to travel to?")
# if(continent=="North America"):
#     loc = input("United States or International? (US or I)")
# elif(continent=="South America"):
# elif(continent=="Africa"):
# elif(continent=="Asia"):
# elif(continent=="Antarctica"):
# elif(continent=="Australia"):
# elif(continent=="Europe"):
#     print("Tropical or Sightseeing? (T or S)")
# else:
#     print("Please enter a continent.")

# numBottles = int(input("How many bottles?\n"))
# for i in range(numBottles,0,-1):
#     if(i!=1):
#         print(str(i) + " bottles of milk on the wall")
#     else:
#         print(str(i) + " bottle of milk on the wall")
import random
print("Welcome to the Dice Rolling game\nLet's roll the first die")
reachedGoal = false
count=0
while(reachedGoal==false):
    firstRoll= random.randint(1,7)
    secondRoll= random.randint(1,7)
    print("You rolled a "+str(firstRoll)+" and a "+str(secondRoll)+".")
    count++
    if(firstRoll==1 and secondRoll==1):
        reachedGoal=true
        print("Congrats! You rolled snake eyes! It took you "+str(count)+ " rolls.")

        



