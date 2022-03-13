#Activity1
Friends = ["Nimra", "Zohra", "Sabahat", "Jameela", "Javeria"]
print(len(Friends)) #length of an array

#for index in range(0, 5, 1):
for index in range(0, len(Friends)):
    print(Friends[index])
for index in Friends:
    print(index)

#Activity2
Numbers = [2,4,6,8,10,12]

for index in range(5, -1, -1):
    print(Numbers[index])

for index in range(len(Numbers)-1, -1 ,-1):
    print(Numbers[index])

#Activity
Animals = ["Cat", "Lion"]
Animals.append("Dog")  #add an item to an array
Animals.insert(0, "Zebra")  #add an item based on index
Animals.remove("Cat") #remove an item from an array
del Animals[0]  #remove an item based on index

