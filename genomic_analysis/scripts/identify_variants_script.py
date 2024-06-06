"""
NAME: identify_variants_script.py

VERSION: 1.0

AUTHOR: Silvana Yalú Cristo Martínez 

DESCRIPTION: 

    Script para identificar variantes genómicas (SNPs e indels) desde la línea de comandos.

CATEGORY: Genómica/Bioinformática

USAGE:

    % python identify_variants_script.py --sequence_file <path_to_sequence_file> --reference_file <path_to_reference_file>

ARGUMENTS:

    --sequence_file (str): Archivo de ADN del cual leer la secuencia.
    --reference_file (str): Archivo de ADN de referencia para comparar.

METHOD:

    El script lee una secuencia de ADN de un archivo y la compara con una secuencia de referencia para identificar variantes.

SEE ALSO:

    identify_variants.py, file_io.py
"""

# ===========================================================================
# =                            imports
# ===========================================================================
import argparse
from genomic_analysis.utils.file_io import read_dna_sequence
from genomic_analysis.variant_calling.identify_variants import identify_variants

# ===========================================================================
# =                            Command Line Options
# ===========================================================================
def main():
    parser = argparse.ArgumentParser(description="Identifica variantes genómicas comparando una secuencia de ADN con una secuencia de referencia.")
    parser.add_argument("--sequence_file", type=str, required=True, help="Archivo de ADN del cual leer la secuencia.")
    parser.add_argument("--reference_file", type=str, required=True, help="Archivo de ADN de referencia para comparar.")
    args = parser.parse_args()

    try:
        # step 1. Leer las secuencias desde los archivos
        sequence = read_dna_sequence(args.sequence_file)
        reference = read_dna_sequence(args.reference_file)

        # step 2. Identificar variantes en la secuencia comparada con la referencia
        variants = identify_variants(sequence, reference)
        
        # step 3. Mostrar las variantes encontradas
        print(f"Variantes encontradas: {variants}")
    except Exception as e:
        print(f"Error: {str(e)}")

# ===========================================================================
# =                            main
# ===========================================================================
if __name__ == "__main__":
    main()
