Feel free to contribute to antd Cookbook by adding a snippet you've found useful.

## Re-use locale config for `Popconfirm` `Modal` etc...

There is no `locale` property on `Popconfirm`. So, we have to set button text by `okText` and `cancelText`, it is inconvenient to re-use locale config for different components. However, we can set properties by [spreading attributes](https://facebook.github.io/react/docs/jsx-spread.html#spread-attributes), which makes re-use locale config easier.

```jsx
const locale = {
  okText: 'Yes',
  cancelText: 'No',
};

<Popconfirm {...locale} title="Are you sure?">
  <a href="#">Delete</a>
</Popconfirm>
```