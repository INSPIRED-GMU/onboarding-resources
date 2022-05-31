### 重要
本手册只针对非 SIP003 规范的插件进行配置，如果你是用的插件符合 SIP003 规范，请阅读插件的手册或帮助文档来进行配置。

### 适用版本
4.1.2 及以上

### 环境变量
在 Shadowsocks for Windows 中，可通过环境变量来使用不支持 [SIP003](https://github.com/shadowsocks/shadowsocks-org/wiki/Plugin) 规范的插件。

Shadowsocks for Windows 提供了四个环境变量对插件进行基本的配置：

`%SS_LOCAL_HOST%` `%SS_LOCAL_PORT%` `%SS_REMOTE_HOST%` `%SS_REMOTE_PORT%`

这些环境变量将会告知插件如何配置本机地址、本机端口、远程地址、远程端口。

### 快速入门
下载插件，并保存到 Shadowsocks.exe 所在的目录，或者其他你知道的路径中，例如：
```
D:\Shadowsocks\plugin_windows_amd64.exe
```

阅读插件的手册或说明文件，了解如何配置插件参数，以及如何指定本机地址、本机端口、远程地址和远程端口。

对于大多数情况，可以在命令行（cmd.exe）下使用 `-h` 参数来获得这些信息：
```
plugin_windows_amd64.exe -h
```

打开 Shadowsocks for Windows 的“编辑服务器”对话框，像往常一样填写服务器信息。

在服务器端输入框中，填写服务器端的插件端口号。

在插件程序输入框中，输入插件路径，比如：
```
D:\Shadowsocks\plugin_windows_amd64.exe
```

插件选项保持空白。

在插件参数中，以 [kcptun](https://github.com/xtaci/kcptun) 为例， kcptun 使用`-l`参数来指定`本机地址:本机端口`，使用`-r`参数来指定`远程地址:远程端口`，那么：
```
-l %SS_LOCAL_HOST%:%SS_LOCAL_PORT% -r %SS_REMOTE_HOST%:%SS_REMOTE_PORT% --key <插件密码> --crypt <加密方式> --mode <选择的模式>
```

当一切配置完毕后，点击确定按钮，即可开始工作。

### 疑难解答
如果不工作，打开 Windows 任务管理器，转到进程（或详情）选项卡，检查进程列表，插件程序的文件名是否出现在进程列表中？

如果没有出现，说明可能是由于指定的插件参数存在问题，通常是由于拼写错误或者参数冲突导致的。

如果存在于进程列表中，可能是由于指定的参数变量有误，通常是由于密码不正确、加密协议或者模式不匹配，可配合服务端设置检查配置是否一致。
