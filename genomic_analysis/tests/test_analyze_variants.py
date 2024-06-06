#comando para correr python -m unittest tests/test_analyze_variants.py
import unittest
from variant_calling.analyze_variants import classify_variant, analyze_variants 

class TestAnalyzeVariants(unittest.TestCase):

    def test_classify_variant(self):
        self.assertEqual(classify_variant('A', 'G'), 'Transition')
        self.assertEqual(classify_variant('C', 'T'), 'Transition')
        self.assertEqual(classify_variant('A', 'C'), 'Transversion')
        self.assertEqual(classify_variant('G', 'T'), 'Transversion')

    def test_analyze_variants(self):
        variants = [
            ('17', 43041129, 'C', 'G'),
            ('12', 112161652, 'A', 'T'),
            ('1', 1234567, 'A', 'G')
        ]
        expected_report = {
            'total_variants': 3,
            'transitions': 1,
            'transversions': 2,
            'variant_summary': [
                {'chrom': '17', 'pos': 43041129, 'ref': 'C', 'alt': 'G', 'type': 'Transversion'},
                {'chrom': '12', 'pos': 112161652, 'ref': 'A', 'alt': 'T', 'type': 'Transversion'},
                {'chrom': '1', 'pos': 1234567, 'ref': 'A', 'alt': 'G', 'type': 'Transition'}
            ]
        }
        self.assertEqual(analyze_variants(variants), expected_report)

    def test_no_variants(self):
        variants = []
        expected_report = {
            'total_variants': 0,
            'transitions': 0,
            'transversions': 0,
            'variant_summary': []
        }
        self.assertEqual(analyze_variants(variants), expected_report)

    def test_invalid_variant(self):
        variants = [
            ('17', 'invalid_pos', 'C', 'G')
        ]
        with self.assertRaises(ValueError):
            analyze_variants(variants)

if __name__ == '__main__':
    unittest.main()