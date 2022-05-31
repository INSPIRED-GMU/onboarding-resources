This page serves as a list of some of the more commonly encountered issues while using the Terminal.

In addition to this FAQ, please make sure to refer to the [official docs](https://docs.microsoft.com/en-us/windows/terminal). There you can find more detailed info on features of the Terminal, the available settings and how they work, and various tips and tricks for using the Terminal.

<!-- 
There used to be a table of contents here, that I generated with 
https://ecotrust-canada.github.io/markdown-toc/
However, since I did that, github added support for the table of contents in the sidebar, so I'm removing it.
 -->


## General

### Where can I find the settings file?

The settings file can be found in the following location:
* Windows Terminal (Stable): `%localappdata%\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json`
* Windows Terminal (Preview): `%localappdata%\Packages\Microsoft.WindowsTerminalPreview_8wekyb3d8bbwe\LocalState\settings.json`

Additionally in that directory is the `state.json` file, which contains additional state that the Terminal generates at runtime.

### Unable to find the selected font "Cascadia Mono"

There is a bug in the application deployment platform on recent versions of Windows that results in the Cascadia Mono font (the default font) being unreadable.

![image](https://user-images.githubusercontent.com/34492055/114411512-17e5c800-9b61-11eb-8818-3728d8764a8e.png)

Unfortunately, that means that through no fault of your own, you'll get a dialog that says we can't find Cascadia Mono or Cascadia Code.

**KNOWN SOLUTIONS**:
* Either reboot or
* choose to "Repair" the Terminal application in the "All apps" list in Settings.

### The Terminal window disappears immediately on launch!

Before filing a bug, please check your settings file to see if you have `"closeOnExit": "always"` set. It's possible that the Terminal window is closing when the shell application closed immediately, or it's possible that the commandline failed to launch entirely. `"closeOnExit": "graceful"` will help debug if that's the case.

### Version XYZ was just released, why doesn't it show up as an update in the Store?

This unfortunately happens [every](https://github.com/microsoft/terminal/issues/11622) [release](https://github.com/microsoft/terminal/issues/12403). We're using a ring-based rollout system for the Terminal. We need to be more cautious with the stable build, given how many users it could potentially impact if something were to be wrong with it. For example, [our CI absolutely blew up ALL localization in the first 1.12 release](https://github.com/microsoft/terminal/issues/12351). That's not the kind of thing you want to roll out immediately to everyone using the Terminal 😅. If you install the `.msixbundle` off our [Releases page](https://github.com/microsoft/terminal/releases), then it'll stay linked to the Store version and still auto-update in the future, if you manually want to hop to the next version without waiting for the Store. 

Sorry for the inconvenience, and thanks for your enthusiasm for staying on the latest version!

### Can I use the Terminal on (Windows 7, Windows Server 2019, any other down-level Windows version)

Unfortunately no, and we have no plans to make the Terminal available on operating systems below version 1903. There are some important operating system features we depend on. Namely:
* XAML Islands is the technology we use to host our XAML UI in a Win32 process. Without that, we'd be unable to display anything. Since XAML Islands is only complete as of 1903, there's nothing we can do about it.
* 1903 Also added support for side-by-side WinRT component activation, something deep in the COM stack that lets us find our DLLs when they're right next to our EXE.

These are unfortunately features that aren't going to be back-ported to earlier versions of Windows, so we won't be able to bring the Terminal to those versions either.

### What about porting the Windows Terminal to MacOS or Linux?
<!-- #2331 #504 #563 #624 #2466 #699 #498 #6074 #4235 -->
The answer is actually basically the same as the above. Windows Terminal requires a good number of Windows-specific technologies. We unfortunately won't be supporting it on Mac or anywhere else any time soon. There are some really good terminals on OS X, including iTerm and Hyper, and an uncountable number of good terminals on Linux.

### Why am I seeing `[process exited with code ...]`?

This message is printed by the Terminal whenever the client application closes with a non-zero exit code. Notably, `exit` in `cmd.exe` will also return the exit code of the command that was previously run. So if you happen to type something like

```cmd
> foo
'foo' is not recognized as an internal or external command,
operable program or batch file.
> exit
[process exited with code 9009]
``` 
You'll see this message, because `cmd` returned the `9009` from the original failure to find `foo`.

This behavior exists to stop an error message printed out by a program from _disappearing instantly_ when it exits. There is a class of applications for which that is extremely important. This is a behavior that's highly conserved across multiple shells and terminal emulators on most mainstream operating systems. We're following this behavior because it is the right behavior to follow, _and because you can turn it off with a config option very easily!_

If you'd rather it just exit every time, you can set `"closeOnExit": "always"`. For more information, please [check out the docs for this setting](https://docs.microsoft.com/en-us/windows/terminal/customize-settings/profile-advanced#profile-termination-behavior). In the Settings UI, this setting can be found here: 

![closeOnExit setting in UI](https://user-images.githubusercontent.com/3933920/132601625-d6a9fce7-ab5a-41fa-bc92-4d37830854d4.png)

See also: [#4223 (comment)](https://github.com/microsoft/terminal/issues/4223#issuecomment-574834181).

### `wt.exe` stopped working

This is something that can happen intermittently whenever the Terminal is updated. Something in the upgrade process causes the execution alias to stop working correctly. You might get an error message like:

> Windows cannot find 'C:\Users\username\AppData\Local\Microsoft\WindowsApps\wt.exe'. Make sure you've typed the name correctly, then try again.

Most of the time, you can resolve this by toggling the App Execution Alias for WT off then on the screen at https://stackoverflow.com/a/66539884/1743

### `wt` from the File Explorer address bar doesn't work!

If you try typing `wt` at the explorer address bar, you'll notice that the Terminal doesn't open at that path, it instead uses your `startingDirectory`. This is unlike `cmd` or `pwsh`, which _will_ inherit the current path of explorer correctly. Unfortunately, this is a complicated situation - there's no good way to determine that the Terminal was launched in this way. There are more details in [this comment](https://github.com/microsoft/terminal/issues/878#issuecomment-579508860). Fortunately, there is an easy workaround. Simply type 

```
wt -d .
```

instead. That `-d .` will tell the Terminal to use explorer's CWD as the `startingDirectory` instead!

### Windows Terminal fails to run as Administrator

This can happen often if you're running the Terminal from a user profile that is _not_ an administrator, **AND** the Terminal isn't installed for your Admin account on this machine. You might see an error message like:

![image](https://user-images.githubusercontent.com/31540828/121568349-86d38600-ca17-11eb-8735-c9c02912f603.png)

This happens because packaged applications need to be installed for the Admin account to be able to be run elevated. **To fix this**: install the Terminal for your Admin account as well. There are more details in [#7806]. We're working with the platform team to try and fix this issue, and get the fix brought to downlevel Windows versions. We'll update this if this issue is resolved. 

### Can you run the Terminal as an Admin from the taskbar?

Yes you can! It just requires a second right click. Right click on the taskbar entry, then right click on the app name (Windows Terminal), to reveal the "run as administrator" option.

![image](https://user-images.githubusercontent.com/18356694/150791531-d2ce99dd-e0b5-4d68-bf50-d642dbeff6fb.png)


### How do changes to the console in this repo get to `conhost.exe` in the OS?

Every couple of weeks (time permitting), one of our team members merges the changes from this repository's `main` branch into an internal mirror's `inbox` branch. Once that happens, another tool called `git2git` migrates the tree from that internal mirror into a directory on our team's branch in the Windows OS git repository. Some weeks later, that branch's content has made its way to `main`, which is approximately where Insider builds come from. The time it takes to get from our team's branch to the Windows `main` branch is dependent on many factors, so it can range from 2-6 weeks. 

## Default Terminal

### Unable to set Windows Terminal as the Default Terminal on Windows 11

Currently, this is by design. You can set the Preview version of the Windows Terminal as the Default Terminal, but not the Stable version. We're currently working through a few more bugs that we'd like to get sorted before allowing the Stable version to be set as the Default Terminal on Windows.
Windows 11 is shipping a new OS feature we're calling "defterm" - the ability to set the default terminal application for console launches in Windows. This was originally tracked in #492, #5000. This feature initially shipped in Terminal Preview version [`v1.9.1445.0`](https://github.com/microsoft/terminal/releases/tag/v1.9.1445.0).

As of writing, this feature is still only available in "Preview" versions of the Terminal, and Stable versions 1.11+. There are two different versions of the Terminal available:
* [Windows Terminal Preview](https://www.microsoft.com/en-us/p/windows-terminal-preview/9n8g5rfz9xk3?activetab=pivot:overviewtab) (which we refer to as "preview").
* [Windows Terminal](https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701?activetab=pivot:overviewtab) (which we call "stable" or "release")

Stable is usually one minor version behind the Preview version, +/- a couple features. If you're wondering why the Terminal doesn't appear in the dropdown, then this is why.

If you only have "Windows Terminal" (stable) installed, you will not see the Terminal in the Settings app for the Default Terminal setting.

### Launching the Windows Terminal as the Default Terminal doesn't work - it opens the vintage console window instead!

There could be multiple causes to this:
* Launching elevated commandline applications won't open in the Terminal. Unfortunately, this is by design right now. Due to a limitation in the app platform it is impossible for Terminal to be "discovered" as the handler when the application that needs a terminal is running elevated. We're working on this, but this is something that needs OS-side work to resolve.
* In v1.12.2931.0 Preview and v1.11.2921.0 Stable or below, you'll need to have the VC Redistributable installed.   
  ![image](https://user-images.githubusercontent.com/18356694/139054972-77aaeed4-876f-4362-98e9-74631c85f144.png)

  This is often installed alongside other applications as a dependency, but on fresh Windows installs, it might not be present yet. 
* If you're still running into issues, then please file a new issue! We're probably going to ask you to follow [these steps](https://github.com/microsoft/terminal/issues/11529#issuecomment-948649578).

### Will the default terminal functionality be coming to Windows 10?

Nope. That feature is going to remain a Windows 11-only feature. It's powered by a fairly large feature change to the OS, which is unlikely to be serviced as a "bugfix" to earlier OS versions.

## Transparency

### Why does acrylic not work?

As a system-wide policy, acrylic is only enabled for the foreground window. So if you activate any other window than the Terminal, the Terminal's acrylic will turn off.

There are other system policies that control when acrylic is or isn't enabled. For example, if your laptop is in power saver mode, or you're accessing your machine through RDP, then acrylic will be disabled. Before filing a bug, make sure that acrylic works in other apps, like Calculator, or the Start Menu. Furthermore, if the Windows OS setting "Transparency effects" is not turned on (Windows Settings -> Customize -> Colors -> Transparency effects), then acrylic will not take effect.

We're currently using [#7158] to track adding support for "enable acrylic even for inactive Terminal windows" - if you're passionate about this, we'd love your contribution!

### Can I have non-blurred transparency?

Yes! As of Terminal v1.12.2922.0, this feature is supported **on Windows 11**.

### Can I have non-blurred transparency on Windows 10?

Soon<sup>TM</sup>. We're working with the servicing folks to make this happen. The API we're using to achieve unblurred transparency is actually broken on Windows 10, so we need to get the fix for that serviced down to Windows 10.

## Quake Mode & Global Summon

Please make sure to check out [#8888], which is tracking all the quake-mode and `globalSummon` related issues.

### What is "Global Summon"

"Global Summon" refers to the `globalSummon` action. This action allows you to bind a shortcut _systemwide_ to activate the Terminal window. This means that you can bind something like <kbd>win+\`</kbd>, and press that _anywhere_ in the OS to instantly activate the Terminal window. `globalSummon` supports a ton of different parameters to control its behavior, so please make sure to [check out the docs](https://docs.microsoft.com/en-us/windows/terminal/customize-settings/actions#global-commands).

### What is "Quake Mode"?

"Quake Mode" is a specific version of `globalSummon`. It summons a window that's named `_quake`, and the window named `_quake` has certain special properties. Check out [the docs](https://docs.microsoft.com/en-us/windows/terminal/tips-and-tricks#quake-mode) for more details.

### I can't use the `quakeMode`/`globalSummon` keybinding unless I've already launched the Terminal

That's correct - the Terminal needs to be running to be able to register the global hotkeys. You can configure the Terminal to launch on machine startup with `"startOnUserLogin":  true`. We're also using [#9996] to track "Allow the Terminal to start up and process global hotkeys without creating a window".

### How do I set the size of the `quakeMode` window? 

Right now, you can't. The window named `_quake` will always open on the top half of the monitor. 

What you _can_ do, though, is rebind <kbd>win+\`</kbd> to a different `globalSummon` action. The following will be equivalent to the `quakeMode` action, but without the requirement that the window's name is `_quake`:

```json
{ "keys": "win+`", "command": { "action": "globalSummon", "dropdownDuration": 200, "toggleVisibility": true, "monitor": "toCursor", "desktop": "toCurrent" } }
```

Then, your window will still obey your standard `initalPosition`, `initialRows`, etc. settings.

Additionally, [#9992] is the issue we're tracking for "Allow configuring global settings per-window name". That means you'll be able to use that to change the settings for the window named `_quake`.

### The `quakeMode` window doesn't have any tabs / How can I have tabs in the quake window

The `_quake` window always opens in ["focus mode"](https://docs.microsoft.com/en-us/windows/terminal/customize-settings/actions#toggle-focus-mode) by default. That doesn't mean that the quake window doesn't _have_ tabs, just that they're hidden. You can use the [Command Palette](https://docs.microsoft.com/en-us/windows/terminal/command-palette) to disable focus mode if you want to see the tabs again. 

If you don't want the global hotkey to summon the window in quake mode, there are two options:
* Either re-bind it to a different `globalSummon` action, like the above, without `"name": "_quake"`.
* Wait patiently for [#9992] to allow changing the settings of the `_quake` window name.

### I want to use a different hotkey to summon different profiles

This is another scenario that'll have to wait for [#9992]. What you'd end up with is different window names for each profile you want a specific hotkey for. The `defaultProfile` for those windows would be set to whatever profile you want. Then, you'd bind `globalSummon` actions, with the `name` set to each of those window names. 

### I want the Terminal to hide on minimize / minimize to the tray

This is a feature that's commonly associated with Quake Mode. Unfortunately, it didn't quite make the cut for 1.9. Never fear! We're working on it currently. Please follow [#5727] for updates on adding this functionality to the Terminal.

## Other

This is a small list of FAQ-like questions that have had lengthy replies in the past. They're all preserved in the doc [`niksa.md`](https://github.com/microsoft/terminal/blob/main/doc/Niksa.md)

- [Why do we avoid changing CMD.exe?](https://github.com/microsoft/terminal/blob/main/doc/Niksa.md#cmd)
- [Why is typing-to-screen performance better than every other app?](https://github.com/microsoft/terminal/blob/main/doc/Niksa.md#screenPerf)
- [How are the Windows graphics/messaging stack assembled?](https://github.com/microsoft/terminal/blob/main/doc/Niksa.md#gfxMsgStack)
- [Output Processing between "Far East" and "Western"](https://github.com/microsoft/terminal/blob/main/doc/Niksa.md#fesb)
- [Why do we not backport things?](https://github.com/microsoft/terminal/blob/main/doc/Niksa.md#backport)
- [Why can't we have mixed elevated and non-elevated tabs in the Terminal?](https://github.com/microsoft/terminal/blob/main/doc/Niksa.md#elevation)
- [What's the difference between a shell and a terminal?](https://github.com/microsoft/terminal/blob/main/doc/Niksa.md#shell-vs-terminal)

[#603]: https://github.com/microsoft/terminal/issues/603
[#5727]: https://github.com/microsoft/terminal/issues/5727
[#7158]: https://github.com/microsoft/terminal/issues/7158
[#7806]: https://github.com/microsoft/terminal/issues/7806
[#8888]: https://github.com/microsoft/terminal/issues/8888
[#9992]: https://github.com/microsoft/terminal/issues/9992
[#9996]: https://github.com/microsoft/terminal/issues/9996
[microsoft/microsoft-ui-xaml#1247]: https://github.com/microsoft/microsoft-ui-xaml/1247