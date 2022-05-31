## Deprecating a method or property

Here are some things that contributors wanting to deprecate old code may have to keep in mind:

* Before making any changes, install all the npm modules that jquery's build process depends on by running `npm install`.

* For deprecation, a function is usually **moved** from its original position to its own file under`src/`. This file is then referenced from all the usages blocks by passing it within `define` and then accepting a parameter by the functions name within the subsequent anonymous function. [This commit](https://github.com/jquery/jquery/commit/bb4d888f4f7886371347b59eae5d4e6135acb7ed) is a good example.

* If the function was exposed through the jQuery variable, the function needs to be added as a reference under `src/deprecated.js`. Refer to [this line for an example](https://github.com/jquery/jquery/blob/3.2.1/src/deprecated.js#L38). 

* The corresponding tests are moved from its original position to `test/unit/deprecated.js`.

* Now when you run `grunt test`, you should see a list of huge list of tests running. Wait until the tests are run to check if your code breaks any of those tests.

* Unfortunately, while running grunt test does check a few things, it's not enough. We have lots of unit tests that have to be run manually in a browser. [Refer to this page](https://github.com/jquery/jquery#running-the-unit-tests) for more info on unit tests. After setting up the PHP server you need to navigate to /test/ and wait for the tests to finish.

* To have all tests running you need to set up Apache+PHP but the local PHP server `php -S localhost:8000` should work as well with the only caveat being that a few tests may fail.

* You can also fire up a regular non-PHP static HTTP server (e.g. using Python or the npm http-server package) but then AJAX tests won't work at all and a few other tests might not.

* Please also run tests in `AMD mode` (there's a checkbox on the test page). If there are some mistakes in the order of parameters passed to the define function they disappear in the full built file; you should see some errors when you run it that on AMD mode.

* If you find the list of scrolling tests too much to take in, you can reduce the output to only show failing tests by clicking on the `Hide passed tests` checkbox on the test page.