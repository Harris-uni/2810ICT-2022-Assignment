import unittest
# import main
import data

class dataTest(unittest.TestCase):
    def test_import(self):
        self.assertTrue(data.stats.all) # Test a file has been imported correctly

    # def test_infoByTime(self):
    #     self.assertIn("3", data.infoByTime()) # Test info by time loads data

    def test_accidentByHour(self):
        self.assertTrue(data.accidentByHour())


if __name__ == '__main__':
    unittest.main
