On Windows by default both Chrome and Firefox use ANGLE based rendering backend.

ANGLE is a translation layer between OpenGL ES 2.0 API calls and DirectX 9 API calls:

https://code.google.com/p/angleproject/

If your computer has decent OpenGL drivers, you should be able to run WebGL also using native OpenGL API rendering backend.

## Chrome

For using OpenGL in Chrome, you need to start it with a command line option:

```
chrome.exe --use-angle=gl
```

For example you could create a separate shortcut and add this flag in `properties -> target`.

Please note that all existing Chrome instances need to be closed before starting new Chrome with a flag, otherwise new Chrome window will be just a clone of the current running instance started without a flag.

If you have Chrome Canary installed in addition to other Chrome channel, it can be run in parallel with  different flags (e.g you can have stable Chrome with ANGLE and Chrome Canary with OpenGL opened both at the same time).

## Firefox

For using OpenGL in Firefox you need to change the runtime option. Type into address bar: 

```
about:config
```

Find `webgl.disable-angle` option and set its value to `true`. The effect is immediate, Firefox doesn't need to be restarted. ([source](http://www.geeks3d.com/20130611/webgl-how-to-enable-native-opengl-in-your-browser-windows/))
