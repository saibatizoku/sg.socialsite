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

    def getSocialImage(self, item_url, content_type):
        if content_type == u"Code Snippet":
            return u"%s/++resource++code.jpg" % item_url
        if content_type == u"Question":
            return u"%s/++resource++question.jpg" % item_url
        if content_type == u"News Item":
            return u"%s/++resource++comments.jpg" % item_url
