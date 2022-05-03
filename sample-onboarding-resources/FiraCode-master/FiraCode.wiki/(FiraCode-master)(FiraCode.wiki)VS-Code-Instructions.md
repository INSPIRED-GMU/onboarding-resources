## Requirements

Make sure you [install the font](https://github.com/tonsky/FiraCode/wiki/Installing).

## Using the visual Settings Editor

To open the settings editor: from the `Code` menu, choose `Preferences` > `Settings`, or use keyboard shortcut <kbd>Ctrl</kbd>+<kbd>,</kbd> (<kbd>Cmd</kbd>+<kbd>,</kbd> on Mac).

To enable FiraCode in the settings editor: under "Commonly Used", expand the "Text Editor" settings and then click on "Font".  In the "Font Family" input box type `Fira Code`, replacing any content.  Tick the check box "Enables/Disables font ligatures" under "Font Ligatures" to enable the special ligatures.

## Manually editing `settings.json`

Visual Studio Code allows you to also edit the underlying `settings.json` config file.  First open the settings editor as described above, then click the "curly brackets" icon to open the `settings.json` file.

Then paste the following lines and save the file.
```json
"editor.fontFamily": "Fira Code",
"editor.fontLigatures": true,
```

If this doesn't work for you, you can try:
1. restarting VS Code;
1. wrapping the "Fira Code" section with additional apostrophes:
    ```json
    "editor.fontFamily": "'Fira Code'",
    "editor.fontLigatures": true,
    ```

### Font weights

To achieve different weights, add one of the following (verified on Mac/Windows 10):
```json
    "editor.fontWeight": "300" // Light
    "editor.fontWeight": "400" // Regular
    "editor.fontWeight": "450" // Retina !! Only works with FiraCode-VF.ttf installed, see below when using separated font files (the normal case).
    "editor.fontWeight": "500" // Medium
    "editor.fontWeight": "600" // Bold
```

To use Retina weight when not using FiraCode-VF.ttf, change fontFamily to `FiraCode-Retina` if on macOS (exactly that, no spaces):
```json
    "editor.fontFamily": "FiraCode-Retina",
```

...or to `Fira Code Retina` if on Windows or Linux:
```json
    "editor.fontFamily": "Fira Code Retina",
```

### Stylistic sets

Since version [1.40](https://code.visualstudio.com/updates/v1_40#_font-feature-settings), you can define stylistic sets in `settings.json`:
```json
"editor.fontLigatures": "'calt', 'ss01', 'ss02', 'ss03', 'ss04', 'ss05', 'ss06', 'zero', 'onum'"
```

To avoid possible bugs, you must uninstall Fira Code 1.x before installing Fira Code 2+.

### Useful extensions

- [Disable ligatures in unwanted contexts](https://marketplace.visualstudio.com/items?itemName=kshetline.ligatures-limited)