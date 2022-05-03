## Source
To get this font to work with MATLAB, you have to load the TTFs into the MATLAB JRE font directory as described in this [link at Mathworks](https://www.mathworks.com/matlabcentral/answers/514119-can-i-add-custom-fonts-to-my-matlab-desktop-in-preferences).

## Summary
To use this font with MATLAB for Windows 10 64-bit:
1. Load the font TTF files into: `MATLAB\<ver>\sys\java\jre\win64\jre\lib\fonts`
1. Restart MATLAB 
1. Change the font in **Preferences** -> **Fonts** as you wish

### Confirmed Case
This was confirmed working with Windows 10, MATLAB2020a 64-bit on with Fira Code v5.2.