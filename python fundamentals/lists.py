#chapter 3: lists
polytechnics = ["temasek", "singapore", "ngee ann", "nanyang", "republic"]
print(polytechnics[-1].title())
polytechnics[0]= "sportssch"
#removing an item using del statement
del polytechnics[4]
#using individual values from a list    
converse = ("i study at " + polytechnics[0].title() + " polytechnic !")
print(converse)


jcs = []
#appending elements to the end of a list
jcs.append("raffles")
jcs.append("saintandrews")
jcs.append("anglochinese")
jcs.append("catholic")
jcs.append("tampines")
#inserting elements into a list
jcs.insert(2,"yishun")
#sorting a list alphabetically can also be set in reverse alphabetical order
jcs.sort(reverse= True)
print (jcs)


sprints = ["100m", "200m", "400m"]
#removing any item Using the pop() Method and still being able to use it elsewhere
DNS = sprints.pop(1)
print("His status is DNS for the " + DNS.title() + " smh")

mousepads = ["saturn", "artisan", "vaxee", "zowie", "aquacontrol"]
#removing an item by value
too_fast = "artisan"
mousepads.remove(too_fast)
print("the hayate otsu by " + too_fast + " was too fast for me sadly ")

#finding the length of a list
mice = ["superlight", "dav3", "viperv2", "ec2"]
len(mice)
print (len(mice))

#sorted
estates =  ["pasir ris", "tampines", "bishan", "serangoon" ]
print (sorted(estates))