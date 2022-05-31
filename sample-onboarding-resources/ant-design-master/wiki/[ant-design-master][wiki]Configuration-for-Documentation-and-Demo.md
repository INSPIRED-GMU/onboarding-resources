We use [YAML](http://yaml.org/) to set the configuration of documentation.

```yaml
---
order: 1
title: Introduction
---
```

---

Configurations of documentation and demo are different.

### Demo

If a Markdown file is under a folder named `demo`, it is a demo. Here is an [example](https://github.com/ant-design/ant-design/blob/e1a6123aa6a4cf47b3be8d681692b7256d4485c6/components/checkbox/demo/controller.md).

- `title: string | Object` The title of demo. If it is an object, it has the following fields:
  - `zh-CN: string`
  - `en-US: string`
- `debug: boolean` This demo is just for debugging, and it will be threw away while building.
- `order: number` The order of demo. 
  > Normal demo should start from `0` to `n`, demo for debugging should start from `-1` to `-n`.
- `only: boolean` Only show this demo. It's useful to debug locally.

### Documentation

If a Markdown file is not a demo, it is a documentation. e.g.: https://github.com/ant-design/ant-design/blob/e1a6123aa6a4cf47b3be8d681692b7256d4485c6/components/checkbox/index.md

- `category: string` 文档分类，可自行定义。
- `order: number` 在当前分类下的展示顺序。
- `type: string` 组件类型，特别针对组件文档，目前有 `基本` `表单` `展示` `导航` `其他`。
- `title: string | Object` 文档标题，与演示标题一致支持多语言设置。
- `subtitle: string | Object` 文档副标题，与演示标题一致支持多语言设置。
- `cols:1 | 2` 页面代码演示区块的展示列数，默认为 `2`，对于演示宽度不够的组件可设置为 `1`。
- `disabled: boolean` 使侧边菜单的链接不可点。