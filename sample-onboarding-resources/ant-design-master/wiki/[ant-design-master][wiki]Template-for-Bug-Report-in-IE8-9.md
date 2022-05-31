```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <!-- 引入样式 -->
    <link rel="stylesheet" href="https://npmcdn.com/antd/dist/antd.css">
    <!-- Polyfills -->
    <!--[if lt IE 10]>
    <script src="https://npmcdn.com/es5-shim@4.5.8/es5-shim.js"></script>
    <script src="https://npmcdn.com/es5-shim@4.5.8/es5-sham.js"></script>
    <script src="https://as.alipayobjects.com/g/component/??console-polyfill/0.2.2/index.js,html5shiv/3.7.2/html5shiv.min.js,media-match/2.0.2/media.match.min.js"></script>
    <script src="https://npmcdn.com/jquery@1.x"></script>
    <![endif]-->
    <script src="https://npmcdn.com/react@0.14.8/dist/react"></script>
    <script src="https://npmcdn.com/react-dom@0.14.8/dist/react-dom"></script>
    <script src="https://npmcdn.com/antd/dist/antd.js"></script>
    <style>body { margin: 100px; }</style>
  </head>
  <body>
    <div id="example"></div>
  </body>
  <script>
    ReactDOM.render(
      React.createElement(antd.DatePicker),
      document.getElementById('example')
    );
  </script>
</html>
```

You can use [babel playground](http://babeljs.io/repl/) for transform.