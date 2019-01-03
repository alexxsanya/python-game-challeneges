import unittest
import lib

class TestAndelaAssign(unittest.TestCase):
  def setUp(self): 
    
    pass 

  def test_no_dice_value_in_range_of_1_and_6():
    ass = lib.AndelaAssign() 
    self.assertGreater(ass.tossDice(),0,msg="value should be greater 0")
    self.assertLessEqual(ass.tossDice(),7,msg="Out should be < = 7")


if __name__ == "__main__":
    unittest.main()