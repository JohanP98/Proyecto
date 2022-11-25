   # Proyecto
Aqui se encuentra el proyecto final de la materia Algoritmo y ProgramaciónEl proyecto realizado fue un videojuego conocido llamado "Snake". Este proyecto fue mayormente trabajado con Pygame y con Visual Studio Code.

   # Pygame
Es una libreria usada para el desarrollo de juegos en segunda dimension 2D con el lenguaje de Python. Pygame se masa en SDL, que es una librería que provee acceso de bajo nivel al audio, teclado, mouse y al hardware gráfico del PC. Es un programa que funciona tanto en MacOS, Windows y Linux. 

El SDL son bibliotecas en lenguaje C para gestión de gráficos 2D (manipulación de las imágenes como objetos de 2D en la ventana), imágenes (ficheros de tipo jpg o png o tif), audio y periféricos a bajo nivel (teclado, ratón).

Para poder realizar un juego en Pygame se deben realizar 3 pasos iniciales:

  <li> Una preparación del entorno: primero, se debe importar Pygame al programa en Python en el entorno virtual, pues es una librería que no forma parte del startup de Python. Esto lo hacemos con la instrucción: pip install pygame.
  
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
  
  # Numpy
  Es una biblioteca para el lenguaje de programación Python que da soporte para crear vectores y matrices grandes multidimensionales, junto con una gran colección de funciones matemáticas de alto nivel para operar con ellas, diccionarios y listas. Entre otras cosas tambien ofrece una ayuda para manejar los datos mucho mas rapido. 
  
  Para poder usar algun tipo de comando de esta libreria primero hay que poner al principio del codigo el 'import numpy as np'.
 
  # Visual Studio Code
  Visual Studio Code (VS Code) es un editor de código fuente desarrollado por Microsoft. Es software libre y multiplataforma, está disponible para Windows, GNU/Linux y macOS. VS Code tiene una buena integración con Git, cuenta con soporte para depuración de código, y dispone de un sinnúmero de extensiones, que básicamente te da la posibilidad de escribir y ejecutar código en cualquier lenguaje de programación.
  
  Según una encuesta realizada por Stack Overflow a más de 80,000 desarrolladores en mayo del 2021, Visual Studio Code es el entorno de desarrollo más usado y con mucha diferencia, un 71.06%. 
  
  Algunas de sus caracteristicas son:
  <li> Como se menciona anteriormente, es multiplataforma, lo que en pocas palabras significa que esta disponible para Windows, Linux y MacOS.
  
  <li>  Otra característica es que es IntelliSense, esta característica está relacionada con la edición de código, autocompletado y resaltado de sintaxis, lo que permite ser más ágil a la hora de escribir código. Como su nombre lo indica, proporciona sugerencias de código y terminaciones inteligentes en base a los tipos de variables, funciones, etc. Con la ayuda de extensiones se puede personalizar y conseguir un IntelliSense más completo para cualquier lenguaje.
    
  <li> Depuración: Visual Studio Code incluye la función de depuración que ayuda a detectar errores en el código. De esta manera, nos evitamos tener que revisar línea por línea a puro ojo humano para encontrar errores. VS Code también es capaz de detectar pequeños errores de forma automática antes de ejecutar el código o la depuración como tal.
    
  <li> Uso del control de versiones: Visual Studio Code tiene compatibilidad con Git, por lo que puedes revisar diferencias o lo que conocemos con git diff, organizar archivos, realizar commits desde el editor, y hacer push y pull desde cualquier servicio de gestión de código fuente (SMC). Los demás SMC están disponible por medio de extensiones.
  <li> Extensiones: Hasta ahora, se ha mencionado varias veces el término extensiones porque es uno de los puntos fuertes. Visual Studio Code es un editor potente y en gran parte por las extensiones. Las extensiones nos permiten personalizar y agregar funcionalidad adicional de forma modular y aislada. Realmente las extensiones permiten tener una mejor experiencia, y lo más importante, no afectan en el rendimiento del editor, ya que se ejecutan en procesos independientes.
  </ul> 
  
  # Mas allá del proyecto
  
En este trabajo quisimos hacer un juego basico, de lo mas conocidos que es snake pero con cambios como los de la propia serpiente y los puntos que esta tiene que agarrar para crecer. Entre las cosas que utilizamos esta lo aprendido en el curso que seria las lista y funciones. 

Ademas de esto hicimos uso de la implementación de imagenes con ayuda de comandos de pygame. Estas imagenes se encuentran en una carpeta con el nombre 'demas' dentro de la carpeta 'Proyecto'. 

Para realizar este trabajo, tomamos como guia listas de reproducciones de youtube acerca del manejo de pygame y sus elementos.

Intentamos implementar un cambio a la manera clasica de jugar este videojuego el cual trataba de que, la serpiente, en vez de tener que agarrar los puntos para crecer tuviera que dispararle a estos para no morir al tocarlos y a la vez aumentar su tamaño pero no se logró, dentro del codigo principal del juego se encuentra las lineas de codigo para intentar realizar este cambio, estas lineas no afectan en nada al juego principal, entonces estan como evidencia del intento.
