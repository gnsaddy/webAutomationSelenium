__author__ = 'Aditya'

import unittest
import os

import HtmlTestRunner
from AssignmentSecond import TestCaseFirst, LoadYoutube

direct = os.getcwd()


class MyTestSuite(unittest.TestCase):

    def test_Issue(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(TestCaseFirst.TestOpeningGoogle),
            unittest.defaultTestLoader.loadTestsFromTestCase(LoadYoutube.LaunchFacebook),
        ])

        outfile = open(direct + "./SmokeTest.html", "w")

        HtmlTestRunner.HTMLTestRunner(
            stream=outfile,
            report_title='Test Report',
            descriptions=True
        ).run(smoke_test)


if __name__ == '__main__':
    unittest.main()
