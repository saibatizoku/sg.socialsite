# -*- coding: utf-8 -*-
import unittest2 as unittest
import doctest

from plone.testing import layered

from sg.socialsite.testing import FUNCTIONAL_TESTING
from sg.socialsite.testing import INTEGRATION_TESTING

def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([
        layered(doctest.DocFileSuite('installation.txt',
            optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS),
            layer=FUNCTIONAL_TESTING),
    ])
    return suite
