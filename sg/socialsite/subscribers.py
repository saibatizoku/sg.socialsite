from zope import event
from zope.interface import alsoProvides
from zope.app.container.interfaces import IObjectAddedEvent

from Products.ATContentTypes.interfaces.news import IATNewsItem
from cioppino.twothumbs.interfaces import ILoveThumbsDontYou
from cioppino.twothumbs import rate
from sg.questions.question import IQuestion
from sg.pastebin.paste import IPaste


def contextThumbs(context, event):
    if not ILoveThumbsDontYou.providedBy(context):
        alsoProvides(context, ILoveThumbsDontYou)
        rate.setupAnnotations(context)
        context.reindexObject()

