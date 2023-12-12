
import pickle

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
# file = open("my_text_file.txt", 'r')
# content = file.read()
# print(content)
# file.close()




# The file is automatically closed after the 'with' block -
# with open("my_text_file.txt", 'r') as file:
#     content = file.read()
#     print(content)


# OPEN 2 FILES AT ONCE
# with open("my_text_file.txt") as file1, open("my_empty_text_file.txt") as file2:
#     content1 = file1.read()
#     content2 = file2.read()
#     print(content1)
#     print(content2)



# READ A NUMBER OF CHARACTERS:
# space/enter is a character also
# file.read(number_of_characters)
#
# with open("my_text_file.txt", 'r') as file:
#     content = file.read(7)
#     print(content)



# Reading line by line
# OPTION 1 -
# with open("my_text_file.txt", 'r') as file:
#     content = file.readline(2)
#     content2 = file.readline()
#     content3 = file.readline()
#     print(content)
#     print(content2)
#     print(content3)



# OPTION 2 -FOR LOOPS
# with open("my_text_file.txt", 'r') as file:
#     times = 1
#     for line in file:
#         print(times)
#         print(line)
#         times += 1



# Writing to a file
# with open("new_file.txt", 'w') as file:
#     file.write('Hello, World!\n')
#     file.write('This is a new line.')

# with open("my_text_file.txt", 'r') as file:
#     content = file.read()
#     print(content)



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


class Book:
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

if __name__ == '__main__':

    my_book = Book("this is my name", "tania")
    print(my_book)
#     try:
#         with open('library_books', 'wb') as books_file:
#             pickle.dump({'class': my_book}, books_file)
#     except Exception as e:
#         print(e)
#
# with open('library_books', 'rb') as file:
#     content = file.read()
#     print(content)