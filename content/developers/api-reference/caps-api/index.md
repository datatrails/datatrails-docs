---
title: "Caps API"
description: "Caps API Reference"
lead: "Caps API Reference"
date: 2024-03-05T11:30:29Z
lastmod: 2024-03-05T11:30:29Z
draft: false
images: []
menu:
  developers:
    parent: "api-reference"
weight: 999
toc: true
---
{{< note >}}
**Note:** This page is primarily intended for developers who will be writing applications that will use DataTrails for provenance.
If you are looking for a simple way to test our API you might prefer our [Postman collection](https://www.postman.com/datatrails-inc/workspace/datatrails-public/overview), the [YAML runner](/developers/yaml-reference/story-runner-components/) or the [Developers](https://app.datatrails.ai) section of the web UI.

Additional YAML examples can be found in the articles in the [Overview](/platform/overview/introduction/) section.
{{< /note >}}
## Caps API Examples

The Caps API enables you to check the resource limits remaining under your Tenancy subscription.

### Retrieve a Cap

Retrieve the number of remaining Access Policies:

```bash
curl -g -v -X GET \
     -H "@$HOME/.datatrails/bearer-token.txt" \
     "https://app.datatrails.ai/archivist/v1/caps?service=access_policies"
```

The response is:

```json
{
    "caps": [
        {
            "resource_type": "AccessPolicies",
            "resource_remaining": "6"
        }
    ]
}
```
These are the available values for "**?service=**":
* access_policies
* applications
* assets
* blobs
* members


## Caps OpenAPI Docs
{{< openapi url="https://raw.githubusercontent.com/datatrails/datatrails-openapi/main/doc/capsv1.swagger.json" >}}
