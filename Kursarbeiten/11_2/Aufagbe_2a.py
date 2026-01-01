class Item:
    def __init__(self,
                 attacke_mult:int|float,
                 defense_mult:int|float) -> None:
        self.attacke_mult = attacke_mult
        self.defense_mult = defense_mult

class Inventar:
    def __init__(self, items:list[Item]) -> None:
        assert len(items) <= 10
        self.items  = items
        
    def huege_hinzu(self, item:Item) -> bool:
        if len(self.items) <= 9:
            self.items.append(item)
            return True
        return False
    
    def entferne(self, item:Item):
        self.items.remove(item)

class Charakter:
    def __init__(self,
                 name:str,
                 hp:int|float,
                 gold:int|float) -> None:
        self.name = name
        self.hp = hp
        self.gold = gold
        
class Gegner(Charakter):
    def __init__(self, 
                 name:str,
                 hp: int | float,
                 gold: int | float,
                 schaden:int|float,
                 verteidigung:int|float) -> None:
        super().__init__(name, hp, gold)
        self.schaden = schaden
        self.verteidigung = verteidigung
        
    def attacke(self, player:'Player'):
        player.verteidige(self.schaden)
    
    def verteidige(self, schaden:int|float):
        diff = schaden - self.verteidigung
        if diff > 0:
            self.hp -= schaden
        if self.hp <= 0:
            del self
        
class Player(Charakter):
    def __init__(self, 
                 name:str,
                 hp: int | float,
                 gold: int | float,
                 schaden:int|float,
                 verteidigung:int|float,
                inventar:list[Item]) -> None:
        super().__init__(name, hp, gold)
        self.schaden = schaden
        self.verteidigung = verteidigung
        self.inv = Inventar(inventar)
        
    def attacke(self, gegner:'Gegner'):
        mult = 1
        for item in self.inv.items:
            mult += item.attacke_mult
        gegner.verteidige(self.schaden*mult)
    
    def verteidige(self, schaden:int|float):
        mult = 1
        for item in self.inv.items:
            mult += item.defense_mult
        diff = schaden - self.verteidigung*mult
        if diff > 0:
            self.hp -= schaden
        if self.hp <= 0:
            del self

    def kaufen(self, gold:int|float, item:Item):
        if self.gold < gold:
            return
        if self.inv.huege_hinzu(item):
            self.gold -= gold
    
class Haendler(Charakter):
    def __init__(self, 
                name:str,
                hp: int | float,
                gold: int | float,
                inventar:list[Item]) -> None:
        super().__init__(name, hp, gold)
        self.inv = Inventar(inventar)
        
    def verkaufen(self, gold:int|float):
        self.gold += gold
    
