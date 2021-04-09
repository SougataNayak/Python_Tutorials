# File I/O

""" Files are used as the RAMs are volatile memories and data stored are lost once the program is closed
    For that purpose files are used to store data permanently
    Files are of majorly two types:
    1. Text files (.txt, .c)
    2. Binary files (.jpg, .mkv)"""

# Opening a file
'''Files in python can be read using the open() function
    It takes two arguments, filename and mode
    read() function is used to read from the file opened
    close() function is used to close the file at the end
    Default mode for opening a file is R (read mode)
    To open a file we use the relative path from our code'''

f = open('README.md', 'r')
data = f.read(10)
'''Used to read just 10 characters from the file, if no argument passed, whole file is read
     the read method has a list of all the lines in the file, using for we can print it line by line'''
print('First 10 words of the file using read function: ', data)


# Other methods to open a file
data = f.readline()
print('\nreadline-1: ', data)
data = f.readline()
print('readline-2: ', data)
f.close()

# To delete a file, we use the os module

# Modes for opening files
''' r -> read mode (read from the file)
    w -> write mode (clear the file's previous contents and write on the file)
    a -> append mode (add contents to the end of the file)
    + -> update mode (both read and write can be done)
    x -> create mode (creates a new file and throws error if it already exists)
    rb -> read file in binary mode
    rt -> read file in text mode'''


# Write on a file
'''Writing on a file can be done using the write() method after opening the file in write or append mode
    Unlike the read method, the write method can be run multiple times'''

f = open('newFile.txt', 'w')
f.write("This text will be written in the 'newFile.txt' after it is created.")
f.close()
f = open('newFile.txt', 'a')
f.write("\nNow the file is opened in append mode and this text will be added to the file.")
f.close()
f = open('newFile.txt', 'r')
print("Contents of the file is: ", f.read())


# with statement: files can be opened and closed using the with statement
with open('README.md', 'r') as f:
    print('\nUsing the with statement: ', f.read())
