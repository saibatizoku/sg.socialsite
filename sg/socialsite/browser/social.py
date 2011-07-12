# -*- coding: utf-8 -*-
# Zope version does not
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class SocialSummaryView(BrowserView):

    # This may be overridden in ZCML
    index = ViewPageTemplateFile("social_summary_view.pt")

    def render(self):
        return self.index()

    def __call__(self):
        return self.render()
