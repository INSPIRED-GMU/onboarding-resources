Hello package author!

We are about to release the official port of Meteor to the Windows operating system. For most packages, this will be a smooth transition — JavaScript runs pretty much just as well on Windows as it does on Mac or Linux. However, if your package has binary NPM dependencies and you are using `meteor publish-for-arch` to publish builds, you will need to publish a new build for Windows.

1. Bump the version of your package. Since your existing version was published with a release that doesn't work on Windows, you will need to publish a new version.
2. Publish the package with `meteor publish --release METEOR@1.1-rc.4`. This will not change your package dependencies — those are set by `package.js` and will not be affected by the release you use to publish.
3. Follow the directions printed in the terminal to publish your package on all 4 supported platforms, including Windows.

Encourage Windows preview users to test your package so that you know it will work when the official release comes out!

If you have any issues publishing your package for Windows using the build machine, please post a comment on the [Meteor 1.1 release candidate comment thread](https://github.com/meteor/meteor/issues/4028).

### SSH weirdness in Meteor 1.0.5

While 1.1 is still in the RC stage, running `meteor admin get-machine os.windows.x86_32` will use the 1.0.5 version of the Meteor command line tool. In this version, there is a bug where the screen is not cleared when you SSH into a Windows machine, so you might not notice the prompt show up at the top of the terminal window. [See an example screenshot.](https://camo.githubusercontent.com/e4bd2751cd7ff28100e6c467c45daba3c5d9645b/687474703a2f2f692e696d6775722e636f6d2f654e52796330782e706e67).