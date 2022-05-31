```mermaid
  flowchart TD
    A[Is it supported?] --> B{Does it exist?};
    B -- Yes --> C[No, it is being deprecated.];
    B -- No --> D[Yes, it will be supported soon.];
```