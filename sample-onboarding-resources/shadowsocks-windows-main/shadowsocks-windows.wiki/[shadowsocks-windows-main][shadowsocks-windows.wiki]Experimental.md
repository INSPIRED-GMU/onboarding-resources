# Experimental Features

Features list here are not fully tested and may be removed in future releases.

#### Custom GeoSite group setting (v4.1.xx.x)

In `gui-config.json` file, add `geositeGroup` string value. Shadowsocks will generate rule using this group.
Add `geositeBlacklistMode` boolean value to control which rule mode Shadowsocks will generate. `true` for blacklist, `false` for whitelist.
Default behavior is generate blacklist for `geolocation-!cn`.

#### Custom GFWList source URL (v4.1.9.0-v4.1.10.0)
In `gui-config.json` file, add `gfwListUrl` key-value. Shadowsocks would fetch the GFWList content from this URL.

Replaced with GeoSite.

#### Listening on local IPv6 interface (v4.1.7)

In `gui-config.json` file, add `isIpv6Enabled` key-value. Default value is `false`.
```
  ...
  "isDefault": false,
  "isIPv6Enabled": true,
  "localPort": 8388,
  ...
```