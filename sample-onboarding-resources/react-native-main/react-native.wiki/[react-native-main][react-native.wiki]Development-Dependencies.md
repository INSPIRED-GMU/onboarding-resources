## ShellCheck

ShellCheck is used to lint shell scripts in the React Native repository automatically as part of the continuous tests. You can install ShellCheck on your local machine by following the instructions at https://github.com/koalaman/shellcheck.

Once installed, you can run `yarn shellcheck` to analyze all shell scripts in the React Native repository. 

### Status of ShellCheck warnings in `master`

The analysis script that runs as part of the CircleCI continuous tests should only leave comments on your pull request if the ShellCheck warnings explicitly match one of the lines being added or changed in your pull request. 

There are several scripts in the React Native repository with warnings that need to be addressed, something you might notice when you first run `yarn shellcheck`. Feel free to ignore any warnings for files you haven't modified in your pull request. However, pull requests that clean up these warnings are appreciated.