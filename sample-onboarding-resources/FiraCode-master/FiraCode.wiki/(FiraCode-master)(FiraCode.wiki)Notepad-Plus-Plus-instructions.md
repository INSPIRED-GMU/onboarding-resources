## Installation on Notepad++

Make sure you [install the font](https://github.com/tonsky/FiraCode/wiki/Installing).

### Enable the font

* Select the font in **Notepad++** via _**`Settings `**_> _**`Style Configurator...`**_ > _**`Global Styles`**_> _**`Global Override`**_.
>![Menu](https://user-images.githubusercontent.com/9272498/93482134-fb342b00-f8c4-11ea-98af-8d304101ce79.png)
* Select *Fira Code* for the font style, turn on _**`Enable global font`**_ and save & close.
>![Configurator window](https://user-images.githubusercontent.com/9272498/93482280-2880d900-f8c5-11ea-8823-78349b5f8878.png)

![Font enabled example code](https://user-images.githubusercontent.com/9272498/93486649-0fc6f200-f8ca-11ea-8451-91dd87eb99a3.png)

### Enable DirectWrite

Scintilla is the text editor control within Notepad++. Enabling DirectWrite in Scintilla lets Windows do some Windows-y things to the text drawn to screen, like rendering the advanced typography features of OpenType.

#### For Notepad++ v7.8.8 and newer
* Open Preferences dialog via _**`Settings `**_> _**`Preferences...`**_
* Enable DirectWrite via _**`MISC.`**_> _**`Use DirectWrite (May improve rendering special characters, need to restart Notepad++)`**_
* Restart Notepadd++

#### For older Notepad++ versions
You need to install **LuaScript** plugin:

* Open the Plugins admin via _**`Plugins`**_ > _**`Plugins Admin...`**_
> ![PLugins menu](https://user-images.githubusercontent.com/9272498/93486915-54eb2400-f8ca-11ea-8060-6fc01beddae5.png)
* Find **LuaScript**, select it, and click on **Install**
> ![Plug-ins admin](https://user-images.githubusercontent.com/9272498/93487307-bf9c5f80-f8ca-11ea-840c-d46b7d39965e.png)
* Edit the **LuaScript** startup file in **_`Plugins `_**> _**`LuaScript `**_> _**`Edit Startup Script`**_ and add the following code:
>![startup.lua](https://user-images.githubusercontent.com/9272498/93484627-c5dd0c80-f8c7-11ea-9b0c-cbb79559c1d3.png) <br>
> editor1.Technology = SC_TECHNOLOGY_DIRECTWRITE <br>
> editor2.Technology = SC_TECHNOLOGY_DIRECTWRITE
* Restart Notepadd++

![ligatures installed](https://user-images.githubusercontent.com/9272498/93487921-6123b100-f8cb-11ea-984d-15df0458c81a.png)



> Based on instructions provided in https://stegriff.co.uk/upblog/enable-ligatures-and-emoji-in-notepad-plus-plus/

