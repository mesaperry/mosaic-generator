# mosaic-generator

Generates a mosaic from a specified keyword or keyphrase. Downloads up to 100 images from Google Images for tiles and selects one at random for the background.

Must have installed Python, the [Pillow](http://pillow.readthedocs.org/en/latest/) imaging library, and [this Google image downloader](https://pypi.org/project/google_images_download/).

Usage is as follows:

<pre>python mosaicgen.py &lt;keyword&gt;</pre>

* `keyword` can be either a word or phrase, however if there are spaces it must be encapsulated by apostrophes.

I used [this script](https://github.com/codebox/mosaic) to do the work compiling the scraped images into a mosaic. As such, you can adjust the parameters within `mosaic-master/mosaic.py` to scale the output mosaic or change tile size.
