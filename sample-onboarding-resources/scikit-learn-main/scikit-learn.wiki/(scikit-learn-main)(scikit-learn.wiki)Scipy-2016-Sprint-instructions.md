I tagged some issues with "sprint" that might be good entry points: https://github.com/scikit-learn/scikit-learn/issues?q=is%3Aopen+is%3Aissue+label%3ASprint
other good tags are "easy" and "needs contributor"

You can find the contributor guide here: http://scikit-learn.org/dev/developers/index.html
Please start with something very simple, happy to talk about more complicated issues.

You can also start reviewing other pull requests, or see if there are pull requests that have been stalled for a long time.

Before you start working on an issue, please comment on it, saying you are working on it, so that we don't do duplicate work.

When changing any behavior, it is important that you don't actually change anything, but instead deprecate the current behavior and warn about future changes, as explained in the deprecation guide: http://scikit-learn.org/dev/developers/contributing.html#deprecation