# ImageInliner
Python Markdown extension to render images inline using 'data:' URLs

## Description
Sometimes it's useful to create a stand-alone HTML document where all of the images are included in the HTML file instead of being refrences to URLs that must be fetched by the browser when the page is rendered.  This makes distributing the document much simpler since it's just a single HTML file.

When this extension is enabled, the Python Markdown tree is post-processed (hopefully the last tree processing before the HTML is rendered) and any "img" elements are converted to using data: URLs.

This will undoubtedly make the HTML file far, far larger, but that's the price you pay for a single-file, stand-alone, document.

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
 * Detect img elements that are already data: URLs and leave them alone
