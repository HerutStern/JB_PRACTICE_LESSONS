

class Profile:
    def __init__(self, name: str, birth_year: int, city: str):
        self._name = name
        self._birth_year = birth_year
        self._city = city
    def my_age(self):
        age = 2023 - self._birth_year
        return age

    def print_my_name(self):
        print(f'Hello! my name is {self._name}')

    @staticmethod
    def type_of_class():
        print('class')


# The "if name equals main" block guards the print statement,
# to ensure it executes only when the file is intentionally run directly as a script or application

if __name__ == '__main__':
    my_person = Profile('Herut', 2001, 'PT')
    print(my_person.my_age())
    my_person.print_my_name()

