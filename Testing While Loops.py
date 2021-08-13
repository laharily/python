yesOrNo = input ("Enter a yes or no value.")
yesOrNo = yesOrNo.lower()
print (yesOrNo)
if yesOrNo == "yes" or yesOrNo == "no":
    print ("All good.")
else:
    print ("Not good.")

while yesOrNo == "yes":
    print ("Still learning Python!")
    yesOrNo = input ("Enter a yes or no value.")
    yesOrNo = yesOrNo.lower()
    
