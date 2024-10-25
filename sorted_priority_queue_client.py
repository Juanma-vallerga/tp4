from sorted_priority_queue import SortedPriorityQueue

def testeo():
    
    sortedPriority = SortedPriorityQueue()
    
    print(f"La cola esta vacia? {sortedPriority.is_empty()}")
    
    print(f"Tamaño de la cola: {len(sortedPriority)}\n")
    
    sortedPriority.add(5, 'E')
    sortedPriority.add(4, 'D')
    sortedPriority.add(3, 'C')
    sortedPriority.add(2, 'B')
    sortedPriority.add(1, 'A')
    print("Se agregaron los elementos: (5, 'E'), (4, 'D'), (3, 'C'), (2, 'B'), (1, 'A')")
    print(f"tamaño despues de las inserciones: {len(sortedPriority)}")
    print(f"Cola: {str(sortedPriority)}\n")
    
    min = sortedPriority.min()
    print(f"La menor clave es: {min}\n")
    
    remove = sortedPriority.remove_min()
    print(f"Item eliminado: {remove}")
    print(f"Tamaño despues de eliminar item: {len(sortedPriority)}\n")
    print(f"Cola despues de eliminar item: {sortedPriority}\n")
    
    
    min = sortedPriority.min()
    print(f"El menor item es: {min}\n")
    
    
    sortedPriority.remove_min()
    sortedPriority.remove_min()
    sortedPriority.remove_min()
    sortedPriority.remove_min()
    print(f"La cola esta vacia? {sortedPriority.is_empty()}")
    print(f"Tamaño de la cola: {len(sortedPriority)}")
    print(f"Str: '{str(sortedPriority)}'")

if __name__ == "__main__":
    testeo()