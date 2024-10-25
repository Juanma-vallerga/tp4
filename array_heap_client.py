from array_heap_ext import ArrayHeapExt

def crearheap():

    heap = ArrayHeapExt()
    
    heap.add(1, 'A')
    heap.add(2, 'B')
    heap.add(3, 'C')
    heap.add(4, 'D')
    heap.add(5, 'E')
    heap.add(6, 'F')
    heap.add(7, 'G')
    heap.add(8, 'H')
    heap.add(9, 'I')
    heap.add(10, 'J')
    
    print("heap despues de agregar elementos:")
    print(heap)
    
    return heap

def testeo_de_heap():
    
    heap = crearheap()
    print("\n")
    
    print(f"Elemento con menor clave: {min}:", heap.min())
    print("\n")
    
    print("Eliminar nodo con clave 5: ")
    heap.eliminar_por_prioridad(5)
    print(heap)
    print("\n")

    print("Cambiar la clave del nodo con clave 6 a 1: ")
    heap.cambiar_prioridad(6, 1)
    print(heap)
    print("\n")
    
    otroHeap = ArrayHeapExt()
    otroHeap.add(54, 'Z')
    otroHeap.add(23, 'L')
    
    print("Fusionar con otro heap: ")
    heap.fusionar(otroHeap)
    print(heap)
    print("\n")
    
    print("Vaciar heap: ")
    heap.vaciar()
    print(heap)
    
    

if __name__ == "__main__":
    testeo_de_heap()