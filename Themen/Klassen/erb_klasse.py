from basis_klasse import Person

class Student(Person):
    """
    Diese Klasse erb von "Person" alle Metoden und Arttribute.
    Diese können einerseits in anderen Funktionen genutzt werden, aber auch überschrieben werden.
    """
    def __init__(self,
                 first_name:str,
                 last_name:str,
                 year:int):

        super().__init__(first_name, last_name)
        self.year = year

    def greet_other_student(self, name:str):
        self.say_hello(name)

    def say_goodbye(self):
        print(f'After {self.year} years in school, {self.first_name} says goodbye')