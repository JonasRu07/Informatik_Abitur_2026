from string import ascii_uppercase

from caeser import Ceaser


class Cryptool:
    def __init__(self, alpha:list[str]) -> None:
        self.ceaser = Ceaser(alpha)

        
        
if __name__ == "__main__":
    alphabet = [l for l in ascii_uppercase]
    tool = Cryptool(alphabet)
    
    print(tool.ceaser.encode("ASTERIX IST TOLL", "C"))
    print(tool.ceaser.encode("ASTERIX IST TOLL", 3))
    print(tool.ceaser.decode("DVWHULA LVW WROO", 3))
    