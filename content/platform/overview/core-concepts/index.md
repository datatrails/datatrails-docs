---
title: "Core Concepts"
description: "DataTrails Core Concepts"
lead: "DataTrails Core Concepts"
date: 2021-06-14T10:57:58+01:00
lastmod: 2021-06-14T10:57:58+01:00
draft: false
images: []
menu: 
  platform:
    parent: "overview"
weight: 31
toc: true
aliases:
  - ../quickstart/when-who-did-what-to-an-asset
  - /docs/overview/core-concepts/
---

## Tenancies

A Tenancy is an Organization's private area within DataTrails, containing [Event](./#events) data that build over time to create Audit Trails.
The user who created the Tenancy is by default the Administrator and has full control over everything in that Tenancy.
An Administrator can also create granular [Access Policies](./#access-policies) which allow Event metadata from their Tenancy to be shared to other Tenancies; for example, Organization A would share supply chain data from their Tenancy to Organization B's Tenancy.

Administrators may invite other users into their Tenancy.
The invited user will start off with no permissions and can then be given specific access rights (including being upgraded to an Administrator) by any existing Administrator in that Tenancy.
For more details on this, see [Identity and Access Management](/platform/administration/identity-and-access-management/)

## Events

The fundamental purpose of DataTrails, like any transparency service, is to record and prove the origins and authenticity of the data that fuels the modern enterprise.
This is achieved through the registration of immutable _Events_ on the platform.

Events are attestations: individual pieces of evidence recorded as observations or claims about a thing from qualified witnesses.
Each Event Record contributes to the ['Golden Thread'](./#the-golden-thread) of the Audit Trail by building a rich lineage of history.

Events can never be deleted or modified by anyone, not even administrators of the DataTrails platform.
Once asserted, they cannot be shredded, tampered, or backdated.

## Assets

{{< note >}}
**Note:** Assets will soon be deprecated for a more flexible and powerful concept of _Trails_.

The change is subtle, but where Assets only allow Events to be registered against a single thing or theme, Trails will enable Events to be free of any such restriction leading to more natural expression of _what happened when_ or _who said what about what_.

To prepare for this change, when writing code integrations be sure to focus on Event attributes and not mutable `asset_attributes`.
This will ensure best performance and minimal code changes to take advantage of the newer API.
{{< /note >}}

Asset Records represents _**a thing**_: this could be a file; a physical object; a smart device; or even a business process.
An Asset is just the subject that the Events are talking about.

A DataTrails Asset acts as a container for Events which share a topic or have a similar relationship.
When combined with a complete history of Events that brought it to that state, an immutable Audit Trail is realized.
As Assets are retired, a collection of Events can be correlated through Trails or Event Attributes.
DataTrails Event attributes track anything deemed important.
For example, a Document may trace the evolution of authors, versions and release dates.
Modeling a Shipping Container may have a handling history of movements through ports.

These are examples of completely different _**things**_ that can have a DataTrails Audit Trail.

Each Asset has a fixed identity across all stakeholders, ensuring that all relevant parties are collaborating on the same object and see the same history of the Asset at any given time when shared through [Access Policies](./#access-policies).
As Assets are retired, all relevant parties may collaborate across Trails or named Event Attributes.

## Proving Provenance

Artifacts and Events are core to the DataTrails platform, and being able to quickly demonstrate proof that these artifacts have not been tampered is key to knowing the information is secure and trustworthy.

DataTrails attestations are committed to immutable storage that is underpinned by cryptographically verifiable Merkle Mountain Range data structures for long term verifiability, even when offline.

### Four Increasing Trust Levels

At DataTrails we believe in holding ourselves to the same levels of accountability as our customers, and the Merkle Log proof mechanism provides the robustness, integrity and availability guarantees needed to ensure data authenticity in any digital or data supply chain.
And you don't have to just take our word for it: you can check.

Here's how it works:

{{< img src="merkleflow.png" alt="Rectangle" caption="<em></em>" class="border-0" >}}

Without an Immutable Audit Trail, there is always the risk - or at least the suspicion - that data can be shredded, backdated or otherwise tampered with.

Once `STORED` in DataTrails and shared with partners, no party to the transaction can tamper, back-date or shred evidence.
However while the security and integrity of our customers' data is our top priority, there could still be a suspicion that DataTrails, a hacker in our systems, or our cloud service provider under subpena, could tamper with the data, or make it unavailable.

Once `COMMITTED` in the customer’s Tenancy Merkle tree in public blob storage, customers can prove their Events to 3rd parties, AND any tampering by DataTrails, or any other party that can gain access is detectable.
Because this data is public, anyone can maintain a copy just in case the DataTrails’ version disappears.
These copies are great for availability and holding DataTrails accountable, but there is a risk that a kind of Sybil attack could be mounted where the community creates forks and then tries to accuse the DataTrails version of being wrong.

By adding all Tenancies to the Merkle Mountain Range (MMR) and signing the root, Events move to the `CONFIRMED` stage.
The signature on the root holds DataTrails to account _and_ prevents forks and the Sybil attack mentioned above.Even so, a tiny chance of tampering remains: in principle, multiple MMRs could be signed, creating multiple versions of history.

To make the whole history and individual events `UNEQUIVOCAL`, the root hash of the Committed MMR is periodically broadcast so that it is clear that there is one, and only one, version of history to underpin your data authenticity.

## Access Policies

Sharing the right amount of information with the consumers of your data is critical to creating a trustworthy shared history of information.
It is important that every participant be able to see and contribute to the Audit Trail without compromising security and personal private information.
To ensure stakeholders can access only the information relevant to them, Events are private by default, unless posted [as Public](./#the-public-view).
Tenant Administrators define how much of the Audit Trail a user or partner can see, so they only see what they need to complete a task.

Like any high end transparency service, DataTrails operates a 'once seen always seen' system, so while you remain completely in control of what Audit Trail data you share with your partners, it cannot be deleted or modified later.

An Attribute-Based Access Control (ABAC) policy is used to share with Non-Administrators within a Tenancy.
An Organization-Based Access Control (OBAC) policy is used to share with the Administrators of another Tenancy.
The Administrator of the external Tenancy may then use an ABAC policy to grant permissions to the relevant Non-Administrators of their Tenancy.
In both cases, attribute-specific read and write access can be granted using fine-grained controls.

## The Public View

Every Audit Trail has a private view which is only visible to Tenancy Administrators and those who are given access through an Access Policy.
Additionally some Trails, such as those that meet the requirements of the [Document Profile](/developers/developer-patterns/document-profile/), have a [Public View](/platform/overview/public-attestation/) which is visible to everyone.
The purpose of this view is to allow anyone to verify that the document they're using is genuine and has not been altered.
When the document Audit Trail is combined with [Instaproof](/platform/overview/instaproof/) a user of your data can easily find out which version of a document they have and confirm that it is genuine.

## The Golden Thread

Putting all these concepts together, it is possible to create a Golden Thread of evidence that makes up the DataTrails Audit Trail.
This has many use cases relating to content authenticity but can also be applied to supply chain integrity and standards compliance, or anything where stakeholders need transparency and trust.

{{< img src="TheGoldenThread.png" alt="Rectangle" caption="<em>The Golden Thread</em>" class="border-0" >}}
