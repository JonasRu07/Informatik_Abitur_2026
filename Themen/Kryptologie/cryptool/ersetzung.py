
class SchlueselError(Exception):
    def __init__(self, message:str='') -> None:
        super().__init__(message)


class Ersetzung:
    def __init__(self,
                 alphabet:list[str]) -> None:
        self.alpha = alphabet
        self.groesse = len(alphabet)
        
    def encode(self,
               klar_text:str,
               key:list[str]):
        if len(key) != self.groesse:
            raise SchlueselError(
                f"Schluesselgroesse ({len(key)}) passt nicht zum Alphabet {self.groesse}"
                )
        
        for buchstabe in self.alpha:
            if not buchstabe in key:
                raise SchlueselError(
                    f"Buchstabe {buchstabe} nicht im Key"
                )
        
        geheim_text = ""
        for buchstabe in klar_text:
            if buchstabe in key:
                geheim_text += self.alpha[
                    key.index(buchstabe)
                ]
            else:
                geheim_text += buchstabe
        return geheim_text

    def decode(self,
               geheim_text:str,
               key:list[str]):
        if len(key) != self.groesse:
            raise SchlueselError(
                f"Schluesselgroesse ({len(key)}) passt nicht zum Alphabet {self.groesse}"
                )
        
        for buchstabe in self.alpha:
            if not buchstabe in key:
                raise SchlueselError(
                    f"Buchstabe {buchstabe} nicht im Key"
                )
        
        klar_text = ""
        for buchstabe in geheim_text:
            if buchstabe in key:
                klar_text += key[
                    self.alpha.index(buchstabe)
                ]
            else:
                klar_text += buchstabe
        return klar_text