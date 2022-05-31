### Version 2019.3 and later

- Enable in `Settings` → `Editor` → `Font` → `Enable Font Ligatures`
- Select `Fira Code` as "Font" under `Settings` → `Editor` → `Font`
- [Optional extension to disable ligatures in unwanted contexts](https://plugins.jetbrains.com/plugin/14736-ligatures-limited/)

### Version 2018.2

- Enable in `Settings` → `Editor` → `Font` → `Enable Font Ligatures`
- Select `Fira Code` as "Primary font" under `Settings` → `Editor` → `Font`

Additionally, if a Color Scheme is selected: 
- Enable in `Settings` → `Editor` → `Color Scheme` → `Color Scheme Font` → `Enable Font Ligatures`
- Select `Fira Code` as "Primary font" under `Settings` → `Editor` → `Color Scheme` → `Color Scheme Font`

### Version 2018.1

- Enable in `Settings` → `Editor` → `Color Scheme` → `Color Scheme Font` → `Enable Font Ligatures`
- Select `Fira Code` as "Primary font" under `Settings` → `Editor` → `Color Scheme` → `Color Scheme Font` → `Font`

### Version 2016.2 and prior to 2018.1

Proper support for ligatures was added in 2016.2 (incl. font compatibility & better performance).
- Enable in `Settings` → `Editor` → `Colors & Fonts` → `Font` → `Enable Font Ligatures`
- Select `Fira Code` as "Primary font" under `Settings` → `Editor` → `Colors & Fonts` → `Font` → `Editor Font`

_NOTE:_ Since 2016.3 IntelliJ products come with Fira Code bundled with the editor itself. If you want the latest version of Fira Code, install it separately & restart your editor.

### Corrupted text on Windows

If you see something like that

![this](https://cloud.githubusercontent.com/assets/12413929/18270117/3dcbbe18-7423-11e6-88cd-c7725657babf.png)

Open `cmd.exe`, `cd C:\Windows\Fonts` and then `del` every file that looks like `FiraCode-Regular_**.ttf`. NB these files are invisible if you open `Fonts` in Explorer

If the files are locked you can use [Unlocker](http://www.emptyloop.com/unlocker/). In details you should:
* Install unlocker
* Open `cmd.exe` as admin (press the Windows key, type `cmd` and right click on the result to run it as admin)
* `subst q: c:\windows\fonts`, replace `q` with any other letter if you already have a unit with that name
* Open unlocker from the start menu, `Start Unlocker`
* Select any file named `FiraCode-Regular_**.ttf` from the `q` unit, select `Delete` and press `Unlock all` (you could also try simply closing the applications if you can)
* type `subst /D q:` inside the command prompt to remove the new unit

Issue: https://youtrack.jetbrains.com/issue/IDEA-159901

### Prior to 2016.2

This should work for **Fira Code 1.102** and IntelliJ products **v. 15** and later (IDEA, PhpStorm, PyCharm, RubyMine, WebStorm, AppCode, CLion, DataGrip):

- Create `idea.properties` file in the configuration directory of your IDE (see [where you can locate your configuration directory for your product](https://intellij-support.jetbrains.com/hc/en-us/articles/206544519))
- Add this:
```
editor.enable.optional.ligatures=true
```
- Restart your IDE

_NOTE:_ IDEA support of ligatures is considered experimental. E.g. scroll performance may be very slow. It has been [reported here](https://youtrack.jetbrains.com/issue/IDEA-127539#comment=27-1267636)

_NOTE:_ There’s an issue on OS X when Fira Code Light is used instead of Regular weight by default ([discussion](https://github.com/tonsky/FiraCode/issues/96#issuecomment-167119788)). To work around that, do not install Light weight at all. **(this is fixed in latest 16 EAP)** Also, installing TTF as opposed to OTF renders better with IntelliJ on the Mac.

_NOTE:_ For latest EAPs of JetBrains products, that file doesn’t matter without setting preference:
`Editor`→`Font`→[`Enable Font Ligatures`](https://confluence.jetbrains.com/display/IDEADEV/Support+for+Ligatures+in+Editor)