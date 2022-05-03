## Make sure you actually installed Fira Code 

See [Installing](https://github.com/tonsky/FiraCode/wiki/Installing)

## Make sure the font your editor displays is actually Fira Code

Easiest way is to compare the shape of `@` `&` and `r` with the reference image:

![](https://user-images.githubusercontent.com/285292/26971424-c609be76-4d15-11e7-8684-23e7b1c08929.png)

Issues: [#393](https://github.com/tonsky/FiraCode/issues/393) [#373](https://github.com/tonsky/FiraCode/issues/373) [#227](https://github.com/tonsky/FiraCode/issues/227)

## Make sure you’ve enabled ligatures in your editor

Consult this wiki (see above ↑) for instruction on how to do that.

Issues: [#291](https://github.com/tonsky/FiraCode/issues/291)

## Make sure you’re on the latest version of Fira Code

Consult [CHANGELOG](https://github.com/tonsky/FiraCode/blob/master/CHANGELOG.md) to see when it was last updated.

## Characters look weird, not monospaced, not rendered at all

Some Unicode characters are not in Fira Code. You can start by checking [Fira Mono doc](https://github.com/bBoxType/FiraSans/raw/master/Fira_Mono_3_2/PDF/FiraMono-Regular.otf.pdf) and [Fira Code Changelog](https://github.com/tonsky/FiraCode/blob/master/CHANGELOG.md).

If character is missing, you’ll see glyphs from a fallback font chosen by your system, which might have drastically different look and metrics. Create an issue and I’ll try to add it to the Fira Code in the next version.

Issues: [#812](https://github.com/tonsky/FiraCode/issues/812), [#811](https://github.com/tonsky/FiraCode/issues/811), [#800](https://github.com/tonsky/FiraCode/issues/800), [#796](https://github.com/tonsky/FiraCode/issues/796)

## Font looks blurry/bad on Linux/Windows

Make sure you installed TTF, not OTF files. Issues: [#798](https://github.com/tonsky/FiraCode/issues/798#issuecomment-579094899)

## Hinting issues

Known problem, can’t be easily fixed.

* Uneven spacing in `===` and `!==` at certain font sizes, esp. on Windows [#405](https://github.com/tonsky/FiraCode/issues/405) [#243](https://github.com/tonsky/FiraCode/issues/243) [#119](https://github.com/tonsky/FiraCode/issues/119) [#114](https://github.com/tonsky/FiraCode/issues/114). The issue with `===` could be worked around by increasing/decreasing the font size by 0.5, so go from 12 to 12.5 or from 13.5 to 13.0 and test.


* Different height of `[]` at certain font sizes [#332](https://github.com/tonsky/FiraCode/issues/332) [#251](https://github.com/tonsky/FiraCode/issues/251)

## Powerline characters are of slightly wrong size

Unfortunately this can’t be fixed for all terminals because they have different ways of calculate font metrics. See [this comment](https://github.com/tonsky/FiraCode/issues/44#issuecomment-187305276)

Issues: [#426](https://github.com/tonsky/FiraCode/issues/426) [#131](https://github.com/tonsky/FiraCode/issues/131) [#44](https://github.com/tonsky/FiraCode/issues/44)

## Some ligatures work while some don’t

This is an issue with your editor and how it handles tokenization/syntax highlighting. Nothing can be done in a font to work around that. Report your problem to the corresponding editor’s issue tracker.

- All ligatures with dashes in Visual Studio (not Code) [#422](https://github.com/tonsky/FiraCode/issues/422) [#395](https://github.com/tonsky/FiraCode/issues/395) [#360](https://github.com/tonsky/FiraCode/issues/360) [#273](https://github.com/tonsky/FiraCode/issues/273) [#259](https://github.com/tonsky/FiraCode/issues/259) [#233](https://github.com/tonsky/FiraCode/issues/233) [#220](https://github.com/tonsky/FiraCode/issues/220) [#196](https://github.com/tonsky/FiraCode/issues/196) [#181](https://github.com/tonsky/FiraCode/issues/181) [#157](https://github.com/tonsky/FiraCode/issues/157) [#99](https://github.com/tonsky/FiraCode/issues/99) [#43](https://github.com/tonsky/FiraCode/issues/43) [#32](https://github.com/tonsky/FiraCode/issues/32)

- Ligatures in column 100 in VS Code [#403](https://github.com/tonsky/FiraCode/issues/403) [#397](https://github.com/tonsky/FiraCode/issues/397) [#372](https://github.com/tonsky/FiraCode/issues/372)

- Atom/VS Code are known to break certain ligatures in certain syntaxes [#361](https://github.com/tonsky/FiraCode/issues/361) [#353](https://github.com/tonsky/FiraCode/issues/353) [#348](https://github.com/tonsky/FiraCode/issues/348) [#328](https://github.com/tonsky/FiraCode/issues/328) [#326](https://github.com/tonsky/FiraCode/issues/326) [#235](https://github.com/tonsky/FiraCode/issues/235)

## Corrupted font in IntelliJ on Windows

Go to `C:\Windows\Fonts` with `cmd.exe`, find and delete everything having Fira in the file name. It’s important that you use terminal commands, not Explorer.

Issues: [#589](https://github.com/tonsky/FiraCode/issues/589) [#581](https://github.com/tonsky/FiraCode/issues/581) [#398](https://github.com/tonsky/FiraCode/issues/398) [IDEA-159901](https://youtrack.jetbrains.com/issue/IDEA-159901)

## No italics/bad italics

Fira Code does not have italics at all. If you see italicized glyphs it means your editor is “faking” them. 

Issues: [#375](https://github.com/tonsky/FiraCode/issues/375) [#320](https://github.com/tonsky/FiraCode/issues/320) [#281](https://github.com/tonsky/FiraCode/issues/281)

## Not recognized as monospace by fontconfig (e.g. in Kitty)

Issues: [#840](https://github.com/tonsky/FiraCode/issues/840)