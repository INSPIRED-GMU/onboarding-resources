## Enabling

In a workspace:

1. Click goormIDE, then Preferences.
2. Go to Theme, then focus Custom Theme CSS.
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

.editor_container pre {
    -webkit-font-feature-settings: "liga" on, "calt" on;
    -webkit-font-smoothing: antialiased;
    text-rendering: optimizeLegibility;
    font-family: 'Fira Code';
}
```

4. Click Aplly or OK
5. Happy coding!