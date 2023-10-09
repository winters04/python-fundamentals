# A simple example
pokka = ["green", "peach", "honey lemon", "blueberry"]
for drinks in pokka:
    if drinks == "banana":
     print(drinks.upper())
    else: 
        print(drinks.title())

# != means not equals to, == verifies the python equality of 2 variables
pain_level = input("How painful is your injury? ")
if pain_level == "extremely":
   print ("bring us the ice pack!")
else:
   print ("we dont need the ice pack.")

#using 'and', and 'or' but 'and' fails if not both pass while or passes as long as one passes but fails if none pass
age_1 = 22
age_2 = 19
if (age_1>=21) and (age_2>=21):
   print("both of age")
else: 
   print("not of age")

#checking if value is in a list, can also use not in 
banned_users = ["vikash", "matt", "winters"]
if "winters" not in banned_users:
   print("welcome back to the game!")
else:
   print("you have been permanently banned.")

age_limit = int(input("how old are you? "))
if(age_limit <= 21):
   print("you are qualified for junior college.")
else:
   print("you are not qualified for junior college.")

#using elif
age = 12 

if age < 4:
   price = 0
   
elif age < 18:
   price = 10

elif age < 65:
   price = 20

else:
   price = 10

print("your cost of admission is $" + str(price) + "." )

#if you want only one block of code to run, use an if-elifelse chain. If more than one 
# block of code needs to run, use a series of independent if statements.

requested_toppings = ("pearls", "aiyu", "pudding")
if "pearls" in requested_toppings:
   print ("adding pearls.")
if "aiyu" in requested_toppings:
   print ("adding aiyu.")
if "pudding" in requested_toppings:
   print ("adding pudding.")
print ("Finished making your bubble tea")

#checking for special items
requested_sauces = ["ranch", "barbecue", "chipotle southwest", "ketchup", "chili"]
for requested_sauce in requested_sauces:
   if requested_sauce == "ranch":
      print("sorry, we ran out of ranch")
   else:
      print("adding " + requested_sauce + ".")
print("\nyour sandwich is ready")
   
#using multiple lists
available_vegetables = ["tomatoes", "carrots", "cabbage", "cucumber", "lettuce"]
requested_vegetables = ["tomatoes", "avocado", "cucumber", "hummus"]

for requested_vegetable in requested_vegetables:
   if requested_vegetable in available_vegetables:
      print("adding " + requested_vegetable + ".")
   else:
      print("apologies, but we  dont have " + requested_vegetable + "." )

print ("\nfinished making your subway sandwich sir!")


