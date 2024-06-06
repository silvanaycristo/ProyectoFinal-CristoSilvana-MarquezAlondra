# Casos de prueba o escenarios

Este documento detalla los casos de prueba para el paquete `genomic_analysis`, enfocándose en las funcionalidades de `analyze_variants` e `identify_variants`.

## Casos de prueba para analyze_variants

### Caso de prueba 1: Identificación de transiciones y transversiones

- **Descripción**: Verificar que la función `analyze_variants` clasifica correctamente las transiciones y transversiones en una lista de variantes.

- **Entrada**:

  ```python
  variants = [
      ('17', 43041129, 'C', 'G'),
      ('12', 112161652, 'A', 'T'),
      ('1', 1234567, 'A', 'G')
  ]

    'total_variants': 3,
    'transitions': 1,
    'transversions': 2,
    'variant_summary': [
        {'chrom': '17', 'pos': 43041129, 'ref': 'C', 'alt': 'G', 'type': 'Transversion'},
        {'chrom': '12', 'pos': 112161652, 'ref': 'A', 'alt': 'T', 'type': 'Transversion'},
        {'chrom': '1', 'pos': 1234567, 'ref': 'A', 'alt': 'G', 'type': 'Transition'}
    ]
``

## Resultado: La función debe generar el informe con las clasificaciones correctas.


## Caso de prueba 2: No Hay Variantes

- **Descripción:** Verificar que la función analyze_variants maneja correctamente el caso donde no hay variantes en la lista.

- **Entrada**:

```python
variants = []

Salida Esperada:
python

{
    'total_variants': 0,
    'transitions': 0,
    'transversions': 0,
    'variant_summary': []
}
```

## Resultado: La función debe devolver un informe vacío sin errores.


## Casos de prueba para identify_variants

## Caso de prueba 3: Identificación de SNPs

-**Descripción**: Verificar que la función identify_variants identifica correctamente los SNPs entre dos secuencias.

-**Entrada**

```python
sequence = "ACTGACTGACTG"
reference = "ACTGACTAATTG"
```

-**Salida Esperada:**

```python

[(7, 'G', 'A'), (8, 'T', 'T')]

```

## Resultado: La función debe identificar y listar correctamente los SNPs.


## Caso de prueba 4: Secuencias idénticas

-**Descripción**: Verificar que la función identify_variants maneja correctamente el caso donde las secuencias son idénticas.

-**Entrada**:

```python
sequence = "ACTGACTGACTG"
reference = "ACTGACTGACTG"
````

-**Salida esperada**:

```python
[]
```

## Resultado: La función debe devolver una lista vacía indicando que no hay variantes.


## Caso de prueba 5: Identificación de Indels

-**Descripción**:  Verificar que la función identify_variants identifica correctamente los indels entre dos secuencias.

-**Entrada**:

```python
sequence = "ACTGACTGACTGA"
reference = "ACTGACTGACTG-"
```

-**Salida esperada:**

```python
[(12, '-', 'A')]
````

## Resultado: La función debe identificar y listar correctamente los indels.


## Caso de prueba 6: Longitudes diferentes de secuencias

-**Descripción**: Verificar que la función identify_variants maneja correctamente el caso donde las secuencias tienen longitudes diferentes y lanza una excepción.

-**Entrada**:

```python
sequence = "ACTGACTGACTG"
reference = "ACTGACTGACTGA"
```

-**Salida esperada**: La función debe lanzar un ValueError.

## Resultado: La función debe manejar el error y lanzar una excepción.


## Caso de prueba n: Otros casos de prueba

-**Descripción**: Agregar otros casos de prueba según sea necesario para cubrir más escenarios y asegurarse de que todas las funcionalidades sean verificadas adecuadamente.

Este documento detalla los casos de prueba para los módulos principales del paquete genomic_analysis. Asegúrese de ejecutar todas las pruebas para verificar la correcta funcionalidad del paquete.
