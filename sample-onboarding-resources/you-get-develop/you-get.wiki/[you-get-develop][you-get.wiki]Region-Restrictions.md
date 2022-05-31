Some video sites have region restrictions (for accessing some of their videos). To name a few:

* **YouTube**: Germany (see also: https://en.wikipedia.org/wiki/Blocking_of_YouTube_videos_in_Germany)
  * On YouTube, uploaders have the option to filter out watchers by region, which is often the case when you see a message "_The uploader has not made this video available in your country._" on some videos.
* **CBS.com**:  outside U.S.
* **Youku**, **Tudou**, etc.: outside mainland China
  * Note that although some sites do forbid overseas users streaming videos from a browser, e.g. **YinYueTai**, you may still fetch these videos with `you-get` effortlessly.

With a proxy or VPN (located in unblocked countries) and a tool like [proxychains](https://github.com/rofl0r/proxychains-ng). you can easily bypass such restrictions.

You may also use the `-x` option to specify an HTTP proxy to use explicitly for `you-get`.

For extracting videos only available in China, you also have the option of `-y proxy.uku.im:443` to employ a dedicated proxy kindly provided by the [Unblock-Youku](https://github.com/Unblocker/Unblock-Youku) project.