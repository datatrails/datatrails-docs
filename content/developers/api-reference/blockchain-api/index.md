---
title: "Blockchain API (v1alpha2)"
description: "Blockchain API Reference"
lead: "Blockchain API Reference"
date: 2021-06-09T13:57:04+01:00
lastmod: 2021-06-09T13:57:04+01:00
draft: false
images: []
menu: 
  developers:
    parent: "api-reference"
weight: 105
toc: true
aliases: 
  - /docs/api-reference/blockchain-api/
---
{{< note >}}
This page is primarily intended for developers who will be writing applications that will use RKVST for provenance. 
If you are looking for a simple way to test our API you might prefer our [Postman collection](https://www.postman.com/rkvst-official/workspace/rkvst-public-official/overview), the [YAML runner](/developers/yaml-reference/story-runner-components/) or the [Developers](https://app.rkvst.io) section of the web UI. 

Additional YAML examples can be found in the articles in the [Overview](/platform/overview/introduction/) section.
{{< /note >}}
## Blockchain API Examples

Create the [bearer_token](/developers/developer-patterns/getting-access-tokens-using-app-registrations) and store in a file in a secure local directory with 0600 permissions.

### Fetch Transactions for an event (v1alpha2)

Blockchain transactions can be fetched from the blockchain endpoint using the Asset's Event ID as a parameter:

```bash
assets/add30235-1424-4fda-840a-d5ef82c4c96f/events/11bf5b37-e0b8-42e0-8dcf-dc8c4aefc000
```

To fetch all transactions for an Asset's Events GET the blockchain resource:

```bash
curl -v -X GET \
     -H "@$HOME/.rkvst/bearer-token.txt" \
     https://app.rkvst.io/archivist/v1alpha2/blockchain/assets/add30235-1424-4fda-840a-d5ef82c4c96f/events/11bf5b3
```

Depending on the type of [proof mechanism](/platform/overview/advanced-concepts/#proof-mechanisms) used, the response will be:

#### Simple Hash:

```json
{
   "transactions":[
      {
         "transaction":{
            "hash":"0x4bb529697a096b23947e13f78492d90a66e2e9d76c5feb015cd321590b00e72a",
            "nonce":"402",
            "blockhash":"0x9ea557196d44e6433be7676ca5bdef5f8753fa6d92bbb5e7456fe3979f84ea40",
            "block_number":"861180",
            "transaction_index":0,
            "r":"0xcb4282065fb5c0b6c674bf7d3b7fb9ee4c49f135b02b9b1cf1c607bb3ff406a",
            "s":"0x5fa50214efdbc1cf13f98bb962ddf3224f1d5ba77cb19aafac5171b6ae1e8074",
            "from":"0xED3939b59D1fC93dD3158522E728Df483BC9998d",
            "to":"0x4c07935361B497EBD5801E3b4D2cF29C2179069e",
            "value":"0",
            "gas":"500000000",
            "gas_price":"0",
            "input":"0xa7ea3ea7607b464c8c5d4172880146c1c303329600000000000000000000000000000000ab6e28d836193ad54e941e9ff09b27946bdc7838c46fcf91bc11026e6737afb6000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000060000000000000000000000000000000000000000000000000000000000000002000000000000000000000000000000000000000000000000000000000000016000000000000000000000000000000000000000000000000000000000000001a0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000635bc6bb00000000000000000000000000000000000000000000000000000000000001e000000000000000000000000000000000000000000000000000000000000002200000000000000000000000000000000000000000000000000000000000000014313937302d30312d30315430303a30303a30305a0000000000000000000000000000000000000000000000000000000000000000000000000000000000000014323032322d31302d32385431323a31303a33355a0000000000000000000000000000000000000000000000000000000000000000000000000000000000000003677465000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000026c74000000000000000000000000000000000000000000000000000000000000",
            "v":"0xea"
         },
         "simple_hash_details":{
            "api_query":"https://app.rkvst.io/archivist/v2/assets/-/events?order_by=SIMPLEHASHV1&proof_mechanism=SIMPLE_HASH&timestamp_accepted_since=1970-01-01T00:00:00Z&timestamp_accepted_before=2022-10-28T12:10:35Z",
            "start_time":"1970-01-01T00:00:00Z",
            "end_time":"2022-10-28T12:10:35Z",
            "hash_schema_version":1,
            "anchor_hash":"ab6e28d836193ad54e941e9ff09b27946bdc7838c46fcf91bc11026e6737afb6",
            "event_count":6
         },
         "kind":"SIMPLE_HASH"
      }
   ],
   "next_page_token":""
}
```

#### Khipu:

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

{{< note >}}
Check out our guide for [Verifying Assets and Events with Simple Hash](/developers/developer-patterns/verifying-with-simple-hash/).
{{< /note >}}

## Blockchain OpenAPI Docs

{{< openapi url="https://raw.githubusercontent.com/rkvst/archivist-docs/master/doc/openapi/blockchainv1alpha2.swagger.json" >}}
