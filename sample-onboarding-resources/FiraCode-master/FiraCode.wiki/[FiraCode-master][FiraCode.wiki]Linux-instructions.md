# **IMPORTANT**

Starting from v5, Fira Code does not distribute OTF. All packages here that have `otf-*` in the name are **now outdated** and should be replaced with ttf equivalents.

## Installing with a Package Manager

### Ubuntu Zesty (17.04), Debian Stretch (9) or newer

1. Make sure that the `universe` (for Ubuntu) or `contrib` (for Debian) repository is enabled (see [how-to for Ubuntu](https://askubuntu.com/questions/148638/how-do-i-enable-the-universe-repository) or [Debian docs](https://wiki.debian.org/SourcesList#Component))
2. Install `fonts-firacode` package either by executing `sudo apt install fonts-firacode` in the terminal or via GUI tool (like “Software Center”)

### Arch Linux

Fira Code package is available in the official repository: [ttf-fira-code](https://www.archlinux.org/packages/community/any/ttf-fira-code/).

Variant of Fira Code package is available in the AUR: [otf-fira-code-git](https://aur.archlinux.org/packages/otf-fira-code-git/).

### Gentoo

```bash
emerge -av media-fonts/fira-code
```

### Fedora


Fira Code package is available in the official repository.

To install, perform the following command:
```bash
dnf install fira-code-fonts
```

### Solus

```bash
sudo eopkg install font-firacode-ttf
```

### Void linux

```bash
xbps-install font-firacode
```
## Manual Installation

With most desktop-oriented distributions, double-clicking each font file in the ttf folder and selecting “Install font” should be enough. If it isn’t, create and run download_and_install.sh script:

```bash
#!/usr/bin/env bash

fonts_dir="${HOME}/.local/share/fonts"
if [ ! -d "${fonts_dir}" ]; then
    echo "mkdir -p $fonts_dir"
    mkdir -p "${fonts_dir}"
else
    echo "Found fonts dir $fonts_dir"
fi

version=5.2
zip=Fira_Code_v${version}.zip
curl --fail --location --show-error https://github.com/tonsky/FiraCode/releases/download/${version}/${zip} --output ${zip}
unzip -o -q -d ${fonts_dir} ${zip}
rm ${zip}

echo "fc-cache -f"
fc-cache -f
```


[More details](https://github.com/tonsky/FiraCode/issues/4)