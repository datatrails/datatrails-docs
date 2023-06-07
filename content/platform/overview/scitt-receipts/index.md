---
 title: "Verify RKVST SCITT Receipts"
 description: "Proof of Posting Receipts for SCITT"
 lead: "Proof of Posting Receipts for SCITT"
 date: 2021-05-18T14:52:25+01:00
 lastmod: 2021-05-18T14:52:25+01:00
 draft: false
 images: []
 menu:
   platform:
     parent: "overview"
 weight: 37
 toc: true
---

## What are receipts?

Having a receipt for an RKVST Event allows you to prove that you recorded the Event on the RKVST Blockchain, independent of RKVST. 


Receipts can be retrieved for [Simple Hash](/platform/overview/advanced-concepts/#simple-hash) Events once they have been confirmed and [anchored](/glossary/common-rkvst-terms/).

Receipts can be retrieved for [Khipu](/platform/overview/advanced-concepts/#khipu) Events once they have been confirmed.


A user may get a receipt for any Event they have recorded on the system. You must be an Administrator for your Tenancy to retrieve receipts for any Event within the Tenancy, including those shared by other organizations.

Receipts for Public Events can be obtained by any authenticated API request.

{{< note >}}
**Note:** Receipts are currently an API-only feature. In order to obtain a receipt, you will need an App Registration. 
{{< / note >}}

## What is in a receipt?

The Receipts API is provided as an integration with emerging standards driven by [Supply Chain Integrity, Transparency, and Trust (SCITT)](https://www.rkvst.com/what-is-scitt-and-how-does-rkvst-help/).

Regardless of how the standards evolve, any receipt you obtain today cannot be repudiated as proof of posting for the Event.

{{< warning >}}
**Warning:** The complete contents of the Event are present in the receipt in clear text. If the Event information is sensitive, the receipt should be regarded as sensitive material as well. 
{{< / warning >}}

<br>

The `/archivist/v1/notary/claims/events` API is a convenience API to create a claim for an RKVST event.

In the SCITT model, a claim is then presented to a trusted service to obtain a receipt. When you present a claim to the `/archivist/v1/notary/receipts` API to obtain your receipt, RKVST is acting as the trusted service in the SCITT model. The response from that API is a (draft) standards-compatible receipt proving that you recorded your Event on the RKVST Blockchain. 

## How do I retrieve a receipt?

As a convenience, RKVST provides a Python script that can be used to retrieve a receipt. For full details, please visit our [Python documentation](https://python-scitt.rkvst.com/index.html).

This can also be done with independent tools. 

Receipts can also be retrieved offline using curl commands. To get started, make sure you have an [Access Token](/developers/developer-patterns/getting-access-tokens-using-app-registrations/), [Event ID](/platform/overview/creating-an-event-against-an-asset/), and [jq](https://github.com/stedolan/jq/wiki/Installation) installed. 


First, save the identity of an event in `EVENT_IDENTITY`.

1. Get the transaction_id from the Event.

```bash
EVENT_TRANSACTION_ID=$(curl -s \
        -X GET -H "Authorization: Bearer ${TOKEN}" \
        https://app.rkvst.io/archivist/v2/${EVENT_IDENTITY} \
        | jq -r .transaction_id)
```

{{< warning >}}
The transaction_id is available once the event has been committed to the blockchain. For assets using the Simple Hash `proof_mechansim` it is available once the event is included in an anchor. For Khipu, it is available when the event is confirmed.
{{< / warning>}}

2. Get a claim for the Event identity.

```bash
CLAIM=$(curl -s -d "{\"transaction_id\":\"${EVENT_TRANSACTION_ID}\"}" \
        -X POST -H "Authorization: Bearer ${TOKEN}" \
        https://app.rkvst.io/archivist/v1/notary/claims/events \
        | jq -r .claim)
```

3. Next, get the corresponding receipt for the claim. 

```bash
RECEIPT=$(curl -s -d "{\"claim\":\"${CLAIM}\"}" \
        -X POST -H "Authorization: Bearer ${TOKEN}" \
        https://app.rkvst.io/archivist/v1/notary/receipts \
        | jq -r .receipt)
```

4. Get the block details.

Get the block number using:

```bash
echo ${RECEIPT} | base64 -d | less
```

Look for the first `"block":"<HEX-BLOCK-NUMBER>"` in the decoded output and set the value in the environment, for example: `BLOCK="0x1234"`.

Next, get the private state root:

```bash
WORLDROOT=$(curl -s -X GET -H "Authorization: Bearer ${TOKEN}" \
            https://app.rkvst.io/archivist/v1/archivistnode/block?number="${BLOCK}" \
            | jq -r .privateStateRoot)
```

4. Finally, use the `rkvst_receipt_scittv1` command to verify the receipt offline at any time.

```bash
echo ${RECEIPT} | rkvst_receipt_scittv1 verify -d --worldroot ${WORLDROOT}
```