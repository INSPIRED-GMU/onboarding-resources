## Any component from [react-component](https://github.com/react-component) should be named with prefix `Rc`.

```jsx
// Good
import RcSlider from 'rc-slider';

// Bad
import Slider from 'rc-slider';
```

## All the components of antd should use its name in documentation.

```jsx
// Good
class Button extends React.Component {}

// Bad
class AntButton extends React.Component {}
```

This will make it more clear in developer tool.

![image](https://cloud.githubusercontent.com/assets/3580607/13939937/4e680a1c-f014-11e5-849f-c9512cc46563.png)

## Extends `React.Component` instead of `Component`

```jsx
// Good
import React from 'react';
class Button extends React.Component {}

// Bad
import React, { Component } from 'react';
class Button extends Component {}
```

## Bind `this` in class definition with ES6 syntax

```jsx
// Good
class Button extends React.Component {
  onClick = () => {}

  render() {
    return <button onClick={this.onClick} />
  }
}

// Bad
class Button extends React.Component {
  onClick() {}

  render() {
    return <button onClick={this.onClick.bind(this)} />
  }
}

// Bad
class Button extends React.Component {
  constructor(props) {
    super(props);

    this.onClick = this.onClick.bind(this);
  }

  onClick() {}

  render() {
    return <button onClick={this.onClick} />
  }
}
```

## Define static property in class definition

```jsx
// Good
class Button extends React.Component {
  static propTypes = {...}
  static defaultProps = {...}
}

// Bad
class Button extends React.Component {}
Button.propTypes = {...};
Button.defaultProps = {...};
```