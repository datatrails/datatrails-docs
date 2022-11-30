---
title: "YAML Runner Components"
description: "Commmon Keys Used for the Yaml Runner"
lead: "Common Keys Used for the Yaml Runner"
date: 2021-06-09T11:39:03+01:00
lastmod: 2021-06-09T11:39:03+01:00
draft: false
images: []
menu: 
  docs:
    parent: "yaml-reference"
weight: 201
toc: true
---

{{< note >}}
**Note:** To use the YAML Runner you will need to install the `jitsuin-archivist` python package.

[Click here](https://python.rkvst.com/runner/index.html) for installation instructions.
{{< /note >}}

| **Key**            | **Value**                                                                                                                                                                                                                                                                                                       |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **action**         | Required for every operation, the action specifies what function will be performed.                                                                                                                                                                                                                             |
| **description**    | Optional string that describes what the step is doing. For example, "Create the Asset My First Container".                                                                                                                                                                                                      |
| **asset_label**    | For a series of steps run as one file, the asset label could be a friendly name used by later steps to refer back to an asset created in a previous step. If the asset already exists, this field may be used to reference the Asset ID in the form assets/add30235-1424-4fda-840a-d5ef82c4c96fa.               |
| **location_label** | For a series of steps run as one file, the location label could be a friendly name used by later steps to refer back to a location created in a previous step. If the location already exists, this field may be used to reference the Location ID in the form locations/add30235-1424-4fda-840a-d5ef82c4c96fa. |
| **subject_label**  | For a series of steps run as one file, the subject label could be a friendly name used by later steps to refer back to a subject created in a previous step. If the subject already exists, this field may be used to reference the Subject ID in the form subjects/add30235-1424-4fda-840a-d5ef82c4c96fa.      |
| **print_response** | Specifying this field as true emits a JSON representation of the response, useful for debugging purposes.                                                                                                                                                                                                       |
| **wait_time**      | Optional field specifying a number of seconds the story runner will pause before executing the next step. Useful for demonstration and/or testing compliance policies.                                                                                                                                          |

Each step of the YAML Runner follows the same general pattern: 

```yaml
---
steps:
  - step:
      action: ASSETS_CREATE
      description: Create new EV Pump with id 1.
      wait_time: 10
      print_response: true
      asset_label: Radiation bag 1
      location_label: Cape Town
    ...definition of request body and other parameters
```

Depending on the action, some fields are required but others are optional. We will discuss each action in further detail in the upcoming sections.

Once you have created a YAML file with your desired steps, run the file using the `archivist_runner` command to execute the actions you defined. The command follows this format: 

```bash
$ archivist_runner \
      -u https://app.rkvst.io \
      --client-id <your-client-id> \
      --client-secret <your-client-secret> \
      <path-to-yaml-file>
```