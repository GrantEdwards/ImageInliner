#!/usr/bin/python3

from markdown.treeprocessors import Treeprocessor
from markdown.extensions import Extension
import sys, os, base64
import requests

class ImageInlinerProcessor(Treeprocessor):
    def __init__(self, md):
        self.md = md

    def getImageData(self,src):
        if '://' in src:
            r = requests.get(src,allow_redirects=True)
            r.raise_for_status()
            return r.content
        else:
            with open(src,'rb') as f:
                return f.read()
        
    def run(self, root):
        for element in root.iter('img'):
            attrib = element.attrib
            tail = element.tail
            element.clear()
            element.tag = 'img'
            src = attrib.pop('src')
            base,ext = os.path.splitext(src)
            imgtype = ext.lstrip('.')
            if imgtype == 'svg':
                imgtype = 'svg+xml'
            imgdata = self.getImageData(src)
            b64str = base64.b64encode(imgdata).decode('ascii')
            attrib['src'] = f"data:image/{imgtype};base64,{b64str}"
            element.tail = tail
            for k, v in attrib.items():
                element.set(k, v)

class ImageInliner(Extension):
    def __init__(self):
        self.config = {}
        super(ImageInliner, self).__init__()

    def extendMarkdown(self, md, config):
        md.treeprocessors.register(ImageInlinerProcessor(md), 'imageinlinerprocessor', 15)

if __name__ == "__main__":
    import markdown
    input = """
    ![a local image](bar.png)
    ![a remote image](http://www.panix.com/~grante/foo.png)
    ![another remote image](https://www.panix.com/~grante/uxcell-1156.jpg)
    ![a remote svg image](https://www.panix.com/~grante/bpdata.svg)
    """
    html = markdown.markdown(input, extensions=[ImageInliner()])
    print(html)

