"""
NAME: file_io.py
VERSION: 0.2
AUTHOR: [Tu Nombre]
DESCRIPTION: Funciones para manejar operaciones de entrada/salida de archivos de ADN.
CATEGORY: Genómica, Bioinformática
USAGE:
    % python file_io.py
ARGUMENTS:
    filename (str): El nombre del archivo de ADN.
METHOD:
    Las funciones read_dna_sequence y write_dna_sequence permiten leer y escribir secuencias de ADN en archivos.
SEE ALSO:
    validators.py
"""

# ===========================================================================
# =                            imports
# ===========================================================================

# ===========================================================================
# =                            functions
# ===========================================================================
def read_dna_sequence(filename):
    """
    Lee una secuencia de ADN de un archivo de texto.
    
    Args:
        filename (str): El nombre del archivo del cual leer la secuencia.
        
    Returns:
        str: La secuencia de ADN contenida en el archivo.
        
    Raises:
        FileNotFoundError: Si el archivo especificado no se encuentra.
        ValueError: Si el archivo está vacío o contiene caracteres no válidos.
    """
    with open(filename, 'r') as file:
        sequence = file.read().strip().upper()
    if not sequence:
        raise ValueError("El archivo está vacío.")
    if any(char not in 'ACGT' for char in sequence):
        raise ValueError("La secuencia contiene caracteres no válidos.")
    return sequence

def write_dna_sequence(filename, sequence):
    """
    Escribe una secuencia de ADN en un archivo de texto.
    
    Args:
        filename (str): El nombre del archivo donde se escribirá la secuencia.
        sequence (str): La secuencia de ADN a escribir.
        
    Raises:
        IOError: Si no se puede escribir en el archivo.
    """
    with open(filename, 'w') as file:
        file.write(sequence + '\n')

# ===========================================================================
# =                            main
# ===========================================================================
if __name__ == "__main__":
    # Ejemplo de uso
    test_sequence = "ATCGATCG"
    test_filename = "test_dna.txt"
    
    try:
        write_dna_sequence(test_filename, test_sequence)
        print(f"Secuencia escrita en {test_filename}")
        
        read_sequence = read_dna_sequence(test_filename)
        print(f"Secuencia leída de {test_filename}: {read_sequence}")
    except Exception as e:
        print(f"Error: {str(e)}")

