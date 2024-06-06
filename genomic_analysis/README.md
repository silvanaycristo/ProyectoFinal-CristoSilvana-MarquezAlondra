# genomic_analysis

## Descripción del paquete

`genomic_analysis` es un paquete de bioinformática diseñado para analizar secuencias de ADN y identificar variantes genómicas (SNPs e indels). El paquete incluye funcionalidades para comparar secuencias de ADN con una secuencia de referencia y generar informes detallados de las variantes encontradas.

## Uso

El paquete ofrece varias herramientas para el análisis de secuencias de ADN. A continuación se detallan las principales funcionalidades:

### Identificar variantes

Para identificar variantes genómicas comparando una secuencia de ADN con una secuencia de referencia:

```bash
python -m genomic_analysis.scripts.identify_variants_script --sequence_file <path_to_sequence_file> --reference_file <path_to_reference_file>
```

### Análisis de variantes

Para analizar las variantes y generar un informe detallado:

```bash
python -m genomic_analysis.variant_calling.analyze_variants --variants_file <path_to_variants_file>
```

### Salida

El paquete genera la siguiente salida:

- identify_variants_script: Imprime una lista de variantes encontradas (SNPs e indels) con sus posiciones y nucleótidos de referencia y alternativos.

- analyze_variants: Genera un informe detallado de las variantes, incluyendo el número total de variantes, transiciones y transversiones.

### Control de errores

El paquete maneja diversos errores para asegurar un uso correcto:

- Verificacion de que las secuencias de entrada tienen la misma longitud.
- Validación de que las secuencias de ADN contienen solo caracteres válidos (A, C, G, T).
- Manejo de archivos no encontrados y archivos vacíos.

### Pruebas

Las pruebas unitarias están incluidas en el directorio tests. Para ejecutar las pruebas, use el siguiente comando:

```bash 
python -m unittest discover -s genomic_analysis/tests
```
Las pruebas verifican la correcta identificación de variantes, manejo de errores y otras funcionalidades del paquete.

### Datos

Los archivos de datos de prueba deben estar en formato de texto simple, conteniendo secuencias de ADN. Ejemplos de archivos de entrada:

- reference.txt: ATGCGTGC
- sequence.txt: ATGCATGC

### Metadatos y documentación

Este README ofrece información de uso básico. 

### Código fuente

El código fuente está disponible en este repositorio. Se acoge con satisfacción cualquier contribución o sugerencia a través de solicitudes pull request.

### Términos de uso

Este paquete está disponible bajo la licencia Apache 2.0. Consulte el archivo LICENSE para obtener más detalles.

### Contáctenos

Si tiene problemas o preguntas, por favor abra un problema en este repositorio o póngase en contacto con nosotras en: [Silvana Yalú Cristo Martínez (silvanac@lcg.unam.mx) o Alondra Yolotzin Márquez Mendoza (alondram@lcg.unam.mx)]
