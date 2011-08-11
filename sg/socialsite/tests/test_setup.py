# -*- coding: utf-8 -*-
import unittest2 as unittest

from plone.app.testing import TEST_USER_ID
from plone.app.testing import TEST_USER_NAME
from plone.app.testing import login
from plone.app.testing import setRoles
from Products.CMFPlone.utils import getToolByName

from sg.socialsite.testing import INTEGRATION_TESTING

PROJECTNAME = "sg.socialsite"
JS = (
    '++resource++sg.socialsite.javascripts/onethumb.js',
    )
CSS = (
    '++resource++sg.socialsite.css/onethumb.css',
    )


class TestInstall(unittest.TestCase):
    """ensure product is properly installed"""

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def test_installed(self):
        qi = getattr(self.portal, 'portal_quickinstaller')
        self.failUnless(qi.isProductInstalled(PROJECTNAME),
                            '%s not installed' % PROJECTNAME)

    def test_css(self):
        portal_css = getattr(self.portal, 'portal_css')
        #print '\n'.join(portal_js.getResourceIds())
        for css in CSS:
            self.failUnless(css in portal_css.getResourceIds(),
                            '%s stylesheet not installed' % css)

    def test_javascripts(self):
        portal_js = getattr(self.portal, 'portal_javascripts')
        #print '\n'.join(portal_js.getResourceIds())
        for js in JS:
            self.failUnless(js in portal_js.getResourceIds(),
                            '%s javascript not installed' % js)

    def test_workflow(self):
        wf_tool = getToolByName(self.portal, 'portal_workflow')
        self.failUnless(wf_tool.getDefaultChain(), ('one_state_flow',))


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

    def test_css(self):
        portal_css = getattr(self.portal, 'portal_css')
        #print '\n'.join(portal_js.getResourceIds())
        for css in CSS:
            self.failIf(css in portal_css.getResourceIds(),
                            '%s stylesheet not uninstalled' % css)

    def test_javascripts(self):
        portal_js = getattr(self.portal, 'portal_javascripts')
        for js in JS:
            self.failIf(js in portal_js.getResourceIds(),
                        '%s javascript not uninstalled' % js)


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
