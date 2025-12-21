from random import shuffle, randint, seed
seed(0)

def binaere_suche(array:list[int], suche:int) -> None|int:
    """
    Durchsucht den Array nach dem Element "suche".
    Array **muss** nach der Groesse nach (<) sortiert sein.

    Args:
        array (list[Any]): Zu durchsuchende Liste.
        suche (Any): Element, welches durchsucht wird.

    Returns:
        None|int: index des gesuchten Element, falls im Array ansonsten
            None
    """
    linke_grenze = 0
    rechte_grenze = len(array)
    while True:
        # Linke Grenze ist rechts der rechten
        if linke_grenze > rechte_grenze :
            return None
        pivot = int((linke_grenze + rechte_grenze)/2)
        if array[pivot] == suche:
            return pivot
        elif array[pivot] < suche:
            linke_grenze = pivot + 1
        else:
            rechte_grenze = pivot - 1

def erstelle_array(groesse:int) -> list[int,]:
    return list(range(groesse))


for i in range(100):
    array = erstelle_array(i+1)
    suche = randint(0, i)
    index = binaere_suche(array, suche)
    if index is not None:
        print(f"Gesucht:{suche:3} in {len(array):3}-array. " \
              f"Gefunden am Index:{index:3} Element:{array[index]:3}")
    else:
        print(f"Gesucht:{suche:3} in {len(array):3}-array. " \
              f"Element nicht gefunden")