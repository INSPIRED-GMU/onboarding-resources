Boilerplate for implementing your own `VideoExtractor`:

```python
#!/usr/bin/env python

from ..common import *
from ..extractor import VideoExtractor

class FooBar(VideoExtractor):
    name = "Foo Bar"

    stream_types = []

    def prepare(self, **kwargs):
        pass

    def extract(self, **kwargs):
        pass

site = FooBar()
download = site.download_by_url
download_playlist = playlist_not_supported('foo_bar')
```

See [pinterest.py](https://github.com/soimort/you-get/blob/develop/src/you_get/extractors/pinterest.py) for a real-world example.
