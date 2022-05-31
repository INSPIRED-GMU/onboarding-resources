1. On windows the script keeps printing the process bar

Different reasons for different windows. On windows 10 default console(```cmd.exe```) the Unicode characters used in the process bar takes 2-character space. Not sure changing the font for the console can fix it or not.

You can test this with the following script:
```
print('_' * 80)
print('├' * 80)
print('█' * 80)
print('┤' * 80)
```

The script does print 80 characters but it takes spaces for 160 characters in the last three statements. A ```'\r'``` cannot move to the last printed line so it will keep printing the process bar.

Solution: Perhaps you can switch to a better console emulator, ```cmder``` for instance.

---

2. How to tell ```you-get``` the correct URL

F.I. the URL is ```http://www.icourses.cn/jpk/changeforVideo.action?resId=722918&courseId=5929&firstShowFlag=2```
```
you-get http://www.icourses.cn/jpk/changeforVideo.action?resId=722918&courseId=5929&firstShowFlag=2
``` 
won't work. 
What ```you-get``` received is ```http://www.icourses.cn/jpk/changeforVideo.action?resId=722918```
You have to quote the URL like 
```
you-get "http://www.icourses.cn/jpk/changeforVideo.action?resId=722918&courseId=5929&firstShowFlag=2" 
```

NOTE: On the homepage URLs are single quoted, which won't work with ```cmd.exe```.

---

3. What is ```PATH```

Check [this](https://superuser.com/questions/284342/what-are-path-and-other-environment-variables-and-how-can-i-set-or-use-them)

---

4. ```python``` or ```python3```? ```pip3``` or ```pip```?

On windows 10 python 3.6.2 official binary(32bits), it's ```python``` and ```pip3```