# Overview

For PowerToys, we are a rapid incubation, open source team aimed to provide power users with ways to squeeze more efficiency out of the Windows 10 shell and customize it for individual workflows. As we see opportunities to help improve everyone's productivity, we will reassess our priority list of work and adjust as needed. We [shared a document](https://github.com/microsoft/PowerToys/wiki/Version-1.0-Strategy) back in February 2020 that outlined what we thought was a good roadmap and list of goals when we started on developing PowerToys into what it is now.

With us sharing the roadmap, we hope to give transparency on what we are going to be focusing on. We'll start picking items off the top of backlog to provide a more agile motion. If you feels strongly on taking on work we haven't started yet, please lets have a discussion and kick off the workflows. We also have the '[help wanted](https://github.com/microsoft/PowerToys/issues?q=is%3Aopen+is%3Aissue+label%3A%22Help+Wanted%22+-label%3AResolution-Fix-Committed)' tag which are other items we feel strongly would be good things for the project but aren't something we're prioritizing. 

We'll also start shifting into a 'preview' and 'stable' mode for our utilities which then will make sure stability is an evergreen item.

## Current planned large work items

| status | Title | GitHub # | 
|---|---|---|
| Blocked | Support ARM processor support | [#490](https://github.com/microsoft/PowerToys/issues/490)<br/>[dependent on #6715](https://github.com/microsoft/PowerToys/issues/6715)<br/>[dependent on #8557](https://github.com/microsoft/PowerToys/issues/8557)<br/>[dependent on #12285](https://github.com/microsoft/PowerToys/issues/12285) |
| Blocked| Settings to WinUI3. (including KBM) | [#6715](https://github.com/microsoft/PowerToys/issues/6715)<br/>Settings needs elevation in WinUI 3.1 |
| Planned | Upgrade prompt with what is new (Scoobe) | [#14536](https://github.com/microsoft/PowerToys/issues/14536) |
| In-progress| Remove all .NET Fx dependencies | [#8557](https://github.com/microsoft/PowerToys/issues/8557) |
| In-progress| Update to .NET 6 (Requires Pipeline shift for installer) | [#12285](https://github.com/microsoft/PowerToys/issues/12285) |
| In-progress | Simplifying / Reducing UAC for installer | [#10126](https://github.com/microsoft/PowerToys/issues/10126)
| In-progress | Add in Monaco based preview pane to boost dev language support | [#1527](https://github.com/microsoft/PowerToys/issues/1527) |
| Evergreen | Stability for all existing bugs | [Bugs](https://github.com/microsoft/PowerToys/issues?q=is%3Aopen+is%3Aissue+milestone%3A%222020+Stability+Release%22) |
| Evergreen | Accessibility work for all PT | [Multiple issues](https://github.com/microsoft/PowerToys/issues?q=is%3Aopen+is%3Aissue+label%3AArea-Accessibility) |
| Complete | Presentation mode - Highlight mouse when clicked | [#13808](https://github.com/microsoft/PowerToys/issues/13808) |
| Complete | Always on top | [#13](https://github.com/microsoft/PowerToys/issues/13) |
| Complete | Mac Style "Find cursor" ease of access (shake to find) | [#131](https://github.com/microsoft/PowerToys/issues/131) |

### Backlog

1. Shortcut Guide v2 - [#890](https://github.com/microsoft/PowerToys/issues/890)
1. Migrate UX's to standardize on WinUI 3 - [#891](https://github.com/microsoft/PowerToys/issues/891)
1. GIF / Video Screen Record - [#143](https://github.com/microsoft/PowerToys/issues/143)
1. Presentation mode - On-screen overlay of commands / shortcuts - [#981](https://github.com/microsoft/PowerToys/issues/981)
1. KBM Map to custom keys / diacritic character, not just keycode - [#6976](https://github.com/microsoft/PowerToys/issues/6976)
1. Adjust how fonts Render - [#6918](https://github.com/microsoft/PowerToys/issues/6918)
1. Quick Terminate App - [#322](https://github.com/microsoft/PowerToys/issues/322)
1. Paste as plain text - [#1684](https://github.com/microsoft/PowerToys/issues/1684)
1. Screen measuring tool - [#863](https://github.com/microsoft/PowerToys/issues/863)
1. Who has my file in use - [#114](https://github.com/microsoft/PowerToys/issues/114)
1. Improved Systray flyout/context menu - [#6751](https://github.com/microsoft/PowerToys/issues/6751)
1. Auto-Update feature disabling for enterprise environment - [#2701](https://github.com/microsoft/PowerToys/issues/2701)