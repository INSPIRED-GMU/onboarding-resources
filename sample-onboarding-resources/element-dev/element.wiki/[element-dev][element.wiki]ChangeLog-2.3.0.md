### 新特性
- Table
  - 现在 TableColumn 的 `formatter` 属性可以是动态的，#10184（by @elfman）
  - 新增 `select-on-indeterminate` 属性，#9924（by @syn-zeta）
- Menu
  - 新增 `collapse-transition` 属性，#8809（by @limichange）
- Input
  - 新增 `select` 方法，#10229
  - 新增 `blur` 方法，#10356
- ColorPicker
  - 新增 `predefine` 属性，#10170（by @elfman）
- Tree
  - 新增 `draggable`、`allow-drop` 和 `allow-drag` 属性，以及 `node-drag-start`、`node-drag-enter`、`node-drag-leave`、`node-drag-over`、`node-drag-end` 和 `node-drop` 事件，#9251 #10372（by @elfman）
- Form
  - `validate` 方法新增第二个参数，包含未通过本次校验的表单项信息，#10279
  - 新增 `validate` 事件，#10351
- Progress
  - 新增 `color` 属性，#10352（by @YunYouJun）
- Button
  - 新增 `circle` 属性，#10359（by @YunYouJun）

### 修复
- Form
  - 修复嵌套复合型 Input 时，FormItem 标签与输入框未对齐的问题，#10189
- Menu
  - 现在折叠状态的菜单项仅在传入 `title` slot 时才显示 Tooltip，#10193（by @PanJiaChen）
- Pagination
  - 修复 `current-change` 在未发生用户交互时错误触发的问题，#10247
- DatePicker
  - 现在时间日期选择器下拉面板中的值能够正确地从 `format` 属性中获取对应格式了，#10174（by @remizovvv）
- Upload
  - 现在拖拽上传会拦截不在 `accept` 属性范围内的文件，#10278

##

### New features
- Table
  - Now `formatter` of TableColumn can be dynamically updated, #10184 (by @elfman)
  - Added `select-on-indeterminate` attribute, #9924 (by @syn-zeta)
- Menu
  - Added `collapse-transition` attribute, #8809 (by @limichange)
- Input
  - Added `select` method, #10229
  - Added `blur` method, #10356
- ColorPicker
  - Added `predefine` attribute, #10170 (by @elfman)
- Tree
  - Added `draggable`, `allow-drop` and `allow-drag` attributes, and `node-drag-start`, `node-drag-enter`, `node-drag-leave`, `node-drag-over`, `node-drag-end` and `node-drop` events, #9251 #10372 (by @elfman)
- Form
  - `validate` method now has a second parameter, containing information of form items that failed the validation, #10279
  - Added `validate` event, #10351
- Progress
  - Added `color` attribute, #10352 (by @YunYouJun)
- Button
  - Added `circle` attribute, #10359 (by @YunYouJun)

### Bug fixes
- Form
  - Fixed label of FormItem not align with mixed Input, #10189
- Menu
  - Now collapsed Menu will only show the Tooltip when the `title` slot of MenuItem is set, #10193 (by @PanJiaChen)
- Pagination
  - Fixed `current-change` event wrongly triggering without user interaction, #10247
- DatePicker
  - Now the date and time value in the dropdown panel are correctly formatted based on the `format` attribute, #10174（by @remizovvv）
- Upload
  - Fixed `accept` attribute not working when `drag` is true, #10278