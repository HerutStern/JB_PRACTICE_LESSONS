

# TYPE

# ITEM = KEY(UNIQUE) + VALUE
# {""KEY1" = "VALUE1", "KEY1" = "VALUE2"}: ONE VALUE WILL BE IGNORED
# NESTED DICTS



# LENGTH OF THE DICT
# len(my_dict) - counts the keys


# GET A VALUE
# my_dict[value] - a wrong value raise an error / my_dict.get(value) - a wrong value returns None
# my_dict.keys() / my_dict.values()



# ADDING OR CHANGING A VALUE
# my_dict.update({key: new_value}) / my_car[key] = value


# REMOVING ITEMS
# my_dict.pop(key) / del my_car[key]
# my_dict.popitem - deletes a random item
# del my_dict - deletes the dict / my_dict.clear() - clears the list


# IN / NOT IN



# FOR LOOPS
# for value in my_dict
# for value in my_dict.values() / for key in my_dict.keys()
# for key, value in my_dict.items()


# EX 1 - Write a Python program to print a dictionary line by line.
# EX 2 - Write a Python program to remove duplicates from the dictionary.


# USE THE DICT FOR ANOTHER DICT
# my_dict.copy()


# SORT
# (there is not a built-in sort function for dict)
# use the sorted() function




# EXERCISES


# EX 1 - Write aPython program to create a dictionary for this str - 'hello',
#       in which the key will be the key, and the value will be the letter.

# EX 2 - Write a Python script to concatenate the following dictionaries to create a new one.
#
#       Sample Dictionary :
#       dic1={1:10, 2:20}
#       dic2={3:30, 4:40}
#       dic3={5:50, 6:60}
#       Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


# EX 3 - Write a Python script to check whether a given {key, value} already exists in a dictionary

# EX 4 - Write a Python script to print a given dictionary where
#       the values are the square of the keys.
#       Sample Dictionary:
#       my_dict = {
#           1: 1,
#           2: 4,
#           3: 9,
#           4: 16,
#           5: 25,
#           6: 36,
#           7: 49
#       }

# EX 5 - Write a Python program to map these two lists into a dictionary:
#       my_keys = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
#       my_values = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# EX 6 - Write a Python program to create and display all combinations of letters,
#       selecting each letter from a different key in a dictionary.
#       Sample data : {'1':['a','b'], '2':['c','d']}
#       Expected Output:
#       ac
#       ad
#       bc
#       bd






