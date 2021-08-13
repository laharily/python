daddies = {"Lahari":"Sailu","Sribharathi":"Koti","Sailu":"Sinu","Nithya":"Naresh","Ishanvi":"Raja","Sia":"Sumanth","Sydney":"Craig","Rhea":"Karthik","Naresh":"Nareen","Raja":"Roger","Sumanth":"Sumanth Sr.","Craig":"Steve","Karthik":"Krishna"}
enter = input("\nPress 0 to exit, otherwise press any key: ")

while enter != "0":
    name = input("\nEnter a name: ")
    dg = input("\nPress 1 if you want to know " + name + "'s dad's name. Press 2 if you want to know " + name + "'s grandpa's name: ")
    name = name.title()
    if dg == "1":
        print("\n" + name + "'s dad's name is " + daddies[name] + ".")
    if dg == "2":
        dad = daddies[name]
        print("\n" + name + "'s grandpa's name is " + daddies[dad] + ".")
    enter = input("\nPress 0 to exit, otherwise press any key: ")

