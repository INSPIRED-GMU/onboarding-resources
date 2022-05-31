scikit-learn packages are available in recent distributions of Debian and Ubuntu, but these aren't always up to date. Here is a quick and dirty way to make a scikit-learn `.deb` package from source.

1. Get the [`stdeb`](http://pypi.python.org/pypi/stdeb) package:

        sudo apt-get install python-stdeb python-dev-all

    or

        sudo pip install stdeb

2. Fetch the latest scikit-learn tarball, or even checkout the bleeding edge from GitHub. Enter the toplevel source directory, then issue

        python setup.py --command-packages=stdeb.command sdist_dsc --depends python-numpy,python-scipy bdist_deb

Now, you'll find a directory `deb_dist` under the toplevel dir, which contains a file `python-scikit-learn_0.10-1_amd64.deb` (or similar). There's your `.deb`, ready for installation with a command like `sudo dpkg- i`.