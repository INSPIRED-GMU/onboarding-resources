* Q: I got encoding issues on Windows.

* A: Change your Windows code page to UTF-8, using `chcp 65001`.

* Q: I don't know how to install it on Windows.

* A: Then don't do it. Just put your `you-get` folder into system `%PATH%`.

* Q: I got something like `UnicodeDecodeError: 'gbk' codec can't decode byte 0xb0 in position 1012: illegal multibyte sequence`.

* A: Run `set PYTHONIOENCODING=utf-8`.

* Q: Special characters in the URL (such as `?`, `&`) are interpreted by my shell. How to prevent this?

* A: Use `noglob`.

* Q: UnicodeDecodeError in Windows mintty (such as cygwin, [git-for-windows](https://github.com/git-for-windows/git/releases/latest), [msys2](http://msys2.github.io/) and [git-sdk](https://github.com/git-for-windows/build-extra/releases/latest))

* A:
    * Find a folder called site-packages under python3, for example:
        * `$ python3`
        * `>>> import site; site.getsitepackages()`
        * It should print something like `['C:/git-sdk-64/mingw64/lib/python3.5/site-packages']`
    * Create a new file `sitecustomize.py`
        * `import sys`
        * `sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)`
    * Save it to `C:/git-sdk-64/mingw64/lib/python3.5/site-packages/sitecustomize.py`

* Q: 'width' 'height' 'auto' not exist?

* A: Please quote the URL. This is a bug from the implementation of the Bash.

* Q: I got ````ssl.SSLError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed```?

* A: Kindly refer to #1710 .


汉语最后翻译日期：2017年11月04日

* Q: Windows下编码问题。

* A:使用UTF-8编码, using `chcp 65001`.

![chcp](https://i.imgur.com/mHYEnl1.png)

* Q: 不知道怎么在Windows下安装.

* A: 那就别安了，把`you-get`目录放进系统`%PATH%`.

* Q: `UnicodeDecodeError: 'gbk' codec can't decode byte 0xb0 in position 1012: illegal multibyte sequence`.

* A: 执行 `set PYTHONIOENCODING=utf-8`.

* Q: 命令行下，URL有些特殊字符被执行了(例如 `?`, `&`)。如何避免？

* A: 使用 `noglob`.

* Q: 在 Windows mintty 遇到 UnicodeDecodeError  ( 例如: cygwin, [git-for-windows](https://github.com/git-for-windows/git/releases/latest), [msys2](http://msys2.github.io/) 以及 [git-sdk](https://github.com/git-for-windows/build-extra/releases/latest))

* A:
    * 在python3目錄底下找到一個叫 `site-packages` 的目錄, 例如：
        * `$ python3`
        * `>>> import site; site.getsitepackages()`
        * 這時應該會顯示類似這樣的輸出 `['C:/git-sdk-64/mingw64/lib/python3.5/site-packages']`
    * 創建一個檔案 `sitecustomize.py`
        * `import sys`
        * `sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)`
    * 將它存到 `C:/git-sdk-64/mingw64/lib/python3.5/site-packages/sitecustomize.py`

* Q: 'width' 'height' 'auto' 不存在？

* A: 请对URL加引号。

* Q: macOS下出现 ````ssl.SSLError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed```?

* A: 看 #1710 .