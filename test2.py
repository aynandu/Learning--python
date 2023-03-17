import unittest
import sampleExcercise

class TestMain(unittest.TestCase): 
    #we are inheriting what unittest gives to this class.
    def test_do_stuff_samevalue(self):
        result=sampleExcercise.find_random_num(5, 5)
        self.assertTrue(result)

    def test_do_stuff_largevalue(self):
        result=sampleExcercise.find_random_num(5, 11)
        self.assertFalse(result)    

    def test_do_stuff_typechange(self):
        result=sampleExcercise.find_random_num(5, "5")
        self.assertFalse(result)

if __name__ =='__main__':
    unittest.main()