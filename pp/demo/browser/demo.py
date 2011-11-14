#####################################################################
# zopyx.authoring
# (C) 2011, ZOPYX Limited, D-72070 Tuebingen. All rights reserved
#####################################################################

import os
import glob
import lxml.html
from Products.Five.browser import BrowserView

UNICODE_DIR = os.path.join(os.path.dirname(__file__), 'unicode')
UNICODE_DATA_DIR = os.path.join(os.path.dirname(__file__), 'unicode-data')
LL_DIR = os.path.join(os.path.dirname(__file__), 'leitlinie')
LOTSOFCONTENT_DIR = os.path.join(os.path.dirname(__file__), 'lots_of_content')
TUTORIAL_DIR = os.path.join(os.path.dirname(__file__), 'tutorial')
PICTURES_DIR = os.path.join(os.path.dirname(__file__), 'pictures')
TUTORIAL_FILES = (             
'introduction.html',
'lesson1.html',
'lesson2.html',
'lesson3.html',
'lesson4.html',
'lesson5.html',
'lesson6.html',
'lesson7.html',
'lesson8.html',
'lesson9.html',
'lesson10.html',
'lesson12.html',
'lesson13.html',
'lesson15.html')

def createDocument(folder, id, title='', description='', text=''):
    folder.invokeFactory('AuthoringContentPage', id=id)
    doc = folder[id]
    doc.setTitle(title)
    doc.setDescription(description)
    doc.setText(text)
    doc.getField('text').setContentType(doc, 'text/html')
    doc.reindexObject()

def createFolder(folder, id, title='', description=''):

    folder.invokeFactory('AuthoringContentFolder', id=id)
    folder2 = folder[id]
    folder2.setTitle(title)
    folder2.setDescription(description)
    folder2.reindexObject()


