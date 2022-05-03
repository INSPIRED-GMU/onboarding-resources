This page describes how to use the Meteor command-line tool (for example, when downloading packages, deploying your app, etc) behind a proxy server.

Like a lot of other command-line software, the Meteor tool reads the proxy configuration from the `HTTP_PROXY` and `HTTPS_PROXY` environment variables (the lower case variants work, too). Examples of running Meteor behind a proxy:

- on Linux or Mac OS X

```bash
export HTTP_PROXY=http://user:password@1.2.3.4:5678
export HTTPS_PROXY=http://user:password@1.2.3.4:5678
meteor update
```

- on Windows

```batch
SET HTTP_PROXY=http://user:password@1.2.3.4:5678
SET HTTPS_PROXY=http://user:password@1.2.3.4:5678
meteor update
```