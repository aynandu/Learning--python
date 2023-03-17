import unittest
import testmain

class TestMain(unittest.TestCase): 
    #we are inheriting what unittest gives to this class.
    def test_do_stuff(self):
        test_para = 10
        result=testmain.do_stuff(test_para)
        self.assertEqual(result,15)
                                #testing the value
    def test_do_stuff2(self):
        test_para = 'jhgjh'
        result=testmain.do_stuff(test_para)
        self.assertTrue(isinstance(result,ValueError))
                                #testing if add a string and handling error
    def test_do_stuff3(self):
        test_para = None
        result=testmain.do_stuff(test_para)
        self.assertEqual(result,'please enter number')
                                #testing if giving a None type
    def test_do_stuff4(self):
        test_para = ''
        result=testmain.do_stuff(test_para)
        self.assertEqual(result,'please enter number')
                                #testing if giving a empty string
   
unittest.main()