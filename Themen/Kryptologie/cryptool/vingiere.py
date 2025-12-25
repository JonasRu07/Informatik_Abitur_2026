from caeser import Ceaser


class SchlueselError(Exception):
    def __init__(self, message:str='') -> None:
        super().__init__(message)

class Vigniere:
    def __init__(self, alphabet:list[str]) -> None:
        self.alpha = alphabet
        
    def encode(self, klartext:str, key:str) -> str:
        geheim_array = []
        groesse_key = len(key)
        for idx, buchstabe in enumerate(klartext):
            if buchstabe in self.alpha:
                geheim_array.append(
                    self.alpha[
                        (self.alpha.index(buchstabe) + self.alpha.index(key[
                            idx%groesse_key
                            ]))%len(self.alpha)
                        ]
                )
            else:
                geheim_array.append(buchstabe)
        return ''.join(geheim_array)
    
    def decode(self, geheimtext:str, key:str) -> str:
        klar_array = []
        gr_key = len(key)
        for idx, buchstabe in enumerate(geheimtext):
            if buchstabe in self.alpha:
                klar_array.append(
                    self.alpha[
                        (self.alpha.index(buchstabe) - self.alpha.index(key[
                            idx%gr_key
                            ]))%len(self.alpha)
                        ]
                )
            else:
                klar_array.append(buchstabe)
        return ''.join(klar_array)