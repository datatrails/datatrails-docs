---
title: "Public Assets API"
description: "Public Assets API Reference"
lead: "Public Assets API Reference"
date: 2021-06-09T11:56:23+01:00
lastmod: 2021-06-09T11:56:23+01:00
draft: false
images: []
menu: 
  developers:
    parent: "api-reference"
weight: 112
toc: true
aliases: 
  - /docs/api-reference/public-assets-api/
---
{{< note >}}
This page is primarily intended for developers who will be writing applications that will use DataTrails for provenance. 
If you are looking for a simple way to test our API you might prefer our [Postman collection](https://www.postman.com/datatrails-official/workspace/datatrails-public-official/overview), the [YAML runner](/developers/yaml-reference/story-runner-components/) or the [Developers](https://app.datatrails.ai) section of the web UI. 

Additional YAML examples can be found in the articles in the [Overview](/platform/overview/introduction/) section.
{{< /note >}}
## Public Assets API Examples

Public Assets are created using the [Assets API](../assets-api/) and setting the value of `public` to `true`.

To see more information about creating a Public Asset, see [Creating a Public Asset](../assets-api/#creating-a-public-asset).

Each Public Asset has a private and a public interface. The private interface is used to update the Asset by the creating Tenancy and the public interface is a read-only view of the Asset that you do not need to be authenticated for.

The methods described below cover interacting with the public interface only. To interact with the private interface, use the standard [Assets API](../assets-api/).

{{< note >}}
Visit the [Public Attestation](/platform/overview/public-attestation/) guide for more information.
{{< /note >}}

### Fetch a Public Asset Record

```bash
curl -H "Content-Type: application/json" https://app.datatrails.ai/archivist/publicassets/86b61c4b-030e-4c07-9400-463612e6cee4
```

```json
{
  "identity": "assets/86b61c4b-030e-4c07-9400-463612e6cee4",
  "behaviours": ["RecordEvidence", "Builtin", "AssetCreator"] ,
  "attributes": {
    "arc_display_type": "Asset",
    "foo": "bar",
    "A": "B",
    "arc_description": "This asset is public",
    "arc_display_name": "Public Asset"
  },
  "confirmation_status": "CONFIRMED",
  "tracked": "TRACKED",
  "owner": "0x5eC362570D1b52a01648997db5ed7693fc6b3978",
  "at_time": "2022-07-15T14:26:40Z",
  "storage_integrity": "TENANT_STORAGE",
  "proof_mechanism": "SIMPLE_HASH",
  "chain_id": "8275868384",
  "public": true,
  "tenant_identity": "tenant/8e0b600c-8234-43e4-860c-e95bdcd695a9"
}
```

### Fetch All Of a Public Asset's Events Records

```bash
curl -H "Content-Type: application/json" https://app.datatrails.ai/archivist/publicassets/86b61c4b-030e-4c07-9400-463612e6cee4/events
```

```json
{
    "events": [
        {
            "identity": "assets/86b61c4b-030e-4c07-9400-463612e6cee4/events/083f90fb-c379-40db-b56a-190564d53cd5",
            "asset_identity": "assets/86b61c4b-030e-4c07-9400-463612e6cee4",
            "event_attributes": {
                "arc_display_type": "Change"
            },
            "asset_attributes": {
                "A": "B"
            },
            "operation": "Record",
            "behaviour": "RecordEvidence",
            "timestamp_declared": "2022-07-06T14:56:24Z",
            "timestamp_accepted": "2022-07-06T14:56:24Z",
            "timestamp_committed": "2022-07-06T14:56:24.681514884Z",
            "principal_declared": {
                "issuer": "",
                "subject": "",
                "display_name": "",
                "email": ""
            },
            "principal_accepted": {
                "issuer": "",
                "subject": "",
                "display_name": "",
                "email": ""
            },
            "confirmation_status": "CONFIRMED",
            "transaction_id": "",
            "block_number": 0,
            "transaction_index": 0,
            "from": "0x5eC362570D1b52a01648997db5ed7693fc6b3978",
            "tenant_identity": "tenant/8e0b600c-8234-43e4-860c-e95bdcd695a9"
        },
        {
            "identity": "assets/86b61c4b-030e-4c07-9400-463612e6cee4/events/10d252f2-3116-4c22-b34a-7e3f768895c9",
            "asset_identity": "assets/86b61c4b-030e-4c07-9400-463612e6cee4",
            "event_attributes": {
                "arc_access_policy_always_read": [
                    {
                        "tessera": "SmL4PHAHXLdpkj/c6Xs+2br+hxqLmhcRk75Hkj5DyEQ=",
                        "wallet": "0x5eC362570D1b52a01648997db5ed7693fc6b3978"
                    }
                ],
                "arc_access_policy_asset_attributes_read": [
                    {
                        "0x4609ea6bbe85F61bc64760273ce6D89A632B569f": "wallet",
                        "SmL4PHAHXLdpkj/c6Xs+2br+hxqLmhcRk75Hkj5DyEQ=": "tessera",
                        "attribute": "*"
                    }
                ],
                "arc_access_policy_event_arc_display_type_read": [
                    {
                        "SmL4PHAHXLdpkj/c6Xs+2br+hxqLmhcRk75Hkj5DyEQ=": "tessera",
                        "value": "*",
                        "0x4609ea6bbe85F61bc64760273ce6D89A632B569f": "wallet"
                    }
                ]
            },
            "asset_attributes": {
                "foo": "bar",
                "arc_description": "This asset is public",
                "arc_display_name": "Public Asset",
                "arc_display_type": "Asset"
            },
            "operation": "NewAsset",
            "behaviour": "AssetCreator",
            "timestamp_declared": "2022-07-06T13:38:34Z",
            "timestamp_accepted": "2022-07-06T13:38:34Z",
            "timestamp_committed": "2022-07-06T13:38:35.143791572Z",
            "principal_declared": {
                "issuer": "",
                "subject": "",
                "display_name": "",
                "email": ""
            },
            "principal_accepted": {
                "issuer": "",
                "subject": "",
                "display_name": "",
                "email": ""
            },
            "confirmation_status": "CONFIRMED",
            "transaction_id": "",
            "block_number": 0,
            "transaction_index": 0,
            "from": "0x5eC362570D1b52a01648997db5ed7693fc6b3978",
            "tenant_identity": "tenant/8e0b600c-8234-43e4-860c-e95bdcd695a9"
        }
    ],
    "next_page_token": ""
}
```

### Fetch a Public Asset's Specific Event Record

```bash
curl -H "Content-Type: application/json" https://app.datatrails.ai/archivist/publicassets/86b61c4b-030e-4c07-9400-463612e6cee4/events/7da272ad-19d5-4106-b4af-2980a84c2721
```

```json
{
    "identity": "assets/86b61c4b-030e-4c07-9400-463612e6cee4/events/083f90fb-c379-40db-b56a-190564d53cd5",
    "asset_identity": "assets/86b61c4b-030e-4c07-9400-463612e6cee4",
    "event_attributes": {
        "arc_display_type": "Change",
    },
    "asset_attributes": {
        "A": "B"
    },
    "operation": "Record",
    "behaviour": "RecordEvidence",
    "timestamp_declared": "2022-07-06T14:56:24Z",
    "timestamp_accepted": "2022-07-06T14:56:24Z",
    "timestamp_committed": "2022-07-06T14:56:24.681514884Z",
    "principal_declared": {
        "issuer": "",
        "subject": "",
        "display_name": "",
        "email": ""
    },
    "principal_accepted": {
        "issuer": "",
        "subject": "",
        "display_name": "",
        "email": ""
    },
    "confirmation_status": "CONFIRMED",
    "transaction_id": "",
    "block_number": 0,
    "transaction_index": 0,
    "from": "0x5eC362570D1b52a01648997db5ed7693fc6b3978",
    "tenant_identity": "tenant/8e0b600c-8234-43e4-860c-e95bdcd695a9"
}
```

## Public Assets OpenAPI Docs
<!--
{{< openapi url="https://raw.githubusercontent.com/rkvst/archivist-docs/master/doc/openapi/publicassetsv2.swagger.json" >}}
