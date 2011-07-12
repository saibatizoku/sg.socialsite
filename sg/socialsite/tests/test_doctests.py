import unittest
from Testing import ZopeTestCase as ztc
from sg.socialsite.tests.base import SocialSiteFunctionalTestCase

doc_tests = (
#    'schema_events.txt',
    )
functional_tests = (
    'installation.txt',
    )

def test_suite():
    return unittest.TestSuite(
        [ztc.FunctionalDocFileSuite(
            'tests/%s' % f, package='sg.socialsite',
            test_class=SocialSiteFunctionalTestCase)
            for f in functional_tests] + 
        [ztc.ZopeDocFileSuite(
            'tests/%s' % f, package='sg.socialsite',
            test_class=SocialSiteFunctionalTestCase)
            for f in doc_tests],
        )

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
