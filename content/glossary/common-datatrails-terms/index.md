---
title: "Common DataTrails Terms"
description: ""
lead: ""
date: 2022-10-19T07:39:44-07:00
lastmod: 2022-10-19T07:39:44-07:00
draft: false
images: []
menu: 
  glossary:
    parent: "glossary"
weight: 51
toc: true
aliases: 
  - /docs/glossary/common-rkvst-terms/
---

Select a term for more information.

| **Term**            | **Definition**                                                                                                       |
|---------------------|----------------------------------------------------------------------------------------------------------------------|
| [ABAC](/platform/administration/sharing-access-inside-your-tenant/)                | Attribute-Based Access Control; policy that allows you to grant fine-grain access to members of your Tenancy         |
| [access policy](/platform/overview/core-concepts/#access-policies)       | grants chosen Asset and Event access to stakeholders                                                                 |
| [actor](/platform/overview/creating-an-asset/)| person/machine/software integration that created a particular entry on the provenance record|
| [administrator](/developers/developer-patterns/getting-access-tokens-using-app-registrations/#creating-an-app-registration)           | user with permission to see all Asset and Event information within a Tenancy, and to grant access to other users                                   |
| [anchored](/developers/developer-patterns/verifying-with-simple-hash/)  | Simple Hash events are committed to the blockchain by hashing them in batches. The hash recorded on the chain is called the anchor |
| [asset](/platform/overview/core-concepts/#assets)               | a DataTrails Asset is an entry in your tenancy, which has a collection of attributes that describes its current state and a complete life history of Events |
| [asset attributes](/platform/overview/creating-an-asset/#creating-an-asset)    | key-value pairs that represent information about an Asset                                                            |
| [asset ID](/platform/overview/creating-an-asset/)| the permanent unique identifier for an Asset, under which all provenance information (Events) can be found|
| [audit trail](https://en.wiktionary.org/wiki/audit_trail) | a formal record of activities (Events) that are made against a piece of data (an Asset)|
| [bearer token](/platform/overview/creating-an-asset/#creating-an-asset)        | access token for DataTrails API; created using Custom Integration credentials                                               |
| [behaviors](/platform/overview/creating-an-asset/#creating-an-asset)          | detail what class of events in an Asset lifecycle you might wish to record                                           |
| [compliance policy](/platform/administration/compliance-policies/)   | user-defined rule sets that Assets can be tested against
| [custom integration](/developers/developer-patterns/getting-access-tokens-using-app-registrations/#creating-an-app-registration)    | client ID and client secret credentials that are used to access the DataTrails API. Formerly known as an App Registration                                                             |
| [document hash](/developers/developer-patterns/document-profile/) | cryptographic 'fingerprint' of a file or document that proves it is unmodified|
| [document status](/developers/developer-patterns/document-profile/) | when dealing with Document profile Assets in DataTrails you can attach certain lifecycle stage metadata to them such as 'Draft', 'Published', or 'Withdrawn' in order to properly convey whether or not someone checking provenance of the document should rely on a particular version|
| [event](/platform/overview/core-concepts/#events)               | tracks key moments of an Asset lifecycle; details of Who Did What When to an Asset                                   |
| [event attributes](/platform/overview/creating-an-event-against-an-asset/#creating-events)    | key-value pairs that represent information about an Event                                                            |
| [event ID](/platform/overview/creating-an-event-against-an-asset/)| unique identifier for an entry in the provenance record that means it can be shared and found later|
| [event type](/platform/overview/creating-an-event-against-an-asset/)| events in DataTrails are labeled with a 'type' that signify what kind of evidence they relate to, for instance a 'Publish' event on a document, or a 'Shipping' event on physical goods. Event types can be very useful for defining access control rules as well as filtering the audit trail for specific kinds of information|
| [integration](/platform/administration/dropbox-integration/) | built-in API functionality that allows DataTrails to connect to third party products such as Dropbox |                                                           |
| [linked folder](/platform/administration/dropbox-integration/#editing-the-list-of-linked-folders) | a folder that has been selected to be linked to DataTrails during the configuration of an Integration|
| [metadata](https://en.wiktionary.org/wiki/metadata) | structured information about a file. In DataTrails this metadata is recorded in the Asset and Event attributes|
| [OBAC](/platform/administration/sharing-access-outside-your-tenant/)                | Organization-Based Access Control; policy allows sharing with the Administrator of another organization                  |
| [operation](/platform/overview/creating-an-event-against-an-asset/#creating-events)  | class of Event being recorded                                                                                       |
| [organization](/platform/administration/verified-domain/)| any entity with a distinct DataTrails account who publishes or verifies provenance information on the platform|
| [proof mechanism](/platform/overview/advanced-concepts/#proof-mechanisms)           | method by which information on the DataTrails blockchain can be verified; selected when an Asset is created                                                                                       |
| [provenance](https://en.wiktionary.org/wiki/provenance) | the version and ownership history of a piece of data. With DataTrails this is an immutable audit trail to prove Who Did What When to any piece of data  |
| [public asset](/platform/overview/public-attestation/)        | Assets that can be used to publicly assert data, accessible by URL without the need for a DataTrails account                                                   |
| [selector](/platform/overview/creating-an-asset/#creating-an-asset)            | identifying attribute the Yaml Runner will use to check if your Asset exists already before attempting to create it  |
| [simple hash](/platform/overview/advanced-concepts/#simple-hash)            | Proof Mechanism that commits information to the DataTrails blockchain in batches; value can confirm that information in the batch has not changed |
| [tenancy](/platform/overview/core-concepts/#tenancies)             | an organization’s private area within DataTrails, containing Asset and Event data                                         |
| [tenant display name](/platform/administration/identity-and-access-management/#tenant-display-name) | displayed only within own Tenancy for easy identification and switching |
| [transaction](/developers/developer-patterns/verifying-with-simple-hash/)| final commitment of data to the Distributed Ledger Technology so that it is sealed and cannot be modifed, tampered or erased|
| [unlinked folder](/platform/administration/dropbox-integration/#editing-the-list-of-linked-folders) | a folder that has not been selected to be linked to DataTrails during the configuration or reconfiguration of an Integration                                              |
| [verified domain](/platform/administration/verified-domain/)     | tenancy name visible to others in place of the tenancy ID when viewing the Asset Overview of a public Asset or a shared private Asset. Must be verified by the DataTrails team                                        |
| [verified organization](/platform/administration/verified-domain/)| an organization which has paid to have their domain verified and displayed in place of their tenancy ID in Instaproof results and in the Asset Overview |
| [version](/developers/developer-patterns/document-profile/)| when dealing with Document profile Assets in DataTrails you can differentiate 'final' or 'published' versions of a document from other provenance information such as reviews or downloads |
