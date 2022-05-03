In a workspace:
1. Click **Cloud9**, then **Preferences** (or use keyboard shortcut <kbd>CTRL</kbd> + <kbd>,</kbd>)
2. Go to **Themes**, then click on **You can also style Cloud9 by editing _your stylesheet_** (this will open a blank _styles.css_ file in the C9 editor)
3. Copy & paste the following:
```css
@font-face{
    font-family: 'Fira Code';
    src: url('https://raw.githubusercontent.com/tonsky/FiraCode/5.2/distr/woff2/FiraCode-Regular.woff2') format('woff2'),
         url('https://raw.githubusercontent.com/tonsky/FiraCode/5.2/distr/woff/FiraCode-Regular.woff') format('woff'),
         url('https://raw.githubusercontent.com/tonsky/FiraCode/5.2/distr/ttf/FiraCode-Regular.ttf') format('truetype');
    font-weight: normal;
    font-style: normal;
}

.ace_editor{
    -webkit-font-feature-settings: "liga" on, "calt" on;
    -webkit-font-smoothing: antialiased;
    text-rendering: optimizeLegibility;
    font-family: 'Fira Code';
}
```
4. Back in **Preferences** tab, click on **User Settings**, then click on **Code Editor (Ace)**
5. In **Font Family** field, enter **_Fira Code_**
6. Optionally, repeat step 5 for **Preferences** > **User Settings** > **Terminal**, if you want Fira Code font in C9 terminal.