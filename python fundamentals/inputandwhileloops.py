message = input("hi please enter your name: ")
print ("hi nice to meet you, " + message)

#prompt function
prompt = ("we can customise what you see")
prompt += "\nwhat is your first name? "
name = input(prompt)

print ("hello " + (name) + " nice to meet you!")

#using int to accept numerical input
height = int(input("how tall are you in cm? "))  
if height >= 165:
    print ("you are tall enough to take the ride! ")
else:
    print ("sorry you're too short to take the ride :( ")

number = int(input("odd and even number checker: "))
if number % 2 == 0 :
    print ("The number " + str(number) + " is even. ")
else:
    print ("The number " + str(number) + " is odd")

#using while loops
#setting value of current number to 1
current_number = 1 
#while loop is then set to keep running as long as value of current number <=5
while current_number <= 5: 
    print(current_number)
# += operator is shorthand for current_number = current_number + 1.) 
    current_number += 1

quitting =  "tell me something and i will say it back: "
quitting += "\nenter 'quit' to end the progamme "

message = "" #user input
#when msg is not quit, ask qns again
while message != "quit": #!= means not equal to, this line loops if msg not equals to quit
    message = input(quitting) # users input to qns of quitting
    if message != "quit":
        print (message) #print users input if not quit

#using a flag 
ctf = "continue playing in this server? "
ctf += "\ntype quit to leave game "

active = True #variable active is set to true
while active: 
    message = input(ctf)
    if message == "quit":
        active = False #stops looping active if false
    else:
        print (message)

#using break to exit a loop
game_over = "you have died! continue playing? "
game_over += "\ntype quit to exit to main menu. "

while True: #will run forever unless it reaches a break statement 
    menu = input(game_over)
    if menu == "quit":
        break #causes python to exit the loop
    else:
        print("select difficulty level")

#using continue in a loop
current_digit = 0
while current_digit < 10:
    current_digit += 1 #increase number by one once inside the loop
    if current_digit % 2 == 0:
        continue #continue returns to the beginning of the loops
    print(current_digit)

#moving items from one list to another
unverified_users = ["winters", "matt", "vikash"] #users yet to be verified
verified_users = []#empty list to hold confirmed users  

#verify each user until there are no more unverified users
while unverified_users:
    current_user = unverified_users.pop()
#move each verified user into verified user one by one 
    print("now verifying...: " + current_user.title())
    verified_users.append(current_user)
#display all verified users
print("\nthe following users have been verified:")
for verified_user in verified_users:
    print(verified_user.title())

#removing all instances of specific values from a list
fruits = ["cherries", "apples", "lettuce", "banana", "apples", "lettuce", "banana"]
print(fruits)
#loop through the fruits and remove lettuce since not a fruit
while "lettuce" in fruits:
    fruits.remove("lettuce")

print(fruits)

#filling a dictionary with user input 
responses = {}
#set a flag to indicate that polling is active 
polling_active = True

while polling_active:
    name = input("what is your name? ")
    response = input("what educational route do you want to take? ")
#responses[name] = response: This line assigns the user's response (the educational route) to the name key in the responses 
#dictionary. In other words, it associates the user's name with their educational route choice in the dictionary. 
#So, when you later access responses[name], you will get the educational route that corresponds to that specific user's name.
    responses[name] = response 

#find out if anybody else is going to take the poll
    repeat =  input("any other responses (yes/no) ")
    if repeat == "no":
        polling_active = False #if false will js go back ot looping polling active

#polling is complete, show the results
print(" --- poll results --- ")
for name, response in responses.items(  ): 
    print(name + " would like to go to " + response + " in the future. ")

