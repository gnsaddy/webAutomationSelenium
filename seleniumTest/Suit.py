import unittest as ut
from seleniumTest import loginTest
from seleniumTest import countWidget


class Test_Suite(ut.TestCase):
    def test_main(self):
        self.suite = ut.TestSuite()
        self.suite.addTests([
            ut.defaultTestLoader.loadTestsFromTestCase(loginTest.LoginTest),
            ut.defaultTestLoader.loadTestsFromTestCase(countWidget.countWidget),
        ])

        runner = ut.TextTestRunner()
        runner.run(self.suite)


if __name__ == "__main__":
    ut.main()
