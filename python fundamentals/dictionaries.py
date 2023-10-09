alien_0 = {"color":"green", "points": 5}

new_points = alien_0["points"]
print("you just earned " + str(new_points) + " points")           

#modifying values in a dictionary
alien_0 = {"color": "green"}
print ("the alien is " + alien_0["color"] + ".")

alien_0["color"] = "yellow"
print("the alien is now " + alien_0["color"] + ".")

# creating the original position of the alien under a dictionary
alien_0 = {"x_position":0 , "y_position":25 , "speed": "medium"}
print("original x-position: " + str(alien_0["x_position"]) )

alien_0["speed"] == "fast"

if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:  #this shld be a fast alien
    x_increment = 3 

alien_0["x_position"] = alien_0["x_position"] + x_increment 
print ("new x-position: " + str(alien_0["x_position"]))     

#removing key-value pairs, in this case points
alien_0 = {"color":"blue" , "points":"10"}
print(alien_0)

del alien_0["points"]
print (alien_0)

favourite_subjects = {
    "winters": "history",
    "ilmi" : "ss",
    "vishvah" : "geography",
    "matthias" : "A math",
}
print ("winters's favourite subject is, " + favourite_subjects["winters"].title() + ".")

#looping through all key value pairs 
user_0 = {
    "username" : "winterszj",
    "first" : "winters",
    "last" : "zhang"
}
for key, value in user_0.items():
    print("\nkey:" + key)
    print("value: " + value)

favourite_flavours = {
    "winters" : "matcha",
    "nicole" : "houjicha",
    "ilmi" : "mintchocchip",
}

for name, flavour in favourite_flavours.items():
    print(name.title() + "'s favourite ice cream flavour is: " + flavour.title() + ".")     

#looping thru keys in a dictionary 
favourite_restaurants = {
    "winters" : "wingstop",
    "matt" : "stuff'd",
    "vishvah" : "kfc",
    "ilmi" : "mcdonalds",
}
friends = ["matt", "ilmi"]
for name in favourite_restaurants.keys():
    print(name.title())

    if name in friends:
        print("Hi " + name.title() + ", i see your favourite restaurant is: " +
          favourite_restaurants[name].title() + "!")
if "bala" not in favourite_restaurants.keys():
    print("bala, please vote for your favourite restaurant\n ") 

#a list of dictionaries           
alien_x = { "rank":"minion" , "points" : "5" }
alien_y = { "rank":"tank", "points" : "10" }
alien_z = { "rank":"boss", "points" : "20"}

aliens = [alien_x, alien_y, alien_z]
for alien in aliens:
    print(alien)

#NESTING
#make an empty list for storing aliens 
enemies = []

#creating 30 enemies
for enemy_number in range(30):
    new_enemy = {"rank":"corporal" , "points" : 10, "strength" : "weak" }
    enemies.append(new_enemy) 

for enemy in enemies[2:11]:
    if enemy["rank"] == "corporal":
        enemy["rank"] = "sergeant"
        enemy ["strength"] = "medium"
        enemy ["points"] = 20

    for enemy in enemies [7:11]:
        if enemy["rank"] == "sergeant":
         enemy["rank"] = "colonel"
        enemy["strength"] = "strong"
        enemy["points"] = 40



#printing 10 enemies
for enemy in enemies[:10] :
    print(enemy)
print("...")

#show total number of aliens created 
print("total number of alien:" + str(len(enemies)))

#A list in a dictionary

#store information about a pizza being ordered
bubble_tea = {
    "sugar_level" : "less sweet",
    "toppings" : ["pearls" , "jelly"]
}
#summarise the order 
print("you ordered a " + bubble_tea["sugar_level"] + " bubble tea with the following toppings:")

""" \t produces one horizontal spacing between 
The use of \t ensures that each topping is indented by a tab, making the list of toppings nicely formatted.
"""
for topping in bubble_tea["toppings"]:
    print(topping)

favourite_games = { 
    "winters" : ["valorant" , "csgo"],
    "vikash" : ["warzone" , "valorant"],
    "matt" : ["RL" , "dbz"],
    "jariel" : ["R6" , "csgo"]
}

for name, games in favourite_games.items():
    print (name.title() + "'s favourite languages are:")
    for game in games:
        print("\t" + game.title())

# A dictionary in a dictionary
users = { 
    "eejon" : {
        "first" : "jonathan",
        "last" : "moh",
        "location" : "simei"
    },
    "winterszj" : {
        "first" : "winters",
        "last" : "zhang",
        "location" : "pasir ris"
    },
}
 #remember key value pairs 
for username, user_info in users.items():
    print("Username:" + username) #<key
    full_name = user_info["first"] + " " + user_info["last"]#<value
    location = user_info["location"]#<value

    print("full name:" + full_name.title())
    print ("location:" + location.title())


