from zope.interface import alsoProvides

from cioppino.twothumbs.interfaces import ILoveThumbsDontYou
from cioppino.twothumbs import rate


def contextThumbs(context, event):
    if not ILoveThumbsDontYou.providedBy(context):
        alsoProvides(context, ILoveThumbsDontYou)
        rate.setupAnnotations(context)
        context.reindexObject()

