from Products.Archetypes import atapi
from Products.ATContentTypes.interface import IATNewsItem
from archetypes.schemaextender.field import ExtensionField
from archetypes.schemaextender.interfaces import ISchemaExtender
from zope.component import adapts
from zope.interface import implements


class URLListExtender(ExtensionField, atapi.LinesField):
    pass


class NewsExtender(object):
    adapts(IATNewsItem)
    implements(ISchemaExtender)

    fields = [URLListExtender("shared_urls",
        widget = atapi.LinesWidget(
            label=u"Related websites")),
        ]

    def __init__(self, context):
        self.context = context


    def getFields(self):
        return self.fields
