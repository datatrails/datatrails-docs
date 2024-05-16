---
title: "Assets YAML Runner"
description: "Asset Actions Used with the Yaml Runner"
lead: "Asset Actions Used with the Yaml Runner"
date: 2021-06-09T11:39:03+01:00
lastmod: 2021-06-09T11:39:03+01:00
draft: false
images: []
menu: 
  developers:
    parent: "yaml-reference"
weight: 202
toc: true
aliases: 
  - /docs/yaml-reference/assets/
---

{{< note >}}
**Note:** To use the YAML Runner you will need to install the `datatrails-archivist` python package.

[Click here](https://python.datatrails.ai/runner/index.html) for installation instructions.
{{< /note >}}

## Assets Create

Adding an `asset_label` allows your Asset to be referenced in later steps of the story. For example, if you want to add a Compliance Policy for the Asset after it is created.

The `arc_namespace` (for the Asset) and the `namespace` (for the location) are used to distinguish between Assets and Locations created between runs of the story. Usually, these field values are derived from an environment variable `ARCHIVIST_NAMESPACE` (default value is namespace).

The optional `confirm: true` entry means that the YAML Runner will wait for the Asset to be committed before moving on to the next step. This is beneficial if the Asset will be referenced in later steps.

For example:

```yaml
---
steps:
  - step:
      action: ASSETS_CREATE
      description: Create new EV Pump with id 1.
      asset_label: ev pump 1
    behaviours:
      - RecordEvidence
    attributes:
      arc_display_name: ev pump 1
      arc_display_type: pump
      arc_namespace: wipp
      ev_pump: "true"
    confirm: true
```

The output of this action is available in the [DataTrails UI](https://app.datatrails.ai):

{{< img src="AssetsCreate.png" alt="Rectangle" caption="<em>ASSETS_CREATE Output</em>" class="border-0" >}}

## Assets Create If Not Exists

This action is similar to `ASSETS_CREATE`, with the additional functionality of checking if an Asset with the same identifier exists before executing the creation of a new one.

```yaml
---
steps:
  - step:
      action: ASSETS_CREATE_IF_NOT_EXISTS
      description: Create new EV Pump with id 1.
      asset_label: ev pump 1
    behaviours:
      - RecordEvidence
    attributes:
      arc_display_name: ev pump 1
      arc_display_type: pump
      arc_namespace: wipp
      ev_pump: "true"
    confirm: true
```

## Assets List

This action returns a list of all Assets that meet your specified criteria. Setting `print_response: true` is necessary to print the full output.

In the example below, our action will return a list of all Assets with `arc_display_type: pump`.

```yaml
---
steps:
  - step:
      action: ASSETS_LIST
      description: List all pumps
      print_response: true
    attrs:
      arc_display_type: pump
```

The response printed was ev pump 1, the Asset created in the `Assets Create` example:

```json
Response {
    "identity": "assets/<asset-id>",
    "behaviours": [
        "RecordEvidence",
        "Builtin",
        "AssetCreator"
    ],
    "attributes": {
        "arc_display_type": "pump",
        "arc_namespace": "wipp",
        "ev_pump": "true",
        "arc_display_name": "ev pump 1"
    },
    "confirmation_status": "COMMITTED",
    "tracked": "TRACKED",
    "owner": "0x6ba1CA0a5f4a2aBC23412419bC0E14233E88d233",
    "at_time": "2022-11-18T16:55:44Z",
    "storage_integrity": "TENANT_STORAGE",
    "chain_id": "827586838445807967",
    "public": false,
    "tenant_identity": "tenant/<tenant-id>"
}
```

## Assets Count

This action returns a count of all Assets that meet your specified criteria. Setting `print_response: true` is necessary to print the full output.

In the example below, our action will return a count of all Assets with `arc_display_type: pump`.

```yaml
---
steps:
  - step:
      action: ASSETS_COUNT
      description: Count all pumps
      print_response: true
    attrs:
      arc_display_type: pump
```

## Assets Wait For Confirmed

This action tells the YAML Runner to wait before proceeding to the next step until all Assets that meet your specified criteria are confirmed/committed.

```yaml
---
steps:
  - step:
      action: ASSETS_WAIT_FOR_CONFIRMED
      description: Wait for all Assets in the wipp namespace to be confirmed
    attrs:
      arc_namespace: wipp
```
