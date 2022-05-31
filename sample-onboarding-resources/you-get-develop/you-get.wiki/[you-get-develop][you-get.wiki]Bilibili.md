## Member-only videos

To download member only videos (such as [this one](http://www.bilibili.com/video/av2987444/) and [this one](http://www.bilibili.com/video/av3057394/)), it is required to preload cookies from your browser, using the `-c` option:

```
$ you-get -i -c ~/.mozilla/firefox/gggfz9xl.default/cookies.sqlite \
  http://www.bilibili.com/video/av2987444
```

Note: at this point, only `cookies.txt` and Mozilla-style `cookies.sqlite` are supported. Loading Chrome cookies would be possible in the future but [not a priority](https://github.com/soimort/you-get/pull/686#issuecomment-148879122).

## I got an empty (0.0 MiB) video. Why?

[As reported](https://github.com/soimort/you-get/issues/688#issuecomment-147031370), some videos on Bilibili are known to have [region restrictions](https://github.com/soimort/you-get/wiki/Region-Restrictions). Use a proxy.

With an European IP:

```
λ  you-get-develop [develop] ./you-get -i http://www.bilibili.com/video/av1652964/
Video Site: bilibili.com
Title:      【10月】黑服物语 01 中岛健人-佐佐木希-山本裕典-柏木由纪【人人字幕】
Type:       Unknown type ()
Size:       0.0 MiB (0 Bytes)
```

With a proxy of American IP:

```
λ  you-get-develop [develop] proxychains -q ./you-get -i http://www.bilibili.com/video/av1652964/
Video Site: bilibili.com
Title:      【10月】黑服物语 01 中岛健人-佐佐木希-山本裕典-柏木由纪【人人字幕】
Type:       Flash video (video/x-flv)
Size:       183.8 MiB (192725874 Bytes)
```

# 中文翻译最终日期：2016年03月18日

## 会员的世界

下载会员的世界 (例如 [这个](http://www.bilibili.com/video/av2987444/) 或者 [这个](http://www.bilibili.com/video/av3057394/)), 需要加载浏览器的cookie, 使用 `-c`:

```
$ you-get -i -c ~/.mozilla/firefox/gggfz9xl.default/cookies.sqlite \
  http://www.bilibili.com/video/av2987444
```

注意：目前只支持 `cookies.txt` 或者 Mozilla样式的`cookies.sqlite` . 以后有可能可以加载Chrome的cookies，但[优先级不高](https://github.com/soimort/you-get/pull/686#issuecomment-148879122).

## 视频大小为空 (0.0 MiB). 为什么?

[据报告](https://github.com/soimort/you-get/issues/688#issuecomment-147031370), 有些 Bilibili 视(xin)频(fan)有 [区域限制](https://github.com/soimort/you-get/wiki/Region-Restrictions). 挂代理吧.

用欧洲IP:

```
λ  you-get-develop [develop] ./you-get -i http://www.bilibili.com/video/av1652964/
Video Site: bilibili.com
Title:      【10月】黑服物语 01 中岛健人-佐佐木希-山本裕典-柏木由纪【人人字幕】
Type:       Unknown type ()
Size:       0.0 MiB (0 Bytes)
```

用美国IP:

```
λ  you-get-develop [develop] proxychains -q ./you-get -i http://www.bilibili.com/video/av1652964/
Video Site: bilibili.com
Title:      【10月】黑服物语 01 中岛健人-佐佐木希-山本裕典-柏木由纪【人人字幕】
Type:       Flash video (video/x-flv)
Size:       183.8 MiB (192725874 Bytes)
```