import unittest
from app.versions.v3.classes.human import Human

class TestHuman(unittest.TestCase):

    def setUp(self):
        self.human = Human()

    def test_validations_with_valid_dna(self):
        self.human._dna = ["ATCG", "TAGC", "CGTA", "GCAT"]
        try:
            self.human._validations()
        except Exception as e:
            self.fail(f"_validations() raised Exception unexpectedly: {e}")

    def test_validations_with_invalid_dna(self):
        self.human._dna = ["ATCG", "TAGC", "CGT", "GCAT"]
        with self.assertRaises(Exception) as context:
            self.human._validations()
        self.assertTrue("DNA must be a square matrix" in str(context.exception))

    def test_is_mutant_with_mutant_dna(self):
        dna = ["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"]
        result = self.human.is_mutant(dna)
        self.assertTrue(result)
        self.assertTrue(self.human._is_mutant)

    def test_is_mutant_with_human_dna(self):
        dna = ["ATGCGA", "CAGTGC", "TTATTT", "AGACGG", "GCGTCA", "TCACTG"]
        result = self.human.is_mutant(dna)
        self.assertFalse(result)
        self.assertFalse(self.human._is_mutant)

if __name__ == '__main__':
    unittest.main()