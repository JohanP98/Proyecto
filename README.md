# Proyecto
Aqui se encuentra el proyecto final de la materia Algoritmo y Programación, este proyecto fue mayormente trabajado con Pygame y con Visual Studio Code.

# Pygame
Es una libreria usada para el desarrollo de juegos en segunda dimension 2D con el lenguaje de Python. Pygame se masa en SDL, que es una librería que provee acceso de bajo nivel al audio, teclado, mouse y al hardware gráfico del PC. Es un programa que funciona tanto en MacOS, Windows y Linux. 

El SDL son bibliotecas en lenguaje C para gestión de gráficos 2D (manipulación de las imágenes como objetos de 2D en la ventana), imágenes (ficheros de tipo jpg o png o tif), audio y periféricos a bajo nivel (teclado, ratón).

Para poder realizar un juego en Pygame se deben realizar 3 pasos iniciales:

  <li> Una preparación del entorno: primero, se debe importar Pygame al programa en Python en el entorno virtual, pues es una librería que no forma parte del startup   de Python. Esto lo hacemos con la instrucción: pip install pygame.
  
  <li> Bucle principal de evento-actualización-repintado: nace del contenedor de nuestro videojuego. Allí encontramos el constructor y la función del lanzamiento del videojuego. Este último creará el bucle con funciones como start, mainloop y handleEvent.
    
  <li> Finalización del juego: cuando se finaliza Pygame, es decir, el juego; GameOver.
  </ul>

    Para entender Pygame, hay que tener en cuenta algunos de estos aspectos:
        El esqueleto de un programa se compone de los siguientes componentes:
  <li> Función main() o clase Game(): contenedor del videojuego.
  
  <li> Control de eventos: pygame.event.get(), es decir, lista de eventos a procesar.
    
  <li> Sprites: rectángulos que representan los objetos móviles o fijos del juego. Estos pueden animarse con frames o modificarse gráficamente. También se pueden detectar colisiones entre ellos. 
      
  <li> Sonidos: pygame.mixer.Sound() y play.
      
  <li> Textos: pygame.font.Font(file_path, size) y render.
  </ul>
  
  # Visual Studio Code
  
