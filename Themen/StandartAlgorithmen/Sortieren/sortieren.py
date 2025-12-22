from random import shuffle


def selection_sort(array:list[int]):
    """
    Selection Sort
    Der Array wird sortiert. Dabei wird immer das kleinste unsortierte 
    Element nach ans Ende der sortierten Elementen gesetzt.

    Args:
        array (list[int]): Liste mit zu sortierenden Zahlen.

    Returns:
        None : Sortiervorgang finded "in place" statt.
    """
    for i in range(len(array)):
        # Setzen von Maximalwerten
        min = float("inf")
        min_idx = 0
        # Herausfinden vom kleinsten Wert
        for idx_wert, wert in enumerate(array[i:]):
            if wert < min:
                min = wert
                min_idx = idx_wert + i
        # Wechseln der Grenze mit dem kleinsten Wert
        array[i], array[min_idx] = array[min_idx], array[i]
        
for i in range(0,5000, 100):
    array = list(range(i))
    array_unsorted = array.copy()
    shuffle(array_unsorted)
    selection_sort(array_unsorted)
    if array_unsorted == array:
        print(f"{i:3} Iteration hat funktioniert")
    
    