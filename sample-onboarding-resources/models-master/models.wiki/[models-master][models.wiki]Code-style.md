# Python coding style

Changes to Python code should conform to
[Google Python Style Guide](https://github.com/google/styleguide/blob/gh-pages/pyguide.md)

Use `pylint` to check your Python changes.

To install `pylint` and check a file
with `pylint` against TensorFlow's custom style definition:

**Please use Pylint version 2.4.4. and the [pylint configuration file](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/tools/ci_build/pylintrc)
available from TensorFlow.**


```bash
pip install pylint==2.4.4
pylint --rcfile=pylintrc myfile.py
```
Be sure to run it before you push your commits.

## TensorFlow Conventions

Follow the guidance in the [TensorFlow Style Guide - Conventions](https://www.tensorflow.org/community/contribute/code_style#tensorflow_conventions_and_special_uses).

## Coding style for other languages

* [Google C++ Style Guide](https://google.github.io/styleguide/cppguide.html).
* [Google Java Style Guide](https://google.github.io/styleguide/javaguide.html)
* [Google JavaScript Style Guide](https://google.github.io/styleguide/jsguide.html)
* [Google Shell Style Guide](https://google.github.io/styleguide/shell.xml)
* [Google Objective-C Style Guide](https://google.github.io/styleguide/objcguide.html)

## License

Include a license at the top of new files.

* [C/C++ license example](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/core/framework/op.cc#L1)
* [Python license example](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/ops/nn.py#L1)
* [Java license example](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/java/src/main/java/org/tensorflow/Graph.java#L1)
* [Go license example](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/go/operation.go#L1)
* [Bash license example](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/tools/ci_build/ci_sanity.sh#L2)
* [HTML license example](https://github.com/tensorflow/tensorboard/blob/master/tensorboard/components/tf_backend/tf-backend.html#L2)
* [JavaScript/TypeScript license example](https://github.com/tensorflow/tensorboard/blob/master/tensorboard/components/tf_backend/backend.ts#L1)
