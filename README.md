# ImageInliner
Python Markdown extension to render images inline using 'data:' URLs

This extension was inspired by [Waylan Limberg's](https://github.com/waylan) wiki page [Tutorial Altering Markdown Rendering](https://github.com/Python-Markdown/markdown/wiki/Tutorial-Altering-Markdown-Rendering).

## Description
Sometimes it's useful to create a stand-alone HTML document where all of the images are included in the HTML file instead of being refrences to URLs that must be fetched by the browser when the page is rendered.  This makes the file usable offline, and distributing the document is much simpler since it's self-contained in a single HTML file.

When this extension is enabled, the Python Markdown tree is post-processed before the HTML is rendered, and any "img" elements are converted to using data: URLs.

This will make the HTML file far larger, but that's the price you pay for a self-contained single-file document.

## Usage

Usage goes a little like this:

```Python
import sys, markdown
from ImageInliner import ImageInliner

intext = sys.stdin.read()

outtext = markdown.markdown(intext, extensions=[ImageInliner()], output_format="html5")

sys.stdout.write(outtext)
```

## TODO:
 
 * Add some sort of configuration to allow the user to exclude some img elements from inlining.
