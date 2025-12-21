from typing import Any
from random import shuffle, randint, seed
seed(0)

def linear_suche(array:list[Any], suche:Any) -> None|int:
    """
    suchees the array for the element "suche" and returns the index if 
    the element is found else None

    Args:
        array (list[Any]): list to suche
        suche (Any): item, which shall be found

    Returns:
        None|int: index of suche in array if found else None
    """
    for index, element in enumerate(array):
        if element == suche: return index 
    return None

def erstelle_array(groesse:int) -> list[int,]:
    l = list(range(groesse))
    shuffle(l)
    return l

for i in range(100):
    array = erstelle_array(i+1)
    suche = randint(0, i)
    index = linear_suche(array, suche)
    if index is not None:
        print(f"Gesucht:{suche:3} in {len(array):3}-array. " \
              f"Gefunden am Index:{index:3} Element:{array[index]:3}")
    else:
        print(f"Gesucht:{suche:3} in {len(array):3}-array. " \
              f"Element nicht gefunden")