from random import shuffle, seed, choice
from string import ascii_uppercase

from caeser import Ceaser
from ersetzung import Ersetzung

seed(0)

class Cryptool:
    def __init__(self, alpha:list[str]) -> None:
        self.ceaser = Ceaser(alpha)
        self.ersetzung = Ersetzung(alpha)
        
        
if __name__ == "__main__":
    alphabet = [l for l in ascii_uppercase]
    schluessel = alphabet.copy()
    shuffle(schluessel)
    rnd = ''.join(choice(ascii_uppercase) for _ in range(256))
    tool = Cryptool(alphabet)
    
    print(tool.ceaser.encode("ASTERIX IST TOLL", "C"))
    print(tool.ceaser.encode("ASTERIX IST TOLL", 3))
    print(tool.ceaser.decode("DVWHULA LVW WROO", 3))
    print(tool.ceaser.encode(tool.ceaser.decode(rnd, 3), "C") == rnd)
    print()
    print(tool.ersetzung.encode("ASTERIX IST TOLL", schluessel))
    print(tool.ersetzung.decode("BDQKOVC VDQ QAPP", schluessel))
    print(tool.ersetzung.encode(tool.ersetzung.decode(rnd, schluessel), schluessel) == rnd)
    