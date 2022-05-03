## macOS

In the [downloaded TTF folder](https://github.com/tonsky/FiraCode/releases):

1. Select all font files
1. Right click and select `Open` (alternatively `Open With Font Book`)
1. Select "Install Font"

*or*

- Use [brew](http://brew.sh) and [cask](https://caskroom.github.io): 

  *Not officially supported, might install outdated version*
  ```bash
  brew tap homebrew/cask-fonts
  brew install --cask font-fira-code
  ```

## Linux

- Install a package available for your distribution following [the instructions](https://github.com/tonsky/FiraCode/wiki/Linux-instructions#installing-with-a-package-manager)

*or*

- In the ttf folder double-click each font file and click “Install font”; see [“Manual Installation”](https://github.com/tonsky/FiraCode/wiki/Linux-instructions#manual-installation) if double-clicking doesn't work


## FreeBSD

- Using pkg(8): `pkg install firacode`

*or*

- Using ports: `cd /usr/ports/x11-fonts/firacode && make install clean`

## Windows

- Download the latest font zip file https://github.com/tonsky/FiraCode#download--install
- In the ttf folder, double-click each font file, click “Install font”; to install all at once, select all files, right-click, and choose “Install”
- On some systems (especially Windows 10), you may need to "Unblock" each font file before installing. To do so, right-click each font file, click Properties, then check Unblock next to Security at the bottom of the General tab. Click OK, and then install. _Note: Skipping this step may cause the Fira Code fonts to intermittently stop working in VS Code, even though the fonts still appear in other programs._

*or*

On Windows 10 open the System Settings, go to Fonts and drag and drop the the font files from the ttf folder into the drop area indicated at the top of the dialog.

*or*

- Use [chocolatey](https://chocolatey.org): `choco install firacode`

- Use [scoop](https://github.com/lukesampson/scoop):

  *Run as administrator*
  ```
  scoop bucket add nerd-fonts
  scoop install firacode
  ```
