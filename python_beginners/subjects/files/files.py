

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
#
# "a" - Append - Opens a file for appending, creates the file if it does not exist
#
# "w" - Write - Opens a file for writing, creates the file if it does not exist
#
# "x" - Create - Creates the specified file, returns an error if the file exists




# OPENING A FILE
# IF THE FILE DOES NOT EXIST - IT WILL CREATE IT
# TYPE OF THE CONTENT - str
# file = open(file_path, 'r')
# content = file.read()
# file.close()



# The file is automatically closed after the 'with' block -
# with open(file_path, 'r') as file:
#     content = file.read()
#     print(content)


# OPEN 2 FILES AT ONCE
# with open(file_path_1) as file1, open(file_path_2) as file2:



# READ A NUMBER OF CHARACTERS:
# space/enter is a character also
# file.read(number_of_characters)



# Reading line by line
# OPTION 1 -
# with open(file_path, 'r') as file:
#     content = file.readline(limit)
#     content2 = file.readline(limit)
#     print(content)
#     print(content2)



# OPTION 2 -FOR LOOPS
# with open(file_path, 'r') as file:
#     for line in file:
#         print(line)



# Writing to a file
# with open(file_path, 'w') as file:
#     file.write('Hello, World!\n')
#     file.write('This is a new line.')



# Appending to a file
# with open(file_path, 'a') as file:
#     file.write('\nAppending a new line.')


# CREATING A FILE
# RETURNS AN ERROR IF EXISTS
# (better using 'w' - if it exists it will just rewrite the file)
# f = open("my_new_file.txt", "x")


# REMOVING A FILE
# import os = Miscellaneous operating system interfaces = ממשקי מערכת הפעלה
# "https://docs.python.org/3/library/os.html"
# os.remove(file_path)
# RETURNS AN ERROR IF THE FILE DOES NOT EXIST (CHECK FIRST)
# if os.path.exists(file_path):




# * REMOVE A FOLDER
# os.rmdir('my_folder')



# It's a good practice to handle exceptions, especially when working with files.
# try:
#     with open('nonexistent_file.txt', 'r') as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print("File not found.")
# except Exception as e:
#     print(f"An error occurred: {e}")


# EXERCISES

# EX 1 - Write a Python program to read a file line by line store it into an array.

# EX 2 - Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.
#       import string and use string.ascii_uppercase.

# EX 3 - Write a function in Python to count and display the total number of words in a text file.
#       use str.split().

# Write a function in Python to count the word "the" present in a text file "article.txt".
#       use str.split().

