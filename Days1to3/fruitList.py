# favFruits = ["mango","avocado","pineapple","grapes","pomegranate"]
# print(favFruits)
# favFruits.append("orange")
# print(favFruits)

# enisFav = favFruits[2]
# print(enisFav)

# #favFruits.pop(2)
# #favFruits.remove("pineapple")
# favFruits[2]="apple"
# print(favFruits)

# for fruit in favFruits:
#     print("I like "+fruit+".")
    
# for index in range(0,len(favFruits)):
#     print("I like "+favFruits[index]+".")
    
#fruitCriteria=[True, 0.20, True, True, 100, "banana", True]
fruitCriteria = {"isFresh": True, "costPerPound": 0.20, "isRipe":True, "inSeason":True,"howMuchLike":100, "whatIsIt":"banana","isAllergic":True}
print(fruitCriteria)

#                    key                    value
print(fruitCriteria["isAllergic"]) #returns true
fruitCriteria["specialFeature"]="GMO"
print(fruitCriteria)

for key in fruitCriteria:
    print("The answer to " + key + " is "+str(fruitCriteria[key])+".")