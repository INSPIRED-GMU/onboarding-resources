## 新特性
- 综合
  - 新增全局配置组件尺寸的功能

    在引入 Element 时，配置 `size` 字段可以改变所有组件的默认尺寸。按照引入 Element 的方式，具体操作如下：
    
    完整引入 Element：
    ```JS
    import Vue from 'vue'
    import Element from 'element-ui'
    Vue.use(Element, { size: 'small' })
    ```
    
    按需引入 Element：
    ```JS
    import Vue from 'vue'
    import { Button } from 'element-ui'

    Vue.prototype.$ELEMENT = { size: 'small' }
    Vue.use(Button)
    ```
    按照以上设置，项目中所有拥有 `size` 属性的组件的默认尺寸均为 'small'。

- Loading
  - 配置对象新增 `spinner` 和 `background` 字段，支持自定义加载图标和背景色，#7390
- Autocomplete
  - 新增 `debounce` 属性，#7413
- Upload
  - 新增 `limit` 和 `on-exceed` 属性，支持对上传文件的个数进行限制，#7405
- Menu
  - 新增 `open` 和 `close` 方法，支持手动打开和关闭 SubMenu，#7412
- DatePicker
  - 新增 `value-format` 属性，支持对绑定值的格式进行自定义，#7367
- TimePicker
  - 新增 `arrow-control` 属性，提供另一种交互形式，#7438
- DateTimePicker
  - 新增 `time-arrow-control` 属性，用于开启时间选择器的 `arrow-control`，#7438
- Form
  - Form 和 Form-item 新增 `size` 属性，用于控制表单内组件的尺寸，#7428
  - `validate` 方法在不传入 callback 的情况下返回 promise，#7405

## 修复
- 修复部分组件的 `Injection "elFormItem" not found` 报错

## 非兼容性更新
- DatePicker 的 `change` 事件参数现在为组件的绑定值，格式由 `value-format` 控制
- Input 组件的 `change` 事件现在仅在输入框失去焦点或用户按下回车时触发，与原生 input 元素一致。如果需要实时响应用户的输入，可以使用 `input` 事件
- 最低兼容 Vue 2.5.2 版本

#

## New features
- General
  - Configure component sizes globally

    Now when you import Element, you can add a global config object with a `size` prop to configure default sizes for all components:
    
    Fully import:
    ```JS
    import Vue from 'vue'
    import Element from 'element-ui'
    Vue.use(Element, { size: 'small' })
    ```
    
    Partial import:
    ```JS
    import Vue from 'vue'
    import { Button } from 'element-ui'

    Vue.prototype.$ELEMENT = { size: 'small' }
    Vue.use(Button)
    ```
    With the above config, the default size of all components that have `size` attribute will be 'small'.

- Loading
  - Now you can customize spinner icon and background color with `spinner` and `background` prop, #7390
- Autocomplete
  - Added `debounce` attribute, #7413
- Upload
  - Added `limit` and `on-exceed` attributes to limit the amount of files, #7405
- Menu
  - Added `open` and `close` methods to open and close SubMenu programmatically, #7412
- DatePicker
  - Added `value-format` attribute to customize the format of the binding value, #7367
- TimePicker
  - Added `arrow-control` attribute to spin the time with arrows #7438
- DateTimePicker
  - Added `time-arrow-control` attribute to activate `arrow-control` of the nesting TimePicker, #7438
- Form
  - Form and Form-item now have a `size` attribute. Inner components will inherit this size if not specified on themselves, #7428
  - `validate` method will now return a promise if the callback is omitted, #7405

## Fixes
- Fixed the console warning `Injection "elFormItem" not found` of some components

## Breaking changes
- The params of DatePicker's `change` event is now the binding value itself. Its format is controlled by `value-format`
- Input's `change` event now behaves like the native input element, which triggers only on blur or pressing enter. If you need to respond to user input in real time, you can use `input` event.
- Only compatible with Vue 2.5.2 and beyond