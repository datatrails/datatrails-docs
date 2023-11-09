---
title: "System API"
description: "System API Reference"
lead: "System API Reference"
date: 2021-06-09T13:49:35+01:00
lastmod: 2021-06-09T13:49:35+01:00
draft: false
images: []
menu: 
  developers:
    parent: "api-reference"
weight: 113
toc: true
aliases: 
  - /docs/api-reference/system-api/
---
{{< note >}}
This page is primarily intended for developers who will be writing applications that will use DataTrails for provenance. 
If you are looking for a simple way to test our API you might prefer our [Postman collection](https://www.postman.com/datatrails-official/workspace/datatrails-public-official/overview), the [YAML runner](/developers/yaml-reference/story-runner-components/) or the [Developers](https://app.datatrails.ai) section of the web UI. 

Additional YAML examples can be found in the articles in the [Overview](/platform/overview/introduction/) section.
{{< /note >}}
## System API Examples

Create the [bearer_token](/developers/developer-patterns/getting-access-tokens-using-app-registrations) and store in a file in a secure local directory with 0600 permissions.

### Querying Blockchain Status

The `archivistnode` endpoint reports on the status of the blockchain.

Query the endpoint:

```bash
curl -v -X GET \
    -H "@$HOME/.datatrails/bearer-token.txt" \
    https://app.datatrails.ai/archivist/v1/archivistnode
```

The response is:

```json
{
    "identity": "quorum",
    "blockchain_nodes": [
        {
            "validator_pubkey": {
                "kty": "EC",
                "crv": "P-256K",
                "x": "VBKHictTWJC-3sqknXCb8MI4IxTc3c_My7lnem2C74E=",
                "y": "ItNeb5d-6vEHkvtUOcDYrEADxsZXeOCJm18pQWntenE=",
                "d": ""
            },
            "block_height": "38773",
            "connection_status": "REACHABLE"
            "genesis_hash":"0x1b526bd9c7f9bf7c43ba91ad07e5530eb7ceedf390396f9fbfeb68722e097e95",
            "state_root":"0x9606fc44a382938703678ac90581ab1260c9efd20ea8c7f90c87852bc982f3a7",
            "timestamp_committed": "2019-01-02T01:03:07Z",
            "timestamp_created": "2019-01-01T12:00:27Z",
            "syncing": null,
            "peers": [
                {
                    "validator_pubkey": {
                        "kty": "EC",
                        "crv": "P-256K",
                        "x": "o0uZ8ix5DE42srPCw1o22wYibkHGkvyCuLVqwcVAxb0=",
                        "y": "W43sUjWg-ociR2x3CcAlWeOqc6oDkYui1JLup1q-ojU=",
                        "d": ""
                    },
                    "connection_status": "REACHABLE"
                },
                {
                    "validator_pubkey": {
                        "kty": "EC",
                        "crv": "P-256K",
                        "x": "5HcU1PJgTe0LGyGxKFrIPFZWdTbxPySfi6bKxdQeO8A=",
                        "y": "dEpMURyTwEGzpgIgLdm4Csl1BgF6H39tb1Kf8wLLhVI=",
                        "d": ""
                    },
                    "connection_status": "REACHABLE"
                }
            ]
        }
    ]
}
```

## System OpenAPI Docs

{{< openapi url="https://raw.githubusercontent.com/datatrails/archivist-docs-old/master/doc/openapi/archivistnodev1.swagger.json" >}}
