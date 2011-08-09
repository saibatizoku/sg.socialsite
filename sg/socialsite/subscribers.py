from five import grok
from zope import event
from zope.app.container.interfaces import IObjectAddedEvent

from Products.ATContentTypes.interfaces.news import IATNewsItem
from cioppino.twothumbs.interfaces import ILoveThumbsDontYou
from sg.questions.question import IQuestion
from sg.pastebin.paste import IPaste


@grok.subscribe(IATNewsItem, IObjectAddedEvent)
def newsThumbs(news, event):
    if not ILoveThumbsDontYou.providedBy(news):
        alsoProvides(news, ILoveThumbsDontYou)
        self.news.reindexObject()

