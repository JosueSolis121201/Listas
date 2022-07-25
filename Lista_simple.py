class Nodo: #! Creacion de caja (NODO) solo necesita lo que contendra (Se uso para todas las listas)
    def __init__(self, info) -> None:
        self.info=info
        self.siguiente=None

class Lista_simple: #! Formato Lista simple
    def __init__(self) -> None:
        self.inicio = None

    def insertar(self,dato):
        nuevo=Nodo(dato)
        if self.inicio == None:#! condicional si inicialmente la lista SI esta vacia
            self.inicio = nuevo
        else:
            aux = self.inicio #! condicional si  inicialmente la lista NO esta vacia
            while aux.siguiente != None:
                #! aux.siguiente es el siguiente de aux por ende la lista se "recorre"
                aux=aux.siguiente 
            #! "nuevo" es la clase Nodo
            aux.siguiente=nuevo





def main():
    lista=Lista_simple()
    lista.insertar(1)
    lista.insertar(2)
    print()
    

main()
