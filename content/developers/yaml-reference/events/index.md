---
title: "Events YAML Runner"
description: "Event Actions Used with the Yaml Runner"
lead: "Event Actions Used with the Yaml Runner"
date: 2021-06-09T11:39:03+01:00
lastmod: 2021-06-09T11:39:03+01:00
draft: false
images: []
menu: 
  developers:
    parent: "yaml-reference"
weight: 203
toc: true
aliases: 
  - /docs/yaml-reference/events/
---

{{< note >}}
**Note:** To use the YAML Runner you will need to install the `rkvst-archivist` python package.

[Click here](https://python.rkvst.com/runner/index.html) for installation instructions.
{{< /note >}}

## Events Create

The `asset_label` must match the setting when the Asset was created in an earlier step. The `asset_label` may also be specified as the Asset ID of an existing Asset, in the form `assets/<asset-id>`. 

There are a few optional settings that can be used when creating Events. `attachments` uploads the attachment to RKVST and the response is added to the Event before posting. `location` creates the location if it does not exist and adds it to the Event. The `sbom` setting uploads the SBOM to RKVST and adds the response to the Event before posting. 

`confirm: true` tells the YAML Runner to wait for the Event to be confirmed before moving to the next step.

For example: 

```yaml
---
steps:
  - step:
      action: EVENTS_CREATE
      description: Access Card, opens Courts of justice front door
      asset_label: Access Card
      print_response: true
    operation: Record
    behaviour: RecordEvidence
    event_attributes:
      arc_description: Opened Courts of Justice Paris Front Door
      arc_display_type: open
      arc_evidence: ARQC 0x12345678
      arc_correlation_value: be5c8061-236d-4400-a625-b74a34e5801b
      wavestone_door_name: Courts of Justice Paris Front Door
      wavestone_evt_type: door_open
    location:
      selector:
        - display_name
        - attributes:
          - namespace
      display_name: Paris Courts of Justice
      description: Public museum in the former Palais de Justice
      latitude: 48.855722
      longitude: 2.345051
      attributes:
        namespace: door entry
        address: 10 Boulevard du Palais, 75001 Paris, France
        wavestone_ext: managed
    attachments:
      - filename: functests/test_resources/doors/events/door_open.png
        content_type: image/png
    confirm: true
```

This example creates an Event with custom Event attributes, creates and adds a location, and adds an image attachment. 

Events may also be used to release a software package as an SBOM, such as the example below: 

```yaml 
---
steps:
  - step:
      action: EVENTS_CREATE
      description: Release YYYYMMDD.1 of Test SBOM for YAML story
      asset_label: ACME Corporation Detector SAAS
      print_response: true
    operation: Record
    behaviour: RecordEvidence
    confirm: true
    event_attributes:
      arc_description: ACME Corporation Detector SAAS Released YYYYMMDD.1
      arc_display_type: Software Package Release
    sbom:
      filename: functests/test_resources/sbom/gen1.xml
      content_type: text/xml
      display_name: ACME Generation1 SBOM
      confirm: True
      params:
        privacy: PRIVATE
```

## Events List

This action returns a list of all Events that meet your specified criteria. The `asset_label` can be identified as the friendly name of an Asset created in a previous step, or as an Asset ID for an existing Asset. If no `asset_label` is set, data for all Assets will be used. 

Specifying `props`, `attrs`, and `asset_attrs` are optional criteria. 

Setting `print_response: true` is necessary to print the full output. 

The following example lists all "open door" Events for the Courts of Justice Paris Front Door: 

```yaml
---
steps:
  - step:
      action: EVENTS_LIST
      description: List all events for Courts of Justice Paris Front Door
      print_response: true
      asset_label: Courts of Justice Paris Front Door
    props:
      confirmation_status: CONFIRMED
    attrs:
      arc_display_type: open
    asset_attrs:
      arc_display_type: door
```

## Events Count

This action returns a count of all Events that meet your specified criteria. The same criteria options available for `Events List` are possible. Setting `print_response: true` is necessary to print the full output.

The following example counts all "open door" Events for the Courts of Justice Paris Front Door:

```yaml 
---
steps:
  - step:
      action: EVENTS_COUNT
      description: List all events for Courts of Justice Paris Front Door
      print_response: true
      asset_label: Courts of Justice Paris Front Door
    props:
      confirmation_status: CONFIRMED
    attrs:
      arc_display_type: open
    asset_attrs:
      arc_display_type: door
```