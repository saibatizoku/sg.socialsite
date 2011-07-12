from Products.PloneTestCase import PloneTestCase as ptc
from sg.socialsite.tests.layer import SocialSiteLayer

ptc.setupPloneSite()

class SocialSiteTestCase(ptc.PloneTestCase):
    layer = SocialSiteLayer

class SocialSiteFunctionalTestCase(ptc.FunctionalTestCase):
    layer = SocialSiteLayer
