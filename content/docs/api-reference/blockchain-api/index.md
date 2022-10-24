---
title: "Blockchain API (v1alpha2)"
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

Create the [bearer_token](../../setup-and-administration/getting-access-tokens-using-app-registrations) and store in a file in a secure local directory with 0600 permissions.

### Fetch Transactions for an event (v1alpha2)

Blockchain transactions can be fetched from the blockchain endpoint using the asset's Event ID as a parameter:

```bash
assets/add30235-1424-4fda-840a-d5ef82c4c96f/events/11bf5b37-e0b8-42e0-8dcf-dc8c4aefc000
```

To fetch all transactions for an asset event GET the blockchain resource:

```bash
curl -v -X GET \
     -H "@$BEARER_TOKEN_FILE" \
     https://app.rkvst.io/archivist/v1alpha2/blockchain/assets/add30235-1424-4fda-840a-d5ef82c4c96f/events/11bf5b3
```

Each of these calls returns a list of matching blockchain transactions in the form:

```json
{
   "transactions":[
      {
         "transaction":{
            "hash":"0xbcb60deea8c70a1f4dea54d7666ca58b73f00e0febe59c099616ecb53d5909e4",
            "nonce":"0",
            "blockhash":"0xa25e4360cd08abade72e34e9a65c670fe6f965454b95021d37baf472e429dc69",
            "block_number":"786720",
            "transaction_index":1,
            "r":"0x4b020ec02b0e88e5519fe43e2d2b33ca39f8807ebe2953c866b553df98ded5aa",
            "s":"0x75620ffa89a21404803201cc279a53f9afa770c16af312db7fb42899b9608d64",
            "from":"0x413aDcF9365C5eBe0F9714b575B5eA792aECC0bB",
            "to":"0x0C0c2c268261F767880f64cE84e088558B38b349",
            "value":"0",
            "gas":"500000000",
            "gas_price":"0",
            "input":"0xdc6b7758811673be442b8a70ad1e37117c76b5abbabc716917a6e5f98f8247a68f6bf368fdce8bd7f685b9aa41148f5c059c8599e3d707f4481e13a8782a0b1a",
            "v":"0x26"
         },
         "kind":"KHIPU"
      },
      {
         "transaction":{
            "hash":"0x4113596f7c9f825104f53ed50b262a116801d89b8e5ac15e9d8dc215e6f49ef0",
            "nonce":"1",
            "blockhash":"0xaf1b9b686bf7a1beea003f84d85da1d8ca4c8eaaeded29ac72fd549e6591f84b",
            "block_number":"786722",
            "transaction_index":0,
            "r":"0x4833ad44bc2fc0bca2f08a958ce1e0f6d3667493c8773bc74e45837bee5de5be",
            "s":"0x3ca22bc844d963e908a19ccbc139543193411650dd97e4978d3e4f243d1295db",
            "from":"0x413aDcF9365C5eBe0F9714b575B5eA792aECC0bB",
            "to":"0x0C0c2c268261F767880f64cE84e088558B38b349",
            "value":"0",
            "gas":"500000000",
            "gas_price":"0",
            "input":"0x06bbc3af74cd2fdd82a6036dfa3c69d0cec5d35782ba56dd4be0c928c9ca1ee3a0e19c97f1c5e5784c7cd305d53a2f5249b18937e1d613eec452c74ae9c619f4",
            "v":"0x26"
         },
         "kind":"KHIPU"
      }
    ]
}
```

## Blockchain OpenAPI Docs

{{< openapi url="https://raw.githubusercontent.com/jitsuin-inc/archivist-docs/master/doc/openapi/blockchainv1alpha2.swagger.json" >}}
