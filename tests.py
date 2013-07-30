import unittest
from enem_parser import EnemParser

class EnemParserTest(unittest.TestCase):
    def setUp(self):
        self.parser = EnemParser()
        self.valid_example = "3000000000072011 1713552403SUMARE                                                                                                                                                SP210000000000000000000003350588363552403SUMARE                                                                                                                                                SP3113552403SUMARE                                                                                                                                                SP1111   543.30   542.80   585.00   559.20BCECAABBBECACBDBEBCCEEDEDABBDBDDCBBADBBECDDCAEEAECBCEBBBAACAAECDECAAAECCDCEAEABBDBBBDAABAABDDCACDDDACACCDECAABAABADEAEDBBAADBDBCBACEAEEEAEBEDCAAABEEEBEACBAEBEDADDCEAEDDABACDACDDAED1211171251291DCEACDBECBCAEBACBEAECEDEDAABDBEDBBDDDCABCBDCAEDEBCEAEDBDAACACECDBBCACEDCDCBAEADADBBDDEAABAEEDBDBDDCAEDDDACDEBBECAACDABADBAECCEADDCEBCBACBAEEBAEEECCEEEBCBECEBADCBDBEADCDBDCCCBADCAECCCCDDP   120.00    80.00   100.00   120.00   120.00   540.00132350588363552403SUMARE                                                                                                                                                SP311"
        self.invalid_example = "3000000000022011 2214125506SAO JOSE DOS PINHAIS                                                                                                                                  PR110000000000000000000011       .      .                                                                                                                                                        ...4125506SAO JOSE DOS PINHAIS                                                                                                                                  PR0000      .        .        .        .                                                                                                                                                                                      1211171251290DCEACDBECBCAEBACBEAECEDEDAABDBEDBBDDDCABCBDCAEDEBCEAEDBDAACACECDBBCACEDCDCBAEADADBBDDEAABAEEDBDBDDCAEDDDACDEBBECAACDABADBAECCEADDCEBCBACBAEEBAEEECCEEEBCBECEBADCBDBEADCDBDCCCBADCAECCCCDDF     0.00     0.00     0.00     0.00     0.00     0.000 .       .      .                                                                                                                                                        ..."


    def test_parse(self):
        valid_data = self.parser.parse(self.valid_example)
        invalid_data = self.parser.parse(self.invalid_example)

        # should return an dictionary
        self.assertEqual(type(valid_data), dict)

        # when the data is valid
        self.assertEqual(valid_data["school_id"], 35058836)
        self.assertEqual(valid_data["city_id"], 5240)
        self.assertEqual(valid_data["state_id"], 35)
        self.assertEqual(valid_data["city"], "SUMARE")
        self.assertEqual(valid_data["state"], "SP")
        self.assertEqual(valid_data["scores"]["nature_science"], 543)
        self.assertEqual(valid_data["scores"]["human_science"], 542)
        self.assertEqual(valid_data["scores"]["languages"], 585)
        self.assertEqual(valid_data["scores"]["mathematics"], 559)

        # when the data is invalid
        self.assertFalse(invalid_data["school_id"])
        self.assertFalse(invalid_data["city_id"])
        self.assertFalse(invalid_data["state_id"])
        self.assertFalse(invalid_data["city"])
        self.assertFalse(invalid_data["state"])
        self.assertFalse(invalid_data["scores"]["nature_science"])
        self.assertFalse(invalid_data["scores"]["human_science"])
        self.assertFalse(invalid_data["scores"]["languages"])
        self.assertFalse(invalid_data["scores"]["mathematics"])

if __name__ == '__main__':
    unittest.main()
