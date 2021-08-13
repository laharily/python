# Tuples are immutable, which means that you cannot change the values or delete
# them.
# Name, age, hobby, grade, letter grade, weight, height, last vacation
mix = ("Lahari", 11, "Reading", 6, "A", 90.5, 5.2)
lv = ("Hawaii", )
mix = mix + lv
print (mix)
xyz = ("apple", "carrot", "rice", "Boba tea", "pasta")
(fruit, vegetable, grain, drink, favorite_food) = xyz
print (grain)
