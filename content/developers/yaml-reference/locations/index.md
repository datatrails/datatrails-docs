---
title: "Locations YAML Runner"
description: "Location Actions Used with the Yaml Runner"
lead: "Location Actions Used with the Yaml Runner"
date: 2021-06-09T11:39:03+01:00
lastmod: 2021-06-09T11:39:03+01:00
draft: false
images: []
menu: 
  developers:
    parent: "yaml-reference"
weight: 204
toc: true
aliases: 
  - /docs/yaml-reference/locations/
---

{{< note >}}
**Note:** To use the YAML Runner you will need to install the `datatrails-archivist` python package.

[Click here](https://python.datatrails.com/runner/index.html) for installation instructions.
{{< /note >}}

## Locations Create If Not Exists

This action checks to see if the location you are looking to create already exists, and if not, executes the creation of your new location. The action checks for a location with the same identifier to verify that the location does not already exist.

If this action is executed as part of a series of YAML Runner steps, the location created can be referenced in later steps using the key `location_label`.

When you create your location, you may also add location attributes. In the example below, information such as the facility address and type have been included, as well as contact information for the location's reception:

```yaml
---
steps:
  - step:
      action: LOCATIONS_CREATE_IF_NOT_EXISTS
      description: Create Cape Town Location
    selector:
      - display_name
      - attributes:
        - namespace
    display_name: Cape Town
    description: South Africa Office
    latitude: -33.92527778
    longitude: 18.42388889
    attributes:
      namespace: synsation industries
      address: Cape Town Downtown
      Facility Type: Satellite Office
      reception_email: reception_CT@synsation.io
      reception_phone: +27 (21) 123-456
```

## Locations List

This action returns a list of all locations that meet your specified criteria. Setting `print_response: true` is necessary to print the full output.

```yaml
---
steps:
  - step:
      action: LOCATIONS_LIST
      description: List locations for which John Smith is director
      print_response: true
    attrs:
      director: John Smith
```

## Locations Count

This action returns a count of all locations that meet your specified criteria. Setting `print_response: true` is necessary to print the full output.

```yaml
---
steps:
  - step:
      action: LOCATIONS_COUNT
      description: Count location for which John Smith is director
      print_response: true
    attrs:
      director: John Smith
```
