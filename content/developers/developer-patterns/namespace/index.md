---
title: "Namespace"
description: "Using Namespace in an DataTrails Tenancy"
lead: "Using Namespace in an DataTrails Tenancy"
date: 2021-05-31T15:18:01+01:00
lastmod: 2021-05-31T15:18:01:31+01:00
draft: false
images: []
menu:
  developers:
    parent: "developer-patterns"
weight: 34
toc: true
aliases:
  - /docs/developer-patterns/namespace/
---

Namespace is a tool that can be used to prevent unwanted interactions when multiple users are performing testing in the same Tenancy. Using two separate namespaces prevents collisions that may cause undesirable results by allowing multiple users to interact with the same Assets and Events without interrupting each other.

Namespace can be added as an attribute within the files you are testing, or as a variable in your Bash environment.

To add namespace as an attribute to your files, use the `arc_namespace` key. For example:

```json
{
    "behaviours": ["RecordEvidence"],
    "attributes": {
        "arc_display_name": "My First Container",
        "arc_display_type": "Shipping Container",
        "arc_description": "Originally shipped from Shanghai",
        "arc_namespace": "test_02-17-23",
        "Width": "2.43m",
        "Length": "6.06m",
        "Height": "2.59m",
    }
}
```

To use namespace as a variable, such as the date, add the argument to your Bash environment:

```bash
 export TEST_NAMESPACE=date
```

See [TEST_NAMESPACE](https://github.com/datatrails/datatrails-samples/blob/main/DEVELOPERS.md#test_namespace) in our GitHub repository for more information. `TEST_NAMESPACE` can also be added to your Bash profile to be automatically picked up when testing.
