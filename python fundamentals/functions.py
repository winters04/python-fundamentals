def say_hello():
    print("hello")

say_hello

def greet_user(username):
    print("hello, " + username.title() + "!")

greet_user("winters")

def phone_specs(model, color):
    print("i have a " + model + ".")
    print("my " + model + "'s color is " +  color) 

phone_specs("iphone 11", "mint green")
phone_specs("iphone 13", "red")     
phone_specs(model="iphone 15" , color = "red")

#default values 
def airpod_types( type , generation = "2nd generation"):
    print("i have a pair of " + type)
    print("my " + type + " are " + generation )

airpod_types("airpod pros")

#return values 
def retrieve_username(first_name, last_name, middle_name = ""):
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name #return a neatly fomatted full name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()

ign = retrieve_username("winters" , "zhang")
print(ign)

ign = retrieve_username("joe", "ziyong" , "zhang")
print(ign)

#returning a dictionary 
def player_title(first_title, last_title):
    player = {"first": first_title , "last": last_title } #return a dictionary of information about a person
    return player

new_player = player_title("winters", "zj",)
print (new_player)

#returning a dictionary with other information
def player_user(first_user, last_user, age = ""):
    player = {"first": first_user, "last": last_user}
    if age:
        player["age"] =  age 
    return player

new_user =  player_user("win", "zhang", age = 18)
print(new_user)

#using a function with a while loop
def make_album(artist_name, album_title, ):

    music_album =(album_title + " by " + artist_name)
    return music_album.title()

while True:
    print("please enter album title and artist name")

    album_t = input("album title: ")
    if album_t == "quit":
        break

    artist_n = input("artist name: ")
    if artist_n == "quit":
        break

    album_details = make_album(album_t,artist_n)
    print("the details of this album are: " + album_details)

#passing a list 
def greet_players(names):

    for name in names: #print a simple greeting to each user in the list 
        msg = "hello " + name.title() + "!"
        print(msg)

usernames = ["winters", "vishvah", "ilmi"]
greet_players(usernames)

#modifying a list in a function
#start with some cars that need to be repaired
unrepaired_cars = ["mercedes", "mcclaren", "audi"]
repaired_cars = []

#simulate repairing each car, until none are left 
#move each repaired car to repaired_cars after repairing
while unrepaired_cars:
    repairing_cars = unrepaired_cars.pop()
#simulate repairing car
    print ("now repairing: " + repairing_cars)
    repaired_cars.append(repairing_cars)

#display all repaired cars
print("The following models have been printed: ")
for repaired_car in repaired_cars:
    print(repaired_car)
      
      