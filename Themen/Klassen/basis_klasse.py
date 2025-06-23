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