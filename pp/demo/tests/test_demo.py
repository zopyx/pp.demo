from base import TestCase
from Testing.makerequest import makerequest

class TestDemoContent(TestCase):

    def afterSetUp(self):
        self.setRoles(('Manager',))

    def testCreateDemoContent(self):
        view = self.portal.restrictedTraverse('@@pp-demo-content')
        view()

def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestDemoContent))
    return suite
