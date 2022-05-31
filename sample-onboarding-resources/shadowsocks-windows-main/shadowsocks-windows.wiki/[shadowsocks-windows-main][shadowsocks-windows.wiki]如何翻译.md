适用于4.1.9.2及以上版本

1. 找到你的语言的ISO 639-1代码
    - 在日志中搜索`Current language is:`
    - 或者在[此](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes)查找
2. 输出翻译模板
    1. 打开程序
    2. 右键点击任务栏图标
    3. 点击`Help` > `Write translation template`
    4. 程序所在目录下会生成`i18n.csv`
3. 编辑`i18n.csv`
    1. 添加一列，标题为语言的ISO 639-1代码
    2. 在新添加的列中翻译

保存文件，重新启动程序以应用翻译。

如果使用文本编辑器，请参照[CSV格式标准](https://tools.ietf.org/html/rfc4180)。