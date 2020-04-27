import unittest as ut

import HtmlTestRunner

from seleniumTest import loginTest
from seleniumTest import countWidget
import os

direct = os.getcwd()

class Test_Suite(ut.TestCase):
    def test_main(self):
        self.suite = ut.TestSuite()
        self.suite.addTests([
            ut.defaultTestLoader.loadTestsFromTestCase(loginTest.LoginTest),
            ut.defaultTestLoader.loadTestsFromTestCase(countWidget.countWidget),
        ])

        outfile = open(direct + "./SmokeTest.html", "w")

        HtmlTestRunner.HTMLTestRunner(
            stream=outfile,
            report_title='Test Report',
            descriptions=True
        ).run(self.suite)

        runner = ut.TextTestRunner()
        runner.run(self.suite)


if __name__ == "__main__":
    ut.main()
