## jQuery 3.6.0

See issue tracker for [3.6.0 tickets](https://github.com/jquery/jquery/milestone/22).

## jQuery 4.0.0

See issue tracker for [4.0.0 tickets](https://github.com/jquery/jquery/milestone/7).

## Ongoing work and ideas

* [ ] Migrate jQuery API to Jekyll and GitHub Pages
* [ ] Migrate CI to GitHub Actions and migrate testwarm to karma + browserstack
* [x] Check minified code for syntax errors (see https://github.com/jquery/jquery/issues/3075)
* [ ] Add CSS linter for test CSS to enforce our [CSS styleguide](http://contribute.jquery.org/style-guide/css/).

* [ ] Potential use of new DOM/ES features (e.g., [gh-1868](https://github.com/jquery/jquery/issues/1868) and [gh-1753](https://github.com/jquery/jquery/issues/1753))
  - Historically, new DOM/ES features have not been performant so we'll need to test them and weigh against increased code size and complexity.
  - May need new API surface for things like `.usedStyle` and it may be main-only
  - Replace `document.hidden` with `document.visibilityState`

* [x] Start using ES6 modules and transpile to other formats.

* [ ] Add e2e tests.
  - [ ] focus tests - https://github.com/jquery/jquery/blob/a644101ed04d0beacea864ce805e0c4f86ba1cd1/test/unit/event.js#L2703, https://github.com/jquery/jquery/blob/a644101ed04d0beacea864ce805e0c4f86ba1cd1/test/unit/event.js#L2676

  - [ ] isDefaultPrevented, stopImmediatePropagation - https://github.com/jquery/jquery/blob/a644101ed04d0beacea864ce805e0c4f86ba1cd1/test/unit/event.js#L375

* [ ] Create a Web Download Builder
  - See [gh-1691](https://github.com/jquery/jquery/issues/1691) for background.

* [ ] Add automated code coverage
  - See [gh-1965](https://github.com/jquery/jquery/issues/1965) for background.

* [ ] Run unit tests with XHTML doctype
  - See [gh-1731](https://github.com/jquery/jquery/issues/1731) for background.

## Refactoring efforts

* [ ] Change code style for checking method presence
  - See [gh-3221](https://github.com/jquery/jquery/pull/3221) for background

* [ ] Rewrite speed framework

* [x] Investigate possible unnecessary modularization of some variables

* [x] Investigate possible reuse of support divs
  - See [gh-2405](https://github.com/jquery/jquery/issues/2405) for background

* [ ] Investigate implementing jQuery (specifically .init) as an Array subclass
  - See [gh-1754](https://github.com/jquery/jquery/issues/1754) for background

* [x] Remove grunt-npmcopy and pull dependencies from `node_modules`.

* [ ] Drop support for EdgeHTML when the market share is low enough
  - See [gh-4568](https://github.com/jquery/jquery/issues/4568) for background