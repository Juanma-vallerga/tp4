from data_structures import ArrayHeap
from array_heap_ext_abstract import ArrayHeapExtAbstract
from typing import Any

class ArrayHeapExt(ArrayHeap, ArrayHeapExtAbstract):
    
    def fusionar(self, otro: ArrayHeap) -> None:
        while not otro.is_empty():
            key, value = otro.remove_min()
            self.add(key, value)
        
    def vaciar(self) -> None:
        self._data.clear()
    
    def eliminar_por_prioridad(self, k: Any) -> None:
        for i in range(len(self._data)):
            if self._data[i]._key == k:
                self._swap(i, len(self._data) - 1)
                self._data.pop()
                self._downheap(i)
                break
    
    def cambiar_prioridad(self, k_actual: Any, k_nueva: Any) -> None:
        for i in range(len(self._data)):
            if self._data[i]._key == k_actual:
                self._data[i]._key == k_nueva
                parent = self._parent(i)
                if i > 0 and self._data[i] < self._data[parent]:
                    self._upheap(i)
                else:
                    self._downheap(i)
                break

