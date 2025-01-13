class Libro:
    def __init__ (self, titulo, autor, año):
        self.titulo= titulo
        self.autor=autor
        self.año=año
        self.prestado= False
    
    def prestar (self):
        if self.prestado==True:
            print("No se puede prestar, ya estaba prestado")
        else:
            self.prestado = True
            print (f"Se procede a prestar el libro {self.titulo}")
        
    def devolver (self):
        if self.prestado==False:
            print("No se puede devolver, ya estaba devuelto")
        else:
            self.prestado = False
            print(f"Se procede a devolver el libro {self.titulo}")

class Biblioteca:
    def __init__(self):
        self.nombre= "Biblioteca pública de Oliva"
        self.libros= list ()
    
    def agregar_libros (self, titulo):
        self.libros.append(titulo)
    
    def mostrar_libros(self):
        for libro in self.libros:
            print(libro.titulo)
    
    def buscar_libro(self, titulo):
        for libro in self.libros:
            libro_encontrado=False
            if titulo==libro.titulo:
                libro_encontrado=True
                break
            else:
                libro_encontrado=False
        print ("El libro se ha encontrado" if libro_encontrado else "El libro no se ha encontrado")

libro_1= Libro("La comunidad del anillo","Tolkien", 1990)
libro_2= Libro("Las dos torres", "Tolkien", 1991)
libro_3= Libro("El retorno del rey", "Tolkien", 1992)

biblioteca= Biblioteca()

biblioteca.agregar_libros(libro_1)
biblioteca.agregar_libros(libro_2)
biblioteca.agregar_libros(libro_3)

# for i in biblioteca.libros:
#     libro=biblioteca.libros
#     for j in libro:
#         print (i,j)
# print(biblioteca.libros)

biblioteca.mostrar_libros()

biblioteca.buscar_libro("Las dos torres")
biblioteca.buscar_libro("El alquimista")

libro_1.prestar()
libro_2.devolver()
libro_1.devolver()



