Stylistic sets allow you to access additional, optional parts of the font on a per-feature basis. In Fira Code, they allow you to enable/disable alternative character variants.

Fira Code v6 supports these stylistic sets:

![](https://raw.githubusercontent.com/tonsky/FiraCode/master/extras/character_variants.png)
![](https://raw.githubusercontent.com/tonsky/FiraCode/master/extras/ligature_variants.png)

You can enable stylistic sets **only if your editor supports it.**

# Atom

Go to `Atom` -> `Stylesheet`, add:

```css
atom-text-editor {
  font-feature-settings: "ss01", "ss02", "ss03", "ss04", "ss05", "ss06", "zero", "onum";
}
```
# iTerm2

Go to `iTerm2` -> `Preferences` -> `Advanced` and scroll to the `Drawing` section, then change:
 
`Improves drawing performance at the expense of disallowing alphanumeric characters to belong to ligatures.` to `No`

# Sublime Text

Go to `Sublime Text` -> `Preferences` -> `Settings`, add:

```json
"font_options": ["ss01", "ss02", "ss03", "ss04", "ss05", "ss06", "ss07"]
```

For now Sublime Text [does not allow you to specify `zero` and `onum` features](https://github.com/SublimeTextIssues/Core/issues/2302).

# VS Code

Since version [1.40](https://code.visualstudio.com/updates/v1_40#_font-feature-settings), you can define in `settings.json`:
```json
"editor.fontLigatures": "'ss01', 'ss02', 'ss03', 'ss04', 'ss05', 'ss06', 'zero', 'onum'"
```

To avoid possible bugs, you must uninstall Fira Code 1.x before installing Fira Code 2+.

# CSS

```css
.monaco-editor {
  font-feature-settings: "ss01", "ss02", "ss03", "ss04", "ss05", "ss06", "zero", "onum";
}
```

# RStudio

Create or edit an [`rstheme` file](https://rstudio.github.io/rstudio-extensions/rstudio-theme-creation.html#testing-changes-to-a-theme) and add:

```css
.ace_editor {
  font-feature-settings: "ss01", "ss02", "ss03", "ss04", "ss05", "ss06", "zero", "onum";
}
```

# Kitty

Select which font variant you wish to use (Regular, Medium, Light, ...) and set that as your font on the kitty's config file (`~/.config/kitty/kitty.conf`), for instance:

```
font_family      Fira Code Regular
```

Then fetch the PS Name (the value between parenthesis) of the chosen font variant using kitty:

``` shell
$ kitty + list-fonts --psnames | grep "Fira Code Regular"
    Fira Code Regular (FiraCode-Regular)
```

Finally use the PS Name setting the following key in the `kitty.conf` file:

``` 
font_features FiraCode-Regular +ss01 +ss02 +ss03 +ss04 +ss05 +ss07 +ss08 +zero +onum
```

# Wez’s terminal

```lua
return {
  harfbuzz_features = {"zero" , "ss01", "cv05"}
}
```

Full instruction [here](https://wezfurlong.org/wezterm/config/font-shaping.html).

# Windows Terminal

Open the Windows Terminal settings.json file. You will need to insert a [font object](https://docs.microsoft.com/en-us/windows/terminal/customize-settings/profile-appearance#font) for Fira Code in one or more profiles:

An example font object:
```json
    "font": {
        "face": "Fira Code",
        "features": {
            "ss01": 1,
            "ss02": 1,
            "ss03": 1,
            "ss04": 1,
            "ss05": 1,
            "ss06": 1,
            "zero": 1,
            "onum": 1
        }
    }
```

# Some Apple apps

![](https://user-images.githubusercontent.com/285292/64178997-0f98b780-ce6b-11e9-8091-34eab83ca288.png)

# Adobe apps, MS Word etc

https://www.macworld.com/article/3052388/how-to-access-advanced-opentype-features-in-a-variety-of-mac-apps.html

# Baking in stylistic sets into the font file

This might be an option if your editor does not let you choose stylistic sets on the fly https://github.com/twardoch/fonttools-opentype-feature-freezer