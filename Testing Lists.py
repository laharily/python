#declaring an empty list
fruits = []
numberOfFruits = []
#adding values to the list
fruits.append("strawberry")
fruits.append("apple")
fruits.append("grape")
fruits.append("pineapple")
print (fruits)
numberOfFruits.append(20)
numberOfFruits.append(18)
numberOfFruits.append(34)
numberOfFruits.append(4)
numberOfFruits.append("I like fruits.")
print (numberOfFruits)
#len function is used to find the number of values in a list
print (len(fruits))
print (len(numberOfFruits))
#removing values from the list
fruits.remove('apple')
numberOfFruits.remove(4)
print (fruits)
print (numberOfFruits)
#combining two lists
l = fruits + numberOfFruits
print (l)
print (l[2:4])
#inserting values in a list
fruits.insert(1,"apple")
fruits.insert(3,"orange")
print (fruits)

