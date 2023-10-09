#remove whitespace from str, #capitalize users "name can also lstrip and rstrip
friend = input(f"whats your name? ").strip().title()\
#add a tabspace to output
print ("\tpython")
#add a newline per word in string
print ("\nnanyang\ntemasek\ntampines\nanglochinese")
#can also combine them for both newline and tabspace
print("Languages:\n\tPython\n\tC\n\tJavaScript")
#convert to lowercase
.lower()
#lists , square brackets can be used to choose which variable within the list, -1 can be used to denote the last item
polytechnics = ["temasek", "singapore", "ngee ann", "nanyang", "republic"]
print (polytechnics[-1])
#you can also replace just one item
polytechnics = ["temasek", "singapore", "ngee ann", "nanyang", "republic"]
print(polytechnics[-1].title())
polytechnics[0]= "sportssch"
# start with an empty list and then add items to the list,using a series of append() statements
jcs = []
jcs.append("raffles")
jcs.append("saintandrews")

#print(*objects, sep=' ', end='\n', file=None, cle=False), friend = friend.strip().title()
print ("hello,", friend, end=' cheer!!')
print (f"hello, {friend},", end=' cheer!!')

#remove whitespace from str, #capitalize users name
#.strip
#splitting name into first and last name
(first, last) = name.split("")
#converting variable into a integer
x = int(input("what is the value of X?"))
#if want to be able to calculate decimals as well
x = float(input("What is the value of y?"))
#rounding off integer to nearest whole number, n= no, of decimal places, using round function
x = round (x + y, n)
print (z)
#places commas in big numbers if needed
z= x / y
print (f"{z:,}")
#rounding off integer to nearest whole number, n= no, of decimal places, f-string method
print (f"{z:0.2}")
#use def to create your own function,"to" is a way for you to tell the function who you want to say hello to
#'world': This is the default ingredient that's put into the blank space if you don't provide a different one
def hello(to="world"):
    print("hello, ", to)
#making use of return function
def main():
    x = int(input("what's x?"))
    print ("square of X is", square(x))

def square(n):
        return n * n
#pow is the exponent
def square(n):
     return pow(n, 2)
#replace function can be used to replace spaces with some other argument
replace(" ","...")
print (youtube, sep = '...')
# the meaning of == represents equality while =  represents assignment
#== > equality
# != represents not equal to
# start with if, then elif then end with else, elif makes lines of code mutally exclusive
if x > y:
    print("x is greater than y")
elif x < y:
    print("x is lesser than y")
else x == y:
    print("x equals to y")

# try your best to simplify code as much as possible:
if x != y :
    print("x is not equal to y")
else:
    print("x is equal to y")
# using the divide function which checks if there is a remainder
if x % 2 == 0:
    print ("even")
else:
    print ("odd")
# boolean(bool) values True/False
if x % 2 == 0:
    return True
else:
    return False
# using match, _ used as else essentially
match name:
    case "winters":
        print("green")
    case "pearlyn":
        print("green")
    case _:
        print("not prcs?")
    case "winters" | "meredith" | "pearlyn":
        print("green"   )

 # endswith() function is used to check whether a given Sentence ends with some particular string.
.endswith and .startswith

 #what do keys do exactly
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Using keys() to iterate over the keys
for key in my_dict.keys():
    print(key)
results will be printed as
name 
age
city        


user_info = {"name": "Alice", "age": 30, "city": "New York"}
Now, if you use .items(), it's like opening a box and seeing each pair inside:

First, you see the pair "name" and "Alice".
Next, you see the pair "age" and 30.
Finally, you see the pair "city" and "New York".
You can use this method when you want to check or work with all the keys and values in a dictionary, one pair at a time. It's handy for tasks like printing or processing the information in the dictionary.





