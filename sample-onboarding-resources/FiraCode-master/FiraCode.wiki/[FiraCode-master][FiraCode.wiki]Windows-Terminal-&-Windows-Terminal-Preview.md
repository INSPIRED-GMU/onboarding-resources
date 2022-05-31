## Requirements

* [Windows Terminal](https://www.microsoft.com/store/productId/9N8G5RFZ9XK3)
* [Fira Code](https://github.com/tonsky/FiraCode/wiki/Installing)

## Open the Windows Terminal settings.json file

The visual settings editor for WT and WTp do not currently support changing the font for the program.  You will need to insert the necessary configuration into the settings.json file directly.

**From your favorite editor:**

The settings file for Windows Terminal & Windows Terminal Preview will open in Notepad.exe if your system does not have a default file association set for .json files.   You can open it directly from an alternative editor at the following location.  Be sure to replace `<USER>` with your own username!

`C:\Users\<USER>\AppData\Local\Packages\Microsoft.WindowsTerminalPreview_8wekyb3d8bbwe\LocalState\settings.json`

**From Windows Terminal or Windows Terminal Preview:**

* Open the settings editor from the "New Window" dropdown menu, or using keyboard shortcut <kbd>Ctrl</kbd>+<kbd>,</kbd>
* Click the "Open JSON File" button from the bottom left of the settings menu
* "settings.json" will open in your editor (or Notepad.exe if no other default is set)

## Edit the Windows Terminal settings.json file:

You will need to insert a font object for Fira Code in one or more profiles:

* The font object in the profile defaults will be used in any window or tab that does not have a profile which explicitly sets a font.
* A font object in a named profile will override the default font for windows and tabs using that profile only.

An example font object:
```    
    "font": {
        "face": "Fira Code",
        "size": 14,
        "weight": "normal",
        "features": {
            "cv02": 1, 
            "cv14": 1, 
            "cv25": 1, 
            "cv26": 1, 
            "cv28": 1, 
            "cv32": 1, 
            "ss02": 1, 
            "ss03": 1, 
            "ss05": 1, 
            "ss07": 1, 
            "ss09": 1
        }
    }
```

## References:
[https://docs.microsoft.com/en-us/windows/terminal/customize-settings/profile-appearance](https://docs.microsoft.com/en-us/windows/terminal/customize-settings/profile-appearance)

