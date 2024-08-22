import unittest
import Testing_units

class testing(unittest.TestCase):
    
    def Test_1(self):
        text="python"
        result=Testing_units.working(text)
        self.assertEqual(result,"Python")
    
    def test2(self):
        text2="monty world"
        result=Testing_units.working(text2)
        self.assertEqual(result,"Monty World")
    
if __name__=='__main__':
    unittest.main()