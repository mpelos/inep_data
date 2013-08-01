import unittest
from ..enem_parser import EnemParser

class ParseValidData(unittest.TestCase):
    def setUp(self):
        self.parser = EnemParser()
        self.valid_example = "3000000000072011 1713552403SUMARE                                                                                                                                                SP210000000000000000000003350588363552403SUMARE                                                                                                                                                SP3113552403SUMARE                                                                                                                                                SP1111   543.30   542.80   585.00   559.20BCECAABBBECACBDBEBCCEEDEDABBDBDDCBBADBBECDDCAEEAECBCEBBBAACAAECDECAAAECCDCEAEABBDBBBDAABAABDDCACDDDACACCDECAABAABADEAEDBBAADBDBCBACEAEEEAEBEDCAAABEEEBEACBAEBEDADDCEAEDDABACDACDDAED1211171251291DCEACDBECBCAEBACBEAECEDEDAABDBEDBBDDDCABCBDCAEDEBCEAEDBDAACACECDBBCACEDCDCBAEADADBBDDEAABAEEDBDBDDCAEDDDACDEBBECAACDABADBAECCEADDCEBCBACBAEEBAEEECCEEEBCBECEBADCBDBEADCDBDCCCBADCAECCCCDDP   120.00    80.00   100.00   120.00   120.00   540.00132350588363552403SUMARE                                                                                                                                                SP311"
        self.valid_data = self.parser.parse(self.valid_example)

    def test_type(self):
        self.assertEqual(type(self.valid_data), dict)

    def test_school_id(self):
        self.assertEqual(self.valid_data["school_id"], 35058836)

    def test_city_id(self):
        self.assertEqual(self.valid_data["city_id"], 5240)

    def test_state_id(self):
        self.assertEqual(self.valid_data["state_id"], 35)

    def test_city_name(self):
        self.assertEqual(self.valid_data["city"], "SUMARE")

    def test_state_acronym(self):
        self.assertEqual(self.valid_data["state"], "SP")

    def test_nature_science_score(self):
        self.assertEqual(self.valid_data["scores"]["nature_science"], 543)

    def test_human_science_score(self):
        self.assertEqual(self.valid_data["scores"]["human_science"], 542)

    def test_languages_score(self):
        self.assertEqual(self.valid_data["scores"]["languages"], 585)

    def test_mathematics_score(self):
        self.assertEqual(self.valid_data["scores"]["mathematics"], 559)

class ParseInvalidData(unittest.TestCase):
    def setUp(self):
        self.parser = EnemParser()
        self.invalid_example = "3000000000022011 2214125506SAO JOSE DOS PINHAIS                                                                                                                                  PR110000000000000000000011       .      .                                                                                                                                                        ...4125506SAO JOSE DOS PINHAIS                                                                                                                                  PR0000      .        .        .        .                                                                                                                                                                                      1211171251290DCEACDBECBCAEBACBEAECEDEDAABDBEDBBDDDCABCBDCAEDEBCEAEDBDAACACECDBBCACEDCDCBAEADADBBDDEAABAEEDBDBDDCAEDDDACDEBBECAACDABADBAECCEADDCEBCBACBAEEBAEEECCEEEBCBECEBADCBDBEADCDBDCCCBADCAECCCCDDF     0.00     0.00     0.00     0.00     0.00     0.000 .       .      .                                                                                                                                                        ..."
        self.invalid_data = self.parser.parse(self.invalid_example)

    def test_type(self):
        self.assertEqual(type(self.invalid_data), dict)

    def test_school_id(self):
        self.assertEqual(self.invalid_data["school_id"], "")

    def test_city_id(self):
        self.assertEqual(self.invalid_data["city_id"], "")

    def test_state_id(self):
        self.assertEqual(self.invalid_data["state_id"], "")

    def test_city_name(self):
        self.assertEqual(self.invalid_data["city"], "")

    def test_state_acronym(self):
        self.assertEqual(self.invalid_data["state"], "")

    def test_nature_science_score(self):
        self.assertEqual(self.invalid_data["scores"]["nature_science"], "")

    def test_human_science_score(self):
        self.assertEqual(self.invalid_data["scores"]["human_science"], "")

    def test_languages_score(self):
        self.assertEqual(self.invalid_data["scores"]["languages"], "")

    def test_mathematics_score(self):
        self.assertEqual(self.invalid_data["scores"]["mathematics"], "")

if __name__ == '__main__':
    unittest.main()
