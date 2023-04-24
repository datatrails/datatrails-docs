---
 title: "Verify RKVST SCITT Receipts"
 description: "Proof of Posting Receipts for SCITT"
 lead: "Proof of Posting Receipts for SCITT"
 date: 2021-05-18T14:52:25+01:00
 lastmod: 2021-05-18T14:52:25+01:00
 draft: false
 images: []
 menu:
   docs:
     parent: "beyond-the-basics"
 weight: 45
 toc: true
---

## What are receipts?

Having a receipt for an RKVST Event allows you to prove that you recorded the Event on the RKVST Blockchain, independently of RKVST. 

Receipts can be retrieved for [Simple Hash](https://docs.rkvst.com/docs/overview/advanced-concepts/#simple-hash) and [Khipu](https://docs.rkvst.com/docs/overview/advanced-concepts/#simple-hash) Events once they have been confirmed and anchored.

A user may get a receipt or any Event they recorded on the system. You must be an Administrator for your Tenancy to retrieve receipts for any Event within the Tenancy, including those shared by other organizations.

Receipts for Public Events can be obtained by any authenticated API request.

{{< note >}}
**Note:** Receipts are currently an API-only feature. In order to obtain a receipt, you will need an App Registration. 
{{< / note >}}

## What is in a receipt?

The Receipts API is provided as an integration with emerging standards driven by [Supply Chain Integrity, Transparency, and Trust (SCITT)](https://www.rkvst.com/what-is-scitt-and-how-does-rkvst-help/).

Regardless of how the standards evolve, any receipt you obtain today will remain non-repudiable proof of posting for the Event.

{{< warning >}}
**Warning:** The complete contents of the Event are present in the receipt in clear text. If the Event information is sensitive, the receipt should be regarded as sensitive material as well. 
{{< / warning >}}

<br>

The `/archivist/v1/notary/claims/events` API is a convenience API to create a claim for an RKVST event.

In the SCITT model, a claim is then presented to a trusted service to obtain a receipt. When you present a claim to the `/archivist/v1/notary/receipts` API to obtain your receipt, RKVST is acting as the trusted service in the SCITT model. The response from that API is a (draft) standards-compatible receipt proving that you recorded your Event on the RKVST Blockchain. 

## How do I retrieve a receipt?

RKVST provides a Python script that can be used to retrieve a receipt. For full details, please visit our [Python documentation](https://python-scitt.rkvst.com/index.html).