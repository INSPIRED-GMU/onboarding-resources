1. Download the [`Terminal.wprp` file from this repository](https://github.com/microsoft/terminal/blob/main/src/Terminal.wprp) somewhere on your PC. For example, let's put the file at `C:\path\to\Terminal.wprp`
2. From an elevated commandline, run:
```
wpr -start C:\path\to\Terminal.wprp!Terminal.Verbose
```
3. Reproduce the error.
4. Go back to the elevated commandline window and run:
```
wpr -stop terminal-trace.etl
```
5. Take the `terminal-trace.etl` file and send it to the person who requested that you follow this guide.