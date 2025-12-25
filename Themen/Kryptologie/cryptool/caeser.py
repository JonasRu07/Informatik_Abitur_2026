

class SchlueselError(Exception):
    def __init__(self, message:str='') -> None:
        super().__init__(message)


class Ceaser:
    def __init__(self,
                 alphabet:list[str]) -> None:
        self.alphabet = alphabet
        self.groesse = len(self.alphabet)
        
    def encode(self, klartext:str, key:int|str):
        if isinstance(key, str):
            if len(key) != 1:
                raise SchlueselError(
                    f"Key {key} kann nicht verarbeitet werden. Int | str mit Laenge == 1"
                    )
            try:
                key = self.alphabet.index(key) + 1
            except RecursionError:
                raise SchlueselError("Key nicht im Alphabet")
        
        geheim_text_array = []
        for buchstabe in klartext:
            if buchstabe in self.alphabet:
                geheim_text_array.append(
                    self.alphabet[(self.alphabet.index(buchstabe) + key)%self.groesse]
                )
            else:
                geheim_text_array.append(buchstabe)
        
        return "".join(geheim_text_array)
    
    def decode(self, geheimtext:str, key:int|str):
        if isinstance(key, str):
            if len(key) != 1:
                raise SchlueselError(
                    f"Key {key} kann nicht verarbeitet werden. Int | str mit Laenge == 1"
                    )
            try:
                key = self.alphabet.index(key) + 1
            except RecursionError:
                raise SchlueselError("Key nicht im Alphabet")
        
        klartext_array = []
        for buchstabe in geheimtext:
            if buchstabe in self.alphabet:
                klartext_array.append(
                    self.alphabet[(self.alphabet.index(buchstabe) - key)%self.groesse]
                )
            else:
                klartext_array.append(buchstabe)
        
        return "".join(klartext_array)