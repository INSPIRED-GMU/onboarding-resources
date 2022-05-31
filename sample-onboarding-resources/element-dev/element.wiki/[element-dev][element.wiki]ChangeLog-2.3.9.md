- 修复当 TableColumn 的 `prop` 属性指定的字段在数据源中不存在时，鼠标移入该列单元格会报错的问题，#11137
- 弹出类组件的 `lockScroll` 属性不再为父元素添加内联样式，而是添加相应类名，#11114
- 修复 Progress 在 `status` 为 exception 时图标不显示的问题，#11172
- 修复可搜索的 Cascader 在输入关键词后，选项的 `disabled` 属性失效的问题，#11185
- 修复可展开的 Table 在展开某一行后更新数据源会造成该行无法收起的问题，#11186
- Tree 的 `setCurrentKey` 方法支持传入 `null`，可取消当前高亮的节点，#11205

##

- Fixed when the source data does not have the field specified by a TableColumn's `prop` attribute, an error would occur when the mouse moves into that column's cells, #11137
- The `lockScroll` attribute of pop up components no longer adds an inline style to the parent element, but instead adds a class name, #11114
- Fixed the icon of Progress not displaying when its `status` is exception, #11172
- Fixed options' `disabled` attribute not working in filterable Cascader's filter result list, #11185
- Fixed an issue where Table's expanded row cannot be collapsed if the data source is updated after its expansion, #11186
- `setCurrentKey` of Tree now accepts `null` as its param to cancel the currently highlighted node, #11205