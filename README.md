# Biblioteca de Libros en Python

## Descripción
Este proyecto implementa una sencilla biblioteca en Python para gestionar un catálogo de libros. La clase `Libro` representa un libro individual con atributos como título, autor, año de publicación y estado de préstamo. La clase `Biblioteca` gestiona una colección de libros, permitiendo agregar nuevos libros, buscar libros específicos y prestar/devolver libros.

## Características
* **Gestión de libros:** Permite agregar, buscar y mostrar los libros de la biblioteca.
* **Estado de préstamo:** Cada libro puede estar prestado o disponible.
* **Operaciones de préstamo y devolución:** Se pueden prestar y devolver libros, verificando su estado actual.

## Tecnologías utilizadas
* **Python:** Lenguaje de programación utilizado para implementar el proyecto.
* **POO:** Se utiliza la programación orientada a objetos para modelar los conceptos de libro y biblioteca.

## Funcionamiento
1. **Creación de objetos:** Se crean objetos de la clase `Libro` para representar libros individuales.
2. **Creación de una biblioteca:** Se crea un objeto de la clase `Biblioteca` para representar la biblioteca.
3. **Adición de libros:** Los objetos `Libro` se añaden a la lista de libros de la biblioteca.
4. **Búsqueda de libros:** Se puede buscar un libro por su título.
5. **Préstamo y devolución:** Se pueden prestar y devolver libros, actualizando su estado.

## Ejemplo de uso
biblioteca.mostrar_libros()  # Muestra todos los libros de la biblioteca

biblioteca.buscar_libro("Las dos torres")  # Busca un libro específico

libro_1.prestar()  # Presta un libro

libro_2.devolver()  # Devuelve un libro
