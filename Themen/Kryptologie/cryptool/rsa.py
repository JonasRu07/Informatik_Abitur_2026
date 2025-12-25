

class RSA:
    def encode(self, klar_text:str, priv_key:tuple[int, int]) -> list[int]:
        return [
            byte**priv_key[0]%priv_key[1] for byte in bytes(klar_text, "utf-8")
        ]
        
    def decode(self, geheim_text:list[int]|bytes, pub_key:tuple[int, int]):
        return ''.join(
            [chr(byte**pub_key[0]%pub_key[1]) for byte in geheim_text]
            )