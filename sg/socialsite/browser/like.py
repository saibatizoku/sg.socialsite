# -*- coding: utf-8 -*-
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from cioppino.twothumbs.browser.like import LikeWidgetView


class TotalLikeWidgetView(LikeWidgetView):
    """ """
    render = ViewPageTemplateFile("thumbs.pt")
