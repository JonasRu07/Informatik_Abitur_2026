from basis_klasse import Person

class Teacher(Person):
    """
    Die "Teacher"-Klasse hat ein privates Attribut, auf welches man von außen nicht darauf zugreifen soll/können soll.
    Die "subjects" sind dieses private Arrtibut. um es als solchen zu kennzeichen wird es mit einem doppelten "_"
    markiert. Es kann innerhalb der Klasse ganz normal aufgerufen werden und verwendet werden
    """
    def __init__(self,
                 first_name:str,
                 last_name:str,
                 subject:str):

        super().__init__(first_name, last_name)
        self.__subject = subject

    def greet_class(self):
        print(f'{self.first_name} {self.last_name} greets the {self.__subject} class')