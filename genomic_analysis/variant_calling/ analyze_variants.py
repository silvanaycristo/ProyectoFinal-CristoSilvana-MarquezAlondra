"""
NAME: analyze_variants.py

VERSION: 1.0

AUTHOR: Alondra Marquez 

DESCRIPTION: Analiza variantes genómicas y genera un informe con estadísticas básicas y clasificaciones de variantes.

CATEGORY: Bioinformática

USAGE:
    % python analyze_variants.py --variants_file variants.txt

ARGUMENTS:
    --variants_file: Archivo que contiene la lista de variantes a analizar (formato: chrom pos ref alt)

METHOD:
    El programa analiza una lista de variantes genómicas y genera un informe que incluye estadísticas básicas y clasificaciones de variantes como transiciones y transversiones.

SEE ALSO:
    Biopython
"""

# ===========================================================================
# =                            imports
# ===========================================================================
import argparse
import csv
from collections import Counter

# ===========================================================================
# =                            Command Line Options
# ===========================================================================
def parse_args():
    parser = argparse.ArgumentParser(description="Analiza variantes genómicas y genera un informe.")
    parser.add_argument("--variants_file", type=str, required=True, help="Archivo que contiene la lista de variantes a analizar.")
    return parser.parse_args()

# ===========================================================================
# =                            functions
# ===========================================================================
def classify_variant(ref, alt):
    """
    Clasifica la variante como transición o transversión.
    """
    transitions = {('A', 'G'), ('G', 'A'), ('C', 'T'), ('T', 'C')}
    if (ref, alt) in transitions:
        return 'Transition'
    else:
        return 'Transversion'

def analyze_variants(variants):
    """
    Analiza una lista de variantes y genera un informe.

    Args:
        variants (list): Lista de variantes a analizar.

    Returns:
        dict: Un informe con estadísticas sobre las variantes.
    """
    report = {
        'total_variants': len(variants),
        'transitions': 0,
        'transversions': 0,
        'variant_summary': []
    }

    for variant in variants:
        chrom, pos, ref, alt = variant
        variant_type = classify_variant(ref, alt)
        report['variant_summary'].append({
            'chrom': chrom,
            'pos': pos,
            'ref': ref,
            'alt': alt,
            'type': variant_type
        })
        if variant_type == 'Transition':
            report['transitions'] += 1
        else:
            report['transversions'] += 1
    
    return report

def print_report(report):
    """
    Imprime el informe de variantes.

    Args:
        report (dict): El informe generado por analyze_variants.
    """
    print("Variant Analysis Report")
    print("=======================")
    print(f"Total Variants: {report['total_variants']}")
    print(f"Transitions: {report['transitions']}")
    print(f"Transversions: {report['transversions']}")
    print("\nVariant Details:")
    for variant in report['variant_summary']:
        print(f"Chromosome: {variant['chrom']}, Position: {variant['pos']}, Ref: {variant['ref']}, Alt: {variant['alt']}, Type: {variant['type']}")

# ===========================================================================
# =                            main
# ===========================================================================
def main():
    # step 1. Parse arguments
    args = parse_args()

    # step 2. Read variants from file
    variants = []
    try:
        with open(args.variants_file, 'r') as var_file:
            reader = csv.reader(var_file, delimiter='\t')
            header = next(reader)  # Leer la fila de encabezado y omitirla
            for row in reader:
                chrom = row[0]
                pos = int(row[1])
                ref = row[2]
                alt = row[3]
                variants.append((chrom, pos, ref, alt))
    except Exception as e:
        print(f"Error reading variants file: {e}")
        return

    # step 3. Analyze variants and generate report
    report = analyze_variants(variants)

    # step 4. Print the report
    print_report(report)

if __name__ == "__main__":
    main()
    