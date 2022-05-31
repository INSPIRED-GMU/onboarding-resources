### 新特性
- Menu
  - SubMenu 新增 `popper-class` 和 `disabled` 属性，#9604 #9771
  - 现在水平模式下的 Menu 支持多级 SubMenu 了，#9741
- Tree
  - 新增 `node-contextmenu` 事件，#9678
  - 现在可以使用 scoped slot 自定义树节点的模板了，#9686
  - 新增 `getNode`、`remove`、`append`、`insertBefore`、`insertAfter`、`getCheckedKeys`、`getHalfCheckedNodes`、`getHalfCheckedKeys` 方法和 `check` 事件，#9718 #9730
- Transfer
  - 新增 `clearQuery` 方法，#9753
- Select
  - 新增 `popper-append-to-body` 属性，#9782

### 修复
- Table
  - 修复点击可展开行的展开图标会触发 `row-click` 事件的问题，#9654
  - 修复某些情况下通过拖动改变列宽后，布局没有同步更新的问题，#9668
  - 修复合计行与固定列并存时的样式问题，#9667
- Container
  - 修复布局组件在 IE11 中无法自动填充可用空间的问题，#9655
- Loading
  - 修复在 `mounted` 中修改 `v-loading` 的值为 true 时不能正确显示 Loading 的问题，#9722
- Switch
  - 修复点击时会触发两次原生 click 事件的问题，#9760

##

### New features
- Menu
  - Added `popper-class` and `disabled` attributes for SubMenu, #9604 #9771
  - Horizontal Menu now supports multi-layered SubMenu, #9741
- Tree
  - Added `node-contextmenu` event, #9678
  - Now you can customize node template using scoped slot, #9686
  - Added `getNode`, `remove`, `append`, `insertBefore`, `insertAfter`, `getCheckedKeys`, `getHalfCheckedNodes`, `getHalfCheckedKeys` methods and `check` event, #9718 #9730
- Transfer
  - Added `clearQuery` method, #9753
- Select
  - Added `popper-append-to-body` attribute, #9782

### Bug fixes
- Table
  - Fixed clicking expanding icon of an expandable row triggers `row-click` event, #9654
  - Fixed layout not update when column width is changed by user dragging, #9668
  - Fixed style issue when summary row co-exists with fixed columns, #9667
- Container
  - Fixed container components not stretching in IE11, #9655
- Loading
  - Fixed Loading not showing when the value of `v-loading` is changed to true in the `mounted` hook, #9722
- Switch
  - Fixed two native click events are triggered when Switch is clicked, #9760