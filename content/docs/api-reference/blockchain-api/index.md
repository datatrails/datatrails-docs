---
title: "Blockchain API (v1alpha1)"
description: "Blockchain API Reference"
lead: "Blockchain API Reference"
date: 2021-06-09T13:57:04+01:00
lastmod: 2021-06-09T13:57:04+01:00
draft: false
images: []
menu: 
  docs:
    parent: "api-reference"
weight: 105
toc: true
---

## Blockchain API Examples

Create the [bearer_token](../../setup-and-administration/getting-access-tokens-using-client-secret) and store in a file in a secure local directory with 0600 permissions.

### Fetch Transactions for an event (v1alpha1)

Blockchain transactions can be fetched from the blockchain endpoint using the asset's Event ID as a parameter:

```bash
assets/add30235-1424-4fda-840a-d5ef82c4c96f/events/11bf5b37-e0b8-42e0-8dcf-dc8c4aefc000
```

To fetch all transactions for an asset event GET the blockchain resource:

```bash
curl -v -X GET \
     -H "@$BEARER_TOKEN_FILE" \
     https://app.rkvst.io/archivist/v1alpha1/blockchain/assets/add30235-1424-4fda-840a-d5ef82c4c96f/events/11bf5b3
```

Each of these calls returns a list of matching blockchain transactions in the form:

```json
{
    "transactions": [
        {
            "hash": "0x9fc76417374aa880d4449a1f7f31ec597f00b1f6f3dd2d66f4c9c6c445836d8b",
            "nonce": 2,
            "blockHash": "0xef95f2f1ed3ca60b048b4bf67cde2195961e0bba6f70bcbea9a2c4e133e34b46",
            "blockNumber": 3,
            "transactionIndex": 0,
            "r": "0x8912348621879462817634897216348712638941",
            "s": "0x1234689712638957682375682364892376487238",
            "from": "0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b",
            "to": "0x6295ee1b4f6dd65047762f924ecd367c17eabf8f",
            "value": "123450000000000000",
            "gas": 314159,
            "gasPrice": "2000000000000",
            "input": "0x57cb2fc4",
            "v": "0x26"
        },
        {
            "hash": "0x9fc76417374aa880d4449a1f7f31ec597f00b1f6f3dd2d66f4c9c6c445836d8b",
            "nonce": 2,
            "blockHash": "0xef1234567d3ca60b048b4bf67cde2195961e0bba6f70bcbea9a2c4e133e34b46",
            "blockNumber": 3,
            "transactionIndex": 0,
            "r": "0x8912348621879462817634897216348712638941",
            "s": "0x1234689712638957682375682364892376487238",
            "from": "0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b",
            "to": "0x6295ee1b4f6dd65047762f924ecd367c17eabf8f",
            "value": "123450000000000000",
            "gas": 314159,
            "gasPrice": "2000000000000",
            "input": "0x57cb2fc4",
            "v": "0x26"
        }
    ]
}
```

## Blockchain OpenAPI Docs

{{< openapi url="https://raw.githubusercontent.com/jitsuin-inc/archivist-docs/master/doc/openapi/blockchainv1alpha1.swagger.json" >}}
