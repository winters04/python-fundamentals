#reading an entire file 
with open("pi_digits.txt") as file_contents: #open accesses a file 
    content = file_contents.read()#python stores this object in file_contents
    print(content) #with closes the file once access to it is no longer needed
    #rstrip removes the whitespace at end of numbers
    print(content.rstrip())
 
 #relative file paths
 with open("testing_files\\pi_digits.txt") as file_object1:
    test1 = file_object1.read()
    print(test1)

#absolute file path
file_path = "C:\\Users\\winte\\desktop - REDEX Pte. Ltd\\testing.txt.txt\\drinks list.txt"
with open(file_path) as file_object2:    
    test2 = file_object2.read()

#reading line by line 

