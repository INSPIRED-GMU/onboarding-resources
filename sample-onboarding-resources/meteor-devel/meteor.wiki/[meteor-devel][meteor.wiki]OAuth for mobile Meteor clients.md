### OAuth in mobile apps in local development

Meteor's OAuth2 implementation (used in the accounts-google, accounts-facebook, and accounts-meteor-developer packages, among others) does not currently work in Cordova apps when run in local development mode, except on the iOS simulator. This limitation is because you need a public Internet address to register as an authorized redirect URL with the login provider.

As a workaround, you can deploy your app and modify your app's configuration to test OAuth login on a mobile app when developing locally.

1. Run `meteor deploy <your site>.meteor.com`.
2. In a desktop browser, visit `<your site>.meteor.com`, and click "Configure <provider name> Login." Follow the instructions to create a new application with the login provider.
3. Run your app on a mobile emulator or device, using the `--mobile-server` option to point to your deployed app. For example,
```
meteor run [android|android-device|ios|ios-device] --mobile-server https://<your site>.meteor.com`
```

### Popup versus redirect flow

When configuring OAuth login with a provider (such as Facebook or Google), Meteor lets you choose a popup- or redirect-based flow. In a popup-based flow, when a user logs in, they will be prompted to login at the provider in a popup window. In a redirect-based flow, the user's whole browser window will be redirected to the login provider, and the window will redirect back to your app when the login is completed.

You can also pick which type of login to do by passing an option `Meteor.loginWith<ExternalService>`: http://docs.meteor.com/#meteor_loginwithexternalservice.

Usually, the popup-based flow is preferable because the user will not have to reload your whole app at the end of the login flow. However, the popup-based flow requires browser features such as `window.close` and `window.opener` that are not available in all mobile environments. In particular, we recommend using `Meteor.loginWith<ExternalService>({ loginStyle: "redirect" })` in the following environments:

* Inside UIWebViews (when your app is loaded inside a mobile app)
* In Safari on iOS8 (`window.close` is not supported due to a bug)