import random as rnd
rnd.seed(1)


class Person:
    """
    Basis Klasse fuer alle Personen.
    Es hat eine Konstruktionsmethode (__init__), welche beim Erstellen der Klasse gerufen wird.
    Diese Methode nimmt Argumente, welche mit einem "self."-Prefix innerhalb der Klasse gespeichert werden können.
    Diese können dann später in anderen Methoden der Klasse benutzt werden um weitere Bearbeitungen zu ermöglichen.
    """
    def __init__(self,
                 first_name:str,
                 last_name:str):

        self.first_name = first_name
        self.last_name = last_name

    def say_hello(self, to_whom:str):
        print(f'{self.first_name} {self.last_name} says hello to {to_whom}')

    def say_goodbye(self):
        print(f'{self.first_name} {self.last_name} says Goodbye')

class Student(Person):
        """
        Diese Klasse erb von "Person" alle Metoden und Arttribute.
        Diese können einerseits in anderen Funktionen genutzt werden, aber auch überschrieben werden.
        """

        def __init__(self,
                     first_name: str,
                     last_name: str,
                     year: int):
            super().__init__(first_name, last_name)
            self.year = year

        def greet_other_student(self, name: str):
            self.say_hello(name)

        def say_goodbye(self):
            print(f'After {self.year} years in school, {self.first_name} says goodbye')

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

class Dice:
    """
    Klasse die einen Wuerfel darstellt
    """
    def __init__(self):
        self.eyes = rnd.randint(1, 6)

    def throw(self):
        self.eyes = rnd.randint(1, 6)

    def get_eyes(self):
        return self.eyes

class Player:
    """
    Spieler Klasse mit 2 Wuerfeln.
    dice_1 ist dem Spieler als Referenz übergeben, das gheißt, dass dieser außerhalb der Klasse explezit erstellt werden
    um ihn dem Spieler zuzuweisen. Die Referenz is NICHT an einen Spieler gebunden und kann von meheren Spielern
    gleichzeitig referenziert werden. !! ACHTUNG: SEITENEFFEKTE !!
    Der andere Wuerfel (dice_2) hat der Spieler von Anfang an. Dieser ist direkt ihm zugeschrieben und nur über diese
    Klasse einsehbar und benutztbar.
    """
    def __init__(self, dice):
        self.dice_1 = dice
        self.dice_2 = Dice()

        self.total_eyes = self.dice_1.get_eyes() + self.dice_2.get_eyes()

    def throw_dices(self):
        self.dice_1.throw()
        self.dice_2.throw()

        self.total_eyes = self.dice_1.get_eyes() + self.dice_2.get_eyes()



# Person wird mithilfe des Klassennames erstellt
person_1 = Person('Marcel', 'Schuetz')
# Person gruesst Yuzo
person_1.say_hello('Yuzo')

#Student mit name Flinn Fuchs aus der 12 Klasse wird erstellt
student_1 = Student('Flinn', 'Fuchs', 13)
# Flinn gruesst Luca
student_1.greet_other_student('Luca')

# Die "Person" und "Student" Klasse geben unterschiedliche Resultate der gleichen Methode, obwohl "Student" sie von
# "Person" erbt, da sie neu defeniert wird
person_1.say_goodbye()
student_1.say_goodbye()

# Teacher Herr Haag wird erstellt
teacher_1 = Teacher('Patrick', 'Haag', 'math')

# Auf privates Attribut zugreifen
try:
    print(teacher_1.__subject)
except AttributeError:
    print('Kein passendes Attribut für teacher_1.__subject gefunden')

# Die Klasse kann aber auf private Atttribute zugreiffen
teacher_1.greet_class()

# Referenz Beispiel
print('\nRefernzen:')
dice = Dice()

# Erstellung von 2 Spielern mit dem gleichen Refernz-Wuerfel
player_1 = Player(dice)
player_2 = Player(dice)

# Gesamt Augenzahl beider Spieler
print('Gesamt Augenzahl von player_1', player_1.total_eyes)
print('Gesamt Augenzahl von player_2', player_2.total_eyes)

# Seiteneffekt erstellen
# Auch bei "player_2" sollten sich die gesamt Augenzehlen aendern
player_1.throw_dices()

print('Gesamt Augenzahl von player_1', player_1.total_eyes)
print('Gesamt Augenzahl von player_2', player_2.total_eyes)
