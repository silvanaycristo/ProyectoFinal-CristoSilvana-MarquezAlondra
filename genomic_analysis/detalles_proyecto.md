## Detalles del Proyecto
Descripción del Paquete.

## Fecha: 05/junio/2024

## Participantes:

Silvana Yalú Cristo Martínez (silvanac@lcg.unam.mx)
Alondra Yolotzin Márquez Mendoza (alondram@lcg.unam.mx)

## Descripción del Problema

El problema a resolver es la identificación y análisis de variantes genómicas (SNPs e indels) en secuencias de ADN comparando una secuencia de prueba con una secuencia de referencia. Esto es crucial para estudios genéticos, diagnósticos y terapias personalizadas.

## Especificación de Requisitos

## Requisitos Funcionales

- Identificación de Variantes: El sistema debe identificar y listar las posiciones y tipos de variantes entre dos secuencias de ADN.

- Análisis de Variantes: El sistema debe generar un informe detallado de las variantes, clasificándolas en transiciones y transversiones.

- Manejo de Archivos de Entrada: El sistema debe ser capaz de leer secuencias de ADN desde archivos de texto.

- Manejo de Errores: El sistema debe manejar y reportar adecuadamente los errores como archivos no encontrados, secuencias inválidas, etc.

## Requisitos No Funcionales

- Rendimiento: El sistema debe ser capaz de procesar secuencias de tamaño moderado en un tiempo razonable.
- Usabilidad: El sistema debe ser fácil de usar a través de una interfaz de línea de comandos.
- Portabilidad: El sistema debe ser ejecutable en diferentes plataformas (Windows, Linux, MacOS) con una configuración mínima.
- Documentación: El sistema debe estar bien documentado para facilitar su uso y mantenimiento.

## Análisis y Diseño

## Lógica del Código

El paquete genomic_analysis se divide en varios módulos que gestionan diferentes aspectos del análisis de secuencias de ADN:

- identify_variants.py: Contiene la función identify_variants que compara una secuencia de ADN con una secuencia de referencia para identificar SNPs e indels.

- file_io.py: Contiene funciones para leer y escribir secuencias de ADN desde y hacia archivos de texto.

- identify_variants_script.py: Script de línea de comandos que utiliza identify_variants y file_io para identificar variantes en secuencias de ADN proporcionadas por el usuario.

- analyze_variants.py: Contiene la funcionalidad para generar un informe detallado de las variantes identificadas.

## Formato de los Archivos

## Archivos de Entrada

- sequence.txt: Contiene la secuencia de ADN de prueba.

- reference.txt: Contiene la secuencia de referencia.

## Archivos de Salida

- Informe de Variantes: Lista de variantes identificadas con sus posiciones y tipos (SNP o indel).

## Caso de Uso: Identificación de Variantes Genómicas

         +---------------+
         |    Usuario    |
         +-------+-------+
                 |
                 | 1. Proporciona archivos de entrada (secuencia y referencia)
                 v
         +-------+-------+
         |  identify_variants_script.py  |
         +-------+-------+
                 |
                 | 2. Lee archivos de entrada
                 v
         +-------+-------+
         |  identify_variants  |
         +-------+-------+
                 |
                 | 3. Compara secuencias y detecta variantes
                 v
         +-------+-------+
         |  Generar informe  |
         +-------+-------+
                 |
                 | 4. Muestra el resultado en pantalla
                 v
         +-------+-------+
         |    Usuario    |
         +---------------+


- Actor: Usuario

- Descripción: El usuario proporciona los archivos de secuencia y referencia. El sistema lee estos archivos, compara las secuencias y genera un informe de las variantes encontradas.

## Flujo Principal:

- El usuario proporciona los archivos sequence.txt y reference.txt.
- El sistema lee las secuencias desde los archivos.
- El sistema compara las secuencias y detecta variantes (SNPs e indels).
- El sistema genera un informe de las variantes encontradas.
- El sistema muestra el informe al usuario.

## Flujos Alternativos:

- Si no se proporciona un archivo, el sistema debe mostrar un mensaje de error.
- Si el formato del archivo no es correcto (por ejemplo, contiene caracteres no válidos), el sistema debe imprimir un mensaje de error en pantalla.
