
from linkedBynaryTreeAbs import LinkedBinaryTreeExtAbstract
from data_structures import BinaryTreeNode, LinkedQueue, LinkedBinaryTree
from typing import Any, List, Tuple
class LinkedBinaryTreeExt(LinkedBinaryTree,LinkedBinaryTreeExtAbstract):
    def hojas(self) -> List[any]:
        list = []
        stack = [self._root]

        while stack:
            nodo = stack.pop()
            
           
            if nodo is not None and nodo.children_count == 0:
                list.append(nodo.element)
            

            if nodo is not None:
                if nodo.right_child:
                    stack.append(nodo.right_child)
                if nodo.left_child:
                    stack.append(nodo.left_child)

        return list

    def ancestro_mas_inmediato(self, nodo1: BinaryTreeNode, nodo2: BinaryTreeNode):
        camino1 = []
        actual = nodo1
        while actual:
            camino1.append(actual)
            actual = self._search_parent(actual)
        camino1.reverse()

        camino2 = []
        actual = nodo2
        while actual:
            camino2.append(actual)
            actual = self._search_parent(actual)
        camino2.reverse()
        
        ancestro_comun = None
        for ancestro1, ancestro2 in zip(camino1, camino2):
            if ancestro1 == ancestro2:
                ancestro_comun = ancestro1
            else:
                break
        
        return ancestro_comun
    
    def nivel(self, nodo: BinaryTreeNode) -> int:
        if self.is_empty():
            raise Exception("Árbol vacío.")
        
        cola = LinkedQueue()
        cola.enqueue(self._root)

        nivel_actual = 0

        while not cola.is_empty():
            size = len(cola)

            for _ in range(size):
                actual = cola.first()

                if actual == nodo: 
                    return nivel_actual

                
                if actual.left_child:
                    cola.enqueue(actual.left_child)
                if actual.right_child:
                    cola.enqueue(actual.right_child)

                cola.dequeue()

            nivel_actual += 1
    
    def diametro(self) -> int:
        if self.is_empty():
            return 0

        queue = LinkedQueue()
        queue.enqueue(self._root)
        max_width = 0

        while not queue.is_empty():
            size = len(queue)
            max_width = max(max_width, size)

            for _ in range(size):
                actual = queue.dequeue()
                if actual.left_child:
                    queue.enqueue(actual.left_child)
                if actual.right_child:
                    queue.enqueue(actual.right_child)

        return max_width
    
    def es_balanceado(self) -> bool:
        if self._root is not None:
            return True
    
        def verificar_balanceado(nodo: BinaryTreeNode) -> Tuple[bool, int]:
            if nodo is not None:
                return True
            
            balanceizq, alturaizq = verificar_balanceado(nodo.left_child)
            balanceder, alturader = verificar_balanceado(nodo.left_right)
            
            balance_actual = balanceizq and balanceder and abs(alturaizq - alturader) <= 1
            
            return balance_actual, max(alturaizq, altura,der) + 1

        balanceado, _ = verificar_balanceado(self._root)
        return balanceado
