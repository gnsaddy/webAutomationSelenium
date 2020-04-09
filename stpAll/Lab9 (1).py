import unittest
import Lab6
import Lab7
#two test cases are run together
class Test_Suite(unittest.TestCase):
    def test_main(self):
        self.suite = unittest.TestSuite()
        self.suite.addTests([unittest.TestLoader().loadTestsFromModule(Lab6),
            unittest.TestLoader().loadTestsFromModule(Lab7)])

        runner = unittest.TextTestRunner()
        runner.run(self.suite)

if __name__ == "__main__":
        unittest.main()