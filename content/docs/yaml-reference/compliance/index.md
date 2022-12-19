---
title: "Compliance Policies YAML Runner"
description: "Compliance Policy Actions Used with the Yaml Runner"
lead: "Compliance Policy Actions Used with the Yaml Runner"
date: 2021-06-09T11:39:03+01:00
lastmod: 2021-06-09T11:39:03+01:00
draft: false
images: []
menu: 
  docs:
    parent: "yaml-reference"
weight: 206
toc: true
---

{{< note >}}
**Note:** To use the YAML Runner you will need to install the `jitsuin-archivist` python package.

[Click here](https://python.rkvst.com/runner/index.html) for installation instructions.
{{< /note >}}

## Compliance Policies Create

This action creates a compliance policy that assets may be tested against.

The specific fields required for creating compliance policies vary depending on the type of policy being used. Please see the [Compliance Policies](https://docs.rkvst.com/docs/beyond-the-basics/compliance-policies/) section for details regarding compliance policy types and YAML Runner examples of each.

For example, a `COMPLIANCE_RICHNESS` policy that asserts radiation level must be less than 7:

```yaml
---
steps:
  - step:
      action: COMPLIANCE_POLICIES_CREATE
      description: Create COMPLIANCE_RICHNESS policy
      print_response: true
    description: "Radiation level must be less than 7"
    display_name: Rad Limit
    compliance_type: COMPLIANCE_RICHNESS
    asset_filter:
      - or: [ "attributes.arc_home_location_identity=locations/<location-id>" ]
    richness_assertions: 
      - or: [ "radiation_level<7" ]
```

## Compliance Compliant At

The `COMPLIANCE_COMPLIANT_AT` action checks an asset against its compliance policies. 

`asset_label` is required, and may be specified as the friendly name defined in a previous step or as the Asset ID of an existing subject, in the form `assets/<asset-id>`. Setting `report: true` will trigger a report to be printed on the assets compliance status. 

```yaml
---
steps:
  - step:
      action: COMPLIANCE_COMPLIANT_AT
      description: Check Compliance of EV pump 1.
      report: true
      asset_label: ev pump 1
```