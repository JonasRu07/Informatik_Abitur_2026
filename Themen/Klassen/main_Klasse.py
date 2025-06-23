from basis_klasse import Person
from erb_klasse import Student
from private_attribute import Teacher

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