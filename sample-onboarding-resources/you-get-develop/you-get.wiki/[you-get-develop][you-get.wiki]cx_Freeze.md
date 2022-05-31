## How-to: turn `you-get` into an executable

This method is known to work on **GNU/Linux (x86-64)**, with **Python 3.5.0** and **cx_Freeze 5.0** directly installed [from source](https://bitbucket.org/anthony_tuininga/cx_freeze). (Hint: don't use the pip version of cx_Freeze. It might be too old for you!).

Create a file `freezer.py` under the project directory, with the following content:

```py
from cx_Freeze import setup, Executable

executables = [
    Executable('you-get')
]

setup(
    name = 'you-get',
    version = '0.0',
    description = 'you-get',
    executables = executables
)
```

Run:

```
$ python3 freezer.py build
```

Find the executable produced by cx_Freeze in `build/exe.linux-x86_64-3.5/you-get` (based on your platform and Python version).
