from random import shuffle, seed
seed(0)

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
        
def insertion_sort(array:list[int]):
    """
    Insertion Sort
    Der Array wird sortiert. Dabei wird immer das erste unsortierte 
    Element in einen bereits sortierten Teilbereich einsortiert.

    Args:
        array (list[int]): Liste mit zu sortierenden Zahlen.

    Returns:
        list[int]: Sortierte Liste
    """
    for i in range(len(array)):
        for j in range(i):
            if array[i] < array[j]:
                array = array[:j] + [array[i]] + array[j:i] + array[i+1:]
    return array

def bubble_sort(array:list[int]):
    """
    Bubble Sort
    Der Array wird sortiert. Dabei wird immer zwei Elemente miteinander 
    verglichen und sortiert. So "wandern" die groessten Werte nach rechts 
    und kleine nach links.

    Args:
        array (list[int]): Liste mit zu sortierenden Zahlen.

    Returns:
        None : Sortiervorgang finded "in place" statt.
    """
    for i in range(len(array)):
        # Subtraktion von i, da immer i-Elemente hinten schon sortiert sind
        for j in range(0, len(array)-i-1):
            if array[j] > array[j+1]:
                array[j+1], array[j] = array[j],array[j+1]
                
def quick_sort(array:list[int]):
    """
    Quick Sort.
    Es wird ein Pivot Element ausgesucht. Alle anderen werden nun in zwei
    Listen einsortiert, jenachdem ob sie groesser oder kleiner sind als 
    das Pivotelement.
    Diese Listen werden dann rekursiv sortiert.
    
    Args:
        array (list[int]): Liste mit zu sortierenden Zahlen.

    Returns:
        list[int]: Sortierte Liste
    """
    if len(array) <= 1:
        return array
    pivot = array[int(len(array)/2)]
    
    links = []
    pivots = []
    rechts = []
    for wert in array:
        if wert < pivot:
            links.append(wert)
        elif wert == pivot:
            pivots.append(wert)
        else:
            rechts.append(wert)
    return quick_sort(links) + pivots + quick_sort(rechts)
        

# Demo
for i in range(100,5100, 100):
    array = list(range(i))
    array_unsorted = array.copy()
    shuffle(array_unsorted)
    # selection_sort(array_unsorted)
    # array_unsorted = insertion_sort(array_unsorted)
    # bubble_sort(array_unsorted)
    array_unsorted = quick_sort(array_unsorted)
        
    if array_unsorted == array:
        print(f"{i:3} Iteration hat funktioniert")
    
    