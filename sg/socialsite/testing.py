# -*- coding: utf-8 -*-

from plone.app.testing import PloneSandboxLayer
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting


class Fixture(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import cioppino.twothumbs
        import sg.pastebin
        import sg.questions
        import sg.socialsite
        self.loadZCML(package=cioppino.twothumbs)
        self.loadZCML(package=sg.pastebin)
        self.loadZCML(package=sg.questions)
        self.loadZCML(package=sg.socialsite)

    def setUpPloneSite(self, portal):
        # Install into Plone site using portal_setup
        self.applyProfile(portal, 'sg.socialsite:default')


FIXTURE = Fixture()
INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,),
    name='sg.socialsite:Integration',
    )
FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FIXTURE,),
    name='sg.socialsite:Functional',
    )
