# -*- coding: utf-8 -*-
from zope.interface import alsoProvides
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from cioppino.twothumbs.browser.like import LikeWidgetView
from cioppino.twothumbs.interfaces import ILoveThumbsDontYou

class TotalLikeWidgetView(LikeWidgetView):
    """ """
    render = ViewPageTemplateFile("thumbs.pt")

    def __init__(self, context, request):
        super(TotalLikeWidgetView, self).__init__(context, request)
        if not ILoveThumbsDontYou.providedBy(self.context):
            alsoProvides(self.context, ILoveThumbsDontYou)
            self.context.reindexObject()
