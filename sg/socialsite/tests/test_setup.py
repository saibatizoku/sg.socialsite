# -*- coding: utf-8 -*-
import unittest2 as unittest

from plone.app.testing import TEST_USER_ID
from plone.app.testing import TEST_USER_NAME
from plone.app.testing import login
from plone.app.testing import setRoles
from Products.CMFPlone.utils import getToolByName

from sg.socialsite.testing import INTEGRATION_TESTING

PROJECTNAME = "sg.socialsite"
DEMO_CONTENT_IDS = ['codigo', 'historias', 'preguntas']

class TestInstall(unittest.TestCase):
    """ensure product is properly installed"""

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def test_installed(self):
        qi = getattr(self.portal, 'portal_quickinstaller')
        self.failUnless(qi.isProductInstalled(PROJECTNAME),
                            '%s not installed' % PROJECTNAME)

    def test_demo_content(self):
        for folder_id in DEMO_CONTENT_IDS:
            self.failUnless(folder_id in self.portal.objectIds())

    def test_workflow(self):
        wf_tool = getToolByName(self.portal, 'portal_workflow')
        self.assertEquals(wf_tool.getDefaultChain(), ('one_state_workflow',))


class TestUninstall(unittest.TestCase):
    """ensure product is properly uninstalled"""

    layer = INTEGRATION_TESTING
    
    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        login(self.portal, TEST_USER_NAME)
        self.qi = getattr(self.portal, 'portal_quickinstaller')
        self.qi.uninstallProducts(products=[PROJECTNAME])

    def test_uninstalled(self):
        self.failIf(self.qi.isProductInstalled(PROJECTNAME))


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
