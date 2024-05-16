---
title: "Subjects YAML Runner"
description: "Subject Actions Used with the Yaml Runner"
lead: "Subject Actions Used with the Yaml Runner"
date: 2021-06-09T11:39:03+01:00
lastmod: 2021-06-09T11:39:03+01:00
draft: false
images: []
menu: 
  developers:
    parent: "yaml-reference"
weight: 205
toc: true
aliases: 
  - /docs/yaml-reference/subjects/
---

{{< note >}}
**Note:** To use the YAML Runner you will need to install the `datatrails-archivist` python package.

[Click here](https://python.datatrails.ai/runner/index.html) for installation instructions.
{{< /note >}}

## Subjects Create

This action creates a Subject using their `wallet_pub_key` and `tessera_pub_key`. Adding a `subject_label` allows the Subject to be referenced in later YAML Runner steps.

```yaml
---
steps:
  - step:
      action: SUBJECTS_CREATE
      description: Create a subjects entity.
      print_response: true
      subject_label: A subject
    display_name: A subject
    wallet_pub_key:
      - wallet_pub_key1
    tessera_pub_key:
      - tessera_pub_key2
```

## Subjects Create From base64

This action creates a Subject using their base64 `subject_string`. Adding a `subject_label` allows the Subject to be referenced in later YAML Runner steps.

For example:

```yaml
---
steps:
  - step:
      action: SUBJECTS_CREATE_FROM_B64
      description: Import a subjects entity.
      print_response: true
      subject_label: An imported subject
    display_name: An imported subject
    subject_string: >-
      eyJpZGVudGl0eSI6ICJzdWJqZWN0cy8wMDAwMDAwMC0wMDAwLTAwMDAtMDA
      wMC0wMDAwMDAwMDAwMDAiLCAiZGlzcGxheV9uYW1lIjogIlNlbGYiLCAid2
      FsbGV0X3B1Yl9rZXkiOiBbIjA0YzExNzNiZjc4NDRiZjFjNjA3Yjc5YzE4Z
      GIwOTFiOTU1OGZmZTU4MWJmMTMyYjhjZjNiMzc2NTcyMzBmYTMyMWEwODgw
      YjU0YTc5YTg4YjI4YmM3MTBlZGU2ZGNmM2Q4MjcyYzUyMTBiZmQ0MWVhODM
      xODhlMzg1ZDEyYzE4OWMiXSwgIndhbGxldF9hZGRyZXNzIjogWyIweDk5Rm
      E0QUFCMEFGMkI1M2YxNTgwODNEOGYyNDRiYjQ1MjMzODgxOTciXSwgInRlc
      3NlcmFfcHViX2tleSI6IFsiZWZkZzlKMFFoU0IyZzRJeEtjYVhnSm1OS2J6
      cHhzMDNGRllJaVlZdWVraz0iXSwgInRlbmFudCI6ICIiLCAiY29uZmlybWF
      0aW9uX3N0YXR1cyI6ICJDT05GSVJNQVRJT05fU1RBVFVTX1VOU1BFQ0lGSU
      VEIn0=
```

## Subjects Update

To update a Subject's entity, the `subject_label` from a previous action in the YAML Runner steps is required. The `subject_label` may also be specified as the Subject ID of an existing Subject, in the form `subjects/<subject-id`.

`display_name`, `wallet_pub_key`, and `tessera_pub_key` are optional, but at least one must be specified.

```yaml
---
steps:
  - step:
      action: SUBJECTS_UPDATE
      description: Update a subjects entity.
      print_response: true
      subject_label: A subject
    display_name: A subject
    wallet_pub_key:
      - wallet_pub_key1
      - wallet_pub_key2
    tessera_pub_key:
      - tessera_pub_key1
      - tessera_pub_key2
```

## Subjects Delete

This action deletes the specified Subject.

`subject_label` is required, and may be specified as the friendly name defined in a previous step or as the Subject ID of an existing subject, in the form `subjects/<subject-id>`.

```yaml
---
steps:
  - step:
      action: SUBJECTS_DELETE
      description: Delete subject
      print_response: true
      subject_label: A subject
```

## Subjects Read

This action allows you to read the details for the specified Subject. Setting `print_response: true` is necessary to print the full output.

`subject_label` is required, and may be specified as the friendly name defined in a previous step or as the Subject ID of an existing subject, in the form `subjects/<subject-id>`.

```yaml
---
steps:
  - step:
      action: SUBJECTS_READ
      description: Read subject
      print_response: true
      subject_label: subjects/<subject-id>
```

## Subjects List

This action returns a list of all Subjects that meet your specified criteria. Setting `print_response: true` is necessary to print the full output.

For example, to list all Subjects with the name John Doe:

```yaml
---
steps:
  - step:
      action: SUBJECTS_LIST
      description: List all subjects with name John Doe
      print_response: true
    display_name: John Doe
```

## Subjects Count

This action returns a count of all Subjects that meet your specified criteria. Setting `print_response: true` is necessary to print the full output.

```yaml
---
steps:
  - step:
      action: SUBJECTS_COUNT
      description: Count all subjects
      print_response: true
    display_name: John Doe
```

## Subjects Wait for Confirmation

This action tells the YAML Runner to wait before proceeding to the next step until all Subjects that meet your specified criteria are confirmed/committed.

`subject_label` is required, and may be specified as the friendly name defined in a previous step or as the Subject ID of an existing subject, in the form `subjects/<subject-id>`.

```yaml
---
steps:
  - step:
      action: SUBJECTS_WAIT_FOR_CONFIRMATION
      description: Wait for all subjects to be confirmed
      print_response: true
      subject_label: A subject
``
