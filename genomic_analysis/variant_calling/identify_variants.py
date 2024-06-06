"""
NAME: identify_variants.py

VERSION: 1.0

AUTHOR: Silvana Yalú Cristo Martínez 

DESCRIPTION: 

    Módulo para identificar variantes genómicas (SNPs e indels) comparando secuencias de ADN con una secuencia de referencia.

CATEGORY: Genómica/Bioinformática

USAGE:

    % python identify_variants.py --sequence_file <path_to_sequence_file> --reference_file <path_to_reference_file>

ARGUMENTS:

    --sequence_file (str): Archivo que contiene la secuencia de ADN a analizar.
    --reference_file (str): Archivo que contiene la secuencia de referencia.

METHOD:

    La función identify_variants analiza una secuencia de ADN y la compara con una secuencia de referencia para detectar variaciones (SNPs e indels).

SEE ALSO:

    annotate_variants.py
"""

# ===========================================================================
# =                            imports
# ===========================================================================
import argparse
from Bio import SeqIO

# ===========================================================================
# =                            functions
# ===========================================================================
def identify_variants(sequence, reference):
    """
    Identifica SNPs e indels comparando una secuencia de ADN con una secuencia de referencia.

    Args:
        sequence (str): La secuencia de ADN a analizar.
        reference (str): La secuencia de referencia.

    Returns:
        list: Una lista de variantes encontradas (SNPs e indels).
    """
    # Asegurar que las secuencias tengan la misma longitud
    if len(sequence) != len(reference):
        raise ValueError("Las secuencias deben tener la misma longitud para la comparación.")

    variants = []
    for i in range(len(sequence)):
        if sequence[i] != reference[i]:
            variants.append((i, reference[i], sequence[i]))
    return variants

# ===========================================================================
# =                            main
# ===========================================================================
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Identifica variantes genómicas comparando una secuencia de ADN con una secuencia de referencia.")
    parser.add_argument("--sequence_file", type=str, required=True, help="Archivo que contiene la secuencia de ADN a analizar.")
    parser.add_argument("--reference_file", type=str, required=True, help="Archivo que contiene la secuencia de referencia.")
    args = parser.parse_args()

    # Leer las secuencias desde los archivos
    with open(args.sequence_file, 'r') as seq_file:
        sequence = seq_file.read().strip().upper()

    with open(args.reference_file, 'r') as ref_file:
        reference = ref_file.read().strip().upper()

    try:
        variants = identify_variants(sequence, reference)
        print(f"Variantes encontradas: {variants}")
    except Exception as e:
        print(f"Error: {str(e)}")
