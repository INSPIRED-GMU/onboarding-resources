Some applications may cause issues and sadly, at times, we can't work around it.

## General

### Applications that impact PowerToys on System Startup/Restart
- TaskbarX, [#9959](https://github.com/microsoft/PowerToys/issues/9959): Causes PowerToys not to work until manually closed and restarted. Also causes sys-tray icon to not appear.


## FancyZones

### Applications that cannot be zoned exactly

In multi-monitor configuration, when the monitors have different DPI scaling factors, and a zone touches a screen edge, the snapped window may be resized so that its border is a few pixels away from the edge of the screen.
That happens when the snapped application is not DPI aware.

### Applications that cannot be zoned

| Application | Issue # | Why / Possible Workaround |
| --- | --- | --- |
| Application Guard | [#616](https://github.com/microsoft/PowerToys/issues/616) | None (`EVENT_SYSTEM_MOVESIZESTART` is not raised) |
| Citrix | [#690](https://github.com/microsoft/PowerToys/issues/690) | None |
| Citrix Workspace | [#7135](https://github.com/microsoft/PowerToys/issues/7135) | A comment in the issue has [possible workaround](https://github.com/microsoft/PowerToys/issues/7135#issuecomment-704553358) |
| Civilization 4 | [#1004](https://github.com/microsoft/PowerToys/issues/1004) | None |
| GoToWebinar | [#3734](https://github.com/microsoft/PowerToys/issues/3734) | None |
| Hyper-V Connection | [#4336](https://github.com/microsoft/PowerToys/issues/4336) | None |
| iLO Remote Console | [#8067 ](https://github.com/microsoft/PowerToys/issues/8067) | A comment in the issue has [possible workaround](https://github.com/microsoft/PowerToys/issues/8067#issuecomment-728150030) |
| LDPlayer | [#8082](https://github.com/microsoft/PowerToys/issues/8082) | Use secondary mouse button to activate zones instead of `Shift` |
| [Parsec](https://parsec.app/) | [#9138](https://github.com/microsoft/PowerToys/issues/9138) | None |
| Mir4 App | [#16864](https://github.com/microsoft/PowerToys/issues/16864) | None |
| Origin game launcher | [#1466](https://github.com/microsoft/PowerToys/issues/1466#issuecomment-605591336) | None |
| RemoteApp | [#441](https://github.com/microsoft/PowerToys/issues/441) | None, the app steals all the keyboard/mouse events |
| Runelite | [commnet in #1466](https://github.com/microsoft/PowerToys/issues/1466#issuecomment-635951523) | Partial workaround: Disable its 'custom chrome window' in the runelite settings |
| TeamViewer | [#6945](https://github.com/microsoft/PowerToys/issues/6945) | TeamViewer may install display drivers that prevent FZ to be able to set the layout on each monitor independently |
| TWS InteractiveBrokers | [#6771](https://github.com/microsoft/PowerToys/issues/6771) | None |
| UPlay game launcher | [#1466](https://github.com/microsoft/PowerToys/issues/1466#issuecomment-605591336) | None |
| Windows Virtual Desktop | [#10018](https://github.com/microsoft/PowerToys/issues/10018) | None |
| VMware Workstation Player | [#666](https://github.com/microsoft/PowerToys/issues/666) | None (`EVENT_SYSTEM_MOVESIZESTART` is not raised) |
| [WindowsFX](https://www.stardock.com/products/windowfx/) | [#8321](https://github.com/microsoft/PowerToys/issues/8321) | [Detailed explanation](https://github.com/microsoft/PowerToys/issues/8321#issuecomment-742453379) |

### Applications that cause FancyZones Editor to fail to open:

 - RivaTunerStatisticsServer (MSI Afterburner). [#707](https://github.com/microsoft/PowerToys/issues/707)

### Applications that cause FancyZones snapping to crash apps:

 - [active-win](https://github.com/sindresorhus/active-win), [#12341](https://github.com/microsoft/PowerToys/issues/12341)

### Applications that need FancyZones to run elevated:
Since at present FancyZones runs in the same process of PowerToys, these applications require PowerToys to run as administrator in order to be zonable:
 - HWiNFO64 
 - TeamSpeak 3 

 
### Screen capture software: 

Workaround is to add the incompatible application to the FancyZones excluded apps list:

| Application | Issue # | Why / Possible Workaround |
| --- | --- | --- |
| ShareX | [#7291](https://github.com/microsoft/PowerToys/issues/7291) | Add ShareX to the FancyZones excluded apps |
| Screenpresso | [#4478](https://github.com/microsoft/PowerToys/issues/4478) | None |
| Greenshot | [#4373](https://github.com/microsoft/PowerToys/issues/4373) | Recent version seems to not have the compatibility issue |

## Keyboard manager

| Application | Issue # | Why / Possible Workaround |
| --- | --- | --- |
| Avid Pro Tools (2020) | [#7396](https://github.com/microsoft/PowerToys/issues/7396) | They use a lower level hook, possibly driver based |
| Microsoft Mouse and Keyboard Center | [#7328](https://github.com/microsoft/PowerToys/issues/7328) | See [comment](https://github.com/microsoft/PowerToys/issues/7328#issuecomment-730046147) |