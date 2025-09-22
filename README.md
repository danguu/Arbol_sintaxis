# Arbol_sintaxis

# Analizador Sintáctico en Python

Este proyecto implementa un **analizador léxico y sintáctico** sencillo en Python que permite:

1. Leer una **gramática** definida en un archivo (`gra.txt`).
2. Recibir una **cadena de prueba** (ejem.txt).
3. Generar e imprimir el **árbol de sintaxis** correspondiente a la cadena.
4. Guardar el árbol en una imagen (`arbol_sintactico.png`).

## Archivos del proyecto

* **`main.py`**
  Programa principal. Solicita el archivo de entrada con la expresión a analizar, ejecuta el analizador y genera el árbol de sintaxis.

* **`tree.py`**
  Contiene:

  * Un **tokenizador** manual que divide la cadena en tokens (`num`, `id`, operadores, paréntesis).
  * La clase **`Parser`**, que implementa el análisis sintáctico descendente recursivo con la gramática dada.
  * Funciones para **dibujar el árbol de sintaxis** usando `networkx` y `matplotlib`.

* **`gra.txt`**
  Archivo que contiene la gramática libre de contexto usada:

  ```
  E -> E opsuma T
  E -> T
  T -> T opmul F
  T -> F
  F -> id
  F -> num
  F -> pari E pard
  ```

  Donde:

  * `opsuma` = `+` o `-`
  * `opmul` = `*` o `/`
  * `pari` = `(`
  * `pard` = `)`

* **`ejem.txt`**
  Archivo que contiene la cadena a analizar

  
* **`arbol_sintactico.png`**
  Imagen generada automáticamente con el árbol de sintaxis de la última cadena analizada.

##  Requisitos

Antes de ejecutar, instala las dependencias:

```bash
pip install networkx matplotlib
```

## Ejecución

1. Crea un archivo de entrada (por ejemplo `entrada.txt`) con una expresión, por ejemplo:

   ```
   2+3*(4-5)
   ```

2. Ejecuta el programa:

   ```bash
   python3 main.py
   ```

3. Ingresa el nombre del archivo cuando lo solicite:

   ```
   Dame el archivo: ejem.txt
   ```

4. El programa:

   * Lee la cadena.
   * Muestra si fue aceptada por la gramática.
   * Genera el árbol de sintaxis en `arbol_sintactico.png`.

   <img width="1000" height="700" alt="image" src="https://github.com/user-attachments/assets/a3a9e529-eda5-4a90-bf86-45ce251224af" />


## Ejemplos de pruebas

* `3+5`
* `a*b+c`
* `(2+3)*4`
* `x*(y+7)-z`

Cada una generará un árbol sintáctico con la estructura definida por la gramática.