class Demo(BrowserView):

    def __call__(self):

        project_id= 'demo-project'
        title = 'Produce & Publishing Demo Authoring Project'

        if project_id in self.context.objectIds():
            self.context.manage_delObjects(project_id)

        self.context.invokeFactory('AuthoringProject', id=project_id, title=title)
        project = self.context[project_id]


    
        #####################################
        # nested folders
        #####################################

        view = project.restrictedTraverse('add-new-authoringproject')
        view('Nested')
        content_folder = project['contents']['nested']
        content_folder.manage_delObjects(content_folder.objectIds())
        createFolder(content_folder, id='section1', title='Section 1', description='Section 1')
        createFolder(content_folder, id='section2', title='Section 2', description='Section 2')
        createFolder(content_folder.section1, id='subsection11', title='Subsection 1.2', description='Subsection 1.1')
        createFolder(content_folder.section1, id='subsection12', title='Subsection 1.2', description='Subsection 1.2')
        createFolder(content_folder.section2, id='subsection21', title='Subsection 2.1', description='Subsection 2.1')
        createFolder(content_folder.section2, id='subsection22', title='Subsection 2.2', description='Subsection 2.2')
        createDocument(content_folder.section1.subsection11,
                       id='One Page', 
                       title='One page', 
                       description='Description for "One page"', text='<h2>Heading 1</h2><h3>Heading 2</h3><h4>Heading 3</h4>')

        #####################################
        # Leitlinie
        #####################################

        view = project.restrictedTraverse('add-new-authoringproject')
        view('Leitlinie')
        content_folder = project['contents']['leitlinie']
        content_folder.manage_delObjects(content_folder.objectIds())
        content_folder.invokeFactory('AuthoringContentPage', id='index.html')
        page = content_folder['index.html']
        page.setText(file(os.path.join(LL_DIR, 'index.html')).read())
        page.getField('text').setContentType(page, 'text/html')
        page.processForm() # trigger subscribers
        for img in glob.glob('%s/*jp*' % LL_DIR):
            base = os.path.basename(img)
            content_folder.invokeFactory('Image', id=base)
            content_folder[base].setImage(file(img, 'rb').read())

        #####################################
        # Pictures
        #####################################

        view = project.restrictedTraverse('add-new-authoringproject')
        view('Pictures')
        content_folder = project['contents']['pictures']
        content_folder.manage_delObjects(content_folder.objectIds())
        content_folder.invokeFactory('AuthoringContentPage', id='index.html')
        page = content_folder['index.html']
        page.setText(file(os.path.join(PICTURES_DIR, 'index.html')).read())
        page.getField('text').setContentType(page, 'text/html')
        page.processForm() # trigger subscribers
        for img in glob.glob('%s/*jp*' % PICTURES_DIR):
            base = os.path.basename(img)
            content_folder.invokeFactory('Image', id=base)
            content_folder[base].setTitle(base)
            content_folder[base].setDescription(base)
            content_folder[base].setImage(file(img, 'rb').read())

        #####################################
        # Unicode
        #####################################

        view = project.restrictedTraverse('add-new-authoringproject')
        view('Unicode')
        content_folder = project['contents']['unicode']
        content_folder.manage_delObjects(content_folder.objectIds())
        for name in glob.glob(UNICODE_DIR + '/*.html'):
            basename = os.path.splitext(os.path.basename(name))[0]
            content_folder.invokeFactory('AuthoringContentPage', id=basename, title=basename)
            page = content_folder[basename]
            page.setText(file(name).read())
            page.getField('text').setContentType(page, 'text/html')
            page.processForm() # trigger subscribers

        #####################################
        # Unicode
        #####################################

        view = project.restrictedTraverse('add-new-authoringproject')
        view('Lots-of-Content')
        content_folder = project['contents']['lots-of-content']
        content_folder.manage_delObjects(content_folder.objectIds())
        for name in glob.glob(LOTSOFCONTENT_DIR + '/*.html'):
            basename = os.path.splitext(os.path.basename(name))[0]
            content_folder.invokeFactory('AuthoringContentPage', id=basename, title=basename)
            page = content_folder[basename]
            page.setText(file(name).read())
            page.getField('text').setContentType(page, 'text/html')
            page.processForm() # trigger subscribers


        #####################################
        # Unicode-Data
        #####################################

        view = project.restrictedTraverse('add-new-authoringproject')
        view('Unicode-Data')
        content_folder = project['contents']['unicode-data']
        content_folder.manage_delObjects(content_folder.objectIds())
        for name in glob.glob(UNICODE_DATA_DIR + '/*.html'):
            basename = os.path.splitext(os.path.basename(name))[0]
            content_folder.invokeFactory('AuthoringContentPage', id=basename, title=basename)
            page = content_folder[basename]
            page.setText(file(name).read())
            page.getField('text').setContentType(page, 'text/html')
            page.processForm() # trigger subscribers

        #####################################
        # Tutorial
        #####################################

        view = project.restrictedTraverse('add-new-authoringproject')
        view('Tutorial')
        content_folder = project['contents']['tutorial']
        content_folder.manage_delObjects(content_folder.objectIds())

        for name in TUTORIAL_FILES:
            fullname = os.path.join(TUTORIAL_DIR, name)
            content_folder.invokeFactory('AuthoringContentPage', id=name)
            page = content_folder[name]
            html = unicode(file(fullname).read(), 'utf-8')
            root = lxml.html.fromstring(html)
            h1_node = root.xpath('//h1')[0]
            page.setTitle(unicode(h1_node.text_content()))
            h1_node.getparent().remove(h1_node)
            page.setText(lxml.html.tostring(root, encoding=unicode))
            page.setContentType('text/html')
            page.getField('text').setContentType(page, 'text/html')
            page.processForm() # trigger subscribers

        names = sorted(os.listdir(TUTORIAL_DIR))
        for name in names:
            basename, ext = os.path.splitext(name)
            if ext in ('.jpg', '.png', '.gif'):
                fullname = os.path.join(TUTORIAL_DIR, name)
                content_folder.invokeFactory('Image', id=name)
                image = content_folder[name]
                image.setImage(file(fullname, 'rb').read())
                image.setTitle(name)
                image.setDescription(name)
                image.reindexObject()

        # inject demo.css styles
        conversions = self.context[project_id].conversions
        for conv in conversions.contentValues():
            conv.setStyles(list(conv.getStyles()) + ['demo.css'])

        self.request.response.redirect(project.absolute_url())

