import pickle

class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating an instance of MyClass
obj = MyClass(name="John", age=30)

# # Save the object to a pickle file
# with open('my_class_instance.pkl', 'wb') as file:
#     pickle.dump(obj, file)

# Load the object from the pickle file
with open('my_class_instance.pkl', 'rb') as file:
    loaded_obj = pickle.load(file)

# Displaying the loaded object
print("Loaded Object:", loaded_obj.name, loaded_obj.age)