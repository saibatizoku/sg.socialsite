from plone.indexer.decorator import indexer
from zope.annotation.interfaces import IAnnotations
from cioppino.twothumbs.interfaces import ILoveThumbsDontYou
from cioppino.twothumbs import rate


@indexer(ILoveThumbsDontYou)
def total_ratings(object, **kw):
    tally = rate.getTally(object)
    return int(tally['ups']) - int(tally['downs'])
