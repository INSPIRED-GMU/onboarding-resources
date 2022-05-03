In the terminal:
1. Use the keyboard shortcut <kbd>CTRL</kbd> + <kbd>SHIFT</kbd> + <kbd>J</kbd> to open the JavaScript Console.
2. Copy & paste the following 3 commands:
```
term_.prefs_.set('font-family', '"Fira Code", Cousine, "Roboto Mono", "Source Code Pro", monospace');
term_.prefs_.set('user-css-text', "x-row { font-feature-settings: 'liga', 'calt', 'ss01', 'ss02', 'ss03', 'ss04', 'ss05', 'ss06', 'ss07'; text-rendering: optimizeLegibility; }")
term_.prefs_.set('user-css', 'https://cdn.jsdelivr.net/npm/firacode@latest/distr/fira_code.min.css')
```

Note: The values for font-feature-settings can be tuned to your preference. For more details see the documentation at [stylistic sets](./How-to-enable-stylistic-sets)