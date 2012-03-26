# -*- coding: utf-8 -*-
from Products.ATContentTypes.lib import constraintypes
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.utils import _createObjectByType

TO_REMOVE = ['news', 'events']
TO_EXCLUDE_FROM_NAV = ['front-page', 'Members',]


class SocialSiteSetupHandler:
    def setupDemoContent(self, portal):
        existing = portal.objectIds()
        for doc in TO_REMOVE:
            if doc in existing:
                del portal[doc]
        for doc in TO_EXCLUDE_FROM_NAV:
            if doc in existing:
                docobj = portal[doc]
                docobj.setExcludeFromNav(True)
                docobj.reindexObject()
        if 'codigo' not in existing:
            _createObjectByType('Folder', portal, id='codigo', title=u"Código",
                description=u"Sección de código fuente")
        codigo = portal['codigo']
        codigo.setConstrainTypesMode(constraintypes.ENABLED)
        codigo.setLocallyAllowedTypes(['sg.pastebin.paste'])
        codigo.setImmediatelyAddableTypes(['sg.pastebin.paste'])
        codigo.reindexObject()
        if 'historias' not in existing:
            _createObjectByType('Folder', portal, id='historias', title=u"Historias",
                description=u"Sección de historias de los usuarios")
        historias = portal['historias']
        historias.setConstrainTypesMode(constraintypes.ENABLED)
        historias.setLocallyAllowedTypes(['News Item', 'Link'])
        historias.setImmediatelyAddableTypes(['News Item', 'Link'])
        historias.reindexObject()
        if 'preguntas' not in existing:
            _createObjectByType('Folder', portal, id='preguntas', title=u"Preguntas",
                description=u"Sección de preguntas")
        preguntas = portal['preguntas']
        preguntas.setConstrainTypesMode(constraintypes.ENABLED)
        preguntas.setLocallyAllowedTypes(['sg.questions.question'])
        preguntas.setImmediatelyAddableTypes(['sg.questions.question'])
        preguntas.reindexObject()

    def setupWorkflow(self, portal):
        wf_tool = getToolByName(portal, 'portal_workflow')
        wf_tool.setDefaultChain('one_state_workflow')


def importVarious(context):
    """Miscellanous steps import handle
    # Ordinarily, GenericSetup handlers check for the existence of XML files.
    # Here, we are not parsing an XML file, but we use this text file as a 
    # flag to check that we actually meant for this import step to be run.
    # The file is found in profiles/default.
    """
    if context.readDataFile('socialsite_various.txt') is None:
        return
    portal = context.getSite()
    handler = SocialSiteSetupHandler()
    handler.setupDemoContent(portal)
    handler.setupWorkflow(portal)
