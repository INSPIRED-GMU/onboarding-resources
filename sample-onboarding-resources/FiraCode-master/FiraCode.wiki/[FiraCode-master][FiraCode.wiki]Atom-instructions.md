## Installation

Make sure you [install the font](https://github.com/tonsky/FiraCode/wiki/Installing).

To change your font to Fira Code, open Atom's preferences (`cmd+,` on Mac or `ctrl+,` on PC), make sure the "Settings" tab is selected, or the "Editor" in Atom 1.10 and forth, and scroll down to "Editor Settings". In the "Font Family" field, enter `Fira Code`.

If you wish to specify a font weight, specify the weight following a space (if Windows, e.g. `Fira Code Light`) or as `FiraCode-Light` (if Mac).

## Ligatures

Ligatures are enabled by default in Atom 1.9 and above.

To enable ligatures on older Atom versions (Atom 1.1 and newer), go to `Menu → Stylesheet...`

![](https://i.imgur.com/sulSOtK.png)

and add `text-rendering` to `atom-text-editor`:

```css
atom-text-editor {
  text-rendering: optimizeLegibility;
}
```

Beware that in some syntaxes **selected ligatures might not work**. This is usually a syntax parser/tokenization issue (e.g. `->` breaks into two symbols by JS/Ruby syntax highlighter). See issues [#63](https://github.com/tonsky/FiraCode/issues/63) and [#69](https://github.com/tonsky/FiraCode/issues/69)

To turn off ligatures inside of strings and regular expressions you can add this to your stylesheet:

```css
atom-text-editor.editor .syntax--string.syntax--quoted,
atom-text-editor.editor .syntax--string.syntax--regexp {
  -webkit-font-feature-settings: "liga" off, "calt" off;
}
```

If there is any other place that you find you do not want to see ligatures, place your cursor on the location, hit `Ctrl+Alt+Shift+P` and add the bottom-most selector listed in the popup notification to the rule above.