

# DECORATOR = NESTED FUNCTION


# SIMPLE EXAMPLE OF NESTED FUNCTION -
# def outer(x):
#     def inner(y):
#         return x + y
#     return inner
#
# add_five = outer(5)
# result = add_five(6)
# print(result)


# SIMPLE EXAMPLE OF DECORATOR
# def simple_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper
#
# @simple_decorator
# def say_hello():
#     print("Hello!")
# say_hello()


# *ARGS AND **KWARGS -
# *args and **kwargs are used in function definitions to allow the function
# to accept a variable number of arguments.
# Using *args and **kwargs in decorators allows decorators to work with functions
# of varying signatures without explicitly specifying the arguments.

# def log_args_and_kwargs(func):
#     def wrapper(*args, **kwargs):
#         print(f"Arguments: {args}")
#         print(f"Keyword arguments: {kwargs}")
#         result = func(*args, **kwargs)
#         return result
#     return wrapper
#
# @log_args_and_kwargs
# def example_function(a, b, c, x, y, z):
#     return a + b + c + x * y * z
#
# # Testing the decorated function
# result = example_function(1, 2, 3, x=4, y=5, z=6)



# DECORATOR PREVENTS CODE DUPLICATION -
# def deleted_selector(func):
#     def wrapper(*args, **kwargs):
#         sentence = "Wellcome to my function - "
#         result = func(*args, **kwargs, sentence=sentence)
#         return result
#     return wrapper
#
# @deleted_selector
# def my_function(sentence):
#     print(sentence)
#     print("This is my function")
#
# my_function()



