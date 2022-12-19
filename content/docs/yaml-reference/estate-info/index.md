---
title: "Estate Information YAML Runner"
description: "Retrieve Estate Info Using the Yaml Runner"
lead: "Retrieve Estate Info Using the Yaml Runner"
date: 2021-06-09T11:39:03+01:00
lastmod: 2021-06-09T11:39:03+01:00
draft: false
images: []
menu: 
  docs:
    parent: "yaml-reference"
weight: 207
toc: true
---

{{< note >}}
**Note:** To use the YAML Runner you will need to install the `jitsuin-archivist` python package.

[Click here](https://python.rkvst.com/runner/index.html) for installation instructions.
{{< /note >}}

## Composite Estate Info

This action returns a report on the current number of assets, events, and locations in your RKVST estate.

```yaml
---
steps:
  - step:
      action: COMPOSITE_ESTATE_INFO
      description: Estate Info Report
```