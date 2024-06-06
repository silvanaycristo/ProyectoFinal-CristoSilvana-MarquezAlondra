import unittest
from genomic_analysis.variant_calling.identify_variants import identify_variants

class TestIdentifyVariants(unittest.TestCase):

    def test_identify_snps(self):
        sequence = "ACTGACTGACTG"
        reference = "ACTGACTAATTG"
        expected_variants = [(7, 'G', 'A'), (8, 'T', 'T')]
        self.assertEqual(identify_variants(sequence, reference), expected_variants)

    def test_identify_no_variants(self):
        sequence = "ACTGACTGACTG"
        reference = "ACTGACTGACTG"
        expected_variants = []
        self.assertEqual(identify_variants(sequence, reference), expected_variants)

    def test_identify_indels(self):
        sequence = "ACTGACTGACTGA"
        reference = "ACTGACTGACTG-"
        expected_variants = [(12, '-', 'A')]
        self.assertEqual(identify_variants(sequence, reference), expected_variants)

    def test_different_length_sequences(self):
        sequence = "ACTGACTGACTG"
        reference = "ACTGACTGACTGA"
        with self.assertRaises(ValueError):
            identify_variants(sequence, reference)

if __name__ == '__main__':
    unittest.main()
