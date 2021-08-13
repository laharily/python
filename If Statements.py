#if statements allow you to make desicions in your code
age = 5
if age > 5:
    print ("Read chapter books.")
elif age < 5:
    print ("Read letter books.")
else:
    print ("Go play!")

weekday = False
vacation = False
if not weekday or vacation:
    print (True)
else:
    print (False)
